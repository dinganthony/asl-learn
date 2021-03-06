import mediapipe as mp
import cv2
import SimpleGestureDetector as gd

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# From Mediapipe Hands Example
#For webcam input:
cap = cv2.VideoCapture(0)
gesture = gd.SimpleGestureDetector()
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    width  = cap.get(3)  # float `width`
    height = cap.get(4)  # float `height`
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        #print('hand_landmarks:', hand_landmarks)
        # print(
        #     f'Index finger tip coordinates: (',
        #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * width}, '
        #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * height})'
        # )
        
        # Detect Gestures
        gesture.simpleGesture(hand_landmarks.landmark)
        
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()