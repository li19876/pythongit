import easygui as e
import getencoding
import os

def run():
    print("请在弹窗中选择要分割的文件!")
    filepath = e.fileopenbox()
    if filepath:
        print("文件路径是:", filepath)
        encoding = getencoding.getencoding(filepath)
    else:
        return False
    while 1:
        try:
            linestr =input("请输入分割后每个文件的行数")
            if int(linestr):
                line=int(linestr)
                break
        except:
            print("输入有误,请重新输入")

    filename = filepath.split("/")[-1][0:-4]
    isExists = os.path.exists(filename)
    if not isExists:
        os.mkdir(filename)
    else:
        pass
    with open(filepath,"r",encoding=encoding) as f:
        ss = [i for i in f]
        n=line
        c =[ss[i:i+n] for i in range(0,len(ss),n)]
        for s in c:
            with open(filename+os.sep+str(c.index(s))+".csv","a",encoding=encoding) as fp:
                print("创建了"+str(c.index(s))+".csv")
                for v in s:
                    fp.write(v)
        print("分割完成")
if __name__=='__main__':
    while 1:
        run()






