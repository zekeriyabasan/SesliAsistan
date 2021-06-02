
import urllib.request
import json
from gtts import  gTTS
from playsound import playsound
import os
import sys
from random import choice
import requests
from lxml import html

class Komut():
    def __init__(self,gelenSes):
        self.ses = gelenSes.upper()
        self.sesBloklari = self.ses.split()
        print(self.sesBloklari)

        self.komutlar = ["ABONE","CEVİR","NABER","NASILSIN","KAPAT","HAVA"]


        # KOMUT VE İŞLEMLERİ

        def seslendirme(self,yazi):
            tts = gTTS(text = yazi,lang = 'tr')
            tts.save("ses.mp3")
            playsound("ses.mp3")
            os.remove("ses.mp3")
            print(yazi)

        def kapat(self):
            self.seslendirme("Kapatıyorum Kendimi Zekeriya Bey kendinize iyi bakın görüşürüz.")
            sys.exit()

        def havadurumu(self):
            r = requests.get("https://mobil.ntvhava.com/konum/adana")
            tree = html.fromstring(r.content)

            derece = tree.xpath('//*[@id="main"]/section[3]/div/ul[3]/li[1]/div[2]/div[1]/p[1]/span')
            durum = tree.xpath('//*[@id="main"]/section[3]/div/ul[3]/li[1]/div[2]/div[1]/p[1]/span')
            uyari = ""

            if durum[0].text == "Yağmurlu":
                uyari = "Şemsiyeni Almayi Unutma"

            yazi = "Zekeriya, Bugün Hava {} derece ve {} gözüküyor. {}".format(derece[0].text,durum[0].text,uyari)
            self.seslendirme(yazi)
        def sohbet(self):
            sozler = ["Kötüyüm desem üzülecekmisin?",
                      "İyilik valla sen nasılsın?",
                      "Saçmalamaaa?",
                      "Benim duygularım yok ama insanlar sanırım bu soruya iyiyim diyor",
                      "Bir milyon parametreli heaplarıma göre hayatın anlamı 5 ve iyi değilim"]
            secim = choice(sozler)

            self.seslendirme(secim)

            # Komut ve İşlemler Kapanış
            def komutBul(self):
                for komut in self.komutlar:
                    if komut in self.sesBloklari:
                        self.komutCalistir(komut)

            def komutCalistir(self,komut):
                if komut == "KAPAT":
                    self.kapat()
                if komut == "NABER" or komut == "NASILSIN":
                    self.sohbet()
                if komut == "HAVA":
                    self.havadurumu()

