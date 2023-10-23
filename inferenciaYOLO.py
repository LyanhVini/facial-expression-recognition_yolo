import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('model/best.pt')

# Open the webcam (you can specify the webcam index, typically 0 for the built-in webcam)
cap = cv2.VideoCapture(0)

# Loop through the webcam frames
while True:
    # Read a frame from the webcam
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Release the webcam capture object and close the display window
cap.release()
cv2.destroyAllWindows()
