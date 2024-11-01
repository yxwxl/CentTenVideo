import requests
import os
from tqdm import tqdm

def download_m3u8(m3u8_url, title_name,episode):
    """提供m3u8地址,剧名,级数 下载对应的视频,返回下载视频的状态码 200为成功 404地址有误 400文件有误"""
    root_path='./videoStorage/'                                 # 根目录
                              
    output_dir = os.path.dirname(root_path+title_name+'/')      # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_path=root_path+title_name+f"/第{episode}集.mp4" # 文件位置目录加文件名
    if os.path.exists(output_file_path):
        print(f"{title_name}第{episode}集.mp4已经存在")
        return {"status":200}   

    last_slash_index = m3u8_url.rfind('/')                      # 获取m3u8前缀文本
    if last_slash_index != -1:
        prefix=m3u8_url[:last_slash_index + 1]                  
    else:
        return {"status":400}
    
    response = requests.get(m3u8_url)                           # 获取M3U8文件内容
    if response.status_code != 200:
        print(f"失败获取m3u8文件: {response.status_code}")
        return {"status":404}

    m3u8_content = response.text                                # 筛选ts_urls,组成下载列表
    lines = m3u8_content.splitlines()
    ts_urls = []                        
    for line in lines:
        if line.startswith('0'):
            # 处理相对路径
            ts_url = prefix+line
            ts_urls.append(ts_url)                              
    
    with open(output_file_path, 'wb') as output_file:           # 下载所有 TS 片段
        for ts_url in tqdm(ts_urls):
            ts_response = requests.get(ts_url)
            output_file.write(ts_response.content)

    print(f"Video downloaded to {output_dir+f'第{episode}集'}")
    return {"status":200}

if __name__ == '__main__':
    #                                                           # 使用示例
    download_m3u8("https://ltsyd.qq.com/B_tRCdt2L6hl1ezG-aht1_p3FpkYDP8_3J9Q1pTAGGOHPB9bKN1JXnP377LeEDEWE5/svp_50112/CMYOUS5ORJ6503kqdcX5i1nBCBfPTbI6ovwLPCF0z1gDHyj72gVi_suKRJMqfLAs45U5yQ8CDVo_ucsz-VJMyVrs-jnZqad8DbYCDlg5N6xUxinCsJ_INvgrgl8KuJGNj4mazAkkC-5CfJ57CqDMAY1f_cNNkQTWtYBu_Paol8lQ9Kb6TQKDiI3qVVXKqanK5e-xV7-PGPEeq2qe4Y-RAzWbtnwO_tBPTOhGCW2yYZymqZDLNSfM3w/gzc_1000102_0b53vaadoaaajuadlnafozt4bkgdg6saam2a.f322016.ts.m3u8?ver=4", "白蛇3",1)
