from flask import Blueprint, jsonify  
from util.loadHotVideo import getChannels

#获取频道id,不同类别的视频,如动漫、电视剧...会有不同的频道id。
Channels=getChannels()
print("Channels\n",Channels)

# 创建蓝图
channels_bp = Blueprint('getChannels', __name__)
# 定义 GET 请求的路由
@channels_bp.route('/getChannels', methods=['GET'])
def get_api_getVideoList():
    try:
        return jsonify({"status":200,"data":Channels})
    except Exception:
        return jsonify({"status":400,"data":[]})

