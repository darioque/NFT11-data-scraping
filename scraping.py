# import urllib library
from operator import indexOf
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def main():
    return scrapeTelegram('https://t.me/nft11official'), scrapeTelegram('https://t.me/nft11_en_official'), scrapeTelegram('https://t.me/NFT11_PT_BR'), scrapeTelegram('https://t.me/nft11_es_official'), scrapeTelegram('https://t.me/nft11_vn'), scrapeDiscord(), int(cg.get_coin_info_from_contract_address_by_id('binance-smart-chain', '0x73F67AE7f934FF15beaBf55A28C2Da1eEb9B56Ec')['community_data']['twitter_followers']), scrapeInstagram(), scrapeFacebook(), cg.get_price(ids='nft11', vs_currencies='usd')['nft11']['usd'], scrapeBscScan(
        'https://bscscan.com/token/0x73f67ae7f934ff15beabf55a28c2da1eeb9b56ec'), cg.get_price(ids='nft11', vs_currencies='usd', include_24hr_vol=True)['nft11']['usd_24h_vol'], cg.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd'], cg.get_price(ids='binancecoin', vs_currencies='usd')['binancecoin']['usd'], scrapeCryptocom(), scrapeTofuLegend(), scrapeTofuLegend2(), scrapeBscScan(
        'https://bscscan.com/token/0xc2dea142de50b58f2dc82f2cafda9e08c3323d53'), scrapeTofuVolume(), scrapeTofuVolume2(), scrapeTofu(
        'https://tofunft.com/collection/nft11-stadium/items?meta_double_2=1,1&sort=price_asc'), scrapeTofu(
        'https://tofunft.com/collection/nft11-stadium/items?meta_double_2=2,2&sort=price_asc'), scrapeTofu(
        'https://tofunft.com/collection/nft11-stadium/items?meta_double_2=3,3&sort=price_asc'), scrapeTofu(
        'https://tofunft.com/collection/nft11-stadium/items?meta_double_2=4,4&sort=price_asc'), scrapeTofu(
        'https://tofunft.com/collection/nft11-stadium/items?meta_double_2=5,5&sort=price_asc'), scrapeTofu(
        'https://tofunft.com/collection/nft11-stadium/items?meta_double_2=6,6&sort=price_asc'), scrapeBscScan(
        'https://bscscan.com/token/0x6bf87165ea4c3442964752c359c3306d74bf4f3c'), scrapeStadiumSales()


def scrapeTelegram(url):
    # store the response of URL
    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    response = urlopen(r).read()

    soup = BeautifulSoup(response, 'html.parser')

    scrapedGroupMembers = soup.find(
        'div', {'class': 'tgme_page_extra'}).text.replace(' ', '')

    tgGroupMembers = re.findall('[0-9]+', scrapedGroupMembers)[0]
    print(tgGroupMembers)
    return int(tgGroupMembers)


def scrapeDiscord():
    # store the URL in url as
    # parameter for urlopen
    url = "https://discord.gg/nft11"

    # store the response of URL
    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    response = urlopen(r).read()

    soup = BeautifulSoup(response, 'html.parser')

    scrapedGroupMembers = soup.find(
        'meta', {'property': 'og:description'}).get('content').replace(',', '')

    # Get the numbers from a string and use the [1] index to get the number of members
    discordGroupMembers = re.findall('[0-9]+', scrapedGroupMembers)[1]

    print(discordGroupMembers)

    return int(discordGroupMembers)


def scrapeInstagram():
    # store the URL in url as
    # parameter for urlopen
    url = "https://www.google.com/search?q=nft11_official+instagram&oq=nft11_official+instagram&aqs=chrome..69i57j69i60l2.3482j0j4&sourceid=chrome&ie=UTF-8"

    # store the response of URL
    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    response = urlopen(r).read()
    soup = BeautifulSoup(response, 'html.parser')

    instagramFollowers = re.findall(
        '[0-9]+', soup.find('div', {'class': 'BNeawe s3v9rd AP7Wnd'}).text)[0]
    print(instagramFollowers)
    return int(instagramFollowers)


# def scrapeFacebook():
#     # store the URL in url as
#     # parameter for urlopen
#     url = "https://www.google.com/search?q=facebook+nft11"
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--disable-gpu')
#     driver = webdriver.Firefox(options=options)
#     driver.get(url)
#     time.sleep(5)  # time to wait to start scraping the html
#     page = driver.page_source  # raw html
#     driver.quit()
#     soup = BeautifulSoup(page, 'html.parser')  # parsing html to text
#     print(soup)
#     rawFacebookData = soup.findAll('span', {'dir': 'auto'})
#     facebookData = rawFacebookData[0:2] + '000'
#     print(facebookData)
#     print(facebookData)
#     return (int(facebookData), int(facebookData))
    
def scrapeFacebook():
    # store the URL in url as
    # parameter for urlopen
    url = "https://www.google.com/search?q=facebook+nft11"
    # store the response of URL
    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    response = urlopen(r).read()
    soup = BeautifulSoup(response, 'html.parser')
    facebookFollowers = re.findall(
        '[0-9]+', soup.find('div', {'class': 'BNeawe s3v9rd AP7Wnd'}).text)[4]
    facebookLikes = facebookFollowers
    print(facebookFollowers, facebookLikes)
    return (int(facebookFollowers), int(facebookLikes))


