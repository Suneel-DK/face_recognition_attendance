Face Recognition Attendance System

This project is a Face Recognition Attendance System that captures a live image from a webcam, compares it with stored face images, and marks attendance in an Excel sheet (attendance.xlsx).

📌 Features

Uses DeepFace for face verification.

Automatically stops when a face is recognized.

Marks attendance in an Excel sheet with a timestamp.

Allows users to add new faces by placing images in the images/ folder.

🚀 Getting Started

1️⃣ Clone the Repository

git clone https://github.com/Suneel-DK/face_recognition_attendance.git
cd face_recognition_attendance

2️⃣ Install Dependencies

Ensure you have Python installed, then run:

pip install opencv-python pandas deepface openpyxl

3️⃣ Setup Known Faces

Place images of people in the images/ folder.

File names should be the person's name (e.g., virat.jpg).

4️⃣ Run the Script

python main.py

5️⃣ How It Works

Opens the webcam and captures an image.

Compares the image with stored images in the faces/ folder.

If a match is found, attendance is marked in attendance.xlsx.

The script stops automatically after recognizing a face.

Press q to exit manually.

📂 Project Structure

/face-attendance
  ├── images/             # Folder for known faces
  │     ├── virat.jpg
  │     ├── john.png
  ├── main.py             # Face recognition script
  ├── attendance.xlsx     # Auto-generated attendance file
  ├── README.md           # Instructions (this file)

❗ Troubleshooting

If you get ModuleNotFoundError, ensure dependencies are installed.

Ensure images are clear and well-lit for better recognition.

📌 Future Improvements

Add support for multiple face detection in a single frame.

Store attendance data in a database instead of an Excel sheet.

✅ Now try it out and mark attendance effortlessly! 🚀