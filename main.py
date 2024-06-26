import cv2
import mediapipe as mp
import pyautogui


cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
#to know screen size below line is used
screen_w, screen_h = pyautogui.size()
while True:
     _, frame = cam.read()
     #below line to detect eye focus to control like mouse
     frame = cv2.flip(frame, 1)

     # below line to detect rgb face
     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
     output  = face_mesh.process(rgb_frame)
     landmark_points = output.multi_face_landmarks
     #below code for frame width and height
     frame_h, frame_w, _ =frame.shape
     #below code is detecting pointers on face that is landmarks
     # to move cursor along eye movement id argument is used
     if landmark_points:
          landmarks = landmark_points[0].landmark
          for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
            #to get auto frame size below code is used also move cursor in entire screen
                screen_x = screen_w / frame_w * x
                screen_y = screen_w / frame_h * y
                pyautogui.moveTo(screen_x, screen_y)
# step 5 click button using eye
# below code left variable is to specific landmark this gives yellow blink points

          left = [landmarks[145], landmarks[159]]
          for landmark in left:
             x = int(landmark.x * frame_w)
             y = int(landmark.y * frame_h)
             cv2.circle(frame, (x, y), 3, (0, 255, 255))
#below line for closing eye between two yellow landmarks you can observe changes in output terminal when you close the second eye
          if (left[0].y - left[1].y) < 0.004:
              pyautogui.click()
              pyautogui.sleep(2)

     cv2.imshow('Eye mouse controller', frame)
     cv2.waitKey(1)








