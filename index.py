from flask import Flask, redirect, url_for, request,render_template , make_response
import urllib
import re
import getDetail


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route('/success/<name>')
def success(name):
    data = ViewScrapedData()
    price = data[0]
    desc = data[1]

    print "Price------>>>", price
    print "Desc------>>>", desc
    kaymu_price = []
    sastodeal_price = []
    kaymu_price.append(price[0][0] + '/-')
    kaymu_price.append(price[1][0] + '/-')
    kaymu_price.append(price[2][0] + '/-')
    kaymu_price.append(price[3][0] + '/-')
    kaymu_price.append(price[4][0] + '/-')
    sastodeal_price.append(str('Rs ') + str(price[5]))
    sastodeal_price.append(str('Rs ') + str(price[6]))
    sastodeal_price.append(str('Rs ') + str(price[7]))
    sastodeal_price.append(str('Rs ') + str(price[8]))
    sastodeal_price.append(str('Rs ') + str(price[9]))

    symbolslist = ["hp-core-i5-4gb-15-6-laptop-1677399", "asus-tf300tg-quad-core-1gb-10-transformer-pad-255667",
                   "lenovo-4080-intel-core-i5-laptop-1677396", "lenovo-thinkpad-l460-core-i5-8gb-14-laptop-1702368",
                   "lenovo-ip-100-intel-celeron-2gb-15-6-laptop-1702386"]
    symbolslist2 = ["hp-15-notebook-free-16-gb-pendrive-and-usb-mouse", "tf300tg", "lenovo-b4080-core-i5-new-model",
                    "lenovo-think-pad-l460-i5", "lenovo-idea-pad-100-core-i3-new-model"]

    dict1 = {
        symbolslist[0]: {'kaymu': kaymu_price[0]},
        symbolslist2[0]: {'sastodeal': sastodeal_price[0]},
    }
    dict2 = {
        symbolslist[1]: {'kaymu': kaymu_price[1]},
        symbolslist2[1]: {'sastodeal': sastodeal_price[1]},
    }
    dict3 = {
        symbolslist[2]: {'kaymu': kaymu_price[2]},
        symbolslist2[2]: {'sastodeal': sastodeal_price[2]},
    }
    dict4 = {
        symbolslist[3]: {'kaymu': kaymu_price[3]},
        symbolslist2[3]: {'sastodeal': sastodeal_price[3]}
    }
    dict5 = {
        symbolslist[4]: {'kaymu': kaymu_price[4]},
        symbolslist2[4]: {'sastodeal': sastodeal_price[4]},
    }

    if(name=='hp-15-notebook'):
        return render_template('modelcompare.html',result=dict1, result_output=desc[0])
    if(name=='asus-tf300tg'):
        return render_template('modelcompare.html', result=dict2, result_output=desc[1])
    if (name == 'lenovo-b4080'):
        return render_template('modelcompare.html', result=dict3, result_output=desc[2])
    if (name == 'lenovo-think-pad-l460'):
        return render_template('modelcompare.html', result=dict4, result_output=desc[3])
    if (name == 'lenovo-idea-pad-100'):
        return render_template('modelcompare.html', result=dict5, result_output=desc[4])

    # return render_template('priceindex.html', kaymu=kaymu_price, sastodeal=sastodeal_price, result=dict)


@app.route('/pdetail')
def pdetail():
    dataToDisplay = getDetails()

    decodedData = dataToDisplay.decode("utf-8")
    print "Data to display------>>>>>", decodedData
    return render_template('modelcompare.html', result_output=decodedData)

