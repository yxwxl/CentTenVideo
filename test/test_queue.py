# import threading
# import queue
# import time
# import random

# # 创建一个队列
# task_queue = queue.Queue()

# # 模拟耗时操作的函数
# def time_consuming_task():
#     while True:
#         # 从队列中获取任务
#         task = task_queue.get()
#         if task is None:  # 接收到结束信号
#             break
#         print(f"开始执行任务: {task}")
#         time.sleep(random.uniform(1, 3))  # 模拟耗时操作
#         print(f"完成任务: {task}")
#         task_queue.task_done()

# # 启动耗时操作线程
# thread = threading.Thread(target=time_consuming_task)
# thread.start()

# # 模拟用户入队列的操作
# for i in range(10):
#     print(f"用户入队列: 任务 {i}")
#     task_queue.put(f"任务 {i}")
#     time.sleep(random.uniform(0.1, 0.5))  # 模拟用户入队列的间隔

# # 等待队列中的所有任务完成
# task_queue.join()

# # 发送结束信号给耗时操作线程
# task_queue.put(None)  # 发送结束信号
# thread.join()  # 等待线程结束

# print("所有任务完成。")

import threading
import queue
import time
import random

# 创建一个队列和计数器
task_queue = queue.Queue()
waiting_count = 0
lock = threading.Lock()  # 用于保护计数器

# 模拟耗时操作的函数
def time_consuming_task():
    global waiting_count
    while True:
        task = task_queue.get()
        if task is None:
            break
        print(f"开始执行任务: {task}")
        time.sleep(random.uniform(1, 3))  # 模拟耗时操作
        print(f"完成任务: {task}")
        task_queue.task_done()
        waiting_count-=1

# 定时查询前面有多少人
def query_waiting_count():
    global waiting_count
    while True:
        time.sleep(1)  # 每秒查询一次

        print(f"当前队列前面还有 {waiting_count} 人")
        if waiting_count == 0 and task_queue.empty():
            break  # 结束条件


# 启动耗时操作线程
thread = threading.Thread(target=time_consuming_task)
thread.start()

# 启动查询线程
query_thread = threading.Thread(target=query_waiting_count)
query_thread.start()

# 模拟用户入队列的操作
for i in range(10):
 
    waiting_count += 1
    print(f"用户入队列: 任务 {i}")

    task_queue.put(f"任务 {i}")
    time.sleep(random.uniform(0.5, 1))  # 模拟用户入队列的间隔

# 等待队列中的所有任务完成
task_queue.join()

# 发送结束信号给耗时操作线程
task_queue.put(None)
thread.join()

# 等待查询线程结束
query_thread.join()

print("所有任务完成。")