def scrapeBscScan(url):
    # store the response of URL
    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    response = urlopen(r).read()
    soup = BeautifulSoup(response, 'html.parser')
    holders = re.findall(
        '[0-9]+', (soup.find('div', {'class': 'mr-3'}).text.replace(',', '')))[0]
    print(holders)
    return int(holders)


def scrapeCryptocom():
    url = "https://crypto.com/price/categories/gamefi"

    # store the response of URL
    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    response = urlopen(r).read()
    soup = BeautifulSoup(response, 'html.parser')
    gameFiMC = soup.find('div', {
                         'class': 'css-qznh9z'}).text.replace('$', '').replace('B', '').replace(' ', '')

    print(gameFiMC)
    return float(gameFiMC)


def scrapeTofu(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(5)  # time to wait to start scraping the html
    page = driver.page_source  # raw html
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')  # parsing html to text
    lowestPrice = soup.find('p', {'class': 'chakra-text css-0'}
                            ).text.replace(' ', '').replace('BNB', '')
    print(lowestPrice)
    return float(lowestPrice)


def scrapeTofuLegend():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)
    url = "https://tofunft.com/collection/nft11players/items?sort=price_asc"
    driver.get(url)
    time.sleep(5)  # time to wait to start scraping the html
    page = driver.page_source  # raw html
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')  # parsing html to text
    lowestPrices = soup.findAll('p', {'class': 'chakra-text css-1ucdead'})
    lowestPrice = 0.03
    lowestPriceRegulars = soup.findAll('p', {'class': 'chakra-text css-0'})[0].text.replace(' ', '').replace('BNB', '')
    for i in range(len(lowestPrices)):
        if 'Legend' in lowestPrices[i].text:
            lowestPrice = soup.findAll('p', {'class': 'chakra-text css-0'})[i].text.replace(' ', '').replace('BNB', '')
    print(lowestPrice, lowestPriceRegulars)
    return float(lowestPrice), float(lowestPriceRegulars)

def scrapeTofuLegend2():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)
    url = "https://tofunft.com/collection/nft-11-legend-player/items?sort=price_asc"
    driver.get(url)
    time.sleep(5)  # time to wait to start scraping the html
    page = driver.page_source  # raw html
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')  # parsing html to text
    lowestPrices = soup.findAll('p', {'class': 'chakra-text css-1ucdead'})
    # lowestPriceRegulars = soup.findAll('p', {'class': 'chakra-text css-0'})[0].text.replace(' ', '').replace('BNB', '')
    for i in range(len(lowestPrices)):
        if 'Legend' in lowestPrices[i].text:
            lowestPrice = soup.findAll('p', {'class': 'chakra-text css-0'})[i].text.replace(' ', '').replace('BNB', '')
            print(lowestPrice)
            return float(lowestPrice)

def scrapeTofuVolume():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)
    url = "https://tofunft.com/collection/nft11players/activities"
    driver.get(url)
    time.sleep(5)  # time to wait to start scraping the html
    page = driver.page_source  # raw html
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')  # parsing html to text
    lastSales = soup.findAll('span', {'class': 'chakra-text css-1dp94ug'})
    salePrices = soup.findAll('p', {'class': 'chakra-text css-1uhznsn'})
    legendTypes = soup.findAll('a', { 'class': 'chakra-link css-1jw7pf0'})
    amountOfSales = 0
    volumeOfSales = 0
    for i in range(len(lastSales)):
        if ('hour' in lastSales[i].text or 'minutes' in lastSales[i].text) and 'Legend' in legendTypes[i].text:
            amountOfSales += 1
            volumeOfSales += float(salePrices[i].text.replace(' ', '').replace('BNB', ''))
    print(amountOfSales, volumeOfSales)
    return amountOfSales, volumeOfSales

def scrapeTofuVolume2():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)
    url = "https://tofunft.com/collection/nft-11-legend-player/activities"
    driver.get(url)
    time.sleep(5)  # time to wait to start scraping the html
    page = driver.page_source  # raw html
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')  # parsing html to text
    lastSales = soup.findAll('span', {'class': 'chakra-text css-1dp94ug'})
    salePrices = soup.findAll('p', {'class': 'chakra-text css-1uhznsn'})
    legendTypes = soup.findAll('a', { 'class': 'chakra-link css-1jw7pf0'})
    amountOfSales = 0
    volumeOfSales = 0
    for i in range(len(lastSales)):
        if ('hour' in lastSales[i].text or 'minutes' in lastSales[i].text) and 'Legend' in legendTypes[i].text:
            amountOfSales += 1
            volumeOfSales += float(salePrices[i].text.replace(' ', '').replace('BNB', ''))
    print(amountOfSales, volumeOfSales)
    return amountOfSales, volumeOfSales

def scrapeStadiumSales():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)
    url = "https://tofunft.com/collection/nft11-stadium/activities"
    driver.get(url)
    time.sleep(5)  # time to wait to start scraping the html
    page = driver.page_source  # raw html
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')  # parsing html to text
    lastSales = soup.findAll('span', {'class': 'chakra-text css-1dp94ug'})
    amountOfSales = 0
    for i in range(len(lastSales)):
        if 'hour' in lastSales[i].text:
            amountOfSales += 1
        else:
            print(amountOfSales)
            return (amountOfSales)