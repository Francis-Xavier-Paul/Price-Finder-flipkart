import bs4
import requests
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

def getFlipkartPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(2) > div > div.dyC4hf > div.CEmiEU > div > div._30jeq3._16Jk6d')
    return elems[0].text.strip()


price = getFlipkartPrice('https://www.flipkart.com/asus-eyecare-23-8-inch-full-hd-led-backlit-va-panel-tuv-certified-eye-care-flicker-free-low-blue-light-monitor-va249he/p/itma1cad1a8d32eb?pid=MONGGYW5MHPXHENC&lid=LSTMONGGYW5MHPXHENCWXYTZK&marketplace=FLIPKART&store=6bo%2Fg0i%2F9no&srno=b_1_2&otracker=hp_omu_Best%2Bof%2BElectronics_4_3.dealCard.OMU_RCXTXAMJM65Y_3&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all%2Chp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_4_NA_view-all_3&fm=neo%2Fmerchandising&iid=9637ba4b-f0b8-4c15-b1ee-c5de7ae2b9f0.MONGGYW5MHPXHENC.SEARCH&ppt=hp&ppn=homepage&ssid=dc5i0hbr340000001672749533054')    
print('The price is ' + price)