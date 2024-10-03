from ultralytics import YOLO 

#model = YOLO('model/yolo_last.pt')
model = YOLO('yolov8x') # For the tracking


filepath = "input_videos\input_video.mp4"


#model.predict(filepath, save = True)
#result = model.predict(filepath, save = True)

#result = model.predict(filepath, conf = 0.2, save = True)  # We run this line when we get the model from our training
result = model.track(filepath, conf = 0.2, save = True)

print(result)
print("boxes:")
for box in result[0].boxes:
    print(box)


#result = model.track('input_videos/input_video.mp4',conf=0.2, save=True)
