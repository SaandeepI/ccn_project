We have successfully completed all the tasks and objectives outlined for this iteration and accomplished more than intially committed.

1) Developed a working prototype that uses the MediaPipe library and OpenCV to detect and track body landmarks in real-time.

2) Implemented algorithms to calculate angles between body landmarks and detect specific exercises, such as bicep curls, pushups, and squats. (Further optimizations are required for pushups and squats)

3) Designed a user interface using Streamlit to display the real-time video feed along with the exercise count.

4) Created the Streamlit app by incorporating the Streamlit Webrtc package to access the user's webcam for real-time pose detection. (Might require further improvements)


After trying out different models and resolving many errors, we have integrated all the code in the excercise_tracker.py file which is perfectly running and gives the desired results.

<b>How this application works?</b>


The application that we developed uses the MediaPipe Pose estimation library to track a person's movements while performing exercises such as bicep curls, pushups, and squats. The application is built with the Streamlit framework and uses the Streamlit-WebRTC library to process the video stream in real-time.

The pretrained model used in this application is the BlazePose model, which is a part of the MediaPipe library. BlazePose is a lightweight, efficient, and fast human pose estimation model that estimates the 2D human body pose in real-time. MediaPipe is a cross-platform framework for building multimodal applied machine learning pipelines. The Pose model estimates the 2D human body pose in real-time, given an image or video stream. It detects 33 body landmarks, such as wrists, elbows, and shoulders, and provides their coordinates in the image. The exercise tracker application uses these landmarks to calculate angles and track the user's movements while performing exercises.

For the next iteration, we will be deploying the application in the streamlit cloud and further optimize the code in the best way possible.

The instructions on how to run this code and how it works(explanation) will be covered in the next iteration.

Sample Demo ScreenShots:

![image](https://user-images.githubusercontent.com/124635398/229953286-77041049-9ba6-467e-a3a0-dbb0caff070b.png)
![image](https://user-images.githubusercontent.com/124635398/229953358-9454b1d4-a9e8-423b-b123-8fcce740e259.png)

