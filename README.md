## Usin Python and Scrapy framework to scripe information form web site : book.toscrape.com.
The purpose of this project is to scrape out info on the web for,'book name','price','rating','in stock' information.
I also strip out the price to number without £ in front of it,  (£32.55 to 32.55) so it is easy for you do analysis later.

The follwoing are the steps to take if you want reproduce the result:

setup virtual environment:       python -m venv venv
Activate virtual environment:    venv\Scripts\activate.bat
Install scrapy:                  pip install scrapy
check installs:                  pip freeze
check all the command:           scrapy
start the project:               scrapy startproject TheSpider
check the folder created:        cd TheSpider
to generate spider:              scrapy genspider thespider book.toscrape.com
To run:                          scrapy crawl thespider
to export result:               scrapy crawl thespider -o book.csv
