import csv


def getSkills(language):
    temp = []
    with open('files/skills-'+language+'.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            temp.append(row[1])

    return temp


def main():
    en = getSkills("en")
    es = getSkills("es")
    new = []
    for i in range(len(en)):
        if(en[i] == es[i]):
            new.append(en[i])

    print(len(new))

    with open('files-out/skills-compare.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        for n in new:
            customObject = ("skill", n)
            writer.writerows([customObject])


if __name__ == '__main__':
    main()
