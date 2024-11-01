from flask import Blueprint, request, jsonify  # 添加了 request 和 jsonify 的导入
from selenium import webdriver
import time
import threading
import datetime

# 创建一个任务队列,为了拿到前方排队人数,需使用数组
task_queue = []
# 存放当天对应视频链接的m3u8链接,获取后可在手机自带的浏览器播放，其他浏览器不行,或可在微信以及其他支持m3u8文件的播放器使用
m3u8_hashmap={

}

#这两个参数请根据自己的网速设置,网速慢可以提高时间 MAX_TIME要比REFRESH_TIME多7-8s
REFRESH_TIME=10 #请求页面刷新时间 
MAX_TIME=18     #最大断开时间

def startBrowser():
    
    # 添加保持登录的数据路径：安装目录一般在C:\Users\****\AppData\Local\Google\Chrome\User Data
    # 自行查看对应的谷歌浏览器目录
    user_data_dir = r'C:\Users\26785\AppData\Local\Google\Chrome\User Data'
    #这是一个选项类
    user_option = webdriver.ChromeOptions()
    #添加浏览器用户数据
    user_option.add_argument(f'--user-data-dir={user_data_dir}')
    user_option.add_argument("--auto-open-devtools-for-tabs")  # 自动打开开发者工具,切勿关闭
    #实例化浏览器（带上用户数据）
    driver = webdriver.Chrome(options=user_option)
    driver.get("https://baidu.com") #打开一个无关界面
    return driver

#启动模拟浏览器
browser=startBrowser()



def getM3U8Url(url,driver):
    """返回m3u8的函数 status状态码 200 成功 404找不到 400报错"""
    time.sleep(1)
    driver.execute_script(f"window.open('{url}', '_blank');")
    all_handles = driver.window_handles
    new_window_handle = all_handles[-1]
    driver.switch_to.window(new_window_handle)
    time.sleep(1)

    t = 0
    my_m3u8 = None
    ifRefresh=False
    while my_m3u8 is None and t < MAX_TIME:
        t += 1
        # 开始时刷新一次
        if new_window_handle in driver.window_handles and not ifRefresh:
            driver.refresh()
            ifRefresh=True
        # 等待页面加载一定时间后刷新    
        if t==REFRESH_TIME:
            driver.refresh()

        my_m3u8 = driver.execute_script("return window.my_m3u8;")
        if my_m3u8!=None:
            break            
        time.sleep(1)

    driver.close()
    original_window_handle = all_handles[0]
    driver.switch_to.window(original_window_handle)
    print(my_m3u8)
    if  my_m3u8!=None:
        return {'status':200,"m3u8":my_m3u8}
    else:
        return {'status':404,"m3u8":my_m3u8} 

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
    global m3u8_hashmap
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

def getPersonNumber(token):
    """获取当前排队的token的下标,即可获取前方人数"""
    global task_queue
    for i in range(len(task_queue)):
        if task_queue[i]['token']==token:
            return i
    return -1

def dealTarget(url,target,token):
    global task_queue
    global m3u8_hashmap
    """
        处理不同情况的返回值 
        target为request意味第一次申请,查找有hashmap有无m3u8,没有则模拟浏览器查找
        target为get意味等待过后的申请,先判断用户前方用户数目,如果有数名用户，返回前方用户数，否则返回加载中
        查找m3u8是否已被加载到hashmap中有则返回,无则等待下一重连，重连次数上限
        status 201 返回开始查找的结果和get没有结果一样  返回前方用户数，否则返回加载中 200 返回m3u8字典
    """
    if url in m3u8_hashmap and needUpdata(m3u8_hashmap[url]['last_time']):
        return m3u8_hashmap[url]['result']
    
    if target=='request':
        index=getPersonNumber(token)
        if index==-1:
            index=len(task_queue)

            task_queue.append({"token":token,"url":url})
            if index>0:
                return {"status":202,"text":f"前方排队{index}人,请耐心等待"}
            else:
                return {"status":201,"text":f"您的视频加载中大概需要20s,请耐心等待"}
        elif index==0:
            return {"status":201,"text":f"您的上一个视频加载中，本次会返回上一次的结果"}
        else:
            task_queue[index]={"token":token,"url":url}
            return {"status":202,"text":f"前方排队{index}人,请耐心等待"}

    elif  target=='get': 
        index=getPersonNumber(token)
        if index>0:
            return {"status":202,"text":f"前方排队{index}人,请耐心等待"}
        elif index<0:
            return {"status":400,"text":f"视频请求失败"}
        else:
            return {"status":201,"text":f"您的视频加载中大概需要20s,请耐心等待"} 
    else :
        return {"status":400,"text":f"目标错误"}



# 模拟浏览器线程,0.5s检测一次队列有无任务
def time_consuming_task():
    global task_queue
    while True:
        time.sleep(0.5)  #节约性能
        # 从队列中获取任务
        #print("线程执行中...")
        if len(task_queue)>0:
            url = task_queue[0]['url']
            print(f"开始访问url: {url}")
            getM3U8(url)
            task_queue=task_queue[1:]


# 启动模拟浏览器操作线程
thread = threading.Thread(target=time_consuming_task)
thread.start()

# 创建蓝图
download_bp = Blueprint('getM3U8', __name__)
# 定义 GET 请求的路由
@download_bp.route('/getM3U8', methods=['GET'])
def get_api_getVideoList():  
    try:
        target=request.args.get('target')
        url=request.args.get('html_link')
        token=request.args.get('token')
        result = dealTarget(url,target,token)
        return jsonify(result)
    except Exception:
        return jsonify({"status":400,"m3u8":""})

