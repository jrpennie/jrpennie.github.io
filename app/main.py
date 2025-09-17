import os
import json
from functools import lru_cache
from typing import List, Dict, Any

import torch
from transformers import pipeline
import gradio as gr


@lru_cache(maxsize=1)
def get_device_index() -> int:
    return 0 if torch.cuda.is_available() else -1


@lru_cache(maxsize=1)
def get_classifier():
    # Smaller model for faster startup; switch to clip-vit-large-patch14 for higher accuracy
    return pipeline(
        task="zero-shot-image-classification",
        model="openai/clip-vit-base-patch32",
        device=get_device_index(),
    )


@lru_cache(maxsize=1)
def load_species_labels() -> List[str]:
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "turtle_species.json")
    with open(data_path, "r", encoding="utf-8") as f:
        labels: List[str] = json.load(f)
    return labels


def predict_species(image, top_k: int = 5, hypothesis_template: str = "a photo of a {}") -> Dict[str, Any]:
    labels = load_species_labels()
    clf = get_classifier()
    outputs = clf(
        image,
        candidate_labels=labels,
        hypothesis_template=hypothesis_template,
        multi_label=False,
    )

    # `outputs` is a list of dicts sorted by score desc
    top = outputs[: max(1, int(top_k))]
    # Prepare table data
    table_rows = [{"label": o["label"], "score": round(float(o["score"]), 4)} for o in top]
    top_label = top[0]["label"] if top else ""
    return {"Top prediction": top_label, "Top‑k table": table_rows}


def build_ui() -> gr.Blocks:
    with gr.Blocks(title="Turtle Species Recognizer (Zero‑shot CLIP)") as demo:
        gr.Markdown("""
        ### Turtle Species Recognizer (Zero‑shot CLIP)
        Upload a turtle image to get species predictions using CLIP zero‑shot classification. Edit labels in `data/turtle_species.json`.
        """)

        with gr.Row():
            with gr.Column():
                image_input = gr.Image(type="pil", label="Upload turtle image")
                topk_input = gr.Slider(1, 10, value=5, step=1, label="Top‑k")
                with gr.Accordion("Advanced", open=False):
                    hypothesis_input = gr.Textbox(value="a photo of a {}", label="Hypothesis template")
                submit_btn = gr.Button("Predict")

            with gr.Column():
                top_label_output = gr.Textbox(label="Top prediction", interactive=False)
                table_output = gr.Dataframe(
                    headers=["label", "score"],
                    datatype=["str", "number"],
                    label="Top‑k scores",
                    interactive=False,
                )

        def _predict(image, top_k, hypothesis_template):
            result = predict_species(image=image, top_k=top_k, hypothesis_template=hypothesis_template)
            return result["Top prediction"], result["Top‑k table"]

        submit_btn.click(
            _predict,
            inputs=[image_input, topk_input, hypothesis_input],
            outputs=[top_label_output, table_output],
        )

    return demo


if __name__ == "__main__":
    ui = build_ui()
    port = int(os.environ.get("PORT", "7860"))
    ui.launch(server_name="0.0.0.0", server_port=port)

