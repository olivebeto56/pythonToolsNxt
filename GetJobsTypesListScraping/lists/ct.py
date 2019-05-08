
def getUrls():
    return [
        ['https://www.computrabajo.com.mx/empleos-jornada-tiempo-completo'],
        ['https://www.computrabajo.com.mx/empleos-jornada-medio-tiempo'],
        ['https://www.computrabajo.com.mx/empleos-jornada-desde-casa']
    ]


def getPageString():
    return "p"


def getUrlBase():
    return "https://www.computrabajo.com.mx"


def getUrlJobsXpath():
    return "//div[contains(@class, 'bClick')]//a[@class = 'js-o-link']/@href"


def getTotalJobs():
    return "//div[@class='pg_grid']/span/span[2]/text()"


def getNPageXpath():
    return ''
    # return '//div[contains(@class, "paginasCenter")]/ul/li[position() = (last()-1)]/a/text()'


def getJobDescriptionXpathArray():
    return [
        '//section[contains(@class, "detail_of")]/ul/li'
    ]
