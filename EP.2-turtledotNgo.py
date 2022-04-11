Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Pen()
t.shape('turtle')
turtle.bgcolor('skyblue')
def dotNgo():
    for i in range(21):
        t.penup()
        if 1<=i<=5 :
            t.goto(i*50,i*50)
        elif 6<=i<=10 :
            t.goto(-(i-5)*50,(i-5)*50)
        elif 11<=i<=15 :
            t.goto(-(i-10)*50,-(i-10)*50)
        elif 16<=i<=21 :
            t.goto((i-15)*50,-(i-15)*50)
        t.pendown()
        t.speed(25)
        for j in range(36):
            t.pencolor("black")
            t.dot(10)
            t.pencolor("magenta")
            t.dot(5)
            t.lt(10)
            t.fd(25)

            
dotNgo()
