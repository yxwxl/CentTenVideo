from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    # 检查请求的 URL 是否是你要修改的 JS 文件
    if "https://vm.gtimg.cn/thumbplayer/core/1.35.13/txhlsjs-kernel.js?max_age=7776000" in flow.request.pretty_url:
        # 获取响应内容
        print(flow.request.pretty_url)
        js_content = flow.response.get_text()

        # 替换特定行，并添加自定义变量
        # js_content = js_content.replace(
        #     "Math.abs(this._videoInfo.duration-e)<=1?e-1:e;",
        #     "Math.abs(this._videoInfo.duration-e)<=1?e-1:e; window.my_result4=this._videoInfo.configInner.url;alert(window.my_result4);debugger;"
        # )
        js_content = js_content.replace(
            "Math.abs(this._videoInfo.duration-e)<=1?e-1:e;",
            "Math.abs(this._videoInfo.duration-e)<=1?e-1:e; window.my_result4=this._videoInfo.configInner.url;"
        )
        # 将修改后的 JS 内容写回响应
        flow.response.set_text(js_content)