from flask import Flask, render_template, request
from collections import defaultdict
import urllib
import re

def ViewScrapedData():
    PriceList = []

    symbolslist = ["hp-core-i5-4gb-15-6-laptop-1677399","asus-tf300tg-quad-core-1gb-10-transformer-pad-255667","lenovo-4080-intel-core-i5-laptop-1677396","lenovo-thinkpad-l460-core-i5-8gb-14-laptop-1702368","lenovo-ip-100-intel-celeron-2gb-15-6-laptop-1702386"]
    i = 0
    while i < len(symbolslist):
            url = "http://www.kaymu.com.np/" + symbolslist[i] + ".html"

            htmlfile = urllib.urlopen(url)
            htmltext = htmlfile.read()

            regex = '<div class="no-discount price fsize-24 bold">(.+?)</div>'

            pattern = re.compile(regex)

            price1 = re.findall(pattern, htmltext)


            print "LAPTOPS IN KAYMU"

            print "The price of", symbolslist[i], " is : ", price1

            PriceList.append(price1)
            i += 1

            print "Updated List : ", PriceList



    symbolslist2 = ["hp-15-notebook-free-16-gb-pendrive-and-usb-mouse", "tf300tg","lenovo-b4080-core-i5-new-model","lenovo-think-pad-l460-i5","lenovo-idea-pad-100-core-i3-new-model"]
    i = 0

    while i < len(symbolslist2):
            url = "https://www.sastodeal.com/product/" + symbolslist2[i]
            htmlfile = urllib.urlopen(url)
            htmltext = htmlfile.read()

            regex = '<span id="main-price" class="product_price"><span class="rupee">(.+?)</span> (.+?)</span>'
            pattern = re.compile(regex)

            #mainPrice = re.findall(pattern, htmltext)
            #splitPrice = mainPrice[0][1].split(' ')

            #price2 = splitPrice[0][1]

            price2 = re.findall(pattern, htmltext)

            print"LAPTOPS IN SASTODEAL"
            print "The price of", symbolslist2[i], " is : Rs.",price2[0][1]

            PriceList.append(price2[0][1])
            print "Updated List : ", PriceList

            i += 1
    return PriceList

output = ViewScrapedData()