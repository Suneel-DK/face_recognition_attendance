import cv2
import os
import pandas as pd
from datetime import datetime
from deepface import DeepFace

# Load reference images
KNOWN_FACES_DIR = "faces"
known_faces = {}

# Load known faces
for filename in os.listdir(KNOWN_FACES_DIR):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        path = os.path.join(KNOWN_FACES_DIR, filename)
        name = os.path.splitext(filename)[0]  
        known_faces[name] = path

# Initialize webcam
cap = cv2.VideoCapture(0)

# Check if the attendance sheet exists
excel_file = "attendance.xlsx"
if not os.path.exists(excel_file):
    df = pd.DataFrame(columns=["Name", "Timestamp"])
    df.to_excel(excel_file, index=False)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Show the live video feed
    cv2.imshow("Face Recognition", frame)

    # Save the captured frame as a temporary image
    cv2.imwrite("temp.jpg", frame)

    # Compare the captured face with known faces
    for name, known_image in known_faces.items():
        try:
            result = DeepFace.verify("temp.jpg", known_image, model_name="VGG-Face", enforce_detection=False)

            if result["verified"]:
                print(f"✅ Match found: {name}")

                # Load existing data
                df = pd.read_excel(excel_file)

                # Append new entry
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_entry = pd.DataFrame({"Name": [name], "Timestamp": [timestamp]})
                df = pd.concat([df, new_entry], ignore_index=True)

                # Save to Excel
                df.to_excel(excel_file, index=False)
                print(f"✅ Attendance marked for {name} at {timestamp}")

                cap.release()
                cv2.destroyAllWindows()
                os.remove("temp.jpg")  # Delete the temporary image
                exit()  # Stop the script

        except Exception as e:
            print(f"Error processing {name}: {e}")

    # Press 'q' to exit manually
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
