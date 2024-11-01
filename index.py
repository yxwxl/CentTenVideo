from flask import Flask
from flask_cors import CORS

#index.py            是主文件负责启动项目 开启 flask服务
#flaskApi            用于不同的接口接收get post请求
#seleniumApi         用于模拟浏览器的相关功能实现
#videoAddressApi     用于获取或更新视频地址，获取视频首页地址和后续一连串地址（电视剧很多集）
#downloadVideoApi    用于下载视频到videoStorage文件夹，每一部作品一个子文件夹
#util                用于存放一些辅助函数
#videoStorage        用于存放下载视频
#videoAddressStorage 用于存放视频地址 以及详情 具体级数的地址和对应的m3u8
#test                用于试验代码

# 运行应用程序 
if __name__ == '__main__':
  
  #不同的请求接口
  from flaskApi.start               import start_bp
  from flaskApi.getVideoListAddress import list_address_bp
  from flaskApi.getSearch           import search_bp
  from flaskApi.getChannels         import channels_bp
  from flaskApi.getSingleVideoList  import html_link_bp
  from flaskApi.getVideoM3u8        import download_bp
  # 创建 Flask 应用程序实例
  app = Flask(__name__)
  CORS(app)  # 允许所有来源的请求
  # 表示成功的路由
  app.register_blueprint(start_bp)
  # 视频列表的路由 
  app.register_blueprint(list_address_bp)
  # 获取搜索框的路由
  app.register_blueprint(search_bp) 
  # 频道路由
  app.register_blueprint(channels_bp)
  # 页面列表下载路由
  app.register_blueprint(html_link_bp)
  # 视频下载请求的的路由
  app.register_blueprint(download_bp)

  app.run(debug=False,host='127.0.0.1', port=3000)