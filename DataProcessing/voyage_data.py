import csv
from NaNAir39.DataLayer.voyage import Voyage

def main():
    data = []
    path = "../DataClasses/UpcomingFlights.csv"
    file = open(path, newline="")
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        flightNumber_str = row[0]
        departingFrom_str = row[1]
        arrivingAt_str = row[2]
        departure_str = row[3]
        arrival_str = row[4]

        data.append(AirplaneType(flightNumber_str, departingFrom_str, arrivingAt_str, departure_str, arrival_str))

        print(row)

main()