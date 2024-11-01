import requests

url = 'https://vd6.l.qq.com/proxyhttp'

# 定义 headers
headers = {
    'Origin':'https://v.qq.com',
    'Referer':'https://v.qq.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}


def getData():
    data = {
        "buid": "vinfoad",
        "vinfoparam": "refer=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200n53vkqc%2Ff0046vebaxn.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200n53vkqc%2Ff0046vebaxn.html&sphttps=1&encryptVer=9.2&cKey=G9MiSr-xCtW1Js1Orq2-LnCjnpb8Ocr0cPTe3FBjzEul_f4vOWcoV2JPcsrTubI9OVVF0xZe3gRz6ILVGCTZlxo--_XGuZWLjvmpaTXWr2DNOLGAi4iBp92IyOBupJKemBGuroMK5ccgDyKh6cqchEKDlC2uGzpCCamWfdlZnHB5x6wVJHKsVyf3svRoLvLp4yt5irIvBazTFI6klX7qSYlxDPbyyf8e8SL3SEnx_Be7hS-CqvGS-3eMyGukyUCh357ATNXrjbMFnHOuoe4n7PAuyCqUYRXnwdjd00NjG9tyPdLj8cf4tKionqqzu9pXa5Iv0r5U5933Leyp0No30P8ehozoduEJe7nwfr5VlonhnQQOMzgKxqsBS3ZQkwwyBrE9dP9JIKBjnsIZ_44Nla_zbIWdsJu84lDK1oci07xMicWeOgLE16ak6nX746ZAdLi8-nKZd5kCQgwwoDzPzkBI9vaI4F4ndcHpRY_tPMTEFLngwcEZXIWWy7yKlQFII4OS5q-pAgJEUKwD&clip=4&guid=29604b53ff7835c9&flowid=83c61f4efa47e1cc1a57027946234d82&platform=10201&sdtfrom=v1010&appVer=1.35.15&unid=&auth_from=&auth_ext=&vid=f0046vebaxn&defn=uhd&fhdswitch=0&dtype=3&spsrt=2&tm=1729666481&lang_code=0&logintoken=%7B%22access_token%22%3A%22259DE695329D1994518F0B86DAF64FA2%22%2C%22appid%22%3A%22101483052%22%2C%22vusession%22%3A%22PoLEchxD9nSm3a-IA0fZ6Q.M%22%2C%22openid%22%3A%2276D6A1DED46C7A8B4A7CDB03ED286DDC%22%2C%22vuserid%22%3A%22804304168%22%2C%22video_guid%22%3A%2229604b53ff7835c9%22%2C%22main_login%22%3A%22qq%22%7D",
        "adparam": "vid=f0046vebaxn"
    }
    # 发送 POST 请求
    # 定义请求的 body（数据）
    
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        data=response.json()
        print(data)
    else :
        print(response.status_code)

getData()