from flask import Blueprint, jsonify  # 添加了 request 和 jsonify 的导入
# 创建蓝图
start_bp = Blueprint('start', __name__)
# 定义 GET 请求的路由
@start_bp.route('/', methods=['GET'])
def get_api_getVideoList():
    """没有什么要做的,给访问根地址的人知道服务可以使用"""
    return jsonify({"status":200})


