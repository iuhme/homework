import requests
from urlextract  import URLExtract

def getHTML():
    try:
        html=input("请输入一个网址：")
    except:
        print("输入错误，请重新输入")
        getHTML()
    return html

def getHTMLText(url):  #获取一个页面所有源代码的函数
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果状态不是200，引发异常
        r.encoding = 'utf-8' #无论原来用什么编码，都改成utf-8
        return r.text
    except:
        return ""

def getURL(text):
    extractor = URLExtract()
    urls = extractor.find_urls(text)  
    print(urls)
    return urls
    
def exit_program():
    n_wanted=eval(input("在第几层结束")) 
    return n_wanted

def getURLS(urln,n_wanted):
    n=0
    for i in range(len(urln)):
        newtext = getHTMLText(urln[i])
        getURLS(getURL(newtext))
        n=n+1
        if n==n_wanted:
            break
        else:
            continue
                    
def urlReptile():
    html= getHTML()
    text= getHTMLText(html)
    urls= getURL(text)
    n_wanted=exit_program()
    getURLS(urls,n_wanted)
    
if __name__=="__main__":
    urlReptile()