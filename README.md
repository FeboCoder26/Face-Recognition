# Face Recognition Screenshot App

A simple Python application that uses **OpenCV** to capture live video from your webcam, take screenshots, and exit the feed with keyboard shortcuts. This project is perfect for beginners to computer vision or anyone wanting a quick way to capture webcam frames.

## Features

- 📷 **Live Webcam Feed**: Real-time video streaming from your webcam.
- 🖼️ **Take Screenshots**: Press **'s'** to save the current frame as an image.
- ❌ **Exit Easily**: Press **'a'** to stop the video feed and close the app.
- 🐍 **Minimal Dependencies**: Only requires OpenCV and Python's standard library.

## Demo

![screenshot demo](demo.gif) <!-- Replace with your actual demo image or GIF if available -->

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/FeboCoder26/Face-Recognition.git
   cd Face-Recognition
   ```

2. **Install dependencies**
   ```bash
   pip install opencv-python
   ```

## Usage

1. Run the script:
   ```bash
   python face_recognition.py
   ```

2. The webcam window will open:
   - Press **'s'** to take a screenshot (saved in the current directory).
   - Press **'a'** to exit the application.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)

## How It Works

- The app initializes the webcam using OpenCV.
- It displays the video stream in a window.
- When you press **'s'**, the current frame is saved as an image file.
- Press **'a'** to release the webcam and close the window.

## Project Structure

```
Face-Recognition/
├── face_recognition.py
├── README.md
└── [saved_screenshots]
```

## Troubleshooting

- **Webcam not detected**: Ensure your camera is properly connected and not used by another application.
- **Permission errors**: On some systems, you may need to grant Python access to your camera.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [OpenCV](https://opencv.org/) for computer vision functionality

---

Feel free to contribute, open issues, or suggest improvements!
