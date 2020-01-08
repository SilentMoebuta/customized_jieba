from modules.jieba import *
import jieba
import cProfile


text = ["妙然欧式简约大号无盖素色垃圾桶家用客厅卫生间垃圾筒纸篓",
        "个人所得税",
        "八件套折叠梅花棒",
        "聚乙烯醇",
        "盖瑞酸牛奶",
        "车用汽油",
        "防腐螺旋焊管",
        "安全技术咨询费",
        "补胎修理费",
        "炎可宁片",
        "高压防水胶布",
        "肾复康胶囊",
        "防盗栅栏",
        "左前下悬臂",
        "水车租赁费",
        "机油压力传感器",
        "黄金叶香烟",
        "液压油管",
        "小米8全网通版内存蓝色",
        "一次性使用静脉采血针",
        "空气压缩机",
        "发动机润滑油添加剂",
        "安保服装及器材",
        "科固k06027生料带防水胶布聚乙烯密封胶带",
        "世达安装锤锤头",
        "希捷usb30移动硬盘睿翼黑钻版商务时尚轻薄便携高速传"]
# print(jieba_cut(text))

jieba.set_dictionary("cfgdata_coreword.txt")


def pyjieba():
    for i in range(1000):
        for x in text:
            res = ','.join(jieba.cut(x)).split(',')

def cusjieba():
    for i in range(1000):
        for x in text:
            res = jieba_cut(x)


if __name__ == '__main__':
    # cProfile.run('pyjieba()')
    # cProfile.run('cusjieba()')
    # for x in text:
    #     res1 = ','.join(jieba.cut(x)).split(',')
    #     res2 = jieba_cut(x)
    #     print(res1)
    #     print(res2)
    #     print()
    print(','.join(jieba_cut("个人所得税")).split(','))
    print(jieba_cut("个人所得税"))
