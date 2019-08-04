# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)

beijing = [17,17,23,43]
shanghai = ['19%','4%','23%','54%']
guangzhou = ['53%','25%','13%','9%']
shenzhen = ['41%','22%','20%','17%']

label = ['2-3 years','3-4 years','4-5 years','5+ years']
color = ['red','green','yellow','purple']

indic = []

#我们将数据最大的突出显示
for value in beijing:
    if value == max(beijing):
        indic.append(0.1)
    else:
        indic.append(0)

plt.pie(
    beijing,
    labels=label,
    colors=color,
    startangle=90,
    shadow=True,
    explode=tuple(indic),#tuple方法用于将列表转化为元组
    autopct='%1.1f%%'#是数字1，不是l
)


plt.title(u'饼图示例——统计北京程序员工龄', FontProperties=font)

plt.show()
