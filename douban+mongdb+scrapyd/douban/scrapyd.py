# coding=utf-8
import urllib
import urllib.request
# 启动爬虫 远程调用服务器上的程序  结果直接存储在本地
test_data = {'project': 'doubanmovie', 'spider': 'doubanmovie'}#用户自定义表单
test_data_urlencode = urllib.parse.urlencode(test_data).encode('utf-8')#将自定义test_data转换成标准格式

requrl = "http://localhost:6800/schedule.json"

# 以下是post请求,发送用户请求
req = urllib.request.urlopen(url=requrl, data=test_data_urlencode)

# 读取并解码内容
res = req.read().decode("utf-8")  # res 是str类型
print(res)

# 查看日志
# 以下是get请求
myproject = "doubanmovie"
requrl = "http://localhost:6800/listjobs.json?project=" + myproject
res_data = urllib.request.urlopen(requrl)

res = res_data.read().decode("utf-8")
print(res)
