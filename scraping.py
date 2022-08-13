# import urllib library
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def main():
    return scrapeTelegram('https://t.me/nft11official'), scrapeTelegram('https://t.me/nft11_en_official'), scrapeTelegram('https://t.me/NFT11_PT_BR'), scrapeTelegram('https://t.me/nft11_es_official'), scrapeTelegram('https://t.me/nft11_vn'), scrapeDiscord(), cg.get_coin_info_from_contract_address_by_id('binance-smart-chain', '0x73F67AE7f934FF15beaBf55A28C2Da1eEb9B56Ec')['community_data']['twitter_followers'], scrapeInstagram(), scrapeFacebook(), cg.get_price(ids='nft11', vs_currencies='usd')['nft11']['usd'], scrapeBscScan(
        'https://bscscan.com/token/0x73f67ae7f934ff15beabf55a28c2da1eeb9b56ec'), cg.get_price(ids='nft11', vs_currencies='usd', include_24hr_vol=True)['nft11']['usd_24h_vol'], cg.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd'], scrapeCryptocom(), scrapeTofuLegend(), scrapeBscScan(
        'https://bscscan.com/token/0xc2dea142de50b58f2dc82f2cafda9e08c3323d53'), scrapeTofuVolume(), scrapeTofu(
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
    return tgGroupMembers


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

    return discordGroupMembers


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
    return instagramFollowers


def scrapeFacebook():
    # store the URL in url as
    # parameter for urlopen
    url = "https://www.facebook.com/nft11"
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    time.sleep(5)  # time to wait to start scraping the html
    page = driver.page_source  # raw html
    driver.quit()
    soup = BeautifulSoup(page, 'html.parser')  # parsing html to text
    rawFacebookData = soup.findAll('span', {
                                   'class': 'd2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh jq4qci2q a3bd9o3v b1v8xokw oo9gr5id'})
    facebookData = rawFacebookData[0].text.replace(',', '')
    facebookData2 = rawFacebookData[2].text.replace(',', '')
    facebookLikes = re.findall('[0-9]+', facebookData)
    facebookFollowers = re.findall('[0-9]+', facebookData2)

    print(facebookLikes[0], facebookFollowers[0])

    return (facebookLikes[0], facebookFollowers[0])


def scrapeBscScan(url):
    # store the response of URL
    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    response = urlopen(r).read()
    soup = BeautifulSoup(response, 'html.parser')
    holders = re.findall(
        '[0-9]+', (soup.find('div', {'class': 'mr-3'}).text.replace(',', '')))[0]
    print(holders)
    return holders


def scrapeCryptocom():
    url = "https://crypto.com/price/categories/gamefi"

    # store the response of URL
    r = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    response = urlopen(r).read()
    soup = BeautifulSoup(response, 'html.parser')
    gameFiMC = soup.find('div', {
                         'class': 'css-qznh9z'}).text.replace('$', '').replace('B', '').replace(' ', '')

    print(gameFiMC)
    return gameFiMC


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
    return lowestPrice


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
    for i in range(len(lowestPrices)):
        if 'Legend' in lowestPrices[i].text:
            lowestPrice = soup.findAll('p', {'class': 'chakra-text css-0'})[i].text.replace(' ', '').replace('BNB', '')
            print(lowestPrice)
            return lowestPrice

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
    amountOfSales = 0
    volumeOfSales = 0
    for i in range(len(lastSales)):
        if 'hours' in lastSales[i].text:
            amountOfSales += 1
            volumeOfSales += float(salePrices[i].text.replace(' ', '').replace('BNB', ''))
        else:
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
        if 'hours' in lastSales[i].text:
            amountOfSales += 1
        else:
            print(amountOfSales)
            return amountOfSales
