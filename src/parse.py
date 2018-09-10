import requests
from src.download import DownLoad
"""
解析网页信息
"""
class Parse(object):

    def __init__(self, htmlJson):
        self.htmlJson = htmlJson.json()

    def getPageSize(self):
        '''
        解析数据大小(职位总数量，每一页显示的数量）
        :return: 总共页面数量
        '''
        self.totalCount = self.htmlJson['content']['positionResult']['totalCount']  # 职位总数量
        resultSize = self.htmlJson['content']['positionResult']['resultSize']  # 每一页显示的数量
        pageCount = int(self.totalCount) // int(resultSize) + 1  # 页面数量
        return pageCount

    def getInfo(self):
        '''
        解析信息
        :return: 信息
        '''
        result = []
        for info in self.htmlJson['content']['positionResult']['result']:
            i = {}
            i['companyName'] = info['companyFullName']  #公司名称
            i['companyDistrict'] = info['district']     #公司所在地
            i['formatCreateTime'] = info['formatCreateTime']  #发布时间
            i['companyLabel'] = info['companyLabelList']  # 公司福利
            i['companySize'] = info['companySize']      #标签
            i['companyStage'] = info['financeStage']    #融资情况
            i['positionType'] = info['firstType']       #职位类型
            i['positionEducation'] = info['education']  #学历要求
            i['positionAdvantage'] = info['positionAdvantage'] #职位福利
            i['positionSalary'] = info['salary']                #薪资
            i['positionWorkYear'] = info['workYear']            #工作经验要求
            result.append(i)
        return result