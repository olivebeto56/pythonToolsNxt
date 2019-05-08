import csv
import os
from os import listdir
from os.path import isfile, join

skills = set()
nFile = 0
nSkill = 0


def getSkills(language):
    temp = []
    with open('files/skills-'+language+'.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            temp.append(row[1])

    return temp


def searchInFile(fileName, skill):
    global skills
    with open('files/categories/'+fileName) as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            if skill.upper() in row[1].upper():
                if not skill in skills:
                    skills.add(skill)
                    addNewSkill(skill)
                print(len(skills))
                break


def getMemoryData(index):
    with open('db.txt', 'r') as file:
        data = file.read().replace('\n', '')
        return int(data.split(",")[index])


def saveMemoryData(indexF, indexS):
    file = open("db.txt", "w")
    file.write(str(indexF)+","+str(indexS))
    file.close()


def fillSkillsGlobal():
    global skills
    try:
        with open('files-out/skills-search.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                skills.add(row[1])
    except FileNotFoundError:
        print("no existe")


def addNewSkill(newSkill):
    with open('files-out/skills-search.csv', 'a') as writeFile:
        skillRow = [('skill', newSkill)]

        writer = csv.writer(writeFile)
        writer.writerows(skillRow)

    writeFile.close()


def main():
    global nFile
    global nSkill

    nFile = getMemoryData(0)
    nSkill = getMemoryData(1)

    fillSkillsGlobal()
    es = getSkills("en")

    onlyfiles = [f for f in listdir(
        "files/categories/") if isfile(join("files/categories/", f))]
    indexF = nFile
    indexs = nSkill
    for file in onlyfiles[nFile:]:
        print(str(indexF)+") "+file)
        for skill in es[indexs:]:
            print(str(len(skills))+"--->"+str(indexs))
            searchInFile(file, skill)
            saveMemoryData(indexF, indexs)
            indexs += 1
        indexF += 1
        indexs = 0
        saveMemoryData(indexF, indexs)


if __name__ == "__main__":
    main()
