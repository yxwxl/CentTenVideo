# 具体的请求 api 实现

## getAddressList.py

### 默认使用 filterSearchAll 输入页面链接 https://v.qq.com/x/cover/mzc002007sqbpce/r4100zvgz9i.html

### 注意页面链接 html 问号后面如果有要去掉 返回所有的 vid 去预告,彩蛋,采访等无关部分

### searchAll 不去除上面部分

## loadHotVideo.py

### getChannels 获取所有频道 动漫,电影,电视剧等...

### getVideoList 获取对应频道视频列表,一次请求 21 个视频

## searchBox.py

### 搜索框的 api,可以自行选择搜索内容,输入搜索文本,返回对应的视频列表,同腾讯的搜索框

## proxy_script.py 需要配合 mitmdump 使用,不熟悉的建议不要使用,要求配置配置很多东西

### 使用命令 mitmdump -s util/proxy_script.py 使用前开启网络代理 127.0.0.1 8000
