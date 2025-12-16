FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    HF_HUB_DISABLE_SYMLINKS_WARNING=1

WORKDIR /app

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt

COPY app ./app
COPY data ./data

ENV PORT=7860
EXPOSE 7860

CMD ["python", "app/main.py"]

