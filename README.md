# videoFramePuller
A short python script to pull image frames from folders of videos. The user can set different start times, end times, and frame rates to pull images from each video based on how the video files are named. The script works really well for pulling image frames from multiple videos 

The format of how imput videos should be is '{startTime}\_{endTime}\_{rate}'.mp4. The format of 'startTime' and 'endTime' replaces standard colons(:) with hyphens(-). This format is important to ensure all videos are treated correctly. 

**EX)** So if we wanted to start pulling frames at the 30 second mark in a video, stop at the 11:31 mark, and pull one frame every two seconds we would name the video '00-30_11-31_2.mp4'

Requires a directory to look for videos in, and it should accept videos in most standard formats (mp4, MOV, etc). 

Outputs still images currently as .jpg, and have a name based on the name of the folder they were in, what video they were taken from, and what frame was taken. 

**EX)** So if the program was outputing the 15th frame of the 1st video in a folder called 'vids', then the name of the image would be 'vids_0_14.jpg'. This is because the counting of images and vids are counting from 0. 
