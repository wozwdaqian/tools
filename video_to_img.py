import cv2
import os
from tqdm import tqdm


dirPath = "video/" # 视频文件夹
saveDir = "image/" # 图片文件夹
max_num = 300 # 每个文件夹保存图片的最大数量
step = 60 # 隔几帧保存一次

datatime = "0110" # 日期
files = os.listdir(dirPath)
count = 0 # 视频帧的计数
imgCount = 0 # 保存图片的计数
dir_name = 0 # 保存的文件夹名字

for oneFile in tqdm(files):
    if oneFile.endswith('.mp4') or True :
        vidcap = cv2.VideoCapture(dirPath + oneFile)
        success, image = vidcap.read()
        while success:
            if count % step == 0:
                success, image = vidcap.read()
                if imgCount % max_num == 0:
                    dir_name += 1
                    if os.path.exists(os.path.join(saveDir, str(dir_name))) is False:
                        os.makedirs(os.path.join(saveDir, str(dir_name)))
                if success:
                    savePath = os.path.join(saveDir, str(dir_name), datatime + '_' + ("%06d.jpg"%imgCount))
                    cv2.imwrite(savePath, image)
                    # print(oneFile, savePath)
                    imgCount +=1

            else:
                vidcap.grab()
            count += 1

print("all done")

