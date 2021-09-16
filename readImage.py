import cv2
import numpy as np

cap=cv2.VideoCapture("/content/drive/MyDrive/readVideoImage/2_2.avi")
is_opened=cap.isOpened

# 视频信息获取
fps=cap.get(cv2.CAP_PROP_FPS)
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 设置求暗信号的时间点
time_point=[5,10,15]

# 建一个列表用来储存平均灰度值
gray_list=[]

# 元素为存储每张图像中通道的灰度的均值
per_image_gray=[]

# 元素为存储每张图像灰度的均值
image_gray_list=[]

# 元素为存储每3张图像灰度的均值
image_gray_list_mean=[]
image_num=0
i=0
while(is_opened):
    # if image_num>=time_point[-1]*30+3:
    #     break
    (frame_state,frame)=cap.read()
    if frame_state==False:
        break
    if image_num==time_point[i]*120 or image_num==time_point[i]*120+1 or image_num==time_point[i]*120+2:   
        if frame_state:
            per_image_gray.append(np.mean(frame[:,:,0]))
            per_image_gray.append(np.mean(frame[:,:,1]))
            per_image_gray.append(np.mean(frame[:,:,2]))
            image_gray_list.append(np.mean(per_image_gray))
            per_image_gray.clear()
        else:
            print('图片读取错误！')
            break
    if len(image_gray_list)==3:
        image_gray_list_mean.append(np.mean(image_gray_list))
        image_gray_list.clear()
        if i<2:
            i=i+1
    image_num=image_num+1
print('暗信号值为:',image_gray_list_mean)
print('num_image:%d'%(image_num))
print("finish!")