import cv2
import numpy as np
import time
from tensorflow.keras.models import load_model
from playsound import playsound
import threading

# تحميل النموذج
model = load_model('fire_detection_model.h5')

# فتح الكاميرا
cap = cv2.VideoCapture(0)

# دالة تشغيل الإنذار
def play_alarm():
    playsound('alarm.mp3')

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ لم يتم التقاط الصورة")
        break

    img_resized = cv2.resize(frame, (224, 224))
    img_normalized = img_resized / 255.0
    img_input = np.expand_dims(img_normalized, axis=0)

    prediction = model.predict(img_input)[0][0]

    label = "🔥 FIRE DETECTED!" if prediction > 0.5 else "✅ No Fire"
    print(label)

    if prediction > 0.5:
        threading.Thread(target=play_alarm).start()
        break

    time.sleep(60)

cap.release()