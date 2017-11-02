__author__ = 'CQC'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class BDTB:
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)

    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #print response.read()
            f = open("/home/angus/test/test.txt","w")
            f.write(response.read())
            return response
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"error link",e.reason
                return None
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<title>.*',re.S)
        result = re.search(pattern, page)
        if result:
            print result.group(1)
            return result.group(1).strip()
        else:
            return None

    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        for item in items:
            print item

baseURL = 'https://tieba.baidu.com/p/2822158075'
bdtb = BDTB(baseURL,1)
#bdtb.getContent(bdtb.getPage(1))
#bdtb.getTitle()
bdtb.getPage(1)