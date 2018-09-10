import csv

class DownLoad(object):

    def __init__(self, jsonFile, city, position):
        self.jsonFile = jsonFile
        self.city = city
        self.position = position

    def downLoad(self, next=False):
        file = open(self.city + self.position + '职位.csv', 'a', newline='')
        writer = csv.writer(file)
        if not next:
            writer.writerow(('公司名称', '公司所在地', '发布时间', '公司福利', '公司规模', '融资情况', '职位类型', '学历要求', '职位福利', '薪资', '工作经验要求'))
        for info in self.jsonFile:
            writer.writerow([info['companyName'],
                                 info['companyDistrict'],
                                 info['formatCreateTime'],
                                 info['companyLabel'],
                                 info['companySize'],
                                 info['companyStage'],
                                 info['positionType'],
                                 info['positionEducation'],
                                 info['positionAdvantage'],
                                 info['positionSalary'],
                                 info['positionWorkYear'],])
        file.close()
