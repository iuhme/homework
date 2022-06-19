import jieba

def syntaxCheck(txt):
    lines=txt.readlines() 
    for line in lines:
        line_Check(line,lines)

def line_Check(line,lines):
    words=jieba.lcut(line)
    if 'if' in words:
        if_syntaxCheck(words,line,lines)
    elif 'for' in words:
        for_syntaxCheck(words,line,lines)
    elif 'try' in words:
        try_syntaxCheck(words,line,lines)
    elif 'else' in words:
        else_syntaxCheck(words,line,lines)
    else:
        return 0

def if_syntaxCheck(words,line,lines):
    if 'else' in words:
        print("special if")
        print(lines.index(line)+1)
        print('')
    else:
        strs='if'
        a=firstCheck(strs,words)
        if a==True:
            endCheck(strs,words,line,lines)
        else:
            endCheck(strs,words,line,lines)
            print("if位置错误")
            print(lines.index(line)+1)
            print('')

def for_syntaxCheck(words,line,lines):
        strs='for'
        a=firstCheck(strs,words)
        if a==True:
            if 'in' in words:
                endCheck(strs,words,line,lines)
            else:
                print("缺失in")
                print(lines.index(line)+1)
        else:
            endCheck(strs,words,line,lines)
            print("for位置错误")
            print(lines.index(line)+1)

def try_syntaxCheck(words,line,lines):
        strs='try'
        a=firstCheck(strs,words)
        if a==True:
            endCheck(strs,words,line,lines)
        else:
            endCheck(strs,words,line,lines)
            print("try位置错误")
            print(lines.index(line)+1)

def else_syntaxCheck(words,line,lines):
        strs='else'
        a=firstCheck(strs,words)
        if a==True:
            endCheck(strs,words,line,lines)
        else:
            endCheck(strs,words,line,lines)
            print("else位置错误")
            print(lines.index(line)+1)

def firstCheck(strs,lists):
    lists=[x for x in lists if x!=' ']
    a=lists.index(strs)
    if a==0:
        return True
    else:
        return False

def endCheck(strs,lists,line,lines):
    strs=':'  
    if strs in lists:
        lists=[x for x in lists if x!=' '] 
        num=lists.count(strs)
        if num!=1:
            print("“:”个数错误")
            print(lines.index(line)+1) 
        else:         
            a=lists.index(strs)
            if a==len(lists)-2:
                return 0
            else:
                print("“:”位置错误")
                print(lines.index(line)+1)
                print('')
    else:
        print("“:”缺失")

def runsyntaxCheck():
    txt=open("test.txt", "r",encoding='utf-8')
    syntaxCheck(txt)

if __name__=="__main__":
    runsyntaxCheck()
