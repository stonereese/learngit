# coding:utf8
import pandas_profiling
import pandas as pd
data = pd.read_excel(r"C:\Users\S\Desktop\录音文件\截止到0820_总表去除重复后.xlsx")
mypath = "c:/users/s/desktop"
# mypath=input("输入一个路径:\n")
print(data.head())
