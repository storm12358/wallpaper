from scrapy.spider import Spider
from scrapy.selector import Selector
import urllib


class WallPaperSpider(Spider):
    name = "wallpaper"
    allowed_domains = ["nationalgeographic.com"]
    start_urls = [
        "http://feeds.nationalgeographic.com/ng/photography/photo-of-the-day/"
    ]

    def parse(self, response):
        sel = Selector(response)
        images = sel.xpath(".//*[@id='feedContent']/xhtml:div[3]/xhtml:div[1]/xhtml:p[3]/xhtml:em").extract()
        for image in images:
            start = image.find('src="//') + 7 
            end = image.find('.jpg"') + 4
            image = 'http://' + image[start:end]
            print(image)
#            urllib.urlretrieve(image, "wallpaper.jpg")
        return
