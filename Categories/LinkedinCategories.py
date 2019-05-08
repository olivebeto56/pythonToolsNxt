from lxml import html
import csv

for numTemp in range(26, 27):
    with open(str(numTemp)+'.txt', 'r') as file:
        data = file.read().replace('\n', '')

    categoriesArray = []

    tree = html.fromstring(data)

    temp = tree.xpath('//select/option/text()')

    for category in temp:
        customObject = (category,)
        categoriesArray.append(customObject)

    with open(str(numTemp)+'.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(categoriesArray)

        writeFile.close()

# print(categoriesArray)
