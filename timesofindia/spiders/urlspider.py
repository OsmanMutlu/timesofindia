import scrapy
import re
import codecs
import json

class QuotesSpider(scrapy.Spider):
    name = "urlspider"

    def start_requests(self):
        urls = [
            'https://timesofindia.indiatimes.com/2001/7/5/archivelist/year-2001,month-7,starttime-37077.cms',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
#        urls = response.xpath('//table[@class="cnt"][last()]//tr[last()]/td[@width="670"]/div[last()]//a/@href').extract()
        urls = response.xpath('//td[@width="49%"]//a/@href').extract()
        print(urls)
        filename = 'urls.jl'
        with codecs.open(filename, 'a', 'utf-8') as f:
            for rl in urls:
                line = json.dumps(rl,ensure_ascii=False) + "\n"
                f.write(line)
        m = re.findall(r"\d+",response.url)
        m = int(m[-1]) + 1
        if m<+43093:
            m = str(m) + ".cms"
            url = re.sub(r"\d+\D+$", m, response.url)
            yield scrapy.Request(url, callback=self.parse)
#stopped at 37449 !!!
