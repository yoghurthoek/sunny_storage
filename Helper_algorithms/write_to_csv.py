import csv
import os


def write_to_csv(wijk, algorithm, price):
    """
    Helper-algorithm that is needed to save the found prices per algorithms
    in a csv-file.
    """

    file = os.path.dirname(os.getcwd()) + \
        f"\\sunny_storage\\Output_Data\\wijk{wijk}_prices.csv"
    with open(file, mode='a') as f:
        file_writer = csv.writer(f, delimiter=',', quotechar='"',
                                 quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow([price, algorithm])
