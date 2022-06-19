import turtle,datetime

def drawGap():
    turtle.penup()
    turtle.fd(5)

def drawOpentube():
    turtle.pensize(1)
    turtle.pendown()
    turtle.left(45)
    turtle.fd(6)
    turtle.right(45)
    turtle.fd(40)
    turtle.right(45)
    turtle.fd(6)
    turtle.right(90)
    turtle.fd(6)
    turtle.right(45)
    turtle.fd(40)
    turtle.right(45)
    turtle.fd(6)
    turtle.right(135)
    turtle.penup()
    turtle.fd(48.48)
    drawGap()
    turtle.right(90) 
    
def drawLine(draw):
    if draw:
       drawGap() 
       turtle.begin_fill()
       turtle.fillcolor("red")
       drawOpentube()
       turtle.end_fill()
    else:
       drawGap()
       drawOpentube()
   
def drawDigit(d):
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '年':
            turtle.write(i,font=("Arial",18,"normal"))
            turtle.pencolor("red")
            turtle.fd(40)
        elif i == '月':
            turtle.write(i,font=("Arial",18,"normal"))
            turtle.pencolor("red")
            turtle.fd(40)
        elif i == '日':
            turtle.write(i,font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))

def drawNum(data):
    turtle.pencolor("red")
    for i in data:
        drawDigit(eval(i))

def tube(): 
    turtle.reset()
    turtle.hideturtle()
    turtle.setup(800,350,200,200)
    turtle.speed(0)
    turtle.penup()
    turtle.fd(-350)

def printIntro():
    print("七段数码管功能：\n1.显示输入日期\n2.显示系统时间\n3.显示数字")

def functionSelect():
        op=input("请选择一项功能：")
        if op=='1':
            date=input("输入日期（*年*月*日）：")
            tube()
            drawDate(date)
        elif op=='2':
            tube()
            drawDate(datetime.datetime.now().strftime('%Y年%m月%d日'))        
        elif op=='3':
            num=input("请输入一个数字：")
            tube()
            drawNum(num)
        else:
            print("敬请期待")

def seg7():
    printIntro()
    functionSelect()
