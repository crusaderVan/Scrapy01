def item_processor(item):
    jobRequire = item['jobRequire']
    for i in jobRequire:
        if i == '\n':
            jobRequire.remove(i)
    temp = '\n'.join(jobRequire)
    item['jobRequire'] = temp

    jobAddress = item['jobAddress']
    for i in jobAddress:
        if i == '\n':
            jobAddress.remove(i)
    temp = '\n'.join(jobAddress)
    item['jobAddress'] = temp

    jobCompanyIntro = item['jobCompanyIntro']
    for i in jobCompanyIntro:
        if i == '\n':
            jobCompanyIntro.remove(i)
    temp = '\n'.join(jobCompanyIntro)
    item['jobCompanyIntro'] = temp

    return item

# item =  {'jobAddress': ['天津市南开区黄河道西南角地铁站附近'],
#  'jobCompany': '天津拓宇数字网络技术有限公司',
#  'jobCompanyIntro': ['\n',
#                      '\u3000\u3000',
#                      '神州优车',
#                      '是一家深度聚焦于智慧出行和汽车全产业链的大型企业集团。旗下业务包括，神州租车、神州专车、神州买买车和神州闪贷四大版块。','\n'],
#  'jobEdu': '大专',
#  'jobExp': '不限',
#  'jobFuli': '五险一金,绩效奖金,全勤奖,交通补助,餐补',
#  'jobName': '数据分析师助理五险一金4K-6K',
#  'jobProperty': '上市公司',
#  'jobRequire': ['\n',
#                 '岗位职责：',
#                 '1、日常项目数据分析统计工作。',
#                 '2、完成数据分析过程中的数据提取、数据分析。',
#                 '3、更侧重互联网产品、运营、商务、用户行为数据。',
#                 '任职要求：',
#                 '1、计算机、统计学或其他相关专业优先，专科及以上学历。',
#                 '2、对互联网有着浓厚的兴趣，富有团队精神并具创造力。',
#                 '3、有较强的沟通能力、严谨的逻辑思维以及数据敏感性。',
#                 '4、具备良好的时间管理、规划执行力。 ',
#                 '公司福利包含五险一金，入职满一年含一份商业保险。',
#                 '周末双休，工作时间为9:00-12:00,13:00-18:00。',
#                 '完善的薪酬体系，广阔的平台发展。',
#                 '\n'],
#  'jobSalary': '4K-6K',
#  'jobScale': '20-99人'}
#
# item = item_processor(item)
#
# print(item)