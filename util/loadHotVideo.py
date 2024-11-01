import requests
import json 
#搜索框的api请求

# 定义请求的 URL
url = 'https://pbaccess.video.qq.com/trpc.universal_backend_service.page_server_rpc.PageServer/GetPageData?video_appid=1000005&vplatform=2&vversion_name=8.9.10&new_mark_label_enabled=1'


# 定义 headers
headers = {
    'Origin':'https://v.qq.com',
    'Referer':'https://v.qq.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

def getData(index,channel_id="100113"):
    channel_id=channel_id  #防止输入数字
    page_context={
        "page_index": f"{index}",
        "sdk_page_ctx": "{\"page_offset\":"+str(index)+",\"page_size\":1,\"used_module_num\":"+str(index)+"}",
        "data_src_647bd63b21ef4b64b50fe65201d89c6e_page": str(index)
    }
    data = {
        "page_params": {
            "channel_id": channel_id,
            "filter_params": "sort=75",
            "page_type": "channel_operation",
            "page_id": "channel_list_second_page"
        },
        "page_context":page_context
    }
    return data 

def getChannels():
    """获取频道id"""
    data = {
        "page_params": {
            "channel_id": "100113",
            "filter_params": "sort=75",
            "page_type": "channel_operation",
            "page_id": "channel_list_second_page"
        },
        "page_context":{
            "page_index": f"0",
            "sdk_page_ctx": "{\"page_offset\":0,\"page_size\":1,\"used_module_num\":0}",
            "data_src_647bd63b21ef4b64b50fe65201d89c6e_page": "0"
        }
    }
    response = requests.post(url, headers=headers, json=data)
    data=response.json()
    sort_dict_list=[] 
    for itemData in data["data"]["module_list_datas"][0]["module_datas"][0]["item_data_lists"]["item_datas"]:
        try:
            sort_dict={
                "label_title":itemData["item_params"]["label_title"],
                "filter_value":itemData["item_params"]["filter_value"]  
            }
            sort_dict_list.append(sort_dict)
        except Exception:
            sort_dict=None
    return sort_dict_list          

def loadVideoList(data):
    # 加载对应分类的视频
    # 发送 POST 请求
    # 定义请求的 body（数据）
       
    response = requests.post(url, headers=headers, json=data)
    response.encoding = response.apparent_encoding
    # 检查响应状态
    if response.status_code == 200:
        data=response.json()
        data_dict_list=[]
        
        #print(data["data"]["module_list_datas"][0]["module_datas"][0]["item_data_lists"]["item_datas"])
        for itemData in data["data"]["module_list_datas"][-1]["module_datas"][0]["item_data_lists"]["item_datas"]:
            try:
                data_dict={
                    "title":itemData["item_params"]["title"],
                    "cid":itemData["item_params"]["cid"],
                    "new_pic_hz":itemData["item_params"]["new_pic_hz"],  #横向图片
                    "new_pic_vt":itemData["item_params"]["new_pic_vt"]   #纵向图片   
                }
                #不一定有的键
                if itemData["item_params"].get("second_title"):
                    data_dict["second_title"] = itemData["item_params"]["second_title"]
                if itemData["item_params"].get("timelong"):
                    data_dict["timelong"] = itemData["item_params"]["timelong"]
                if itemData["item_params"].get("leading_actor"):
                    data_dict["leading_actor"] = itemData["item_params"]["leading_actor"]

                data_dict_list.append(data_dict)
            except Exception :
                
                data_dict=None
  

        return {
            'status':200,
            'dataList':data_dict_list,
        }
    else:
        return {
            'status':response.status_code,
            'dataList':[],
        }

def getVideoList(index,channel_id="100113"):
    """加载视频流信息，按最热门排序，按种类划分,请求数量"""
    print("VideoList请求下标",index,"channel_id",channel_id)
    data=getData(index,channel_id)
    return loadVideoList(data)


if __name__ == '__main__':

    page0=loadVideoList(getData(0,"100173"))
    print(len(page0["dataList"]))