import os
import cv2
import mediapipe as mp

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
 
number_of_classes = 27
classes = [chr(i) for i in range(65, 91)] + ['SPACE']
dataset_size = 100

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

cap = cv2.VideoCapture(0)  # Change to 0 for your main webcam
for letter in classes:
    class_dir = os.path.join(DATA_DIR, letter)
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)
    
    print(f'Collecting data for class {letter}')    

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        cv2.putText(frame, 'Press "Q" when ready', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            continue

        # Detect hand
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        # Only save if hand is detected
        if results.multi_hand_landmarks:
            cv2.imwrite(os.path.join(class_dir, f'{counter}.jpg'), frame)
            counter += 1
            cv2.putText(frame, f'Captured: {counter}/{dataset_size}', (50,80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        # Drawn for visual feedback
        if results.multi_hand_landmarks:
            mp_drawing = mp.solutions.drawing_utils
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
