from turtle import *
import tkinter
import tkinter.messagebox
import random
import math
import datetime

screenMinX = -500
screenMinY = -500
screenMaxX = 500
screenMaxY = 500

def main():
    
    # Start by creating a RawTurtle object for the window. 
    root = tkinter.Tk()
    root.title("Tic Tac Toe!")
    cv = ScrolledCanvas(root,600,600,600,600)
    cv.pack(side = tkinter.LEFT)
    t = RawTurtle(cv)
    screen = t.getscreen()

    screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
    screen.bgcolor("green")
    t.ht()
    
    
    t.width(50)
    t.speed(0)
    
    t.penup()
    t.setposition(-600,-200)
    t.pendown()
    t.setposition(600,-200)
    
    t.penup()
    t.setposition(-600,200)
    t.pendown()
    t.setposition(600,200)
    
    t.penup()
    t.setposition(-200,-600)
    t.pendown()
    t.setposition(-200,600)
    
    t.penup()
    t.setposition(200,-600)
    t.pendown()
    t.setposition(200,600)
    
    data = {}
    data["drawx"] = True
    locks = {}
    locks["onelock"] = False
    locks["twolock"] = False
    locks["threelock"] = False
    locks["fourlock"] = False
    locks["fivelock"] = False
    locks["sixlock"] = False
    locks["sevenlock"] = False
    locks["eightlock"] = False
    locks["ninelock"] = False
    
    def mouseHandler(x,y):
        
        
        t.penup()
        
        if x > -600 and x < -200:
            
                if y > -600 and y < -200:
                    if not locks["sevenlock"]:
                        data["drawx"] = not data["drawx"]
                    
                        if data["drawx"]:
                            t.shape("Xlogo.gif")
                    
                        if not data["drawx"]:
                            t.shape("Ologo.gif")
                           
                        t.setposition(-400,-400)
                        t.pendown()
                        t.stamp()
                        locks["sevenlock"] = True
                    
                if y > -200 and y < 200:
                
                    if not locks["fourlock"]:
                        data["drawx"] = not data["drawx"]
                        if data["drawx"]:
                            t.shape("Xlogo.gif")
                    
                        if not data["drawx"]:
                            t.shape("Ologo.gif")
                           
                        
                        t.setposition(-400,0)
                        t.pendown()
                        t.stamp()
                        locks["fourlock"] = True
                    
                if y > 200 and y < 600:
                    if not locks["onelock"]:
                        data["drawx"] = not data["drawx"]
                        if data["drawx"]:
                            t.shape("Xlogo.gif")
                    
                        if not data["drawx"]:
                            t.shape("Ologo.gif")
                           
                        t.setposition(-400,400)
                        t.pendown()
                        t.stamp()
                        locks["onelock"] = True
                    
        if x > -200 and x < 200:
            
                if y > -600 and y < -200:
                    if not locks["eightlock"]:
                        data["drawx"] = not data["drawx"]
                        if data["drawx"]:
                            t.shape("Xlogo.gif")
                    
                        if not data["drawx"]:
                            t.shape("Ologo.gif")
                           
                        t.setposition(0,-400)
                        t.pendown()
                        t.stamp()
                        locks["eightlock"] = True
                        
                if y > -200 and y < 200:
                    if not locks["fivelock"]:
                        data["drawx"] = not data["drawx"]
                        if data["drawx"]:
                            t.shape("Xlogo.gif")
                    
                        if not data["drawx"]:
                            t.shape("Ologo.gif")
                           
                        t.setposition(0,0)
                        t.pendown()
                        t.stamp()
                        locks["fivelock"] = True
                    
                if y > 200 and y < 600:
                    if not locks["twolock"]:
                        data["drawx"] = not data["drawx"]
                        if data["drawx"]:
                            t.shape("Xlogo.gif")
                    
                        if not data["drawx"]:
                            t.shape("Ologo.gif")
                           
                        t.setposition(0,400)
                        t.pendown()
                        t.stamp()
                        locks["twolock"] = True
                    
        if x > 200 and x < 600:
                
                if y > -600 and y < -200:
                    if not locks["ninelock"]:
                        data["drawx"] = not data["drawx"]
                        if data["drawx"]:
                            t.shape("Xlogo.gif")
                    
                        if not data["drawx"]:
                            t.shape("Ologo.gif")
                           
                        t.setposition(400,-400)
                        t.pendown()
                        t.stamp()
                        locks["ninelock"] = True
                    
                if y > -200 and y < 200:
                    if not locks["sixlock"]:
                        data["drawx"] = not data["drawx"]
                        if data["drawx"]:
                            t.shape("Xlogo.gif")
                    
                        if not data["drawx"]:
                            t.shape("Ologo.gif")
                           
                        t.setposition(400,0)
                        t.pendown()
                        t.stamp()
                        locks["sixlock"] = True
                        
                if y > 200 and y < 600:
                    if not locks["threelock"]:
                        data["drawx"] = not data["drawx"]
                        if data["drawx"]:
                            t.shape("Xlogo.gif")
                    
                        if not data["drawx"]:
                            t.shape("Ologo.gif")
                           
                        t.setposition(400,400)
                        t.pendown()
                        t.stamp()
                        locks["threelock"] = True
        
    screen.listen()
    screen.register_shape("Ologo.gif")
    screen.register_shape("Xlogo.gif")
    screen.onclick(mouseHandler)
    
    tkinter.mainloop()
    
if __name__ == "__main__":
    main()
