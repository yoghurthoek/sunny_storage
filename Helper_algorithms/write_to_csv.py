import csv
import os

def write_to_csv(wijk, algorithm, price, batteries, houses):
    print("which run is this?")
    runnumber = (input("> ")).upper()
    file = os.path.dirname(os.getcwd())+f"\\sunny_storage\\Output_Data\\wijk{wijk}_gridout{runnumber}.csv"
    with open(file, mode='w') as f:
        file_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for h in houses:
            file_writer.writerow([runnumber, "house", houses[h].id, houses[h].posx, houses[h].posy, houses[h].output, houses[h].pluggedin, algorithm])
        for b in batteries:
            connections = []
            for h in batteries[b].connected:
                connections.append(h.id)
            file_writer.writerow([runnumber, "battery", batteries[b].id, batteries[b].posx, batteries[b].posy, batteries[b].capacity, batteries[b].filled, connections, algorithm])
    file2 = os.path.dirname(os.getcwd())+f"\\sunny_storage\\Output_Data\\wijk{wijk}_prices.csv"
    with open(file2, mode='a') as f:
        file_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(["price", price, runnumber, algorithm])
