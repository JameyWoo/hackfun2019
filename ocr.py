# encoding:utf-8
import requests
import json
import base64

'''
人脸对比
'''

def ocrIt(filename):
    request_url = request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

    url_image_1 = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559373867&di=b434e79a8990fe0e9e1822cd97a33079&imgtype=jpg&er=1&src=http%3A%2F%2Fimg1.a.chinanb.org%2F201812%2F27%2F14%2F14-03-13-96-1015697.jpg"
    url_image_2 = "https://b-ssl.duitang.com/uploads/blog/201504/01/20150401204428_U4cjv.thumb.700_0.jpeg"
    url_image_3 = "http://img.hq2011.com/www.hq2011.com/uploads/allimg/181025/230249B06-0.jpg"

    # f = open('./src/ocrtest.jpg', 'rb')
    f = open(filename, 'rb')
    # 参数image：图像base64编码 以及face_fields参数
    # image的值取决于 image_type
    img = base64.b64encode(f.read())

    params2 = {'image': img, 'image_type': 'BASE64', 'language_type': 'CHN_ENG'}

    access_token = '24.c97c2fcdbd93d32d88a6544de071478a.2592000.1561424678.282335-16346792'
    request_url = request_url + "?access_token=" + access_token

    r = requests.post(request_url, data=params2)
    # print(r.text)
    jfile = json.loads(r.text)
    # print(jfile)
    content = ''
    for each in jfile['words_result']:
        content += each['words']
    print(content)
    pre = "重复匹配"
    if pre in content:
        print("ocr 验证成功!")
        return "ocr 验证成功！"
    print("ocr 验证失败!")
    return "ocr 验证失败！"

if __name__ == '__main__':
    ocrIt('./static/ocrtest.jpg')