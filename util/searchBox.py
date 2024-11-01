import requests
import re
#搜索框的api请求

# 定义请求的 URL
url = 'https://pbaccess.video.qq.com/trpc.videosearch.smartboxServer.HttpRountRecall/Smartbox'

# 定义 headers
headers = {
    'Origin':'https://v.qq.com',
    'Referer':'https://v.qq.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def searchByText(text):
    """输入搜索文本返回存在链接地址的视频"""
    # 发送 POST 请求
    # 定义请求的 body（数据）
    data = {
    "query": text,
    "appID": "3172",
    "appKey": "lGhFIPeD3HsO9xEp",
    "pageNum": 0,
    "pageSize": 10
    }
    response = requests.post(url, headers=headers, json=data)

    # 检查响应状态
    if response.status_code == 200:
        data=response.json()
        data_dict_list=[]
        for smartboxItem in data["data"]["smartboxItemList"]:
            try:
                data_dict={
                    "url":smartboxItem["videoInfo"]["playSites"]["episodeInfoList"][0]["url"],
                    "episode_id":smartboxItem["videoInfo"]["playSites"]["episodeInfoList"][0]["id"],
                    "img":smartboxItem["videoInfo"]["imgUrl"],
                    "type":smartboxItem["videoInfo"]["typeName"],
                    "title":remove_html_tags(smartboxItem["basicDoc"]["title"]),
                    "cid":smartboxItem["basicDoc"]["id"]
                    
                }
                data_dict_list.append(data_dict)
            except Exception:
                data_dict=None

        return {'status':200,'ItemList':data_dict_list}
    else:
        return {'status':response.status_code,'ItemList':[]}

if __name__ == '__main__':
    print(searchByText("哈哈哈"))