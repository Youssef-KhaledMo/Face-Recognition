# Face Recognition using OpenCV & Face Recognition Library

This project demonstrates a real-time **face recognition system** built using **OpenCV** and the **face_recognition** library. The system captures video feeds from a webcam, detects faces, and recognizes authorized persons based on pre-encoded images.

## Project Overview

The goal of this project is to recognize faces in a video stream using a simple deep learning-based face recognition model. The project was trained with only three images—one of the author, one of Lionel Messi, and one of Cristiano Ronaldo—to demonstrate its effectiveness in real-world applications.

## Features

- **Face Detection:** Identify faces in a live webcam feed using OpenCV.
- **Face Recognition:** Match detected faces against a set of known faces.
- **Real-Time Processing:** Process each frame of the webcam feed for real-time face recognition.
- **Bounding Box & Label:** Draw bounding boxes around recognized faces and label them accordingly.

## Demo Video

Watch the demo video to see the project in action:

[![Watch the demo video](https://img.youtube.com/vi/7PQ3tGFSY0o/0.jpg)](https://youtu.be/7PQ3tGFSY0o)

> Click the image or [here](https://github.com/Youssef-KhaledMo/Face-Recognition/blob/main/Demo.mp4) to watch the demo.

## How It Works

The system uses the **face_recognition** library to encode and compare faces. Here's an overview of the main process:

1. **Encode Known Faces:** Pre-process and encode images of known persons.
2. **Capture Video Feed:** Read frames from the default webcam using OpenCV.
3. **Face Detection & Recognition:** For each frame:
   - Detect faces in the frame.
   - Compare detected faces with the encoded faces of known individuals.
   - Draw bounding boxes around recognized faces and label them.
4. **Handling Unknown Faces:** Draw a red bounding box around unknown faces.

### Technologies & Libraries

- **Programming Language:** Python
- **Libraries:** OpenCV, face_recognition, NumPy, OS

## Installation

To get started with the project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Youssef-KhaledMo/Face-Recognition.git
   cd Face-Recognition
   ```

2. **Install the Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

   **Requirements:**
   - OpenCV (`cv2`)
   - face_recognition
   - NumPy

3. **Add Images to the `images/` Directory:**
   - Save images of known individuals (like "Youssef khaled.jpg", "Messi.jpg", and "Ronaldo.jpg") inside the `images` directory. Ensure that each image is named appropriately.

4. **Run the Script:**
   ```bash
   python face_recognition.py
   ```

## Usage

- The webcam feed will appear in a new window when you run the script. The system will detect and recognize faces in the feed.
- A green bounding box with the person's name is displayed if a known face is recognized. Unknown faces are displayed with a red bounding box labeled as "Unknown."
- Press **'q'** to exit the webcam feed.

## Project Structure

```
Face-Recognition/
│
├── images/                     # Folder to store known images
│   ├── Youssef khaled.jpg      # This is my image
│   ├── Messi.jpg
│   └── Ronaldo.jpg
│
├── demo_video.mp4              # Demo video file
├── face_recognition.py         # Main script for face recognition
├── README.md                   # Project documentation
└── requirements.txt            # Project dependencies
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
