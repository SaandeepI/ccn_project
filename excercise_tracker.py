import cv2
import mediapipe as mp
import numpy as np
import streamlit as st
import streamlit_webrtc

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

class ExerciseTracker:
    def __init__(self):
        self.pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.curl_stage_left = None
        self.curl_stage_right = None
        self.curl_counter_left = 0
        self.curl_counter_right = 0
        self.pushup_counter = 0
        self.pushup_stage = None
        self.squat_counter = 0
        self.squat_stage = None
        self.process_exercise = None

    @staticmethod
    def calculate_angle(a, b, c):
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        return angle

    def draw_counters(self, image):
        cv2.putText(image, f'Left Bicep Curls: {self.curl_counter_left}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(image, f'Right Bicep Curls: {self.curl_counter_right}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(image, f'Pushups: {self.pushup_counter}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(image, f'Squats: {self.squat_counter}', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    def process_frame(self, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = self.pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark

            if self.process_exercise:
                self.process_exercise(landmarks)

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            self.draw_counters(image)
        except Exception as e:
            print(e)
        return image

    def process_bicep_curls(self, landmarks):
        # Bicep curl logic for both arms
        for side in ["LEFT", "RIGHT"]:
            shoulder = landmarks[getattr(mp_pose.PoseLandmark, f"{side}_SHOULDER").value]
            elbow = landmarks[getattr(mp_pose.PoseLandmark, f"{side}_ELBOW").value]
            wrist = landmarks[getattr(mp_pose.PoseLandmark, f"{side}_WRIST").value]

            curl_angle = self.calculate_angle([shoulder.x, shoulder.y], [elbow.x, elbow.y], [wrist.x, wrist.y])

            if curl_angle > 160:
                setattr(self, f"curl_stage_{side.lower()}", "down")
            if curl_angle < 30 and getattr(self, f"curl_stage_{side.lower()}") == "down":
                setattr(self, f"curl_stage_{side.lower()}", "up")
                counter = getattr(self, f"curl_counter_{side.lower()}") + 1
                setattr(self, f"curl_counter_{side.lower()}", counter)
                print(f"{side} Bicep Curls:", counter)

    def process_pushups(self, landmarks):
        for side in ["LEFT", "RIGHT"]:
            shoulder = landmarks[getattr(mp_pose.PoseLandmark, f"{side}_SHOULDER").value]
            elbow = landmarks[getattr(mp_pose.PoseLandmark, f"{side}_ELBOW").value]
            wrist = landmarks[getattr(mp_pose.PoseLandmark, f"{side}_WRIST").value]

            pushup_angle = self.calculate_angle([shoulder.x, shoulder.y], [elbow.x, elbow.y], [wrist.x, wrist.y])

            if pushup_angle > 160:
                self.pushup_stage = "down"
            if pushup_angle < 30 and self.pushup_stage == "down":
                self.pushup_stage = "up"
                self.pushup_counter += 1
                print("Pushups:", self.pushup_counter)

    def process_squats(self, landmarks):
        hip_left = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
        knee_left = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]
        ankle_left = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value]

        hip_right = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
        knee_right = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]
        ankle_right = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value]

        squat_angle_left = self.calculate_angle([hip_left.x, hip_left.y], [knee_left.x, knee_left.y], [ankle_left.x, ankle_left.y])
        squat_angle_right = self.calculate_angle([hip_right.x, hip_right.y], [knee_right.x, knee_right.y], [ankle_right.x, ankle_right.y])

        if squat_angle_left > 160 and squat_angle_right > 160:
            self.squat_stage = "up"
        if squat_angle_left < 90 and squat_angle_right < 90 and self.squat_stage == "up":
            self.squat_stage = "down"
            self.squat_counter += 1
            print("Squats:", self.squat_counter)

class VideoTransformer(streamlit_webrtc.VideoTransformerBase):
    def __init__(self, exercise):
        self.exercise_tracker = ExerciseTracker()
        if exercise == "Bicep Curls":
            self.exercise_tracker.process_exercise = self.exercise_tracker.process_bicep_curls
        elif exercise == "Pushups":
            self.exercise_tracker.process_exercise = self.exercise_tracker.process_pushups
        elif exercise == "Squats":
            self.exercise_tracker.process_exercise = self.exercise_tracker.process_squats

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = self.exercise_tracker.process_frame(img)
        return img

def create_exercise_tracker(exercise):
    return lambda: VideoTransformer(exercise)


def main():
    st.title("Exercise Tracker")

    exercise = st.sidebar.selectbox(
        "Select exercise",
        ("Bicep Curls", "Pushups", "Squats")
    )

    webrtc_ctx = streamlit_webrtc.webrtc_streamer(
        key="example",
        video_processor_factory=create_exercise_tracker(exercise)
    )

    while True:
        if webrtc_ctx.video_transformer:
            result = webrtc_ctx.video_transformer.result_queue.get()
            st.table(result)
        else:
            break

if __name__ == "__main__":
    main()
