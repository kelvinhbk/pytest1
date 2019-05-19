import requests
import re


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def main():
    goods = '万科城'

    #url = 'https://shenzhen.anjuke.com/sale/?kw=' + goods
    url = 'https://shenzhen.anjuke.com/prop/view/A1669281977?from=comm_auto-saleMetro&spread=commsearch_p&ab=expclick-AJKERSHOUFANG_101_10100009sortpersonalizednewrank&position=60&kwtype=comm_auto&now_time=1557385373'

    html = getHTMLText(url)
    print(html)

main()