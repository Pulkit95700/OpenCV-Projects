import cv2
import mediapipe as mp
import numpy as np 
import time 
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def cal_angle(a,b,c):
    a = np.array(a) 
    b = np.array(b) 
    c = np.array(c) 
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle

counter = 0
stage = None

cap = cv2.VideoCapture("0.mp4.mp4")
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose: # pose objesinin hazırlanması.
    
    prev_frame_time = 0
    new_frame_time = 0

    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.resize(frame,(640,480),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
       

        results = pose.process(image)
        

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

      

        try:
            landmarks = results.pose_landmarks.landmark
            
            hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
            knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
            ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
            
            angle = cal_angle(hip, knee, ankle)
      
            cv2.putText(image, str(angle), 
                           tuple(np.multiply(knee, [640, 480]).astype(int)), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2, cv2.LINE_AA)

            if angle > 160:
                stage = 'down'
            if angle  < 100 and stage == 'down':
                stage = 'up'
                counter += 1
                print(counter) 
        except:
            pass

        new_frame_time = time.time()
        fps2 = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                )
      

        cv2.rectangle(image, (350, 25), (610,75), (255,174,201), -1)
        cv2.rectangle(image, (350, 25), (610,75), (0,0,255))
        cv2.putText(image,str(counter),(380,60), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)
        cv2.putText(image,'REP',(440,60), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2,cv2.LINE_AA)

        cv2.putText(image,"FPS : {0:.2f}".format(fps2),(490,450), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,0,255),2,cv2.LINE_AA)
        # cv2.putText(image,"--KRC--",(25,450), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0,255,0),2,cv2.LINE_AA)
        
        cv2.imshow('POZ TESPIT', image)
     

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    

    cap.release()
    cv2.destroyAllWindows()