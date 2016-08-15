#Working with Excel documents
#data from Electric Reliability Council of Texas

#Python Module XLRD
    #Allows us to work with xls and xlsx formats of Excel

import xlrd

datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile) #command to open the workbook
    sheet = workbook.sheet_by_index(0) #specify sheet we want to work with.  XLRD is zero based indexing so 0 means sheet1

    #example of list comprehension
    #we are looping through all the of rows and columns and reading that data in a Python list
    # data = [[sheet.cell_value(r, col)
    #             for col in range(sheet.ncols)]
    #                 for r in range(sheet.nrows)]

    Coast = sheet.col_values(1,start_rowx=1)

    for i, value in enumerate(Coast):
        if value == max(Coast):
            maxExcelTime = sheet.cell_value(i+1,0)
            maxTime = xlrd.xldate_as_tuple(maxExcelTime,0)

    for i, value in enumerate(Coast):
        if value == min(Coast):
            minExcelTime = sheet.cell_value(i+1,0)
            minTime = xlrd.xldate_as_tuple(minExcelTime,0)

    # print "\nList Comprehension"
    # print "data [3][2]:",
    # print data [3][2]
    #
    # print "\nCells in a nested loop:"
    # for row in range(sheet.nrows):
    #     for col in range(sheet.ncols):
    #         if row == 50:
    #             print sheet.cell_value(row, col),
    #
    # ### Other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:",
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):"
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):",
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3 ,from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)
    #
    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):",
    # print sheet.cell_type(1,0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)

    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast':0
    }

    data['maxtime'] = maxTime
    data['maxvalue'] = max(Coast)
    data['mintime'] = minTime
    data['minvalue'] = min(Coast)
    data['avgcoast'] = sum(Coast)/len(Coast)


    return data

data = parse_file(datafile)
