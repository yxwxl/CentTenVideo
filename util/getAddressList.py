import requests
import re
import json

#搜索框的api请求

# 定义请求的 URL
url = 'https://pbaccess.video.qq.com/trpc.universal_backend_service.page_server_rpc.PageServer/GetPageData?video_appid=3000010&vplatform=2&vversion_name=8.2.96'

# 定义 headers
headers = {
    'Origin':'https://v.qq.com',
    'Referer':'https://v.qq.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

def extract_script_content(text):
    """输入网页文本，返回级数列表"""
    # video_ids' 的位置
    pinia_match = re.search(r"video_ids", text)
    if not pinia_match:
        return None

    pinia_index = pinia_match.start()
    script_start = text.find('[', pinia_index)
    script_end = text.find(']', pinia_index)
    #print(script_start,script_end,pinia_index)
    if script_start==-1 or script_end == -1 :
        return None
    try :
        data=json.loads(text[script_start:script_end+1])
        return data
    except Exception:
        return None

def extract_brief_introduction(text):
    # 正则表达式匹配 <meta> 标签并提取 content 属性
    match = re.search(r'<meta\s+[^>]*itemprop="description"[^>]*content="([^"]*)"[^>]*>', text)
    if match:
        return match.group(1)  # 返回 content 属性的值
    return None     

def searchPage(cid,vid):
    """输入单剧的cid和具体级数的vid,返回所在片段所有的vid_list,包含具体细节"""
    # 发送 POST 请求
    # 定义请求的 body（数据）
    data={
        'has_cache': 1,
        'page_params':{
            "req_from": "web_vsite",
            "page_id": "vsite_episode_list",
            "page_type": "detail_operation",
            "id_type": "1",
            "page_size": "",
            "cid": cid,
            "vid": vid,
            "lid": "",
            "page_num": "",
            "page_context": "",
            "detail_page_type": "1"
        }
    }
    
    response = requests.post(url, headers=headers, json=data)

    # 检查响应状态
    if response.status_code == 200:
        data=response.json()
        episode_id_list=[]
        for smartboxItem in data["data"]["module_list_datas"][0]["module_datas"][0]["item_data_lists"]["item_datas"]:
            
            try:
                #存在部分多余的item_id 内容为空
                if smartboxItem["item_id"]!="":  
                    play_title=smartboxItem['item_params']["play_title"]
                    if  "预告" in play_title or "彩蛋" in play_title or "采访" in play_title:  
                        continue
                    if "预告" in smartboxItem['item_params']['union_title']:
                        continue  
                    episode_id_list.append(smartboxItem["item_id"])
            except Exception:
                smartboxItem["item_id"]=""  #什么也不做

        return {'status':200,'ItemList':episode_id_list}
    else:
        return {'status':response.status_code,'ItemList':[]}

def searchAll(html_link):
    """输入动漫或连续剧的任意一集,返回所有集的vid"""
    try:
        response = requests.get(html_link, headers=headers)
        response.encoding = response.apparent_encoding
        data=extract_script_content(response.text)
        brief_introduction=extract_brief_introduction(response.text)
        # print(brief_introduction)
        # print(data)
        data={
            'status':200,
            'data':{
                'ItemList':data,
                'brief_introduction':brief_introduction
            }
        }
        
        return data
    except Exception:
        return {
            'status':400,
            'data':{}
        }    
  
def filterSearchAll(html_link):
    """输入动漫或连续剧的任意一集,返回所有集的vid 去除无用的预告,直接使用searchAll部分电视剧预告可能夹杂在视频vid中间"""
    result=searchAll(html_link)
    full_episodes=result['data']['ItemList']
    #一般只有电视剧综艺要过滤，级数一般低于100
    if len(full_episodes)>80:
        return result
    
    try:
        select_episodes=[]
        t=0
        cid=html_link.split("/")[-1][:-5]
        while t<len(full_episodes):
            index=0
            vid=full_episodes[t]
            episodes=searchPage(cid,vid)['ItemList']
            while index<len(episodes):
                if t>=len(full_episodes):
                    break
                if full_episodes[t] == episodes[index]:
                    select_episodes.append(episodes[index])
                    index+=1
                t+=1 

        result['data']['ItemList']=select_episodes
        return result         
    except Exception:    
        return result

if __name__ == '__main__':
    print(filterSearchAll("https://v.qq.com/x/cover/mzc002000y0ehh8.html"))

