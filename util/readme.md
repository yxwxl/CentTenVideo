# 具体的请求 API 实现

---

## getAddressList.py

- **默认方法**：`filterSearchAll`
  - **输入**：页面链接，例如 `https://v.qq.com/x/cover/mzc002007sqbpce/r4100zvgz9i.html`
  - **注意**：页面链接中的 `html` 后的问号部分若存在需去除，以返回所有有效的 `vid`，避免预告、彩蛋、采访等无关内容。
  - **searchAll**：不去除上述部分。

---

## loadHotVideo.py

- **方法**：`getChannels`

  - **功能**：获取所有频道，如动漫、电影、电视剧等。

- **方法**：`getVideoList`
  - **功能**：获取对应频道的视频列表，一次请求返回 21 个视频。

---

## searchBox.py

- **功能**：搜索框 API，可自定义搜索内容。
  - **输入**：搜索文本，返回与搜索内容相关的视频列表（类似腾讯视频的搜索框功能）。

---

## proxy_script.py

- **说明**：需要配合 `mitmdump` 使用。由于配置较复杂，不熟悉的用户不建议使用。
  - **使用命令**：`mitmdump -s util/proxy_script.py`
  - **前置要求**：启用网络代理 `127.0.0.1:8000`（此端口可根据需要进行调整）。
