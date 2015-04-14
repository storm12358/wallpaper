from scrapy.spider import Spider
from scrapy.selector import Selector
import urllib


class WallPaperSpider(Spider):
    name = "wallpaper"
    allowed_domains = ["nationalgeographic.com"]
    start_urls = [
        "http://photography.nationalgeographic.com/photography/photo-of-the-day/"
    ]

    def parse(self, response):
        sel = Selector(response)
        images = sel.xpath(".//*[@id='content_top']/div[2]/a/img").extract()
        for image in images:
            start = image.find('src="//') + 7 
            end = image.find('.jpg"') + 4
            image = 'http://' + image[start:end]
            image = image.split('/')
            image = image[-1]
            image = image.split('_')
            image_name = image[0]
            image_id = image[1]
            url = 'http://images.nationalgeographic.com/exposure/core_media/ngphoto/image/'+image_id+'_0_1920x1200.jpg'
            urllib.urlretrieve(url, image_name + ".jpg")
            urllib.urlretrieve(url, "wallpaper.jpg")
        return
