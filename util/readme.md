# 具体的请求 API 实现

---

## 1. getAddressList.py

- **默认方法**：`filterSearchAll`
  - **输入**：页面链接，例如 `https://v.qq.com/x/cover/mzc002007sqbpce/r4100zvgz9i.html`
  - **参数说明**：例如，链接中的 `cid:mzc002007sqbpce` 和 `vid:r4100zvgz9i` 可用于自行组合页面链接。
  - **功能**：返回视频的所有集数中的 `vid` 列表。
  - **使用**：`filterSearchAll(html_link)` 输入对应视频的页面链接，返回包含所有 `vid` 的列表。
  - **注意**：若页面链接中 `html` 后包含问号及其内容，请去除，以避免包含预告、彩蛋、采访等无关内容。
  - **`searchAll` 方法**：此方法在使用时不去除上述问号后的内容，因此返回的 `vid` 列表可能包含无关内容。

---

## 2. loadHotVideo.py

- **方法**：`getChannels`

  - **功能**：获取所有频道，如动漫、电影、电视剧等。
  - **使用**：`getChannels()` 返回所有频道的 `channel_id` 和对应的频道名称。

- **方法**：`getVideoList`
  - **功能**：获取指定频道的视频列表，一次返回 21 个视频。
  - **参数**：
    - `index`：分页参数，从 0 开始。
    - `channel_id`：频道 ID，默认为 "100113"（电视剧频道）。
  - **使用**：`getVideoList(index, channel_id="100113")` 返回对应频道和页码的视频信息，按热度排序。
  - **返回**：包含视频的 `title`、第一集链接、图片链接等详细信息。

---

## 3. searchBox.py

- **方法**：`searchByText`
  - **功能**：搜索框 API，可自定义搜索内容。
  - **参数**：
    - `text`：输入的搜索文本。
  - **使用**：`searchByText(text)` 返回与输入文本相关的视频列表，功能类似于腾讯视频的搜索框。

---

## 4. proxy_script.py

- **说明**：需要配合 `mitmdump` 使用，适用于网络代理设置和特定数据转发，配置较为复杂，不熟悉的用户建议谨慎使用。
  - **使用命令**：`mitmdump -s util/proxy_script.py`
  - **配置要求**：
    - 需下载 `mitmproxy` 及相应证书，安装并配置代理。
  - **前置要求**：启用网络代理 `127.0.0.1:8000`（端口可调整）。

---

请根据具体需求和项目要求，仔细阅读并正确配置各 API 及相关文件。
