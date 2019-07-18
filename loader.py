import csv

class loader:
    # Where the data will be stored
    # note, everything should be on integers (performance?)
    def get(self):
        # Define where the data will be stored
        results = {
            'inputs' : [],
            'targets': []
        }

        data = []
        info = []

        with open('databases/Ozonos_CCN.csv', "r") as f:
            # f = open("demofile.txt", "r")
            # I've verified manually the data. I am sure that this class it's working right
            for x in f:
                y = x.rstrip("\n\r")
                row = y.split(",")

                if data == []:
                    for i in range(11, 22):
                        if row[i] != "":
                            info.append( int(row[i]) )

                # This could be variable... but meh
                for i in range(2, 11):
                    if row[i] != "":
                        data.append( int(row[i]) )

                if row[0] == 'SEPARATE':
                    #Save the current data on temporal
                    results['inputs'].append( data )
                    results['targets'].append( info )

                    # Start a new data
                    data = []
                    info = []
                    
        return results