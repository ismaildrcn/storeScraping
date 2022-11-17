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
    commentCounter = 1

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
        commentCounter += 1

    df = pd.DataFrame(
        {
            "dates": commentDateList,
            "comments": commentList
        }
    )
    time.sleep(5)
    browser.close()
    return df


