import cv2
import torch
import numpy as np

# Load the pre-trained YOLO model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Function to preprocess the input image
def preprocess_image(image):
    # Resize and normalize the image
    img = cv2.resize(image, (640, 640))  # Resize to YOLO input size
    img = img[:, :, ::-1].transpose(2, 0, 1)  # Convert BGR to RGB and HWC to CHW
    img = np.ascontiguousarray(img, dtype=np.float32)  # Convert to contiguous array
    img /= 255.0  # Normalize to [0, 1]
    return img

# Function to detect cars in the input image
def detect_cars(image):
    # Preprocess the input image
    img = preprocess_image(image)

    # Perform object detection
    results = model([img])  # Pass the image through the model

    # Extract car detections
    car_detections = results.xyxy[0]  # Extract bounding boxes and labels

    return car_detections

# Function to draw bounding boxes around detected cars
def draw_boxes(image, detections):
    for detection in detections:
        label = int(detection[5])
        if label == 2:  # Car label index
            x1, y1, x2, y2, _ = detection
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

# Capture video from camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect cars in the frame
    car_detections = detect_cars(frame)

    # Draw bounding boxes around detected cars
    draw_boxes(frame, car_detections)

    # Display the frame
    cv2.imshow("Car Detection", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
