from selenium import webdriver
import pandas as pd
import time

def trendyolScraping(url):
    browser = webdriver.Chrome()
    browser.maximize_window()
    fullUrl = url.split("?")[0] + "/yorumlar"
    browser.get(fullUrl)
    time.sleep(3)

    commentList = []
    commentDateList = []

    # <------ pull the scroll bar to the last position ------>
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
    match = False
    while match == False:
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
        if lastCount == lenOfPage:
            match = True
    time.sleep(3)
    # <------ pull the scroll bar to the last position ------>

    comments = browser.find_elements_by_css_selector(".rnr-com-tx")
    commentDates = browser.find_elements_by_css_selector(".rnr-com-usr")

    for comment in range(len(comments)):
        commentList.append(comments[comment].text)
        commentDateList.append(commentDates[comment].text.split("|")[1])

    df = pd.DataFrame(
        {
            "dates": commentDateList,
            "comments": commentList
        }
    )
    time.sleep(1)
    browser.close()
    return df

def hepsiburadaScraping(url):

    pageCounter = 1
    lastPageList = []
    commentList = []
    commentDateList = []
    #url = "https://www.hepsiburada.com/moodcase-apple-iphone-11-penguen-ve-ayicik-desenli-seffaf-telefon-kilifi-p-hbv00000upk7s"
    browser = webdriver.Chrome()
    browser.maximize_window()
    fullUrl = url + "-yorumlari"
    browser.get(fullUrl)

    lastPage = browser.find_elements_by_css_selector(".hermes-PaginationBar-module-orpYpftpqLf3tX8zZwyv.hermes-PaginationBar-module-PfsExxb6vqeAGDM5WNe7")
    lastPageList.append((lastPage[0].text).split("\n"))
    lastPageList = lastPageList[0][-1]
    print(lastPageList)

    while pageCounter <= int(lastPageList):
        commentUrl = fullUrl + "?sayfa=" + str(pageCounter)
        browser.get(commentUrl)
        time.sleep(3)

        comments = browser.find_elements_by_css_selector(".hermes-ReviewCard-module-KaU17BbDowCWcTZ9zzxw")
        dates = browser.find_elements_by_css_selector(".hermes-ReviewCard-module-WROMVGVqxBDYV9UkBWTS")

        for comment in range(len(comments)):
            if browser.current_url == fullUrl:
                pageCounter = int(lastPageList) + 1
                break
            else:
                commentList.append(comments[comment].text.split("\n")[0])
                commentDateList.append(dates[comment].text.split(",")[0])
                print(str(pageCounter) + "\n-----------------------------------------------")
                print(dates[comment].text.split(",")[0])
                print(comments[comment].text.split("\n")[0])

        pageCounter += 1

    df = pd.DataFrame(
        {
            "dates": commentDateList,
            "comments": commentList
        }
    )
    time.sleep(1)
    browser.close()
    return df

