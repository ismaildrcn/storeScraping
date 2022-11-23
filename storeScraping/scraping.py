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
            #"dates": commentDateList,
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
        commentDates = browser.find_elements_by_css_selector(".hermes-ReviewCard-module-WROMVGVqxBDYV9UkBWTS")

        for comment in range(len(comments)):
            if browser.current_url == fullUrl:
                pageCounter = int(lastPageList) + 1
                break
            else:
                commentList.append(comments[comment].text.split("\n")[0])
                commentDateList.append(commentDates[comment].text.split(",")[0])

        pageCounter += 1

    df = pd.DataFrame(
        {
            #"dates": commentDateList,
            "comments": commentList
        }
    )
    time.sleep(1)
    browser.close()
    return df

def amazonTrScraping(url):
    browser = webdriver.Chrome()
    browser.maximize_window()
    fullUrl = url.split("?")[0]
    fullUrl = fullUrl.replace("dp", "product-reviews")
    browser.get(fullUrl)
    numOfCommentSelect = browser.find_element_by_xpath("//*[@id='filter-info-section']/div")
    numberOfComment = numOfCommentSelect.text.split(", ")[1].split(" ")[0]

    fullUrl = fullUrl + "/ref=cm_cr_arp_d_paging_btm_next_2?pageNumber="

    commentCounter = 1
    commentList = []
    commentDateList = []
    countryStatus = False

    while commentCounter <= round(int(numberOfComment)/10) + 1:
        commentUrl = fullUrl + str(commentCounter)
        browser.get(commentUrl)
        time.sleep(1)
        commentDates = browser.find_elements_by_css_selector(".review-date")
        comments = browser.find_elements_by_css_selector(".review-text-content")

        for comment in range(len(comments)):
            try:
                countryOne = commentDates[comment].text.split(" ")[4]
                countryTwo = commentDates[comment].text.split(" ")[0]
                countryTR = browser.find_elements_by_tag_name("h3")
                if countryTR[1].text == "Diğer ülkelerden":
                    countryStatus = True
            except: pass

            if countryStatus == False:
                if countryTwo.split("’")[0] == "Türkiye":
                    countryTwo = commentDates[comment].text.split(" ")[0]
                    countryTwo = countryTwo.split("’")[0]

                    commentList.append(comments[comment].text)
                    commentDateList.append(" ".join(commentDates[comment].text.split(" ")[1:4]))
                    countryTwo = None


                elif countryOne.split("’")[0] == "Türkiye":
                    countryOne = commentDates[comment].text.split(" ")[4]
                    countryOne = countryOne.split("’")[0]

                    commentList.append(comments[comment].text)
                    commentDateList.append(" ".join(commentDates[comment].text.split(" ")[0:3]))
                    countryOne = None
            else: break

        time.sleep(2)
        commentCounter += 1
        if countryStatus == True: break

    df = pd.DataFrame(
        {
            #"dates": commentDateList,
            "comments": commentList
        }
    )
    time.sleep(1)
    browser.close()
    return df
