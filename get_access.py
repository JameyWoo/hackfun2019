import urllib, sys
import urllib.request as urllib2
import ssl

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=efVUT7QNNCnj81O9mnDx16Gg&client_secret=Hbh4GfCl5l645tEBEUwekRdtKGYFMUmn'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)
    # print(content['access_token'])