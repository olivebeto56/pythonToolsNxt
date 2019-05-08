import requests
import csv
from lxml import html

positionCategoriesObject = []

with open('files/nextlineJobs.csv', newline='') as File:
    reader = csv.reader(File)
    count = 0
    for row in reader:

        count = count + 1

        position = row[0]
        print(str(count)+"/622 -- "+position)
        url = 'https://www.computrabajo.com.mx/ofertas-de-trabajo/?q=' + position

        page = requests.get(url)
        tree = html.fromstring(page.content)

        categoriesArray = tree.xpath(
            "//h3[text()='Categoría']/ancestor::div/ancestor::div/ul/li/span/a/text()")

        customObject = (position,)

        for category in categoriesArray:
            customObject = customObject + (category,)

        positionCategoriesObject.append(customObject)

with open('files/positionCategories.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(positionCategoriesObject)

    writeFile.close()
