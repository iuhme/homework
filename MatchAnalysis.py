from random import random 

def printIntro(): 
    print("这个程序模拟两个选手A和B的某种竞技比赛") 
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）") 

def getInputs(): 
    try:
        a = eval(input("请输入选手A的能力值(0-1): "))
        if not 0<=a<=1:
            raise NameError 
    except NameError:
        a=0.5
        print("设置错误，使用默认值a=0.5")
    try:
        b = eval(input("请输入选手B的能力值(0-1): "))
        if not 0<=b<=1:
            raise NameError 
    except NameError:
        b=0.5
        print("设置错误，使用默认值b=0.5") 
    try:
        weather = eval(input("请输入需要模拟的赛事的天气状况:1.晴天 2.阴天 3.下雨 4.多云 5.下雪"))
    except NameError:
        print("天气设置错误，默认天气晴天")
        weather=1
    try:    
        weather_a = eval(input("请输入选手A擅长比赛的天气:1.晴天 2.阴天 3.下雨 4.多云 5.下雪"))
    except NameError:
        print("优势天气设置错误，无优势天气")
        weather_a=0
    try:
        weather_b = eval(input("请输入选手B擅长比赛的天气:1.晴天 2.阴天 3.下雨 4.多云 5.下雪"))
    except NameError:
        print("优势天气设置错误，无优势天气")
        weather_a=0
    n = eval(input("模拟比赛的场次: ")) 
    return a, b, n, weather, weather_a, weather_b

def simNGames(n, probA, probB,weather,weather_a,weather_b): 
    winsA, winsB = 0, 0 
    for i in range(n): 
        scoreA, scoreB = simOneGame(probA, probB,weather,weather_a,weather_b) 
        if scoreA > scoreB: 
            winsA += 1 
        else: 
            winsB += 1 
    return winsA, winsB 

def gameOver(a,b): 
    return a==15 or b==15 

def simOneGame(probA, probB,weather,weather_a,weather_b): 
    scoreA, scoreB = 0, 0 
    serving = "A" 
    while not gameOver(scoreA, scoreB): 
        if serving == "A": 
            if random() < prob_weather(probA,weather,weather_a): 
                scoreA += 1 
            else: serving="B"
        else:
            if random() < prob_weather(probB,weather,weather_b):
                scoreB += 1
            else:
                serving="A"
    return scoreA, scoreB

def prob_weather(prob,weather,weather_better):
    if weather==weather_better:
        prob=prob+0.05
    else:
        prob=prob
    return prob

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n))

def MatchAnalysis():
    printIntro()
    probA, probB, n, weather,weather_a,weather_b= getInputs()
    winsA, winsB = simNGames(n, probA, probB,weather,weather_a,weather_b)
    printSummary(winsA, winsB)

if __name__=="__main__":
    MatchAnalysis()