# -*- coding: utf-8 -*-
from uamobile.scrapers.base import Scraper

class DoCoMoScraper(Scraper):
    url = 'http://www.nttdocomo.co.jp/service/imode/make/content/ip/'

    def do_scrape(self, doc):
        return [str(x.text) for x in doc.xpath('//div[@id="maincol"]/div[@class="boxArea"][1]/div/div[@class="section"]/ul[@class="normal txt"][1]/li')]

class EZWebScraper(Scraper):
    url = 'http://www.au.kddi.com/ezfactory/tec/spec/ezsava_ip.html'

    def do_scrape(self, doc):
        res = []
        rows = doc.xpath("""//a[@name="Body"]/following-sibling::table//table//table[@cellspacing="1"]/tr[@bgcolor="#ffffff"]""")
        for row in rows:
            cols = row.xpath('./td/div[@class="TableText"]')
            if cols[1].xpath('*//s'):
                # deprecated
                continue
            res.append('%s%s' % (cols[1].text_content(), cols[2].text_content()))
        return res


class SoftBankScraper(Scraper):
    url = 'http://creation.mb.softbank.jp/mc/tech/tech_web/web_ipaddress.html'

    def do_scrape(self, doc):
        return [x.text.strip() for x in doc.xpath("//div[@id='contents']//table[@class='onece_table']/tr/th")]


class WILLCOMScraper(Scraper):
    url = 'http://www.willcom-inc.com/ja/service/contents_service/create/center_info/index.html'

    def do_scrape(self, doc):
        res = []
        sep = 0
        for td in doc.xpath("//*[@class='m_box']/table[@class='plan03']/tr/td"):
            if td.attrib.get('colspan') == "4":
                sep += 1
                if sep > 2:
                    break
            else:
                if td.attrib.get('align') == 'center' and td.attrib.get('bgcolor') == 'white':
                    txt = td.text.strip()
                    if txt:
                        res.append(txt)
        return res
