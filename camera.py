import cv2
import mediapipe as mp
import numpy as np
import math

# Inisialisasi MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Inisialisasi video capture
cap = cv2.VideoCapture(0)

# Membuat canvas untuk menggambar
canvas = np.zeros((480, 640, 3), np.uint8)

# Parameter untuk menebal garis
brushThickness = 15
eraserThickness = 50

# Menentukan apakah sedang menggambar atau menghapus
drawColor = (0, 255, 0)

# Fungsi untuk mencari jarak antara dua titik
def findDistance(p1, p2, img, draw=True):
    x1, y1 = p1
    x2, y2 = p2
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

    if draw:
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

    length = math.hypot(x2 - x1, y2 - y1)
    return length

# Loop utama
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while True:
        # Membaca frame dari webcam
        success, img = cap.read()

        # Flip gambar agar sesuai dengan gerakan tangan
        img = cv2.flip(img, 1)

        # Membuat salinan gambar untuk canvas
        imgCanvas = canvas.copy()

        # Mencari tangan pada frame
        results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Menggambar landmark pada tangan
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Mendapatkan koordinat ujung jari telunjuk dan tengah
                x1, y1 = int(hand_landmarks.landmark[8].x * img.shape[1]), int(hand_landmarks.landmark[8].y * img.shape[0])
                x2, y2 = int(hand_landmarks.landmark[12].x * img.shape[1]), int(hand_landmarks.landmark[12].y * img.shape[0])

                # Menghitung jarak antara kedua jari
                distance = findDistance((x1, y1), (x2, y2), img)

                # Jika jarak cukup dekat, maka gambar
                if distance < 50:
                    cv2.circle(imgCanvas, (x1, y1), brushThickness, drawColor, cv2.FILLED)

        # Menggabungkan gambar asli dan canvas
        imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
        imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
        img = cv2.bitwise_and(img, imgInv)
        img = cv2.bitwise_or(img, imgCanvas)

        # Menampilkan hasil
        cv2.imshow("Image", img)
        cv2.imshow("Canvas", imgCanvas)
        cv2.waitKey(1)