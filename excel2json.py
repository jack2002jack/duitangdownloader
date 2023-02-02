import xlrd2 #需要1.2.0版本的，2.0以上的版本只能读取.xls类型的文件
import csv
import json
# 读取文件(.xlsx .xls .csv) 然后返回字典数据
def readFile(filePath):
    try:
        fileType = filePath.split(".")[-1]
        print(f'{filePath}\t{fileType}')
        if fileType == 'xlsx' or fileType=='xls':
            res = []
            wb = xlrd2.open_workbook(filePath)
            sh = wb.sheet_by_index(0)
            title = []
            for item in sh.row_values(0):
                title.append(item)
            data = []
            # 实现第一行为key，剩下的为value 转为字典了
            [[data.append({title[index]:sh.row_values(it)[index] for index in range(0,len(title))})] for it in range(1,sh.nrows)]
            return data
        elif fileType == "csv":
            data = []
            with open(filePath) as csvfile:
                rows = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
                title = next(rows)  # 读取第一行每一列的标题
                [[data.append({title[index]:it[index] for index in range(0, len(title))})] for it in rows]
            return data
        else:
            return -1
    except(EOFError):
        print("转化过程出错！")
        print(EOFError)
        return -1


# 字符串输入，转成相应的类型
def transfer(string):
    try:
      return str(string)
    except:
        pass
if __name__=="__main__":
    r = readFile("E:\data\教师信息表1014(1).xlsx")
    f = open("./数学系.json",'w',encoding="utf-8")
    m = open("./计算机系.json",'w',encoding="utf-8")

    maths=[]
    cs=[]
    for l in r:
        l.pop("序号")
        l["name"] = l.pop("姓名")
        l["major"] = l.pop("专业")
        i = l.pop("任职时间")
        if  isinstance(i,str):
            l["career_time"] =i
        else:l["career_time"] =str(int(i))
        l["degree"] = l.pop("最高学位")
        l["postitle"] = l.pop("职称")
        l.pop("毕业专业")
        l.pop("毕业院校")
        l["discript"]=l.pop("简介")
        if l["major"]=="数学":
            maths.append(l)
        else:
            cs.append(l)
    json.dump(maths,f,ensure_ascii=False)
    json.dump(cs,m,ensure_ascii=False)
