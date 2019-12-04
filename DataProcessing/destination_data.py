import csv
from NaNAir39 import Destination

def main():
    data = []
    path = "DataClasses/Destinations.csv"
    file = open(path, newline= "")
    reader = csv.reader(file)

    print(reader)

main()