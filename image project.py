'''assignment2'''
import cv2
import numpy as np
with open("C://Users//This PC//OneDrive//Pictures//download.jpg", "w") as img:
    img.write("User Drawing Log\n")
    img.write("================\n")

    print("What do you want to draw?")
    print("Options: circle, rectangle, line, text")
    shape = input("Enter your choice: ").lower()
    img.write(f"Shape chosen: {shape}\n")
    if shape=="line":
        p1=int(input("position of p1="))
        p2=int(input("position of p2="))
        color=int(input("color:"))
        thickness=int(input("thickness="))
        cv2.line(img,p1,p2,color,thickness)
        cv2.imshow("image",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif shape=="circle":
        cv2.circle(img,20,30,(255,0,0),2)
        cv2.imshow("image with circle",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif shape=="rectangle":
        p1 = int(input("position of p1="))
        p2 = int(input("position of p2="))
        color = int(input("color:"))
        thickness = int(input("thickness="))
        cv2.rectangle(img,p1,p2,color, thickness)
        cv2.imshow("im with rectangle",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif shape=="text":
        print("do you answer this",cv2.putText())
user=input("do you want to save")
if user=="yes":
    cv2.imwrite("image",img)
    print("Image saved successfully as", img)
else:
    print("Image not saved.")










