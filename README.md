# Sign_language_detector

A Python-based real-time Sign Language Recognition system that detects hand gestures (A–Z + SPACE), builds sentences, and converts them to speech.

This project uses OpenCV, MediaPipe, and RandomForest to detect hand landmarks and classify gestures.

Features

Detects all alphabet letters (A-Z) and a SPACE gesture.

Builds sentences in real time from detected letters.

Text-to-speech conversion of the sentence.

Live preview of detected hand and gesture.

Controls:

c → Clear the sentence

s → Speak the sentence aloud

q → Quit the program and safely release camera

Project Structure
Sign_language_detector/
│
├── collect_img.py          # Collect hand gesture images
├── create_dataset.py       # Extract hand landmarks and create dataset
├── train_classifier.py     # Train RandomForest model
├── inference_classifier.py # Real-time detection and TTS
├── data/                   # Collected images (0-26 folders)
├── data.pickle             # Saved dataset with landmarks
├── model.p                 # Trained model
└── README.md

Setup Instructions

Clone the project or download files to your local machine.

Create a virtual environment (optional):

python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Mac/Linux


Install required packages:

pip install opencv-python mediapipe==0.10.21 numpy scikit-learn pyttsx3 matplotlib

Steps to Run
1. Collect Images

Open collect_img.py and run:

python collect_img.py


Press q to start capturing each gesture.

Collect 100 images per gesture (0 = A, 1 = B, …, 26 = SPACE).

2. Create Dataset

Run create_dataset.py to extract hand landmarks and save as data.pickle:

python create_dataset.py

3. Train Model

Run train_classifier.py to train a RandomForest classifier:

python train_classifier.py


This will generate model.p in your folder.

4. Run Real-Time Detection

Run inference_classifier.py:

python inference_classifier.py


Make hand gestures in front of the camera.

Sentence will be built automatically.

Use keys:

c → Clear sentence

s → Speak sentence aloud

q → Quit

Skills Learned

Computer Vision: Hand detection and landmark extraction using MediaPipe.

Machine Learning: Training a RandomForest classifier to recognize gestures.

Real-Time Systems: Using OpenCV for live video capture and prediction.

Text-to-Speech Integration: Converting recognized gestures into spoken words.

Future Enhancements

Extend detection to full words or phrases, not just individual letters.

Add more gestures for punctuation or commands.

Improve accuracy by using deep learning models (CNN or LSTM).
