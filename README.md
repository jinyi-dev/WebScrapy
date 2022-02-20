setup virtual environment       python -m venv venv

Activate virtual environment    venv\Scripts\activate.bat
Install scrapy                  pip install scrapy

check installs                  pip freeze

check all the command           scrapy

start the project               scrapy startproject TheSpider

check the folder created        cd TheSpider

to generate spider              scrapy genspider thespider book.toscrape.com
To run                          scrapy crawl thespider

to export result               scrapy crawl thespider -o book.csv
