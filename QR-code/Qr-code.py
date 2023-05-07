# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 01:56:48 2022

@author: neslihan dogan
"""
''' QR kodu sağ alt köşeden okunur. Pikseller, 8 piksel başına bir bayt
 içeren 8 kişilik gruplar olarak okunur. En sık kullanılan QR boyutu, yaklaşık
 50 ASCII karakterini tutabilen 29 x 29 ve 33 x 33 arasındadır.
'''
import cv2
import numpy as np
import random
'''arkaplanı beyaza boyamak için 255 ile çarptım'''
img=255*np.ones((512,512,4),np.uint8)

print(img)#img pixel bıyultlarını göstermek için 


for i in range(1100):# genel kısmına rastgele siyah diktörtgenler oluşturmak
 #random.randrange(start, stop, step)
    X1 = random.randrange(20,490,10)
    Y1 = random.randrange(70,490,10)
    X2 =X1+11
    Y2 =Y1+11
 
    rkareler=cv2.rectangle(img,(X1,Y1),(X2,Y2),(0,0,0),-1)

    cv2.imshow("kare", rkareler)
    
for i in range(100):#üst kısmına rastgele siyah dikdörtgenler oluşturuldu
    X1 = random.randrange(70,420,10)#x1 ekseninde başlangıç ve bitiş aralığı random olarak atama
    Y1 = random.randrange(20,70,10)#y1 ekseninde başlangıç ve bitiş aralığı random olarak atama
    X2 =X1+11
    Y2 =Y1+11
    
    rkareler=cv2.rectangle(img,(X1,Y1),(X2,Y2),(0,0,0),-1)
    
    cv2.imshow("kare", rkareler)
    
    
for i in range(100):#orta
        X1 = random.randrange(140,420,10)
        Y1 = random.randrange(70,420,10)#y1 ekseninde başlangıç ve bitiş aralığı random olarak atama
        X2 =X1+11
        Y2 =Y1+11
        
        rkareler=cv2.rectangle(img,(X1,Y1),(X2,Y2),(0,0,0),-1)
        
        cv2.imshow("kare", rkareler)
        
        
        
'''sol üst kareler -1 le içi boyandı'''
kare1=cv2.rectangle(img,(20,20),(50,50),(0,0,0),-1)#küçük sol üsteki kare
kare1=cv2.rectangle(img,(0,0),(70,70),(0,0,0),10)#büyük sol üsteki kare


'''sağ üst kareler'''
#(x1,y1),(x2,y2),(color),-1(ters döndürme rengi)
kare2=cv2.rectangle(img,(460,20),(490,50),(0,0,0),-1)
kare2=cv2.rectangle(img,(440,0),(510,70),(0,0,0),10)

cv2.imshow("kare", kare1)
cv2.imshow("kare",kare2)


k=cv2.waitKey(0)
if k==ord('q'):
    cv2.imwrite("orcode.jpg",rkareler)#resmi kaydetme işlemi yappar
    print("yeni resim başarı ile kaydedildi :)")
    
    cv2.destroyAllWindows()