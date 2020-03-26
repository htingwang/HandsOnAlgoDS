# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        seen = set()
        queue = collections.deque()
        hostname = startUrl.split("/")[2]
        seen.add(startUrl)
        queue.append(startUrl)
        while queue:
            cur = queue.popleft()
            for url in htmlParser.getUrls(cur):
                if url.find(hostname) != -1 and url not in seen:
                    queue.append(url)
                    seen.add(url)
        return list(seen)                                  
