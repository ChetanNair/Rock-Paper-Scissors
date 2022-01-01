import cv2
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

webcam = cv2.VideoCapture(0)
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

    while webcam.isOpened():
        success, image = webcam.read()
        if not success:
            print("Camera not working")
            continue

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        handNumber = 0
        hand_landmarks = []
        count = 0
        flag = False
        if results.multi_hand_landmarks:
            flag = True
            for hand in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

                label = results.multi_handedness[handNumber].classification[0].label
                for id, landmark in enumerate(hand.landmark):
                    imgH, imgW, imgC = image.shape  # height, width, channel for image
                    xPos, yPos = int(landmark.x *
                                     imgW), int(landmark.y * imgH)
                    hand_landmarks.append([id, xPos, yPos, label])

                # Index Finger
                if hand_landmarks[8][2] < hand_landmarks[6][2]:
                    count += 1
                # Middle Finger
                if hand_landmarks[12][2] < hand_landmarks[10][2]:
                    count += 1
                # Ring Finger
                if hand_landmarks[16][2] < hand_landmarks[14][2]:
                    count += 1
                # Pinky Finger
                if hand_landmarks[20][2] < hand_landmarks[18][2]:
                    count += 1
                # Thumb
                if hand_landmarks[4][3] == "Left" and hand_landmarks[4][1] > hand_landmarks[3][1]:
                    count += 1
                elif hand_landmarks[4][3] == "Right" and hand_landmarks[4][1] < hand_landmarks[3][1]:
                    count += 1
                handNumber += 1
        # Flip the image horizontally for a selfie-view display.
        image = cv2.flip(image, 1)
        if count in [0, 2, 5] and flag:
            if count == 0:
                display = "Rock"
            elif count == 2:
                display = "Scissors"
            elif count == 5:
                display = "Paper"
        else:
            display = "Invalid"

        cv2.putText(image, display, (45, 375),
                    cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 10)
        cv2.imshow('Rock, Paper, Scissors', image)
        if cv2.waitKey(1) & 0xFF == 27:
            break

webcam.release()
cv2.destroyAllWindows()
