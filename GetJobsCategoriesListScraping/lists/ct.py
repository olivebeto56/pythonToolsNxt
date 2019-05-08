
def getUrls():
    return [
        [
            'https://www.computrabajo.com.mx/empleos-de-administracion-y-oficina',
            'https://www.computrabajo.com.mx/empleos-de-direccion-y-gerencia'
        ],
        ['https://www.computrabajo.com.mx/empleos-de-mercadeo-publicidad-comunicacion'],
        ['https://www.computrabajo.com.mx/empleos-de-construccion-y-obra'],
        ['https://www.computrabajo.com.mx/empleos-de-contabilidad-finanzas'],
        ['https://www.computrabajo.com.mx/empleos-de-diseno-artes-graficas'],
        [],
        ['https://www.computrabajo.com.mx/empleos-de-legal-y-asesoria'],
        ['https://www.computrabajo.com.mx/empleos-de-docencia'],
        ['https://www.computrabajo.com.mx/empleos-de-ingenieria'],
        ['https://www.computrabajo.com.mx/empleos-de-almacen-logistica'],
        [
            'https://www.computrabajo.com.mx/empleos-de-produccion-operaciones',
            'https://www.computrabajo.com.mx/empleos-de-compras-comercio-exterior'
        ],
        ['https://www.computrabajo.com.mx/empleos-de-mercadeo-publicidad-comunicacion'],
        ['https://www.computrabajo.com.mx/empleos-de-recursos-humanos'],
        [],
        ['https://www.computrabajo.com.mx/empleos-de-medicina-y-salud'],
        ['https://www.computrabajo.com.mx/empleos-de-informatica-telecomunicaciones'],
        [
            'https://www.computrabajo.com.mx/empleos-de-hosteleria-y-turismo',
            'https://www.computrabajo.com.mx/empleos-de-servicios-generales-aseo-y-seguridad'
        ],
        ['https://www.computrabajo.com.mx/empleos-de-marketing-y-ventas'],
        [],
        ['https://www.computrabajo.com.mx/empleos-de-mantenimiento-y-reparaciones-tecnicas']
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
