#Download a website
import requests
import re

#url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=Time+quotes'

#simulate browser requests
word = input("Input key word: ")
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
result = requests.get(url)

html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
i = 0
for each in pic_url:
    print (each)
    try:
        pic = requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
        print ('【错误】当前图片无法下载')
        continue

    string = 'Puppies\\' + str(i) + '.jpg'
    fp = open(string, 'wb')
    fp.write(pic.content)
    fp.close()
    i += 1


