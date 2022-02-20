import scrapy
pages = int(input('How many pages do you wanna scrape ? '))
dictionary ={'One':1,'Two':2,'Three':3,'Four':4, 'Five':5}

class ThespiderSpider(scrapy.Spider):
    name = 'thespider'
    start_urls = ['https://books.toscrape.com/catalogue/page-{}.html'.format(i+1) for i in range(pages)]

    def parse(self, response):
        data ={}   # empty dictionary to house the scraped data
        books = response.css('ol.row')
        for book in books:
            for b in book.css('article.product_pod'):
                data['Title'] = b.css('a::attr(title)').getall()
                data['Price'] = b.css('div.product_price p.price_color::text').getall()[0][1:6]
                 #.replace('£','')
                data['Stock'] = b.css('div.product_price p.instock.availability::text').getall()[1].strip()
                data['Star'] = b.css('p::attr(class)').getall()[0].split()[-1]
                data['Star'] = [v for k,v in dictionary.items()  if k in data['Star']][0]
                yield data