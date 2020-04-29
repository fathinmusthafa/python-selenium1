import os

from bs4 import BeautifulSoup
from selenium import webdriver
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def image():
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument('--disable-extensions')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')

    browserdriver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\LENOVO\Downloads\chromedriver_win32\chromedriver.exe')
    url = 'https://www.bhinneka.com/jual-smart-phone/3457276/apple'

    browserdriver.get(url)
    content = browserdriver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    search_area = soup.findAll('div', 'col-lg-3 col-md-3 col-xs-6 bt-product-catalog-item')
    return render_template('withImage.html', area = search_area)

@app.route('/without_image')
def without_image():
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    options.add_argument('--disable-extensions')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    browserdriver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\LENOVO\Downloads\chromedriver_win32\chromedriver.exe')
    url = 'https://www.bhinneka.com/jual-smart-phone/3457276/apple'

    browserdriver.get(url)
    content = browserdriver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    search_area = soup.findAll('div', 'col-lg-3 col-md-3 col-xs-6 bt-product-catalog-item')
    return render_template('withoutImage.html', area = search_area)

if __name__ == '__main__':
    app.run(debug=True)