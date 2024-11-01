import datetime
import time

# 获取当前日期
today = datetime.date.today()

# 创建今日0点的datetime对象
midnight = datetime.datetime.combine(today, datetime.time(0, 0))

# 获取时间戳
timestamp = int(midnight.timestamp())

print(f"今日0点的时间戳: {timestamp}")

# 获取当前的datetime对象
now = datetime.datetime.now()

# 获取当前的时间戳
current_timestamp = int(now.timestamp())

print(f"现在的时间戳: {current_timestamp}")

print(f"前方排队{5}人")

print([1,2][1:])