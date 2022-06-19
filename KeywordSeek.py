def printIntro():
    print("此程序功能为找出代码文本中保留字的种类和个数，将前十位展示出来（不足十个全部展示）")

def getText(): 
    txt = open("test.txt", "r",encoding='utf-8').read() 
    txt = txt.lower() 
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~，“”：；’（）': 
        txt = txt.replace(ch, " ") #将文本中特殊字符替换为空格 
    return txt

def KeywordSeek(testTxt):
    words = testTxt.split() 
    keyword={"False","None","Ture","and","as","assert","break","class","continue","def","del","elif","else","except","finally","for","from","global","if","import","in","is","lambda","nonlocal","not","or","pass","raise","return","try","while","with","yield"}
    counts = {}
    for word in words:
        if word in keyword:
            counts[word] = counts.get(word,0) + 1
        else:
            counts[word]=0
            del(counts[word])
    items = list(counts.items()) 
    items.sort(key=lambda x:x[1], reverse=True) 
    cou=len(counts)
    for i in range(cou): 
        word, count = items[i] 
        print ("{0:<10}{1:>5}".format(word, count))

def runKeywordSeek():
    printIntro()
    txt=getText()
    KeywordSeek(txt)

if __name__=="__main__":
    runKeywordSeek()




