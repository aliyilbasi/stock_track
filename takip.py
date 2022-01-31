import time
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from discord_webhook import DiscordWebhook, DiscordEmbed

#discor sunucu urlsi buraya gelecek

webhook_url="https://discord.com/api/webhooks/932604520733745162/9SZzY6BtlyMZ7GBZzdkKpoZh08Wgxfv9hBRB114iHTFVOX-xEA3K1rsOm55SQEvZpcEE"
webhook = DiscordWebhook(url=webhook_url, content="Bağlantı Başarılı")
response = webhook.execute()

opts = Options()
driver = webdriver.Chrome(options=opts)


hedef_url1 = "https://www.vatanbilgisayar.com/sony-playstation-5-digital-surum-oyun-konsolu.html"
hedef_url2 = "https://www.vatanbilgisayar.com/sony-playstation-5-oyun-konsolu.html"
hedef_url3 = "https://www.mediamarkt.com.tr/tr/product/_sony-playstation-5-oyun-konsolu-beyaz-1212362.html"
hedef_url4 = "https://www.mediamarkt.com.tr/tr/product/_sony-playstation-5-dijital-s%C3%BCr%C3%BCm-oyun-konsolu-1213866.html"
hedef_url5 = "https://www.overgameweb.com/playstation-5-konsol"
hedef_url6 = "https://www.overgameweb.com/playstation-5-konsol-dijital-surum"
hedef_url7 = "https://www.arcelik.com.tr/oyun-konsolu/sony-ps5-eas-hobi-oyun"
hedef_url8 = "https://www.arcelik.com.tr/oyun-konsolu/sony-playstation-5-dijital-surum-hobi-oyun"
hedef_url9 = "https://www.beko.com.tr/oyun-konsolu/sony-ps5-eas-hobi-oyun"
hedef_url10 = "https://www.beko.com.tr/oyun-konsolu/sony-playstation-5-dijital-surum-hobi-oyun"

hedef_1 = [hedef_url1, 0, 0]
hedef_2 = [hedef_url2, 0, 0]
hedef_3 = [hedef_url3, 0, 0]
hedef_4 = [hedef_url4, 0, 0]
hedef_5 = [hedef_url5, 0, 0]
hedef_6 = [hedef_url6, 0, 0]
hedef_7 = [hedef_url7, 0, 0]
hedef_8 = [hedef_url8, 0, 0]
hedef_9 = [hedef_url9, 0, 0]
hedef_10 = [hedef_url10, 0, 0]
loopcount = 0

def stokkontrol(hedef):
    global loopcount
    a = loopcount
    a += 1
    loopcount = a
    print(("Döngü = " + str(a)))
    driver.get(hedef[0])
    html = driver.page_source
    soup = bs4.BeautifulSoup(html,"html.parser")

    butonlar = soup.find_all("button", {"class": "btn-success"})
    product_name = soup.find("h1", {"class": "product-list__product-name"})

    for buton in butonlar:
        if "SEPETE EKLE" in buton.text:
            hedef[2] = 1
            if hedef[2] != hedef[1]:
                webhook = DiscordWebhook(url=webhook_url, content='STOKLARDA =' + hedef[0] )
                product_name1 = 'VATAN' + str(product_name.text) + 'STOKLARDA'
                embed = DiscordEmbed(title=product_name1, description=hedef[0])
                webhook.add_embed(embed)
                response = webhook.execute()

                print(" ! !  STOKLARDA ! ! " + product_name.text)
                hedef[1] = hedef[2]



