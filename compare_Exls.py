
import sys
import pandas as pd
from openpyxl import load_workbook


def convExlToCsv(fileNm,sheetName):
    read_NordRenew = pd.read_excel(fileNm,sheet_name= sheetName)
    read_NordRenew.to_csv(fileNm +'.csv', index = None, header=True)
    listedFile = read_NordRenew.values.tolist()
    fileLength = len(listedFile)

    return read_NordRenew, listedFile, fileLength

# the one problem i have to solve here is re-sending the files for converting the to csv..

def compareFileCsv(fileOneNm=None,sheetNameOne=None, fileTwoNm=None, sheetNameTwo=None):

    csvFileOne , csvFileOneList, lenOfFileOne = convExlToCsv(fileOneNm, sheetNameOne)

    csvFileTwo, csvFileTwoList, lenOfFileTwo = convExlToCsv(fileTwoNm, sheetNameTwo)



    # print(f'the file coverted into a list file TWO :{csvFileTwoList} \n')

    # colOnSheetOne = input('colOnSheetOne : ')
    # colOnSheetTwo = input('colOnSheetTwo : ')

    count = 0
    countNotMatch = 0
    for forLenOne in range(1, lenOfFileOne, 1):

        for forLenTwo in range(1, lenOfFileTwo, 1):
            if csvFileOneList[forLenOne][1] == csvFileTwoList[forLenTwo][0]:
                print(f'the Host name is {csvFileOneList[forLenOne][0]} and the serial Number is {csvFileTwoList[forLenTwo][0]} ')
                # this has to be gendralised as these sheets had values starting at 3 and 4 simultaneously I had to use so.
                count += 1
            # else:
            #     print(f'the Host name is {csvFileOneList[forLenOne][1]} and the serial Number is {csvFileTwoList[forLenTwo][1]} ')
            #     countNotMatch +=1
            #     break

                # with open('combineCSV.csv', 'w') as dataIn:
                #     dataIn.write("%s,%s\n" % (csvFileOneList[forLenOne][0], csvFileTwoList[forLenTwo][0]))
    print(f'Total count of matching devices = {count}')
    # print(f'Total count of NON matching devices = {countNotMatch}')


def main(args):
    #the first and 3rd  parameter is the file name , the second and 4th is the tab which you want to compare with
    # print('Please enter sheet name One: ')
    # FileOne = input('Enter Name of fileOne : ')
    # SheetOne = input('Name of the First Sheet : ')
    # FileTwo = input('Enter Name of fileTwo : ')
    # SheetTwo = input('Name of the Second Sheet : ')
    # # print(f'this is the input taken: {SheetOne}')
    #
    # compareFileCsv(FileOne+'.xlsx', SheetOne,  FileTwo+'.xlsx', SheetTwo)

    compareFileCsv('Hostname_serialNo.xlsx', 'Cisco Devices @990', '/Users/few7/Documents/Sasi@Work/Cisco SmartNet Renewal /MyWorkOnIt/Compare.xlsx', 'Powered by Cisco Ready')
    compareFileCsv('Hostname_serialNo.xlsx', 'Cisco Devices @990', 'from_Solarwinds.xlsx', 'NSG_Data')


if __name__ == '__main__':
    main(sys.argv[1:])
