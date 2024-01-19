import requests
from bs4 import BeautifulSoup

#     print(i.text.encode('iso-8859-1').decode('gbk'))

def getHtml(url):
    headers = {
    'Cookie': 'articlevisited=1',
    # 'Referer':  'https://m.xbiqugeo.com/shu/365/20/',
    'Sec-Ch-Ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    }
    #获取网页数据
    html = requests.get(url,headers=headers, verify=False)
    htmlCode = html.text
    #解析网页
    soup = BeautifulSoup(htmlCode,'html.parser')
    #返回解析后的页面内容
    return soup

def getTitle(url):
    soup = getHtml(url)
    title = soup.find('div',class_="book_box").find('dt').string
    return title

#获取各章节目录链接
def getList(url):
    soup = getHtml(url)
    #查找所有章节的链接
    listBox = soup.find('div', class_="book_last").find_all('a')
    #新建列表用来储存list的url
    bookLists = []
    for i in listBox:
        print('href',i['href'])
        print('text',i.text)
        listUrl = i['href']
        listTitle = i.text
        #放进列表里
        bookLists.append({'listUrl':listUrl,'listTitle':listTitle})
    return bookLists

def getNovelContent(url):
    soup = getHtml(url)

    try:
        content = soup.find('div', id="chaptercontent").text
        # content = soup.find('div', id="chaptercontent").prettify(formatter=lambda s: s.replace("<p>", "").replace("</p>", "<br>"))
    except AttributeError:
        content = ""  #
    print(content)
    return content

def saveNovel(url):
    page = 20
    newUrl = url + '/shu/365/' + str(page) + '/'
    # 新建列表用来储存list的url
    bookLists = getList(newUrl)
    title = getTitle(newUrl)

    print(title)
    with open('%s.txt'%title, 'a' ,encoding='utf-8') as f:
        for item in bookLists:
            #拼接完整的章节链接地址
            print(item['listUrl'])
            print(item['listTitle'])
            listUrl  = item['listUrl']
            listTitle =item['listTitle']
            chapterUrl = url + listUrl
            print('chapterUrl',chapterUrl)
            chapterContent = getNovelContent(chapterUrl)
            f.write(chapterContent)
            print('***{}下载完成***'.format(listTitle))

        f.close()

if __name__ == '__main__':
    url = 'https://m.xbiqugeo.com'
    saveNovel(url)