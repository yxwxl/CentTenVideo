# 各 flaskApi 的使用说明 是端口调用的形式,也可以到 util 文件夹中自行使用

## 端口默认在 127.0.0.1:3000 使用例子

### 访问 127.0.0.1:3000/getChannels 即可拿到对应频道 id 的接口

### 部分接口需要传递正确的参数,请观察代码后使用,接口均为 get 请求,可自行修改成 post 请求

## getChannels.py

### 获取对应频道 id 的接口

## getSearch.py

### 搜索框的 api,附加文本信息,返回对应的搜索结果,即腾讯视频的搜索框

## getSingleVideoList.py

### 获取单个视频比如斗破苍穹所有集数的页面 vid,组合后即可拿到完整的网址

### 例子 https://v.qq.com/x/cover/ + mzc002007sqbpce + / + r4100zvgz9i + .html 组合

### cid: mzc002007sqbpce 单个视频是确定的 vid: r4100zvgz9i 每一集都不同

## getVideoListAddress.py

### 获取视频列表,一次返回 21 个视频,比如输入频道 id 和 index 下标返回对应视频列表

### 默认按热门排序

## getVideoM3u8.py

### 最核心的模块,默认不启用,请自行阅读使用说明后启用

### 支持多用户同时访问,用户会按队列排队请求对应视频的 m3u8

### 支持显示前方排队用户数量

### 支持缓存当天 m3u8 在内存中

### 单用户访问大约 15-20s

## getVideoM3u8.py  getM3U8Url函数有一个核心参数

