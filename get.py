import urllib.request
import json

HOST_URL = "http://r.inews.qq.com/getSubItem?omgid=4ab6de1822c31a47380945722c69e7e2e627001021121c&mid=2e9aa13f6ab30b1c485db56c427f91f9e93fa5d2&devid=867981021758886&mac=02%253A00%253A00%253A00%253A00%253A00&qqnetwork=wifi&store=663&format=json&screen_height=2392&Cookie=%20lskey%3D%3B%20luin%3D%3B%20skey%3D%3B%20uin%3D%3B%20logintype%3D0%20&apptype=android&hw=Huawei_Nexus6P&appver=23_android_4.8.9&uid=3dbcd08bb74c1980&screen_width=1440&omgbizid=145265cf6008ee419d8975281ee0de59b41a005021121f&qn-sig=9b51bb14d3a665493d1246a1515101e4&qn-rid=976612818&imsi=460022109848976&chlid="

def oneRequest(chlid):
	url = HOST_URL + chlid
	response = urllib.request.urlopen(url)
	result = response.read().decode('utf-8')
	response.close()
	
	jsonData = json.loads(result)
	ret = jsonData["ret"]
	if(ret == 0):
		jsonChannel = jsonData["channelInfo"]
		
		chlid = jsonChannel["chlid"]
		chlname = jsonChannel["chlname"]
		icon = jsonChannel["icon"]
		sicon = jsonChannel["sicon"]
		desc = jsonChannel["desc"]
		subCount = jsonChannel["subCount"]
		keywords = jsonChannel["keywords"]
		uin = jsonChannel["uin"]
		intro = jsonChannel["intro"]
		recommend = jsonChannel["recommend"]
		wechat = ""
		try:
			wechat = jsonChannel["wechat"]
		except Exception as err:
			return
		readCount = jsonChannel["readCount"]
		shareCount = jsonChannel["shareCount"]
		colCount = jsonChannel["colCount"]
		print(chlid +","+chlname+","+str(subCount))

index = 1
while index < 100000:
	oneRequest(str(index))
	index = index+1