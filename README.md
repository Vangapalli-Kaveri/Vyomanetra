# Vyomanetra – Drone Detection AI using YOLOv8

## Project Overview

Vyomanetra is an AI-powered Drone Detection System developed using YOLOv8 and Python. The project is capable of detecting drones in images, videos, and real-time webcam feeds.

The objective of this project is to build a computer vision model that can automatically identify drones from visual data using deep learning techniques.

---

## Features

* Drone detection in images
* Drone detection in videos
* Real-time webcam detection
* Custom-trained YOLOv8 model
* GPU-accelerated training using NVIDIA RTX 3050
* GitHub-based version control

---

## Technologies Used

* Python
* YOLOv8 (Ultralytics)
* PyTorch
* OpenCV
* NumPy
* Git
* GitHub

---

## Dataset

The model was trained on a custom drone dataset in YOLO format containing:

* Training Images
* Validation Images
* Test Images
* Bounding Box Annotations

Dataset configuration was managed using `data.yaml`.

---

## Project Structure

```text
Project A
│
├── train.py
├── predict.py
├── predict_video.py
├── detect_webcam.py
├── data.yaml
├── requirements.txt
├── train/
├── valid/
├── test/
└── README.md
```

---

## Model Training

The model was trained using YOLOv8 on a custom drone dataset.

Training Environment:

* GPU: NVIDIA GeForce RTX 3050 Laptop GPU
* Framework: PyTorch
* Model: YOLOv8

Generated model files:

* best.pt
* last.pt

---

## Detection Modes

### Image Detection

Detects drones from input images.

### Video Detection

Detects drones frame-by-frame from video files.

### Webcam Detection

Performs real-time drone detection using a webcam.

---

## Results

The model successfully detects drones from:

* Images
* Videos
* Webcam streams

Training metrics and evaluation graphs were generated during training.

---

## Future Scope

* Multi-drone tracking
* Drone classification
* Edge device deployment
* Security and surveillance integration
* Live drone monitoring systems

---

## Author

Vangapalli Kaveri

GitHub:
https://github.com/Vangapalli-Kaveri

Repository:
https://github.com/Vangapalli-Kaveri/Vyomanetra
