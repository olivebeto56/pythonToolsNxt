import boto3
import csv
import sys
import math
import threading
import os
import constants


class Thread(threading.Thread):
    def __init__(self, t, n, list):
        threading.Thread.__init__(self, target=t, args=(n, list))
        self.start()


def translate(number, list):

    translate = boto3.client(service_name='translate',
                             aws_access_key_id=constants.getAwsAccessKey(), aws_secret_access_key=constants.getAwsSecretAccessKey())

    count = 0
    with open('files-out/skills-es-'+str(number)+'.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)

        for word in list:
            positionTranslated = []

            print("thead "+str(number)+": "+str(count) +
                  "/"+str(len(list))+" -- "+word)
            customObject = ("skill",)

            count = count+1
            result = translate.translate_text(
                Text=word, SourceLanguageCode="en", TargetLanguageCode="es")

            customObject = customObject + (result.get('TranslatedText'),)
            positionTranslated.append(customObject)
            writer.writerows(positionTranslated)

        writeFile.close()


def main():
    threads = []

    nThreads = 1
    if len(sys.argv) > 1:
        nThreads = int(sys.argv[1])

    skillsList = []

    with open('files-out/skills-en.csv') as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            count = count + 1
            skillsList.append(row[1])

    nElemts = math.ceil((len(skillsList)/nThreads))

    for n in range(0, nThreads):
        subArray = skillsList[n*nElemts:(n+1)*nElemts]

        threads.append(Thread(translate, n, subArray))

    for x in threads:
        x.join()

    print("finish all")

    fout = open("files-out/skills-es.csv", "a")

    for line in open("files-out/skills-es-0.csv"):
        fout.write(line)

    os.remove("files-out/skills-es-0.csv")

    for num in range(1, nThreads):
        f = open("files-out/skills-es-"+str(num)+".csv")
        for line in f:
            fout.write(line)
        f.close()  # not really needed

        os.remove("files-out/skills-es-"+str(num)+".csv")

    fout.close()


if __name__ == '__main__':
    main()
