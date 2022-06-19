import turtle
def strokestr(startx,starty,headangle1,long):
    turtle.penup()
    turtle.setpos(startx,starty)
    turtle.pendown()
    turtle.seth(headangle1)
    length=int(long/5)
    for i in range(length+1):
        a='*'*i
        b='.'*(length-i)
        c=(i/length)*100
        turtle.fd(5)
        print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end="")
    print('')
    
def strokecir(startx2,starty2,rad,angle,headangle2,):
    turtle.penup()
    turtle.setpos(startx2,starty2)
    turtle.pendown()
    turtle.seth(headangle2)
    length=int(angle/5)
    for i in range(length+1):
        a='*'*i
        b='.'*(length-i)
        c=(i/length)*100
        turtle.circle(rad,5)
        print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end="")
    print('')
        
def adjustTurtle():
    try:
        color=input("请输入一种颜色：") 
        turtle.color(color) 
    except:
        print("输入错误，采用默认值")
        turtle.color("red")
    try:    
        size=input("请输入一个尺寸：")
        turtle.pensize(size)
    except:
        turtle.pensize(30) 
    turtle.setup(1000,1000,0,0)   
    turtle.speed(1)   


def progressbar():
    adjustTurtle()
    strokestr(0,0,0,300)
    strokestr(150,150,270,150)
    strokecir(150,0,-200,80,270)
    strokecir(150,0,200,80,270)
