# http://videlibri.sourceforge.net/cgi-bin/xidelcgi


def getUrls():
    # Url list of job search categories
    # Order:
        # 'Administración',
        # 'Comunicación',
        # 'Arquitectura y Construcción',
        # 'Contabilidad y Finanzas',
        # 'Creatividad y Diseño',
        # 'Fotografía y Cine',
        # 'Derecho y Leyes',
        # 'Educación',
        # 'Ingeniería',
        # 'Logística, Transporte y Distribución',
        # 'Fabricación, producción y operación',
        # 'Marketing, Publicidad y Relaciones Públicas',
        # 'Recursos humanos',
        # 'Deporte, Belleza y Moda',
        # 'Sector Salud',
        # 'Ciencias de la Computación',
        # 'Turismo, Hospitalidad y Gastronomía',
        # 'Ventas',
        # 'Veterinaria y Zoología',
        # 'Reparaciones Técnicas y Mantenimiento'

    return [
        ['https://www.occ.com.mx/empleos/trabajo-en-administrativos/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-comunicaciones/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-construccion/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-contabilidad/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-creatividad-produccion-y-diseno-comercial/'],
        [],
        ['https://www.occ.com.mx/empleos/trabajo-en-derecho-y-leyes/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-educacion/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-ingenieria/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-logistica-transportacion-y-distribucion/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-manufactura-produccion-y-operacion/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-mercadotecnia-publicidad-y-relaciones-publicas/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-recursos-humanos/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-salud-y-belleza/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-sector-salud/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-tecnologias-de-la-informacion-sistemas/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-turismo-hospitalidad-y-gastronomia/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-ventas/'],
        ['https://www.occ.com.mx/empleos/trabajo-en-veterinaria-zoologia/'],
        []
    ]


def getPageString():
    return "page"


def getUrlBase():
    return "https://www.occ.com.mx"


def getUrlJobsXpath():
    # Retur list of url
    return "//a[contains(@class, 'trk-job-ad')]/@href"


def getNPageXpath():
    # Return a list with a single data
    # Data: number of pages
    return '//div[@id="search-results"]/div[3]/div/div[1]/div/div[3]/div/div/div/ul/li[position() = (last()-1)]/text()'


def getJobDescriptionXpathArray():
    # Retur container with jobs description.
    # The information can be separated into different containers.
    return [
        "//div[contains(@class, 'link-back-job-ad')][1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div",
        "//div[contains(@class, 'link-back-job-ad')][1]/div[1]/div[1]/div[1]/div[3]"
    ]
