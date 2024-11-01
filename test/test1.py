# def getM3U8Url(url, browser):
#     try:
#         time.sleep(2)
#         browser.execute_script("window.open('', '_blank');")
#         all_handles = browser.window_handles
#         new_window_handle = all_handles[-1]
#         browser.switch_to.window(new_window_handle)
#         browser.get(url)
#         t = 0
#         my_result4 = None
#         ifRefresh=False
#         while my_result4 is None and t < 20:
#             t += 1
#             # 每次循环中检查窗口是否仍然存在
#             if new_window_handle in browser.window_handles and not ifRefresh:
#                 time.sleep(2)
#                 browser.refresh()
                
#                 ifRefresh=True  
#             my_result4 = browser.execute_script("return window.my_result4;")
#             if my_result4!=None:
#                 break            
#             time.sleep(1)
#         browser.close()
#         original_window_handle = all_handles[0]
#         browser.switch_to.window(original_window_handle)

#         if my_result4!=None:
#             return {'status':200,"m3u8":my_result4}
#         else:
#             return {'status':400,"m3u8":""}
#     except Exception:
#         return {'status':400,"m3u8":""}    

# def getM3U8Url2(url, browser):
#     try:
#         time.sleep(2)

#         browser.get(url)
#         t = 0
#         my_result4 = None
#         # time.sleep(2)
#         # browser.refresh()
#         while my_result4 is None and t < 10:
#             t += 1
#             my_result4 = browser.execute_script("return window.my_result4;")
#             if my_result4!=None:
#                 break            
#             time.sleep(1)
#         if my_result4!=None:
#             return {'status':200,"m3u8":my_result4}
#         else:
#             return {'status':400,"m3u8":""}
#     except Exception:
#         return {'status':400,"m3u8":""} 

# def getM3U8Url3(url, browser):
#     time.sleep(1)
#     browser.execute_script(f"window.open('{url}', '_blank');")
#     time.sleep(1)
#     all_handles = browser.window_handles
#     new_window_handle = all_handles[-1]
#     browser.switch_to.window(new_window_handle)
#     time.sleep(1)

#     t = 0
#     my_result4 = None
#     ifRefresh=False
#     while my_result4 is None and t < 20:
#         t += 1
#         # 每次循环中检查窗口是否仍然存在
#         if new_window_handle in browser.window_handles and not ifRefresh:
#             browser.refresh()
#             ifRefresh=True  
#         my_result4 = browser.execute_script("return window.my_result4;")
#         if my_result4!=None:
#             break            
#         time.sleep(1)
#     time.sleep(5)    
#     browser.refresh()
#     while my_result4 is None and t < 40:
#         t += 1
#         my_result4 = browser.execute_script("return window.my_result4;")
#         if my_result4!=None:
#             break  
#         time.sleep(2)    

#     browser.close()
#     original_window_handle = all_handles[0]
#     browser.switch_to.window(original_window_handle)
#     print(my_result4)
#     if my_result4!=None:
#         return {'status':200,"m3u8":my_result4}
#     else:
#         return {'status':400,"m3u8":""}

# def getM3U8Url4(url,driver):
#     time.sleep(1)
#     driver.execute_script(f"window.open('{url}', '_blank');")
#     all_handles = driver.window_handles
#     new_window_handle = all_handles[-1]
#     driver.switch_to.window(new_window_handle)
#     time.sleep(1)

#     t = 0
#     my_result4 = None
#     ifRefresh=False
#     while my_result4 is None and t < 20:
#         t += 1
#         # 每次循环中检查窗口是否仍然存在
#         if new_window_handle in driver.window_handles and not ifRefresh:
#             driver.refresh()
#             ifRefresh=True  
#         my_result4 = driver.execute_script("return window.my_result4;")
#         if my_result4!=None:
#             break            
#         time.sleep(1)

#     driver.close()
#     original_window_handle = all_handles[0]
#     driver.switch_to.window(original_window_handle)
#     print(my_result4)
#     return {'status':200,"m3u8":my_result4}


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 启动浏览器
options = webdriver.ChromeOptions()

 # 添加保持登录的数据路径：安装目录一般在C:\Users\****\AppData\Local\Google\Chrome\User Data
user_data_dir = r'C:\Users\26785\AppData\Local\Google\Chrome\User Data'
#这是一个选项类
user_option = webdriver.ChromeOptions()
#添加浏览器用户数据
user_option.add_argument(f'--user-data-dir={user_data_dir}')
user_option.add_argument("--auto-open-devtools-for-tabs")
#实例化浏览器（带上用户数据）
driver = webdriver.Chrome(options=user_option)


driver.get("https://baidu.com")
time.sleep(2)

def getM3U8(url):
    time.sleep(1)
    driver.execute_script(f"window.open('{url}', '_blank');")
    all_handles = driver.window_handles
    new_window_handle = all_handles[-1]
    driver.switch_to.window(new_window_handle)
    time.sleep(1)

    t = 0
    my_result4 = None
    ifRefresh=False
    while my_result4 is None and t < 20:
        t += 1
        # 每次循环中检查窗口是否仍然存在
        if new_window_handle in driver.window_handles and not ifRefresh:
            driver.refresh()
            ifRefresh=True  
        my_result4 = driver.execute_script("return window.my_result4;")
        if my_result4!=None:
            break            
        time.sleep(1)

    driver.close()
    original_window_handle = all_handles[0]
    driver.switch_to.window(original_window_handle)
    print(my_result4)
    return my_result4
    
getM3U8("https://v.qq.com/x/cover/mzc00200odc2q2w/y4100sw4hl5.html")
getM3U8("https://v.qq.com/x/cover/mzc002007sqbpce/t3568475p93.html")
time.sleep(5)

driver.quit()

