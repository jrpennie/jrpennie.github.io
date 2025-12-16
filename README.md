## Turtle Species Recognizer (Zero‑shot CLIP)

This is a simple web app that recognizes different types of turtles from an uploaded image using CLIP zero-shot image classification. It does not require a task-specific training dataset and can be extended with more species labels.

### Features
- Upload an image to get top‑k predicted turtle species
- Uses CLIP (via Hugging Face `transformers`) with a configurable hypothesis template
- Minimal Gradio UI you can run locally

### Quickstart
1. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv && source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app/main.py
   ```
4. Open the printed local URL in your browser.

### Run with Docker
Build and run the app as a container (CPU only):
```bash
docker build -t turtle-recognizer .
docker run --rm -p 7860:7860 -e PORT=7860 turtle-recognizer
```

Then visit `http://localhost:7860`.

### Add or Edit Species Labels
Edit `data/turtle_species.json` to add or remove labels. You can include turtles and tortoises. The model performs zero-shot matching against these labels.

### Notes
- Zero-shot CLIP provides reasonable results but is not a substitute for a fine‑tuned specialist model. For production use, consider curating a dataset and training or fine‑tuning a classifier.
- GPU is used automatically if available.

### License
MIT
# John Pennie | Cybersecurity Portfolio

This portfolio website was built with HTML, CSS, and JavaScript, the website showcases my professional background, projects, documents, technical skills, and contact information.
