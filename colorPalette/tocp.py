import cv2
import numpy as np
from sklearn.cluster import KMeans
import os


def clean_old():
    files = [f for f in os.listdir('.') if f.endswith((".jpg",".jpeg",".png",".gif",".tiff",".raw",".webp")) ]
    files.sort(key=os.path.getctime)
    for i,f in enumerate(files[:-20]):
        print(f)
        os.remove(f)

def show_final_img(img, pal ):
    border_size=int(img.shape[0]*0.015)
    pal[0:round(border_size), :, :]=255
    final=np.concatenate((img, pal))
    final=cv2.copyMakeBorder(final,border_size,border_size,border_size,border_size,cv2.BORDER_CONSTANT,value=(255,255,255))
    
    return final


def palette(clusters,img):
    border_size=int(img.shape[0]*0.015)
    width=img.shape[1]
    palette = np.full((round(img.shape[0]*0.15), width, 3), 255)
    steps = (width+border_size)/clusters.cluster_centers_.shape[0]
    
    for idx, centers in enumerate(clusters.cluster_centers_): 
        if(idx+1==len(clusters.cluster_centers_)):
            palette[:, int(idx*steps):(int((idx+1)*steps)), :] = centers
        else:    
            palette[:, int(idx*steps):(int((idx+1)*steps))-int(width*0.01), :] = centers
    return palette


def transform(f_name):
    img=cv2.imread(f_name)
    img_temp  = cv2.resize(img, (150, 150)) 
    #final_path="cp_image.jpg"
    clt_3 = KMeans(n_clusters=8)
    clt_3.fit(img_temp.reshape(-1, 3))
    f=show_final_img(img, palette(clt_3,img))
    final_path='cp_'+f_name
    cv2.imwrite(final_path, f)
    #clean_old() #To clean Old uploaded file
    return final_path