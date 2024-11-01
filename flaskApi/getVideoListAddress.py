from flask import Blueprint, request, jsonify  # 添加了 request 和 jsonify 的导入
from util.loadHotVideo import getVideoList
import time

#保存请求的视频列表，分类，下面是数组
save_video_dict={}
CACHE_EXPIRY_TIME = 24 * 60 * 60  # 24小时

def getVList(index, channel_id):
    """根据index和channel_id获取对应视频的列表"""

    # 确保 index 是数字
    if not isinstance(index, int):
        try:
            index = int(index)
        except ValueError:
            return {'status': 400, 'dataList': []}

    channel_id = str(channel_id)

    if channel_id not in save_video_dict:
        # 如果频道不存在，则初始化并尝试获取数据
        return fetchAndCacheVideoList(index, channel_id)

    # 检查索引范围
    if index < 0 or index >= len(save_video_dict[channel_id]):
        return fetchAndCacheVideoList(index, channel_id)

    # 检查视频是否过期 1天为期
    if time.time() - save_video_dict[channel_id][index]['time'] < CACHE_EXPIRY_TIME:
        return save_video_dict[channel_id][index]['data']
    
    return fetchAndCacheVideoList(index, channel_id)

def fetchAndCacheVideoList(index, channel_id):
    """获取视频并缓存结果"""
    result = getVideoList(index, channel_id)  # 假设这是获取视频数据的函数

    if result['status'] == 200:
        ts = time.time()
        if channel_id not in save_video_dict:
            save_video_dict[channel_id] = []
        save_video_dict[channel_id].append({'data': result, 'time': ts})

    return result
      

# 创建蓝图
list_address_bp = Blueprint('getVideoListAddress', __name__)
# 定义 GET 请求的路由
@list_address_bp.route('/getVideoListAddress', methods=['GET'])
def get_api_getVideoList():
  try:
      channel_id=request.args.get('channel_id')
      index=request.args.get('index')
      result=getVList(index,channel_id)
      return jsonify(result)
  except Exception:
      return jsonify({'status':400,'dataList':[]})