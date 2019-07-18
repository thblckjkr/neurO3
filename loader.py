import csv
import math 

class loader:
    # Where the data will be stored
    # note, everything should be on integers (performance?)
    def get(self):
        # Define where the data will be stored
        results = {
            'inputs' : [],
            'targets': []
        }

        with open('databases/Ozonos.csv', "r") as f:
            next(f) # skip header
            for x in f:
                y = x.rstrip("\n\r")
                row = y.split(",")

                # Ignore ROWS that contain a NULL
                if row[2] == 'NULL' or row[3] == 'NULL' or float(row[2]) < 6 or float(row[2]) > 25  :
                    continue

                # Add data
                results[ 'inputs'].append([
                    float(row[2]),
                    float(row[2]) * float(row[2]),
                    math.sin(float(row[2])),
                    math.cos(float(row[2]))
                ])

                results['targets'].append([
                    float(row[3]),
                    float(row[3]) * float(row[3]),
                    math.sin(float(row[3])),
                    math.cos(float(row[3]))
                ] )

        return results