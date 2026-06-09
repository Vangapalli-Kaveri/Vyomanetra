from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

results = model.predict(
    source=r"C:\Users\kaveri\Pictures\drone.jpg",
    save=True,
    conf=0.25
)

print("Prediction completed")