# @app.route('/getdata')
# def getdata():
#     data = ViewScrapedData()
#     kaymu_price=[]
#     sastodeal_price=[]
#     kaymu_price.append(data[0][0]+'/-')
#     kaymu_price.append(data[1][0]+'/-')
#     sastodeal_price.append(str('Rs ') + str(data[2]))
#     sastodeal_price.append(str('Rs ') + str(data[3]))
#
#     symbolslist = ["hp-core-i5-4gb-15-6-laptop-1677399", "asus-tf300tg-quad-core-1gb-10-transformer-pad-255667",
#                    "lenovo-4080-intel-core-i5-laptop-1677396", "lenovo-thinkpad-l460-core-i5-8gb-14-laptop-1702368",
#                    "lenovo-ip-100-intel-celeron-2gb-15-6-laptop-1702386"]
#
#
#     symbolslist2 = ["hp-15-notebook-free-16-gb-pendrive-and-usb-mouse", "tf300tg", "lenovo-b4080-core-i5-new-model",
#                 "lenovo-think-pad-l460-i5", "lenovo-idea-pad-100-core-i3-new-model"]
#
#     dict={
#         symbolslist[0]: {'kaymu': kaymu_price[0]},
#         symbolslist[1]: {'kaymu': kaymu_price[1]},
#         symbolslist2[0]: {'sastodeal':sastodeal_price[0]},
#         symbolslist2[1]: {'sastodeal':sastodeal_price[1]}
#     }
#     return render_template('priceindex.html', kaymu=kaymu_price,sastodeal=sastodeal_price,result=dict)

@app.route('/getmodel')
def getmodel():
    model_list = ["hp-15-notebook","asus-tf300tg","lenovo-b4080","lenovo-think-pad-l460","lenovo-idea-pad-100"]
    return render_template('modelfile.html',list=model_list)

def ViewScrapedData():
    PriceList = []
    description = []

    symbolslist = ["hp-core-i5-4gb-15-6-laptop-1677399","asus-tf300tg-quad-core-1gb-10-transformer-pad-255667","lenovo-4080-intel-core-i5-laptop-1677396","lenovo-thinkpad-l460-core-i5-8gb-14-laptop-1702368","lenovo-ip-100-intel-celeron-2gb-15-6-laptop-1702386"]
    i = 0
    while i < len(symbolslist):
            url = "http://www.kaymu.com.np/" + symbolslist[i] + ".html"

            dataToDisplay = getDetails(url)

            decodedData = dataToDisplay.decode("utf-8")

            htmlfile = urllib.urlopen(url)
            htmltext = htmlfile.read()

            regex = '<div class="no-discount price fsize-24 bold">(.+?)</div>'

            pattern = re.compile(regex)

            price1 = re.findall(pattern, htmltext)


            print "LAPTOPS IN KAYMU"

            print "The price of", symbolslist[i], " is : ", price1

            PriceList.append(price1)
            description.append(decodedData)
            i += 1

            print "Updated List : ", PriceList



    symbolslist2 = ["hp-15-notebook-free-16-gb-pendrive-and-usb-mouse", "tf300tg","lenovo-b4080-core-i5-new-model","lenovo-think-pad-l460-i5","lenovo-idea-pad-100-core-i3-new-model"]
    i = 0

    while i < len(symbolslist2):
            url = "https://www.sastodeal.com/product/" + symbolslist2[i]

            dataToDisplay = getDetails(url)

            print "data to display------->>>>", dataToDisplay

            #decodedData = dataToDisplay.decode("utf-8")

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
            description.append(dataToDisplay)

            i += 1

            print "Updated List : ", PriceList


    return [PriceList, description]

def getDetails(url):

    print "URL----->>> ", url
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()

    # readregex = re.compile('(<div class="product-description">.*?</div>)')
    #
    # result = regex.search(htmltext)
    #
    # print "Result ---->>>", result
    #
    # matchedText = result.groups()[0]
    #
    # return matchedText

    if url.find("kaymu") != -1:
        regex = re.compile('(<div class="product-description">.*?</div>)')

        result = regex.search(htmltext)

        matchedText = result.groups()[0]

        print "hhahaaaaa",matchedText

        return matchedText


    else:
        if url.find("sastodeal") != -1:
            regex = re.compile('(<div class="descriptions">.*?</div>)')

            result = regex.search(htmltext)

            matchedText = result.groups()[0]

            print "hhahaaaaa", matchedText

            return matchedText

if __name__== '__main__':
    app.run(debug=True)