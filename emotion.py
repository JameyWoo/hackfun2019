# encoding:utf-8
import requests
import json
import base64

'''
人脸情绪检测
'''

def detectEmotion(filename):
    request_url = request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

    url_image_1 = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559373867&di=b434e79a8990fe0e9e1822cd97a33079&imgtype=jpg&er=1&src=http%3A%2F%2Fimg1.a.chinanb.org%2F201812%2F27%2F14%2F14-03-13-96-1015697.jpg"
    url_image_2 = "https://b-ssl.duitang.com/uploads/blog/201504/01/20150401204428_U4cjv.thumb.700_0.jpeg"
    url_image_3 = "http://img.hq2011.com/www.hq2011.com/uploads/allimg/181025/230249B06-0.jpg"

    # f = open('./src/demo.jpg', 'rb')
    f = open(filename, 'rb')
    # 参数image：图像base64编码 以及face_fields参数
    # image的值取决于 image_type
    img = base64.b64encode(f.read())

    params = {'image': img, 'image_type': 'BASE64', "liveness_control": "NONE", \
              "face_field": "emotion", "liveness_control": "LOW"}

    access_token = '24.a7c39f35abb15b26c4a6dc9977fdd9c2.2592000.1561349225.282335-16308521'
    request_url = request_url + "?access_token=" + access_token

    r = requests.post(request_url, data=params)
    print(r.text)
    jfile = json.loads(r.text)
    if jfile['error_code'] != 0:
        return "-1"
    print(jfile['result']['face_list'][0]['emotion']['type'])
    return jfile['result']['face_list'][0]['emotion']['type']

if __name__ == '__main__':
    detectEmotion('./static/demo.jpg')