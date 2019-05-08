from lxml import html
import csv

categoriesArray = []

tree = html.fromstring('<ul class="c01941 c01819"><li><a rel="follow" id="subcategory293" class="c01939 c01817" href="/empleos/trabajo-en-asistente-medico-veterinaria-zoologia/">Asistente Médico</a></li><li><a rel="follow" id="subcategory294" class="c01939 c01817" href="/empleos/trabajo-en-doctor-veterinaria-zoologia/">Doctor</a></li><li><a rel="follow" id="subcategory295" class="c01939 c01817" href="/empleos/trabajo-en-estilista-canino-veterinaria-zoologia/">Estilista Canino</a></li></ul>')

temp = tree.xpath('//ul/li/a/text()')

for category in temp:
    customObject = (category,)
    categoriesArray.append(customObject)


with open('9.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(categoriesArray)

    writeFile.close()

# print(categoriesArray)
