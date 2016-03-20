# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:  #open file
        header = f.readline().split(",") #read first line and split it to get list of keys for dictionary
        counter = 0
        for line in f:
            if counter == 10:
                break

            fields = line.split(",")  #split lines of file
            entry = {}  #initialize dictionary
            for i, value in enumerate(fields):  #enumerate(thing), where thing is either an iterator or a sequence, returns a iterator that will return (0, thing[0]), (1, thing[1]), (2, thing[2]), and so forth.
                entry[header[i].strip()] = value.strip()

            data.append(entry)
            counter += 1
    return data

    
