import csv
import os


def bestplot(wijk, algorithm, price):
    """
    Helper-algorithm that is used to write or overwrite the best price to a
    csv file.
    """

    savefig = False
    absent = True
    file = os.path.dirname(os.getcwd()) + \
        f"\\sunny_storage\\Output_Data\\bestwijk{wijk}.csv"
    try:
        with open(file, mode='r') as f:
            reader = csv.reader(f)
            copy = list(reader)
            for row in copy:
                if algorithm in row:
                    absent = False
                    if price < int(row[0]):
                        savefig = True
                        row[0] = price
    except FileNotFoundError:
        pass

    if absent is True:
        savefig = True
        with open(file, mode='a') as f:
            writer = csv.writer(f, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
            writer.writerow([price, algorithm])

    elif savefig is True:
        with open(file, mode='w') as f:
            writer = csv.writer(f, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
            for row in copy:
                if row != []:
                    writer.writerow(row)

    return savefig
