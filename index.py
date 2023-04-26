import cv2 
#Read the image / video input through web cam

import numpy as np

from pyzbar.pyzbar import decode 
#decodes the qr code or barcode to extract data

import webbrowser

import time

import csv

from datetime import datetime


#img = cv2.imread('QR1.png')


cap = cv2.VideoCapture(0) #capture qr image
cap.set(3,640)
cap.set(4,480)




with open('mydata.txt') as f:
    myDataList = f.read().splitlines()
#print(myDataList)


authorized_individuals = []



with open('log.csv', 'a', newline='') as f:
    log_writer = csv.writer(f)
    log_writer.writerow(['QR Code Data', 'Date and Time'])



last_time = datetime.now() # initialize last_time to current time



while True:
    success,img=cap.read()


    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)


        if myData in myDataList:
            
            if myData not in authorized_individuals:
                authorized_individuals.append(myData)
            
            myOutput = 'Authorized '
            myColor = (0,255,0)

            current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            if current_time != last_time:
                with open('log.csv', 'a', newline='') as f:
                    log_writer = csv.writer(f)
                    log_writer.writerow([myData, datetime.now().strftime("%d/%m/%Y %H:%M:%S")])
                last_time = current_time
            #log_writer.writerow([myData, datetime.now().strftime("%m/%d/%Y %H:%M:%S")])

                
        else:
            myOutput = 'Unauthorized ' 
            myColor = (0,0,255)
                #webbrowser.open(myData,new=2)


        
        pts = np.array([barcode.polygon],np.int32)

        pts=pts.reshape((-1,1,2))

        cv2.polylines(img,[pts],True,myColor,5)

        pts2=barcode.rect

        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)



        if myData.startswith("http"):
            if myData in authorized_individuals:
                if not webbrowser.open_new_tab(myData):
                    print(f"{myData} is already open")
                time.sleep(1) # delay for 1 second to prevent multiple QR codes from opening multiple tabs
            else:
                print(f"{myData} is not authorized for website launch") 



        elif myData.endswith(".in"):
            if myData in authorized_individuals:
                if not webbrowser.open_new_tab(myData):
                    print(f"{myData} is already open")
                time.sleep(1) # delay for 1 second to prevent multiple QR codes from opening multiple tabs
            else:
                print(f"{myData} is not authorized for website launch")




        else:
            print(f"{myData} is not authorized for website launch")
        
    

    cv2.imshow('Result',img)
    if cv2.waitKey(1) == 27:
        break


#log_file.close()

cap.release()        
cv2.destroyAllWindows()    


    
