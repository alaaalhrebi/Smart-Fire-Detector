
# 🔥 Fire Detection AI with Real-Time Camera Monitoring

A simple yet effective fire detection system using a pre-trained deep learning model and your webcam. When fire is detected in the camera frame, the system plays an alarm sound.

## 📸 How it Works

1. Captures video frames using your computer's webcam.
2. Resizes and normalizes each frame.
3. Feeds the frame to a pre-trained TensorFlow model.
4. If fire is detected with confidence > 0.5:
   - A fire alert is printed.
   - An alarm sound (`alarm.mp3`) is played.

## 🚀 Installation

## 🔗 Model File (Google Drive)
This project uses a pre-trained model stored on Google Drive due to file size limitations.

The model will be downloaded automatically when the app runs using the `gdown` library.

**Google Drive Link:** [Download model](https://drive.google.com/file/d/1CEI7wUXISLEoAfXlE2HNl23TzcqHroLe/view?usp=share_link)



### 1. Clone the repository

```bash
git clone https://github.com/alaaalhrebi/fire-detection-ai.git
cd fire-detection-ai


