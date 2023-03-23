import cv2
import mediapipe as mp
import numpy as np
import streamlit as st

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def main():
    # Set up video capture
    cap = cv2.VideoCapture(0)
    # Set up mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        st.title("Sample Streamlit Visual for Pose Detection")
        # Display video feed and pose landmarks
        video_placeholder = st.empty()
        # Process video feed
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            # Make detection
            results = pose.process(image)
            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                            mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                            mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                             )    
            except:
                pass
            # Display video feed and pose landmarks
            video_placeholder.image(image, channels="BGR")

if __name__ == "__main__":
    main()
