import random

# 定义参与抽奖的名字列表
names = ["小明", "小红", "小刚", "大志", "微笑", "小武", "叮铛", "陈桐"]

# 随机选择一个名字
winner = random.choice(names)

# 打印中奖结果
print("本次中奖者是：", winner)
