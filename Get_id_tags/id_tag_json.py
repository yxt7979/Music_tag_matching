import json
import requests
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 获取数据多了之后，就会被禁用访问,可以使用代理
    'Cookie': 'MUSIC_U=f8b73ab123ddad32d44c37546522e06bb123363f4b813922a1902f2ds2ceb750c52sd32ccbb1ab2b9c23asd3a31522c7067cce3c7469;',
    'DNT': '1',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Referer': 'http://music.163.com/album?id=71537',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
person = []
f = open("list.txt",'r+')
data1 = f.readlines()
for i in range(len(data1)):
    id = data1[i]
    url = "http://localhost:3000/playlist/detail?id=" + id
    # print(url)
    res = requests.get(url,headers=headers).json()   #把爬取到的json格式的网页转换成字典格式
    if res.get("playlist") != None:
        if res.get("playlist")["trackIds"] != None:
            num_tags = len(res.get("playlist")["trackIds"])
            for i in range(num_tags):
                # 生成JSON格式
                music = {'id': str(res.get("playlist")["trackIds"][i].get("id")), 'tags': res.get("playlist")["tags"]}
                music = json.dumps(music,indent=4)
                with open("anss.json",'a') as f_js:
                    f_js.write(music + ',')
                person.append(music)
                # print(res.get("playlist")["trackIds"][i].get("id"))
                # print(res.get("playlist")["tags"])
    # print(json_str)
    print(id)
    print(type(person))
json_str=json.dumps(person)
with open("ans5.txt",'w+') as k:
    k.write(json_str)
f_js.close()
f.close()