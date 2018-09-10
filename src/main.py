# -*- coding: utf-8 -*-
import time
import src.setting as SETTING

from src.connect import Connect
from src.parse import Parse
from src.download import DownLoad

def main():
    
    city = SETTING.CITY[0]
    position = SETTING.POSITION[0]
    gx = SETTING.SCHOOL['gx']
    needAddtionalResult = SETTING.SCHOOL['needAddtionalResult']
    isSchoolJob = SETTING.SCHOOL['isSchoolJob']
    xl = SETTING.SCHOOL['xl']
    # 第一次请求开始
    response = Connect(kd=position, city=city, gx=gx
                       , needAddtionalResult=needAddtionalResult, isSchoolJob=isSchoolJob, xl=xl).getConnect()
    para = Parse(response).getInfo()
    count = Parse(response).getPageSize()
    print("请求第" + '1页，下载过程中请勿打开下载文件')
    DownLoad(para, city=city, position=position).downLoad()
    # 第一次请求结束

    for i in range(1, count + 1):

        response = Connect(kd=position, city=city, pn=str(i + 1), gx=gx
                           , needAddtionalResult=needAddtionalResult, isSchoolJob=isSchoolJob, xl=xl).getConnect()
        para = Parse(response).getInfo()
        DownLoad(para, city=city, position=position).downLoad(next=True)
        print("请求第" + str(i + 1) + "页，下载过程中请勿打开下载文件")
        time.sleep(2)
    print("下载完成")

if __name__ == '__main__':
    main()