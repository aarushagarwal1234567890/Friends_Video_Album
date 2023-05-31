import os
import cv2


path = "images2/Images"

images2 = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        #print(file_name)
               
        images2.append(file_name)
        
#print(len(images))
count = len(images2)

frame = cv2.imread(images2[0])
height, width, channels = frame.shape
size = (width,height)
#print(size)


out = cv2.VideoWriter('project1.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 5, size)

#For SUNSET
#for i in range(0,count-1):

#For SUNRISE
for i in range(count-1,0,-1):
    frame = cv2.imread(images2[i])
    out.write(frame)
    
out.release() # releasing the video generated
print("Done")


