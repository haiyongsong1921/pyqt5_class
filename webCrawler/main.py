#coding=utf-8
import certifi
import requests
import re
import lxml
from bs4 import BeautifulSoup
import sqlite3
import urllib.request
import urllib.error


class BookAdditionInfo:
    def __init__(self):
        self.isbn = ""
        self.price = ""
        self.language = ""
        self.pages = ""
        self.overview = ""

class BookInfo:
    def __init__(self, name, author, publisher, publish_date, search_index):
        self.name = name
        self.writer = author
        self.publisher = publisher
        self.publish_date = publish_date
        self.search_index = search_index
        self.addtionalInfo = BookAdditionInfo()


    def __str__(self):
        return self. name + "," + self.writer+"," + self.publisher+"," + self.publish_date+"," + self.search_index


if __name__ == '__main__':
    header = {
        # "cookie": "ugid=e0fbc426bdbaa3a1535b8b1cddd6b6005487957; _ga=GA1.2.75981771.1646387128; uuid=dafdbc50-9b9f-11ec-984b-2fae2bc4cdf5; xpos=%7B%7D; azk=dafdbc50-9b9f-11ec-984b-2fae2bc4cdf5; azk-ss=true; _sp_ses.0295=*; _gid=GA1.2.173632063.1646640856; lux_uid=164664086123274722; downloaded_photo_id=AdnD0rO1feg; _sp_id.0295=fd60fa78-c8df-4325-aceb-88f98cf5198c.1646387128.3.1646643719.1646636424.7fe5ee1c-b945-41ec-b1bb-ed8c12ecf5da; _gat=1",
        # 'Host': "opac.zhlib.com.cn",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
    url = "http://opac.zhlib.com.cn/opac/search?q=*%3A*&searchType=standard&isFacet=true&view=standard&searchWay=title&rows=10&sortWay=score&sortOrder=desc&hasholding=1&searchWay0=marc&logical0=AND&f_class1=c#bookSimpleDetailDiv_1000357690"
    #url =  "http://opac.zhlib.com.cn/opac/search?q=*%3A*&searchType=standard&isFacet=true&view=standard&searchWay=title&rows=10&sortWay=score&sortOrder=desc&hasholding=1&f_class1=c&searchWay0=marc&logical0=AND&page=654"
    url = "http://120.237.162.62:8088/opac/search?q=*%3A*&searchType=standard&isFacet=true&v=standard&searchWay=title&rows=10&sortWay=score&sortOrder=desc&hasholding=1&f_class1=c&searchWay0=marc&logical0=AND"
    url = "http://120.237.162.62:8088/opac/search?q=*%3A*&searchType=standard&isFacet=true&view=standard&searchWay=title&rows=10&sortWay=score&sortOrder=desc&hasholding=1&f_class1=c&searchWay0=marc&logical0=AND&page=2"
    url = "http://120.237.162.62:8088/opac/search?q=*%3A*&searchType=standard&isFacet=true&view=standard&searchWay=title&rows=10&sortWay=score&sortOrder=desc&hasholding=1&f_class1=c&searchWay0=marc&logical0=AND&page="

    for page in range(1, 80):
        url = "http://120.237.162.62:8088/opac/search?q=*%3A*&searchType=standard&isFacet=true&view=standard&searchWay=title&rows=10&sortWay=score&sortOrder=desc&hasholding=1&f_class1=c&searchWay0=marc&logical0=AND&page="
        url += str(page)

        #db = sqlite3.connect("library.db")
        r = requests.get(url=url, headers=header)
        #  print(r.encoding)
      #  print(r.apparent_encoding)
        r.encoding = r.apparent_encoding
        html = r.text
        div_bf = BeautifulSoup(html, features='html.parser')
        #print(div_bf.prettify())
        td_bf = div_bf.find_all('td', class_='bookmetaTD')

        frame_bf = div_bf.find_all('iframe')
        #print(frame_bf)
        #for frame in frame_bf:
            #reponse = requests.get(url=frame.attrs['src'])
            #iframe_soup = BeautifulSoup(reponse)
            #print(iframe_soup)



        # 1. get book name
        a_bf = BeautifulSoup(str(td_bf), features='html.parser')
        bookName = a_bf.find_all('a', class_='title-link')

        bookNameList = []
        bookInfoList = []
        for name in bookName:
            text = str(name.string)
            text = text.replace('\t', '')
            text = text.replace('\r', '')
            text = text.replace('\n', '')
            bookNameList.append(text)


        #2. get author list
        authorList = []
        a_bf = BeautifulSoup(str(td_bf), features='html.parser')
        div_bf = BeautifulSoup(str(a_bf), features='html.parser')
        authors = div_bf.find_all('a', class_='author-link')
        for author in authors:
            text = str(author.string)
            text = text.replace('\t', '')
            text = text.replace('\r', '')
            text = text.replace('\n', '')
            #print(text)
            authorList.append(text)

        #3. get publisher list
        publisherList = []
        a_bf = BeautifulSoup(str(td_bf), features='html.parser')
        div_bf = BeautifulSoup(str(a_bf), features='html.parser')
        publishers = div_bf.find_all('a', class_='publisher-link')
        for publisher in publishers:
            text = str(publisher.string)
            text = text.replace('\t', '')
            text = text.replace('\r', '')
            text = text.replace('\n', '')
            #print(text)
            publisherList.append(text)
        #4. get search index list
        searchIndexList = []
        a_bf = BeautifulSoup(str(td_bf), features='html.parser')
        div_bf = BeautifulSoup(str(a_bf), features='html.parser')
        searchIndexs = div_bf.find_all('span', class_='callnosSpan')
        for index in searchIndexs:
            text = str(index.string)
            text = text.replace('\t', '')
            text = text.replace('\r', '')
            text = text.replace('\n', '')
            #print(text)
            searchIndexList.append(text)

        # 5. get publish date list
        publishDateList = []
        a_bf = BeautifulSoup(str(td_bf), features='html.parser')
        div_bf = BeautifulSoup(str(a_bf), features='html.parser')
        publishDate = div_bf.find_all('div', class_='bookmeta')
        #print(publishDate)

        div_bf = BeautifulSoup(str(publishDate), features='html.parser')
        div_list = div_bf.find_all(text='出版日期')

        for child in div_bf:
            div_bf1 = BeautifulSoup(str(child), features='html.parser')
            div_date = div_bf1.find_all(text=re.compile('出版日期'))

            text = str(div_date)
            if(text.find('出版日期')) == -1:
                continue
            text = text.replace('\\t', '')
            text = text.replace('\\r', '')
            text = text.replace('\\n', '')
            text = text.replace('\\xa0', '')
            text = text.replace('[', '')
            text = text.replace(']', '')
            text = text.replace('\'', '')
            texts = text.split(' ')
            text = texts[1]

            publishDateList.append(text)
            #print(div_list)


        # 附加信息
        all_bf = BeautifulSoup(html, features='html.parser')
        # print(div_bf.prettify())
        info_overview = all_bf.find_all(href=re.compile("bookSimpleDetailDiv"))
        h_bf = BeautifulSoup(str(info_overview), features='html.parser')
        refs = h_bf.find_all('a')
        bookIdList = []
        for ref in refs:
            text = str(ref.get('href'))
            text = text.replace('#bookSimpleDetailDiv_', '')
            bookIdList.append(text)
            # print(text)
        info_url = "http://120.237.162.62:8088/opac/book/{0}?view=simple"
        # 1. isbn
        isbn_list = []
        # 2. price
        price_list = []
        # 3. language
        language_list = []
        # 4. pages
        page_list = []
        # 5. overview
        overview_list = []
        for book_id in bookIdList:
            detail_url = info_url.format(book_id)
            r = requests.get(url=detail_url, headers=header)
            r.encoding = r.apparent_encoding
            html = r.text
            detail_bf = BeautifulSoup(html, features='html.parser')
            # print(detail_bf.prettify())
            bookAdditionalInfo = BookAdditionInfo()

            td_tags = detail_bf.find_all("td", class_="rightTD")

            td_bf = BeautifulSoup(str(td_tags), features='html.parser')

            info_list = []
            for td in td_bf:
                text = str(td.string).strip().replace('\t', '')
                text = text.replace('\r', '')
                text = text.replace('\n', '')
                text = text.replace('[', '')
                text = text.replace(']', '')
                text = text.replace(',', '')
                if text == "None" or text == '' or text == ',':
                    continue
                # print(text)
                # if text:
                info_list.append(text)

            if info_list[0].find("价") != -1:
                t_list = info_list[0].split("价")
                isbn_list.append(t_list[0])
                tmp_list = t_list[1].split('NY')
                if len(tmp_list) < 2:
                    price_list.append("59.00")
                else:
                    price_list.append(tmp_list[1])
            language_list.append(info_list[1])
            if info_list[2].find("页") != -1:
                p_list = info_list[2].split("页")
                page_list.append(p_list[0])
            overview_list.append(info_list[3])


        bookInfo_list = []
        for name, author, publisher, publish_date, search_index, isbn, price, language, pages, overview \
                in zip(bookNameList, authorList, publisherList, publishDateList, searchIndexList, isbn_list, price_list, language_list, page_list, overview_list):
            book = BookInfo(name, author, publisher, publish_date, search_index)
            book.addtionalInfo.isbn = isbn
            book.addtionalInfo.price = price
            book.addtionalInfo.language = language
            book.addtionalInfo.pages = pages
            book.addtionalInfo.overview = overview
            bookInfo_list.append(book)

        '''
        # 6. get place info list
        placeInfoList = []
        all_bf = BeautifulSoup(html, features='html.parser')
        print(div_bf.prettify())
        td_bf = div_bf.find_all(text=re.compile("图书信息概览"))
        print(str(td_bf))
        '''
        #div_bf = BeautifulSoup(str(publishDate), features='html.parser')
        #div_list = div_bf.find_all(text='出版日期')

        '''
        driver = webdriver.Chrome("D:/Tools/chromedriver.exe")
        driver.get(url)
        print(driver.page_source)
        #iframes = driver.find_element(by='tag name', value='iframe')
        iframe = driver.find_elements_by_tag_name("iframe")[0]
        driver.switch_to.frame(iframe)
        print(driver.page_source)
        soup = BeautifulSoup(driver.page_source, features='html.parser')
        '''


        # insert data into db file

        conn = sqlite3.connect("School_library.db")
        cur = conn.cursor()
        createTableStr = "CREATE TABLE IF NOT EXISTS book_info (id INTEGER NOT NULL UNIQUE,name TEXT,writer TEXT,publisher TEXT, publish_date TEXT,search_index INTEGER, " \
                         "isbn TEXT,price TEXT,language TEXT,pages INTEGER,overview TEXT, PRIMARY KEY(id AUTOINCREMENT))"
        cur.execute(createTableStr)

        for book in bookInfo_list:
            sql = 'insert into book_info VALUES(NULL,"{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}")'.format(book.name, book.writer, book.publisher, book.publish_date, book.search_index,
                                                                                                                          book.addtionalInfo.isbn, book.addtionalInfo.price, book.addtionalInfo.language, book.addtionalInfo.pages, book.addtionalInfo.overview)
            #sql = "insert into book_info VALUES(NULL,'%s','%s','%s','%s','%s')" % (book.name, book.writer, book.publisher, book.publish_date, book.search_index)
            try:
                resu = cur.execute(sql)
                #print(resu)
            except:
                print("insert fail")

        conn.commit()
        cur.close()
        conn.close()
