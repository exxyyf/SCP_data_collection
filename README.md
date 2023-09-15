## Pose outliers detection
<b>In this Jupyter Notebook I applied pre-trained model to perform pose estimation in order to find pose outliers inside the dataset.</b> 

There are three pictures in the example: first picture - a paragon picture (person, front view), to which others are compared; second picture - with the wrong pose; third picture - with the right pose. 

As a result of processing, the difference between wrong and right poses compared to the paragon image was seen as difference between cosine and weighted distances between body joints points vectors. Thus, it is possible to implement data cleaning by assesing the pose of each image and comparing distances using distance threshold.

![image](https://github.com/exxyyf/SCP_data_collection/assets/118925388/386812e5-b8aa-4750-b6e4-aa888577d52e)

