from flask import Blueprint, request, jsonify  # 添加了 request 和 jsonify 的导入
from util.getAddressList import filterSearchAll
import time

# 初始化哈希表 python字典即是哈希表
# 缓存视频列表,避免重复请求
hash_table = {}
CACHE_EXPIRY_TIME = 24 * 60 * 60  # 24小时

def getLinkList(html_link):
    """获取对应网页链接的视频列表"""
    current_time = time.time()

    try:
        # 检查哈希表中是否有对应的键——页面链接为键
        if html_link in hash_table:
            cached_entry = hash_table[html_link]
            # 检查缓存是否过期
            if current_time - cached_entry['timestamp'] < CACHE_EXPIRY_TIME:
                return cached_entry['data']

        # 如果没有缓存或缓存已过期，重新请求数据
        result = filterSearchAll(html_link)
        if result['status'] == 200:
            # 更新哈希表
            hash_table[html_link] = {
                'data': result,
                'timestamp': current_time  # 更新缓存时间
            }
        return result

    except Exception:
        return {"status": 400, 'data': {}}
    
# 创建蓝图
html_link_bp = Blueprint('getHtmlLinkList', __name__)
# 定义 GET 请求的路由
@html_link_bp.route('/getHtmlLinkList', methods=['GET'])
def get_api_getVideoList():  
    try:
        html_link=request.args.get('html_link')
        result = getLinkList(html_link)
        return jsonify(result)
    except Exception:
        return jsonify({"status":400,'data':{}})

