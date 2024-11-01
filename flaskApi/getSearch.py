from flask import Blueprint, request, jsonify  
from util.searchBox import searchByText

# 创建蓝图
search_bp = Blueprint('getSearch', __name__)
# 定义 GET 请求的路由
@search_bp.route('/getSearch', methods=['GET'])
def get_api_getVideoList():  
    try:
        text=request.args.get('text')
        #输入搜索文本返回对应视频列表信息的函数
        result=searchByText(text)
        return jsonify(result)
    except Exception:
        return jsonify({"status":400,"ItemList":[]})

