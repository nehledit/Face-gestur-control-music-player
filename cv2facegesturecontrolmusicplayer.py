import cv2
import time as t
import vlc
v=cv2.VideoCapture(0)
b=0
fd=cv2.CascadeClassifier(r'C:\Users\hp\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml')
player=vlc.MediaPlayer(r'F:\other files\pendrive\runtheworld.mp3')
w2=[]
vol=30
while True:
    r,i=v.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    f=fd.detectMultiScale(j)
    X=[]
    Y=[]
    W=[]
    H=[]
    for (x,y,w,h) in f:
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),3)
        
        X.append(x)
        Y.append(y)
        W.append(w)
        H.append(h)

    print(len(f))
    cv2.imshow('img',i)    
    k=cv2.waitKey(1)
    
    player.audio_set_volume(vol)
    if (len(f)>=1):
        player.play()
        
        print(f[0][2])
        w2.append(f[0][2])
        print(w2[-4:])
        w21=w2[-4:].copy()
        w21.sort()
        print(w21)
        if(w2[-4:]==w21):
            
            vol=vol+5
            print('vol inc')
            print(vol)
        w22=w2[-4:].copy()
        w22.sort(reverse=True)
        print(w22)
        if(w2[-4:]==w22):
            
            vol=vol-5
            print('vol dec')
            print(vol)
        
            
        
        
##        while True:
##            W2=[]
##            W2.append(f[0][2])
##            for h in range(0,len(W2)-1):
##                if (W2[h]<W2[h+1]):
##                    player.audio_set_volume(h*10)
##                else:
##                    break
##            for h in range(0,len(W2)-1):
##                if (W2[h]>W2[h+1]):
##                    player.audio_set_volume(h/10)
##                else:
##                    break
##                
                
            
        
    elif(len(f)==0):
        player.stop()
    
    
    
    print(r)
    
    
    if(k==ord('q')):
        cv2.destroyAllWindows()
        v.release()
        player.stop()
        break    
    

        
##    l=cv2.add(i,b)
##    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
##    r,g=cv2.threshold(j,127,255,0)
##    cv2.imshow('black',d)
##    cv2.imshow('digital',g)
##    cv2.imshow('gray',j)
##Project- Multi object detection system-10
##If you get 2 or more than 2 faces swap them
##you can figure if youve touched your face on the basis of length of face then after detecting if yuor face has been detected then play a song
##        face-play
##        no-pause
##        width-volume
##    install library - python-vlc
##    pygame- model mixer

    
