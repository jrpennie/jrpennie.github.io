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

**Live site:** https://jrpennie.us/  
**Repo:** https://github.com/jrpennie/Portfolio

![Portfolio Preview](docs/preview.png)

## Overview
This repository hosts my personal cybersecurity portfolio website. It includes my resume, selected projects, supporting documents, and contact information.

## Documents
- Resume
- CTF report
- Passive Recon report

## Highlights
- **IT Operations / Enterprise Support**: Windows troubleshooting, identity/access, endpoint security, documentation
- **Homelab Engineering**: Proxmox virtualization, Docker services, Linux administration, storage/networking
- **Detection & Monitoring**: Splunk/Wazuh-style logging, alert triage concepts, security hygiene
- **Projects & Writeups**: Pi-hole, CTF results, passive reconnaissance reporting, and more
## Projects

### 🔹 [Pi-hole — Network Traffic Filtering](https://jrpennie.us/#projects)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)
![Proxmox](https://img.shields.io/badge/Proxmox-E57000?logo=proxmox&logoColor=white)

DNS-based ad and tracker blocking deployed in a Docker container on a Proxmox virtual machine.

---

### 🔹 [Homelab — Virtualized Security Lab](https://jrpennie.us/#projects)
![Proxmox](https://img.shields.io/badge/Proxmox-E57000?logo=proxmox&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)

Personal homelab used for red/blue team simulations, service hosting, and security experimentation.

---

### 🔹 [Capture the Flag (CTF)](https://jrpennie.us/docs/CTF.pdf)
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)
![Windows](https://img.shields.io/badge/Windows-0078D6?logo=windows&logoColor=white)

Offensive security exercises completed during a DePaul University course. Recovered 7 out of 9 flags across Windows and Linux hosts.

---

### 🔹 [Passive Reconnaissance](https://jrpennie.us/docs/recon.pdf)
![OSINT](https://img.shields.io/badge/OSINT-2C2C2C)
![Reporting](https://img.shields.io/badge/Reporting-4B8BBE)

Passive reconnaissance report using open-source intelligence techniques on a selected organization.

---

### 🔹 [WildId — Web Application](https://wildid.jrpennie.us)
![Web](https://img.shields.io/badge/Web-App-0ABAB5)
![Deployment](https://img.shields.io/badge/Deployment-Cloudflare-F38020?logo=cloudflare&logoColor=white)

Web-based application deployed under a subdomain with a live demo and source code integration.


## Tech Stack
- HTML / CSS / JavaScript
- GitHub Pages

