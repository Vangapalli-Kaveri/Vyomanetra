from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

for result in model.predict(
    source="drone_video.mp4",
    save=True,
    stream=True,
    conf=0.25
):
    pass

print("Video processing completed")