<h3>System and Software Requirements</h3>

To run the Exercise Tracker AI App, you will need the following system and software requirements:

1) Python 3.7 or higher<br>
2) A webcam or integrated camera<br>
3) A modern web browser (e.g., Chrome, Firefox, or Safari)

Additionally, you will need to install the following Python packages:

OpenCV: pip install opencv-python<br>
MediaPipe: pip install mediapipe<br>
Streamlit: pip install streamlit<br>
Streamlit-WebRTC: pip install streamlit-webrtc<br>


To run the provided Streamlit app, follow these steps:

Install the necessary dependencies as above.<br>
Ensure that you have Python 3.x installed on your machine.<br>
Then, open a terminal or command prompt, and install the required packages with the following command:<br>
pip install streamlit streamlit-webrtc opencv-python mediapipe numpy

Save the app code: Copy the provided code and save it as a Python file (e.g., exercise_tracker.py).<br>
Run the app: In the terminal or command prompt, navigate to the directory where you saved the Python file, and run the following command:<br>
streamlit run exercise_tracker.py<br>
Open the app in your browser: Streamlit will display a message in the terminal with a local URL (e.g., http://localhost:8501).<br>
Open this URL in your web browser to interact with the Exercise Tracker app. You can select an exercise in the sidebar and see the webcam feed with the exercise counter.

<h3>Notes</h3>

1) First, select the excercise you want to perform using the drop-down bar and only then start the camera.
If you want to change the excerise. Stop the camera and then select the excercise you want to perform from the drop-down and then start the camera again.

2) When using the app, ensure that you have a stable internet connection and that your webcam is functioning properly.

3) The app's performance may vary depending on your system's hardware and processing capabilities. For optimal results, use a computer with a dedicated GPU.<br>

4) The BlazePose model used in the app may not accurately detect or track poses in certain lighting conditions or with complex backgrounds.<br>

5) To improve pose detection, try using the app in a well-lit environment with a simple background.<br>

6) To properly execute the bicep curl exercise, one should face forward, whereas for squats, it is one should face sideways.
