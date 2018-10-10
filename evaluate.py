# encoding: utf-8
#--------------------------------------------------------
# Name:            evaluate.py
# Purpose:  获得准确率.
#
# Language:    Python 3.2
# Author:      RainMoun
# E-mail:      775653143@qq.com
# Created:     5-1-2018
#--------------------------------------------------------
from loadMovieLens import loadMovieLensTest

def loadMovieLensResult(fileName='result.txt'):
    str1 = './'  # 目录的相对地址
    prefer = {}
    for line in open(str1 + fileName, 'r'):  # 打开指定文件
        (userid, movieid, rating) = line.split('\t')  # 数据集中每行有4项 用户id 、项目 id 、 评分
        prefer.setdefault(userid, {})  # 设置字典的默认格式,元素是user:{}字典
        prefer[userid][movieid] = float(rating)
    return prefer  # 格式如{'user1':{itemid:rating, itemid2:rating, ,,}, {,,,}}


if __name__ == "__main__":
    print("\n--------------准确率生成中 -----------\n")
    count = 0
    win_count = 0
    prefer_result = loadMovieLensResult()
    prefer_test = loadMovieLensTest()
    for item_1 in prefer_result:
        for item_2 in prefer_test:
            if item_1 == item_2:
                for item1 in prefer_result[item_1]:
                    for item2 in prefer_test[item_2]:
                        if item1 == item2:
                            dis = abs(prefer_result[item_1][item1] - prefer_test[item_2][item2])
                            if dis < 1:
                                win_count += 1
                            count += 1
    print('准确率为：' + str(float(win_count)/count))
    print('预测次数为：' + str(count))
    print('正确预测次数为：' + str(win_count))


