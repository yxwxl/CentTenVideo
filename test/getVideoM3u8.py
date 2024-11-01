from flask import Blueprint, request, jsonify  # 添加了 request 和 jsonify 的导入
from selenium import webdriver
import json
import time
import threading
import queue
import datetime

# 创建一个队列
task_queue = queue.Queue()

m3u8_hashmap={

}

# 模拟耗时操作的函数
def time_consuming_task():
    while True:
        # 从队列中获取任务
        url = task_queue.get()
        print(f"开始访问url: {url}")
        time.sleep(random.uniform(1, 3))  # 模拟耗时操作
        print(f"完成任务: {task}")
        task_queue.task_done()

def startBrowser():
    
    # 添加保持登录的数据路径：安装目录一般在C:\Users\****\AppData\Local\Google\Chrome\User Data
    user_data_dir = r'C:\Users\26785\AppData\Local\Google\Chrome\User Data'
    #这是一个选项类
    user_option = webdriver.ChromeOptions()
    #添加浏览器用户数据
    user_option.add_argument(f'--user-data-dir={user_data_dir}')
    user_option.add_argument("--auto-open-devtools-for-tabs")  # 自动打开开发者工具
    #实例化浏览器（带上用户数据）
    driver = webdriver.Chrome(options=user_option)
    driver.get("https://baidu.com")
    return driver


def getM3U8Url(url,driver):
    """返回m3u8的函数 status状态码 200 成功 404找不到 400报错"""
    time.sleep(1)
    driver.execute_script(f"window.open('{url}', '_blank');")
    all_handles = driver.window_handles
    new_window_handle = all_handles[-1]
    driver.switch_to.window(new_window_handle)
    time.sleep(1)

    t = 0
    my_result4 = None
    ifRefresh=False
    while my_result4 is None and t < 25:
        t += 1
        # 每次循环中检查窗口是否仍然存在
        if new_window_handle in driver.window_handles and not ifRefresh:
            driver.refresh()
            ifRefresh=True
        if t==10:
            driver.refresh()

        my_result4 = driver.execute_script("return window.my_result4;")
        if my_result4!=None:
            break            
        time.sleep(1)

    driver.close()
    original_window_handle = all_handles[0]
    driver.switch_to.window(original_window_handle)
    print(my_result4)
    if  my_result4!=None:
        return {'status':200,"m3u8":my_result4}
    else:
        return {'status':404,"m3u8":my_result4} 

def getDatTime():
    # 获取当前日期
    today = datetime.date.today()

    # 创建今日0点的datetime对象
    midnight = datetime.datetime.combine(today, datetime.time(0, 0))

    return int(midnight.timestamp())

def needUpdata(lastTime):
    """是否要更新m3u8"""
    # 获取当前日期
    today = datetime.date.today()

    # 创建今日0点的datetime对象
    midnight = datetime.datetime.combine(today, datetime.time(0, 0))

    # 获取时间戳
    timestamp = int(midnight.timestamp())

    #返回是否是同一天的m3u8
    return str(timestamp)==str(lastTime)  

def getM3U8(url):
    try:
        # 检查哈希表中是否有对应的键
        if url in m3u8_hashmap and needUpdata(m3u8_hashmap[url]['last_time']):
            return m3u8_hashmap[url]['result']
        else:
            # 如果没有，调用另一个函数并更新哈希表
            result = getM3U8Url(url,browser)
            if result['status']==200:
                m3u8_hashmap[url] = {"result":result,'last_time':getDatTime()}  # 添加键值对到哈希表
            return result  
    except Exception:      
      return  {"status":400,'m3u8':""}

#启动模拟浏览器
browser=startBrowser()

# 创建蓝图
download_bp = Blueprint('getM3U8', __name__)
# 定义 GET 请求的路由
@download_bp.route('/getM3U8', methods=['GET'])
def get_api_getVideoList():  
    try:
        url=request.args.get('html_link')
        result = getM3U8Url(url,browser)
        return jsonify(result)
    except Exception:
        return jsonify({"status":400,"m3u8":""})