def stokkontrolMedia(hedef):
    global loopcount
    a = loopcount
    a += 1
    loopcount = a
    print(("Döngü = " + str(a)))
    driver.get(hedef[0])
    html = driver.page_source
    soup = bs4.BeautifulSoup(html,"html.parser")

    butonlar = soup.find_all("div", {"class": "price-button"})
    product_name = soup.find("h1", {"itemprop": "name"})

    for buton in butonlar:
        if "Hemen Al" in buton.text:
            hedef[2] = 1
            if hedef[2] != hedef[1]:
                webhook = DiscordWebhook(url=webhook_url, content='STOKLARDA =' + hedef[0])
                product_name1 = 'MediaMarkt' + str(product_name.text) + 'STOKLARDA'
                embed = DiscordEmbed(title=product_name1, description=hedef[0])
                webhook.add_embed(embed)
                response = webhook.execute()

                print(" ! !  STOKLARDA ! ! " + product_name.text)
                hedef[1] = hedef[2]





    for buton in butonlar:
        if "Sepete Ekle" in buton.text:
            hedef[2] = 1
            if hedef[2] != hedef[1]:
                webhook = DiscordWebhook(url=webhook_url, content='STOKLARDA =' + hedef[0])
                product_name1 = 'MediaMarkt' + str(product_name.text) + 'STOKLARDA'
                embed = DiscordEmbed(title=product_name1, description=hedef[0])
                webhook.add_embed(embed)
                response = webhook.execute()

                print(" ! !  STOKLARDA ! ! " + product_name.text)
                hedef[1] = hedef[2]


def stokkontrolOver(hedef):
    global loopcount
    a = loopcount
    a += 1
    loopcount = a
    print(("Döngü = " + str(a)))
    driver.get(hedef[0])
    html = driver.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")

    butonlar = soup.find_all("div", {"class": "fl col-12 buyBtn"})
    product_name = soup.find("h1", {"class": "fl col-12 text-regular m-top m-bottom"})

    for buton in butonlar:
        if "Sepete Ekle" in buton.text:
            hedef[2] = 1
            if hedef[2] != hedef[1]:
                webhook = DiscordWebhook(url=webhook_url, content='STOKLARDA =' + hedef[0])
                product_name1 = 'OverGame' + str(product_name.text) + 'STOKLARDA'
                embed = DiscordEmbed(title=product_name1, description=hedef[0])
                webhook.add_embed(embed)
                response = webhook.execute()

                print(" ! !  STOKLARDA ! ! " + product_name.text)
                hedef[1] = hedef[2]

def stokkontrolArcelik(hedef):
    global loopcount
    a = loopcount
    a += 1
    loopcount = a
    print(("Döngü = " + str(a)))
    driver.get(hedef[0])
    html = driver.page_source
    soup = bs4.BeautifulSoup(html,"html.parser")

    butonlar = soup.find_all("div", {"class": "pdp-add-to-cart"})
    product_name = soup.find("h1", {"class": "title"})

    for buton in butonlar:
        if "Sepete At" in buton.text:
            hedef[2] = 1
            if hedef[2] != hedef[1]:
                webhook = DiscordWebhook(url=webhook_url, content='STOKLARDA =' + hedef[0])
                product_name1 = 'Beko/Arçelik' + str(product_name.text) + 'STOKLARDA'
                embed = DiscordEmbed(title=product_name1, description=hedef[0])
                webhook.add_embed(embed)
                response = webhook.execute()

                print(" ! !  STOKLARDA ! ! " + product_name.text)
                hedef[1] = hedef[2]

while True:
    stokkontrol(hedef_1)
    time.sleep(5)
    stokkontrol(hedef_2)
    time.sleep(5)
    stokkontrolMedia(hedef_3)
    time.sleep(5)
    stokkontrolMedia(hedef_4)
    time.sleep(5)
    stokkontrolOver(hedef_5)
    time.sleep(5)
    stokkontrolOver(hedef_6)
    time.sleep(5)
    stokkontrolArcelik(hedef_7)
    time.sleep(5)
    stokkontrolArcelik(hedef_8)
    time.sleep(5)
    stokkontrolArcelik(hedef_9)
    time.sleep(5)
    stokkontrolArcelik(hedef_10)
    time.sleep(5) 