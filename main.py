import head,sys

def functionSelect():
      print("0.退出程序 1.哈希函数 2.写字进度条 3.七段数码管显示 4.保留字查找 5.语法检查 6.体育竞技模拟 7.爬取网页链接")
      op=input("请选择一项功能：")
      if op=='0':
         sys.exit()
      elif op=='1':
         head.hash_run()
         functionSelect()
      elif op=='2':
         head.progressbar_run()
         functionSelect()
      elif op=='3':
         head.digitTube_run()
         functionSelect()
      elif op=='4':
         head.compiler_run()
         functionSelect() 
      elif op=='5':
         head.syntaxCheck_run()
         functionSelect()
      elif op=='6':
         head.MatchAnalysis_run()
         functionSelect()
      elif op=='7':
         head.Reptile_run()
         functionSelect()  
      else:
         print("敬请期待\n")
         functionSelect()

def main():
   functionSelect()

main()



