#coding:utf-8
import pymongo
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
# jd数据库
db = client.jd
# product表,没有自动创建
product_db = db.product
# 统计以下几个颜色
color_arr = ['肤色', '黑色', '紫色', '粉色', '蓝色', '白色', '灰色', '香槟色', '红色']

color_num_arr = []
for i in color_arr:
    num = product_db.count({'product_color': i})
    color_num_arr.append(num)

# 显示的颜色
color = ['bisque', 'black', 'purple', 'pink', 'blue', 'white', 'gray', 'peru', 'red']

indic = []
#我们将数据最大的突出显示
for value in color_num_arr:
    if value == max(color_num_arr):
        indic.append(0.1)
    else:
        indic.append(0)

def create_pie():
    plt.pie(color_num_arr, labels=color, colors=color,
            startangle=90,
            shadow=True,
            explode=tuple(indic),  # tuple方法用于将列表转化为元组
            autopct='%1.1f%%')

    plt.title("内衣颜色比例图", fontproperties=font)
    plt.show()

def create_bar():
    value = []
    index = ["A", "B", "C", "D"]
    for i in index:
        num = product_db.count({'product_size': i})
        value.append(num)

    plt.bar(x=index, height=value, color="green", width=0.5)

    plt.show()

if __name__ == '__main__':
    create_pie()
    # create_bar();

