from pygame import mixer
import pygame
import time

def getdate():
    import datetime
    return datetime.datetime.now()


time_1 = getdate()

 




def water():
    print("Clock has Started!!")
    # i = 3600
    i = 1
    while(i <= 3600): #1 hour
        print(i)
        time.sleep(1)
        if(i == 1800): #30 minutes
            # time.sleep(1800)
            pygame.init()
            pygame.mixer.init()
            sounda= pygame.mixer.Sound("eyes.mp3")
            sounda.play()
            user = input("Write 'done' if done ! : ")
            user = user.lower()
            if(user == 'done'):
                print("DO EYE EXERCISE !!!")
                with open("logs.txt","a") as f:
                    f.write(f"[{time_1}] : i did the eye exercise\n")
                    pygame.mixer.pause()
                    
            else:
                pass 
         # n = 2700
        if(i == 2700): # 45 minutes 
            pygame.init()
            pygame.mixer.init()
        
            sounda= pygame.mixer.Sound("exercise.mp3")
            sounda.play()
            user = input("Write 'done' if done ! : ")
            user = user.lower()
            if(user == 'done'):
                print("DO PHYSICAL EXERCISE !!!")
                with open("logs.txt","a") as f:
                    f.write(f"[{time_1}] : i did the physical exercise\n")
                    pygame.mixer.pause()
                    
            else:
                pass 


        # time.sleep(3600)
        
        if(i == 3600): #complete 1 hr
            pygame.init()
            pygame.mixer.init()
            sounda= pygame.mixer.Sound("water.mp3")
            sounda.play()
            user = input("Write 'done' if done ! : ")
            user = user.lower()
            if(user == 'done'):
                print("DRINK 2 CUPS OF WATER !!!")
                with open("logs.txt","a") as f:
                    f.write(f"[{time_1}] : Drank 2 cups of water\n")
                    pygame.mixer.pause()
                    
            else:
                pass 
        i+=1

            # m = 1800
    
 
     
#the function will be in loop for 8 times , total hours = 8 (in seconds = 28800)  
t = 8
while(t > 0):
    print(f"time {t}")
    # eyes() #30 minutes
    print()
    # exercise() #45 minutes
    print()
    water() # 1 hour
    t -=1

 