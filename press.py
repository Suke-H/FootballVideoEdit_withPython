import cv2
import ffmpeg as fp
import os
import numpy as np
from glob import glob
import subprocess
import re
import shutil
import random

####################################################################
#コーデックを考慮しないならffmpeg -i <in> -crf 10 <out>で済む
#windows10では見れない？ためmp4にするか、コーデックをH.264(265)にする
#1.
#(1)mp4に変換：ffmpeg -i <~.MTS> -vcodec copy -acodec copy <~.mp4>
#(2)圧縮:ffmpeg -i <~.mp4> -crf 30 <~.mp4>

#2.
#(1)圧縮：ffmpeg -i <~.MTS> -crf 30 <~.MTS>
#(2)H.264：ffmpeg -i <~.MTS> -vcodec libx264 <~.MTS>
####################################################################


ori_paths = sorted(glob("**/**.MTS"), key=lambda s: int(re.findall(r'\d+', s)[1]))
print(ori_paths)

#con_paths = []

for i, path in enumerate(ori_paths):
    #con_paths.append("c1/"+path)

    ###MTS->mp4
    mp4path = os.path.splitext(path)[0] + '.mp4'
    #print(mp4path)
    
    cmd = "ffmpeg -i " + path + " -vcodec copy -acodec copy " + "c1/"+mp4path
    subprocess.call(cmd, shell=True)
    
    ####圧縮
    cmd = "ffmpeg -i " + "c1/"+mp4path + " -crf 30 " + "c2/"+mp4path
    subprocess.call(cmd, shell=True)
    


#print(con_paths)
