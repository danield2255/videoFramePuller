import cv2
import os
import math


#The start time, end time, and frame rate should be in the video title, so these can be 
#different for every video

##List the directory where your video folders are 
vid_directory = "videoDirectory"
videos = [x for x in os.listdir(vid_directory) if (x[0] != ".")] 
for d in videos:
    vidNum = 0
    for file in os.listdir(vid_directory + "/" + d):
        filename = vid_directory + "/" + d+ "/" + os.fsdecode(file)
        print(filename)
        if filename.split("/")[-1][0] == ".":
            continue
        cap = cv2.VideoCapture(filename)
        #format is startTime_endTime_rate
        frameRate = int(cap.get(cv2.CAP_PROP_FPS)) #frame rate on cv is different from our rate        
        startEndRate = filename.split("/")[-1].split("_")
        rate = int(startEndRate[2].split(".")[0])
        startTime = (int(startEndRate[0].split("-")[0])* 60 + int(startEndRate[0].split("-")[1])) * 1000
        endTime = (int(startEndRate[1].split("-")[0])* 60 + int(startEndRate[1].split("-")[1])) * 1000

        cap.set(cv2.CAP_PROP_POS_MSEC, startTime) #point in time(ms) to go to in the video

        frame_num = 0
        output_num = 0


        while(cap.isOpened() and cap.get(cv2.CAP_PROP_POS_MSEC) <= endTime):
            frameId = cap.get(1) #current frame number
            ret, frame = cap.read()
            if (ret != True):
                break
            if (frame_num % (rate * frameRate) == 0):
                ## Here define where the image will be saved, and what the file will be named
                ## There is a default name convention for the file --> videoName_videoNumber_frameNumber.jpg
                out_name = "saveDirectory" + d + "_" + str(vidNum) + "_" +str(output_num) + ".jpg"
                cv2.imwrite(out_name, frame)
                output_num += 1
            frame_num += 1

        cap.release()
        vidNum += 1
