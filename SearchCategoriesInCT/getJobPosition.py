import requests
import occArray
import json
import csv

occArray = occArray.getArray()
jobPositionObject = []
count = 0
for occText in occArray:

    count = count + 1
    print(str(count)+"/"+str(len(occArray)))
    url = "https://www.computrabajo.com.mx/Ajax/getSuggestions.ashx"

    payload = "q="+occText+"&type=2171027981D853E4&idportal=7A02BC8BFD169A2F&undefined="
    headers = {
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "es-ES,es;q=0.9,en;q=0.8",
        'Connection': "keep-alive",
        'Content-Length': str(len(occText)),
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Cookie': "_ga=GA1.3.189345862.1550512384; _fbp=fb.2.1550512384215.1341222339; ct_consent=1; cto_lwid=b1e3ffa5-ccd1-499f-b82f-b3ddb14497a6; ccg=i=75E1389D601B74B02918C20A28242E49EEAB82EAC9A3F73107B8F169A23974FA90700E35F6028355&c=B90D88AF0B3AF963&p=2; _gid=GA1.3.1460491355.1554844951; uco=i=0C9AC5653DF503C0&e=DF3E0B8FBBDCB6450E3FB7C45B36F80B094EAF463CAC8E0681F0912B11C890E6&p=54168AE0CA7AD2035B2283E6433271&n=Miguel Ãngel&t=logos/empresas/2019/04/04/b468e56e6ce14c2f8fc2193448519thumbnail.jpg; criteo_lastID=Recursos Humanos",
        'Host': "www.computrabajo.com.mx",
        'Origin': "https://www.computrabajo.com.mx",
        'Referer': "https://www.computrabajo.com.mx/",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        'X-Requested-With': "XMLHttpRequest",
        'cache-control': "no-cache",
        'Postman-Token': "62eaeb72-c077-4974-b5fd-44c9328af613"
    }
    response = requests.post(url, data=payload, headers=headers)

    if response.text:
        binary = response.content
        outputs = json.loads(binary)
        for output in outputs:
            customObject = (output["Value"],)
            jobPositionObject.append(customObject)
            print(output["Value"])


# with open('CT.csv', 'w') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(jobPositionObject)

#     writeFile.close()
