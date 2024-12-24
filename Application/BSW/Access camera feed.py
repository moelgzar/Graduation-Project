import cv2

# Access the camera feed
cap = cv2.VideoCapture(0)

while True:
         ret, frame = cap.read()

         # Display the camera feed
         cv2.imshow('Camera Feed', frame)

         # Break the loop when 'q' is pressed
         if cv2.waitKey(1) & 0xFF == ord('q'):
             break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()