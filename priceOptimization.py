#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Torre Yang
# datetime:2018/11/8 20:24
# 根据现价, 优惠力度, 找出最优购买策略
# 优惠力度 可以存字典项:价格分解
import csv

# 优惠力度：260:298, 360:428,560:668, 1000-1218
# 手机：1000：1128, 仅限于手机店铺
# 优惠券组成: 商家优惠券+平台优惠券


# coupon 商家优惠券
def priceOptimization(nowPrice, coupon):
    mlCard ={}  # 存储美丽卡优惠信息
    mlCard["260"] = 298
    mlCard["360"] = 428
    mlCard["560"] = 668
    mlCard["1000"] = 1218
    res = []  # 存储计算规则的数据
    if nowPrice-coupon >= 1998:
        nowPrice = nowPrice-coupon-375
    elif nowPrice-coupon >= 998 and (nowPrice-coupon) < 1998:
        nowPrice = nowPrice-coupon - 165
    elif nowPrice-coupon >= 588 and (nowPrice-coupon) < 998:
        nowPrice = nowPrice-coupon - 80
        if nowPrice >= 508 and (nowPrice < 668):
            lastPrice = nowPrice
    elif nowPrice-coupon >= 398 and (nowPrice-coupon) < 558:
        nowPrice = nowPrice-coupon - 50
        if nowPrice >= 348 and (nowPrice < 428):
            lastPrice = 360
        else:
            lastPrice = nowPrice - 68
    elif nowPrice-coupon >= 228 and (nowPrice-coupon) < 398:
        nowPrice = nowPrice-coupon - 25
        if nowPrice >= 203 and (nowPrice <= 298):
            lastPrice = 260
        elif nowPrice > 298 and (nowPrice < 398):
            lastPrice = nowPrice - 38
    else:
        nowPrice = nowPrice-coupon

    # return optPrice

# if __name__ == '__main__':
    # priceOptimization()








