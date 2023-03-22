In the last iteration, we attempted to use the TSN (Temporal Segment Network) model for counting bicep curl reps during a livestream. However, we encountered a size 
mismatch issue while attempting to proceed with the model.

While we were unable to proceed with the TSN model, we were able to find an alternative solution for counting bicep curl reps during a livestream. We utilized the 
Mediapipe library to detect the number of bicep curl repetitions, and were able to achieve our desired outcome through this method.

It uses a pre-trained model provided by the Mediapipe library for pose estimation. Specifically, it uses the mp_pose.Pose class which internally loads a pre-trained
model for detecting human poses in images and videos.

The code works perfectly fine and is ready to be integrated with the streamlit app and then we will be hosting it on the heroku or anyother server as a next step.

In parallel, we will have a look into the other models as well and if we found any other model that suits the usecase well and provides the desired output then we will
integrate it into the streamlit app and proceed further on that. 
