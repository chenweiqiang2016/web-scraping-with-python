
# 网站地图爬虫

def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrap html here
        # ...



# ID遍历爬虫

import itertools

for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/%d' % page
    html = download(url)
    if html is None:
        break
    else:
        # success - can scrap the result
        pass


    |
    | ID之间并不是连续的
    | 连续发生多次下载错误后才会退出程序
    |

# maximun number of consecutive download errors allowed
max_errors = 5

# current number of consecutive download errors
num_errors = 0

for page in itertools.count(1):
    url = "http://example.webscraping.com/view/%d" %page
    html = download(url)
    if html is None:
        # received an error trying to download this webpage
        num_errors += 1
        if num_errors == max_errors:
            # reached maximum number of
            # consecutive errors so exit
            break
    else:
        # success - can scrape the result
        # ...
        num_errors = 0

# 链接爬虫

imprt re

def link_crawler(seed_url, link_regex):
	"""Crawl from the given seed URL following links matched by link_regex
	"""
	crawl_queue = [seed_url]
	while crawl_queue:
		url = crawl_queue.pop()
		html = download(url)
		# filter for links matching our regular expression
		for links in get_links(html):
			if re.match(link_regex, link):
				crawl_queue.append(link)

def get_links(html):
	"""Return a list of links from html
	"""
	# a regular expression to extract all links from the webpage
	webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
	# list of all links from the webpage
	return webpage_regex.findall(html)




