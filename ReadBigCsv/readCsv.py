import csv


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()


if __name__ == '__main__':
    setIntance = set()
    setIntance2 = set()

    with open('files/temp_datalab_records_job_listings.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        count = 0

        for row in csv_reader:
            # 68460125
            # printProgressBar(count+1, 100000, prefix='Progress:',
                            #  suffix = 'Complete('+str(count)+")", length = 50)

            count = count+1
            print(row[4])
            setIntance.add(row[6])
            setIntance2.add(row[4])

            if(count == 100000):
                break

    print("Category: "+str(len(setIntance)))
    print("Job-Position: "+str(len(setIntance2)))
