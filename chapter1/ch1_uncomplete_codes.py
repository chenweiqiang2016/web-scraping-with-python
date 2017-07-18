import urllib2

def download(url):
    return urllib2.urlopen(url).read()

         ||
         || 更加健壮的版本
         || 可以捕获异常
         ||
         \／

import urllib2

def download():
    print "Downloading:", url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print "Downloading error:", e.reason
        html = None
    return html

         ||
         || 服务器过载 503 Service Unavailable 5xx错误 服务端存在问题
         || 404 Not Found 4xx错误 请求存在问题
         || 支持重试下载功能
         ||
         \/

def download(url, num_retries=2):
	print "Downloading:", url
	try:
		html = urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print "Downloading error:", e.reason
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500<= e.code < 600:
				# recursively retry 5XX HTTP errors
				return download(url, num_retries-1)
	return html


