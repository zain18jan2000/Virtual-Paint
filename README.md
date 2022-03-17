# Virtual-Paint
Python Program to implement Virtual Paint using Media Pipe

<h1>DEPENDENCIES:</h1>
1) Mediapipe <br>
2) OpenCV <br>
3) math <br>
4) Numpy <br>

<h1>WHAT IS MEDIAPIPE ?</h1>
<p>MediaPipe is a Framework for building machine learning pipelines for processing time-series data like video, audio, etc. This cross-platform Framework works in Desktop/Server, Android, iOS, and embedded devices like Raspberry Pi and Jetson Nano. </p>

<h1>WHAT IS MEDIAPIPE HANDS ?</h1>
<p>MediaPipe contains MediaPipe Hands, which is a high-fidelity hand and finger tracking solution. It employs machine learning to infer 21 3D landmarks of a hand from just a single frame. It utilizes an ML pipeline consisting of multiple models working together. A palm detection model that operates on the full image and returns an oriented hand bounding box. A hand landmark model that operates on the cropped image region defined by the palm detector and returns high-fidelity 3D hand keypoints as shown below. </p>

![hand_landmarks](https://user-images.githubusercontent.com/82854685/158783871-7edf09a1-4f47-465e-a09f-3082038356ae.png)

<h1>WHAT'S INCLUDED IN THIS REPOSITORY ?</h1>
1) <b>handTrackingModule.py</b> <p>This module is used for the detection of hands, to identify their landmarks and to detect their positions.</p>
2) <b>Virtual_Paint.py</b> <p>This is the main module used for real time implementation of virtual paint, utilizing handTrackingModule.py to detect the position of index  and middle finger for drawing and selecting the colors.</p>
