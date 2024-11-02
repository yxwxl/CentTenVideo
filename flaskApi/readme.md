# Flask API 使用说明

> **端口默认在 127.0.0.1:3000**

API 可以通过端口调用的方式使用，也可以直接在 `util` 文件夹中引用相关代码。`util` 文件夹中的 `readme.md` 有详细的 API 说明，这里是 Flask 接口调用的说明。

---

## 使用示例

- 访问 `127.0.0.1:3000/getChannels` 即可获得频道 ID。
- 部分接口需要传递正确的参数，请参阅代码使用。所有接口默认是 `GET` 请求，但可以修改为 `POST` 请求。

---

### API 说明

前缀为 **127.0.0.1:3000/**

#### 1. getChannels.py

- **功能**：获取对应频道 ID 的接口。
- **后缀**：`/getChannels`。
- **参数**：无。

#### 2. getSearch.py

- **功能**：搜索 API，提供附加文本信息，返回对应的搜索结果（如腾讯视频的搜索框）。
- **后缀**：`/getSearch`。
- **参数**：`?text=xxx`（xxx 为搜索文本）。

#### 3. getSingleVideoList.py

- **功能**：获取单个视频（如《斗破苍穹》）所有集数的页面 `vid`。

  **示例**：组合以下部分以获得完整视频地址：

  - https://v.qq.com/x/cover/ + mzc002007sqbpce + / + r4100zvgz9i + .html

- `cid`: `mzc002007sqbpce` (确定的单个视频)
- `vid`: `r4100zvgz9i` (每一集不同)

- **后缀**：`/getHtmlLinkList`。
- **参数**：`?html_link=xxx`（xxx 为页面链接）。

#### 4. getVideoListAddress.py

- **功能**：获取视频列表，一次返回 21 个视频。输入频道 ID 和索引（index）下标返回相应视频列表。
- **默认排序**：按热门排序。
- **后缀**：`/getVideoListAddress`。
- **参数**：`?channel=channel_id&index=number`
- `channel_id` 为频道 ID（可通过 `getChannels.py` 获取），
- `index` 为自然数（0 为当前类别最火的视频）。

#### 5. getVideoM3u8.py

- **功能**：核心模块，默认不启用。请先阅读使用说明后启用。

- 支持多用户同时访问，并将用户按队列顺序请求 `m3u8`。
- 显示前方排队用户数量。
- 支持将当天的 `m3u8` 缓存在内存中。
- 单用户访问耗时约 15-20 秒。

- **后缀**：`/getM3U8`。
- **参数**：
- `?target=调用目的&html_link=页面链接&token=64位数字字符串`
- `target`：分为 `request` 和 `get`。`request` 用于初步请求，`get` 用于后续访问请求结果。
- `html_link`：请求视频当集的视频链接，可在 `getSingleVideoList.py` 中获取。
- `token`：当前用户的唯一标识（64 位字符串），一个用户同时只可以请求一个视频的 `m3u8`。

- **使用**：获取到 `m3u8` 后，可以在微信或手机自带浏览器（其他可能无法播放）或支持 H265/HEVC `m3u8` 的播放器中播放。

#### 6. getVideoM3u8.py 中的 getM3U8Url 函数

- **核心参数**：此函数的参数设置至关重要，请参考代码注释和文档进行配置。
- `REFRESH_TIME=10`：请求页面刷新时间。
- `MAX_TIME=18`：最大断开时间。

---

请务必仔细阅读上述说明，确保正确使用各个接口。
