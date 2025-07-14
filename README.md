
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

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fire-detection-ai.git
cd fire-detection-ai
