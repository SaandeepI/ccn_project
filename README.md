<h2>Group 18 CCN Project - AI Gym Assistant</h2>

<h3>Introduction</h3>

This Exercise Tracker application is a web-based AI gym assistant that uses the BlazePose pre-trained model from the MediaPipe library to track and count repetitions of bicep curls and squats. It provides users with real-time feedback, enabling them to monitor their exercise performance and progress. By utilizing a pretrained BlazePose model and incorporating it into a Streamlit application, the app serves as a personal AI gym assistant. This project aims to address the challenge of tracking exercises and maintaining proper form, promoting a more effective and safer workout experience.

![image](https://user-images.githubusercontent.com/124635398/233852762-93fbae58-8e47-4365-9250-5652e42058e5.png)


<h3>Implementation Details</h3>

The app is built using Python, OpenCV, MediaPipe, Streamlit, and Streamlit-WebRTC. The architecture of the app consists of the following components:

BlazePose model: A pretrained model from MediaPipe, responsible for detecting and tracking human poses in real-time.<br>

ExerciseTracker class: A custom class that processes video frames, analyzes the pose data, and counts exercise repetitions.<br>

VideoTransformer class: A custom class that inherits from Streamlit-WebRTC's VideoTransformerBase class, responsible for handling video processing and transformation.<br>

Streamlit app: The frontend user interface, built using Streamlit, which allows users to select an exercise type and view their webcam feed with pose detection and exercise counters.<br>

The app processes video frames from the user's webcam, detects human poses using the BlazePose model, and counts exercise repetitions based on specific angles and stages (e.g., up/down). The processed frames are then displayed in the frontend, showing the user's pose, skeleton connections, and exercise counters.

Streamlit-WebRTC: This library extends the Streamlit framework to enable real-time video processing. It creates a separate WebSocket connection for handling video streams, using the WebRTC (Web Real-Time Communication) protocol, which is built for real-time peer-to-peer communication.

WebRTC protocol: WebRTC is an open-source project that enables real-time communication of audio, video, and data in web browsers and mobile applications through simple APIs. It uses a combination of protocols like RTP (Real-time Transport Protocol) for media transfer, RTCP (Real-time Transport Control Protocol) for quality control, and ICE (Interactive Connectivity Establishment) for NAT traversal and establishing peer-to-peer connections.

The Exercise Tracker application's networking aspect relies on Streamlit and Streamlit-WebRTC for communication between the frontend and backend. Streamlit sets up a web server and manages WebSocket connections for app updates, while Streamlit-WebRTC establishes separate WebSocket connections for real-time video processing using the WebRTC protocol.

<h3>Description of the application</h3>

User Interface: The application presents a clean and simple user interface using the Streamlit library. Users can select the exercise type (bicep curls or squats) from a sidebar. The main area displays the real-time video feed from the user's camera, overlaying the count of each exercise performed.

Real-time Video Streaming: Streamlit-WebRTC is employed to capture the user's video feed and stream it to the application. The video frames are processed in real-time, providing instant feedback to users as they perform the exercises.

Pose Estimation: The application uses the BlazePose pre-trained model from the MediaPipe library to estimate the user's body pose in each video frame. The model detects key body landmarks (such as shoulders, elbows, wrists, hips, knees, and ankles), which are then used to calculate the angles required for tracking exercises.

Angle Calculation: The application calculates angles between relevant body landmarks using the NumPy library. These angles are critical in determining the user's body position during exercises and detecting whether a repetition has been completed.

Exercise Tracking and Counting: The application includes separate methods for tracking and counting each exercise type (bicep curls and squats). These methods utilize the calculated angles to determine when a repetition is complete and increment the corresponding counters accordingly.

Visual Feedback: The application overlays the count of each exercise on the video feed using OpenCV. This provides real-time visual feedback to the user, allowing them to monitor their performance and progress.

This application is deployed in the streamlit community cloud.<br>
https://saandeepi-ccn-project-excercise-tracker-group-18-iterati-zus8wt.streamlit.app/

Please note that sometimes the streamlit-webrtc connection encounter issues due to several reasons. In such cases:

Make sure you have installed all the latest versions of the dependencies.

Check your network settings: Ensure that your network settings, firewall, and router configurations allow WebRTC connections. You may need to check your router settings or consult your network administrator for assistance.

Inspect browser compatibility: Ensure that your app is compatible with the browser you are testing it on. While most modern browsers support WebRTC, there might be specific features or configurations that are not fully compatible with certain browser versions.

Sometimes the ICE state connection might close pre-maturely. You might have to create a new TURN server to establish the connection. 

<b>To verify the project:</b><br>
Download the <b>excercise_tracker.py</b> file and follow the <b>instructions.md</b> file in the repository on how to run and visualize the output.

<h3>Scope for improvement</h3>

Please note that this code accurately detects only the bicep-curls and squats. Pushups were added in the code as a future improvement and the code logic for the pushup excercise needs to be refined.

Many other excercises can also be included in the application. 

Try to use a different AI model that accurately detects the poses and also use a different method to deploy this application.

Refine the excercise code logics using more complex mathematical calculations to improve the accuracy.

Store the users progress and provide data predictions on the fitness goals.





<h3>Challenges</h3>

During the development of the Exercise Tracker AI App, several challenges were encountered:

Model accuracy: The BlazePose pre-trained model may not always provide accurate pose estimations in various lighting conditions, camera angles, or when the user is wearing loose clothing. This can result in incorrect exercise counting or tracking.

Implementing exercise logic: Coding the logic for detecting and counting different exercises was complex due to the need to accurately interpret pose data and identify the specific stages of each exercise.

Some users may have different exercise techniques or body types, leading to occasional inconsistencies in detecting and counting repetitions.

Real-time video processing: Ensuring smooth and real-time video processing was challenging, as it required optimizing the performance of the application and handling video frames efficiently.

Integration of multiple libraries: Combining OpenCV, MediaPipe, Streamlit, and Streamlit-WebRTC required an understanding of each library's functionality and compatibility to successfully integrate them into the application.






