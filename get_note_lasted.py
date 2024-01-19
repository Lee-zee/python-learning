import requests
from bs4 import BeautifulSoup

#     print(i.text.encode('iso-8859-1').decode('gbk'))

def getHtml(url):
    headers = {
    'Cookie': 'fontFamily=null; fontColor=null; fontSize=null; bg=null; bookid=4729; booklist=%257B%2522BookId%2522%253A4729%252C%2522ChapterId%2522%253A10928968%252C%2522ChapterName%2522%253A%2522%2520%25u7B2C1%25u7AE0%2520%25u767E%25u5206%25u4E4B%25u767E%25u771F%25u5B9E%25u7684%25u6E38%25u620F%25u662F%25u6709%25u591A%25u771F%25u5B9E%25uFF1F%2522%252C%2522BookName%2522%253A%2522%25u8FD9%25u6E38%25u620F%25u4E5F%25u592A%25u771F%25u5B9E%25u4E86%2522%252C%2522Author%2522%253A%2522%25u6668%25u661FLL%2522%257D',
    'Referer':  'https://cn.bing.com/',
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
    title = soup.find('div',class_="top").find('h1').string
    return title.encode('iso-8859-1').decode('gbk')

#获取各章节目录链接
def getList(url):
    soup = getHtml(url)
    #查找所有章节的链接
    listBox = soup.find_all('ul', class_="section-list")[1].find_all('a')
    #新建列表用来储存list的url
    bookLists = []
    for i in listBox:
        listUrl = i['href']
        #放进列表里
        bookLists.append(listUrl)
    return bookLists

def getNovelContent(url):
    soup = getHtml(url)

    try:
        content = soup.find('div', class_="content").text
    except AttributeError:
        content = ""  #
    content = content.encode('iso-8859-1').decode('gbk').strip().replace("牋牋","").replace("(本章完)www.2biqu.com 笔趣阁","")
    print(content)
    return content

def saveNovel(url):
    # 新建列表用来储存list的url
    bookLists = getList(url)
    title = getTitle(url)

    print(title)
    num = 1
    with open('%s.txt'%title, 'a' ,encoding='utf-8') as f:
        for listUrl in bookLists:
            num += 1
            if num >= 930:
                 #拼接完整的章节链接地址
                chapterUrl = url + listUrl
                chapterContent = getNovelContent(chapterUrl)
                f.write(chapterContent)
                print('***第{}章下载完成***'.format(num))

        f.close()

if __name__ == '__main__':
    url = 'https://www.2biqu.com/biqu4729/'
    saveNovel(url)