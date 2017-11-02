__author__ = 'CQC'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re


class Tool:

    removeImg = re.compile('<img.*?>| {7}|')

    removeAddr = re.compile('<a.*?>|</a>')

    replaceLine = re.compile('<tr>|<div>|</div>|</p>')

    replaceTD = re.compile('<td>')

    replacePara = re.compile('<p.*?>')

    replaceBR = re.compile('<br><br>|<br>')

    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)

        return x.strip()



class BDTB:

    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()


    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"error", e.reason
                return None


    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            #print result.group(1)
            return result.group(1).strip()
        else:
            return None


    def getPageNum(self):
        self.page = self.getPage(1)
        page = self.page
        #pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        repattern = re.compile('<li class="l_reply_num.*?><span.*?>(.*?)</span>',re.S)
        result = re.search(repattern, page)
        if result:
            #print result.group(1)
            return result.group(1).strip()
        else:
            return None


    def getContent(self, page,number):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        # for item in items:
        #  print item
        print number
        for i in range(0,int(number)+1):
            print self.tool.replace(items[i])


baseURL = 'https://tieba.baidu.com/p/2822158075'
bdtb = BDTB(baseURL, 1)
#bdtb.getTitle()
bdtb.getContent(bdtb.getPage(1),bdtb.getPageNum())
#bdtb.getPageNum()