import time

import PyPDF2
import re
import os
def merge_pdf(name):
    '''
    合并 pdf
    '''
    print('正在合并最终 pdf')
    # find all the pdf files in current directory.
    mypath = os.getcwd()
    pattern = r"\.pdf$"
    file_names_lst = [mypath + "\\" + f for f in os.listdir(mypath) if re.search(pattern, f, re.IGNORECASE)
                      and not re.search(name+'.pdf', f)]

    # 对文件路径按页码排序
    dic = {}
    for i in range(len(file_names_lst)):
        page = re.findall(r'(\d+)\.pdf', file_names_lst[i])[0]
        dic[int(page)] = file_names_lst[i]
    file_names_lst = sorted(dic.items(), key=lambda x: x[0])
    file_names_lst = [file[1] for file in file_names_lst]

    # merge the file.
    opened_file = [open(file_name, 'rb') for file_name in file_names_lst]
    pdfFM = PyPDF2.PdfFileMerger()
    for file in opened_file:
        # print('写入了{}.pdf'.format(file))
        pdfFM.append(file)

    # output the file.
    start= time.time()
    with open(mypath + "\\" + name + ".pdf", 'wb') as write_out_file:
        pdfFM.write(write_out_file)
    end= time.time()
    print(end-start)
    # close all the input files.
    for file in opened_file:
        file.close()

    print('合并完成 %s' % name)

if __name__=='__main__':
    merge_pdf('从零开始')