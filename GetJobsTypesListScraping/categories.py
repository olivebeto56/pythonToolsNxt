from time import sleep
from lxml import html
import requests
import csv
import sys
from tqdm import tqdm
import os
from os import listdir
from os.path import isfile, join
import importlib

searchObject = importlib.import_module('lists.occ')
fileSelected = ""

nJobs = 0
countJobs = 0
urlBase = ""
specialFieldNextline = ['FullTime',
                        'HalfTime',
                        'Freelance']


specialFieldUrl = []


def getUrlJobsAndTotal(url):
    urls = []
    try:

        page = requests.get(url)
        tree = html.fromstring(page.content)

        jobsA = tree.xpath(searchObject.getUrlJobsXpath())

        if(searchObject.getNPageXpath() != ''):
            pagerTree = tree.xpath(searchObject.getNPageXpath())
            nPages = int(pagerTree[0])
        else:
            pagerTree = tree.xpath(searchObject.getTotalJobs())
            totalJobs = int(pagerTree[0].replace(',', ''))
            nPages = int(totalJobs/len(jobsA))

        for jobA in jobsA:
            jobUrl = urlBase + jobA
            urls.append(jobUrl)
        return (nPages, urls)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("-----Error-------")
        return False


def getRange(sys):
    if len(sys.argv) > 2:
        tupla = (int(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv) > 1:
        tupla = (int(sys.argv[1]), int(sys.argv[1])+1)
    else:
        tupla = (0, len(specialFieldNextline))

    return tupla


def addJobInCsv(jobInfo, index):
    specialField = specialFieldNextline[index]
    with open('files/'+fileSelected+"/"+specialField+'.csv', 'a') as writeFile:
        jobRow = [(specialField, jobInfo)]

        writer = csv.writer(writeFile)
        writer.writerows(jobRow)

    writeFile.close()


def getJobInfo(url):
    
    try:
        page = requests.get(url)
        tree = html.fromstring(page.content)
        containerString = ""

        jobDescriptionSectionArray = searchObject.getJobDescriptionXpathArray()

        for jobDescriptionSection in jobDescriptionSectionArray:
            jobFirstPart = tree.xpath(jobDescriptionSection)

            for items in jobFirstPart:
                containerString = containerString + " " + items.text_content()

        return containerString
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        return False



def createCsvCategories(url, index):
    global nJobs
    global countJobs

    pageTotal = getUrlJobsAndTotal(url)
    nPages = pageTotal[0]

    # tp = tqdm(range(1, nPages))
    for page in range(110, nPages +1):
        # tp.set_description("Pages")
        print("    page)"+str(page))
        urlsJobsAndTotal = getUrlJobsAndTotal(
            url+"?"+searchObject.getPageString()+"="+str(page))

        if(urlsJobsAndTotal != False):
            urlsJobs = urlsJobsAndTotal[1]

            # tj = tqdm(urlsJobs)
            countJobs2 = 0
            for urlJob in urlsJobs:
                print("      jobs) "+str(countJobs2))
                # tj.set_description("Jobs (%s/%s)" %
                                #    (str(countJobs), str(nJobs)))
                countJobs2 = countJobs2+1
                jobInfo = getJobInfo(urlJob)
                if(jobInfo != False):
                    addJobInCsv(jobInfo, index)


# def getTotalJobsOcc(iterationRange):
#     global nJobs

#     t = tqdm(range(iterationRange[0], iterationRange[1]))
#     for counter in t:
#         t.set_description("Calculing jobs")
#         url = specialFieldUrl[counter]

#         page = requests.get(url)
#         tree = html.fromstring(page.content)

#         text = tree.xpath(
#             '//div[@id="search-results"]/div[3]/div/div[1]/div/div[1]/div[9]/div/div/h1/text()')

#         nJobsLocal = [int(s) for s in str(text[0]).split() if s.isdigit()]
#         print(specialFieldNextline[counter]+str(nJobsLocal[0]))
#         nJobs = nJobs + nJobsLocal[0]

#     print("jobs: "+str(nJobs))


def main():
    global searchObject
    global specialFieldUrl
    global urlBase
    global fileSelected

    onlyfiles = [f for f in listdir("lists/") if isfile(join("lists/", f))]

    count = 1
    print("Files:")
    for file in onlyfiles:
        print("  "+str(count)+") "+file)
        count = count+1
    print("\n")

    number = input("Select file: ")
    fileSelected = onlyfiles[int(number)-1][:-3]

    if not os.path.exists("files/"+fileSelected):
        os.mkdir("files/"+fileSelected)

    searchObject = importlib.import_module('lists.'+fileSelected)

    urlBase = searchObject.getUrlBase()
    specialFieldUrl = searchObject.getUrls()

    iterationRange = getRange(sys)

    t = tqdm(range(iterationRange[0], iterationRange[1]))

    for counter in range(iterationRange[0], iterationRange[1]):
        print(str(counter)+") "+specialFieldNextline[counter])
        # t.set_description(specialFieldNextline[counter])

        # t2 = tqdm(specialFieldUrl[counter])
        countUrl = 0
        for url in specialFieldUrl[counter]:
            print("  ulr) "+str(countUrl)+" -- "+url)
            # t2.set_description("Urls")
            createCsvCategories(url, counter)

    print("\n \n \n")


if __name__ == '__main__':
    main()
