#!/usr/bin/env python

# """
# Your task is to process the supplied file and use the csv module to extract data from it.
# The data comes from NREL (National Renewable Energy Laboratory) website. Each file
# contains information from one meteorological station, in particular - about amount of
# solar and wind energy for each hour of day.
#
# Note that the first line of the datafile is neither data entry, nor header. It is a line
# describing the data source. You should extract the name of the station from it.
#
# The data should be returned as a list of lists (not dictionaries).
# You can use the csv modules "reader" method to get data in such format.
# Another useful method is next() - to get the next line from the iterator.
# You should only change the parse_file function.
# """

import csv
import os

DATADIR = ""
DATAFILE = "745090.csv"


def parse_file(datafile):
    name = ""
    data = []
    with open(datafile,'rb') as f:
        energy_reader = csv.reader(f, delimiter= ',', quotechar='"')
        name = energy_reader[0,1]

        # counter = 0
        # for row in energy_reader:
        #     if counter == 0:
        #         name = row[1]
        #     if counter > 1:
        #         data.append(row)

            #counter += 1
            #print name

        #firstline = f.readline().split(",")
        #name = firstline[1]
        #pass
    # Do not change the line below
    return (name, data)
    #print name

parse_file(DATAFILE)


# def test():
#     datafile = os.path.join(DATADIR, DATAFILE)
#     name, data = parse_file(datafile)
#
#     assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
#     assert data[0][1] == "01:00"
#     assert data[2][0] == "01/01/2005"
#     assert data[2][5] == "2"
#
#
# if __name__ == "__main__":
#     test()
