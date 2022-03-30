
# library for read/write with CSV format to/from file
import csv

# library for OS functions and parsing of CLI arguments
import sys, getopt

#Global variables for default file input and default file output

g_inputFileName = "dataset_in.csv"
g_outputFileName = "dataset_out.csv"

#------------------------------------------------------------------------------------------------------------#
#Function to read CLI arguments and use them to set input and output files

def readCLIArgs():
   argv = sys.argv[1:]
   try:
      opts, args = getopt.getopt(argv,"i:o:")
   except:
      print ("Usage:\n")
      print ("dataset.py -i <inputFileName> -o <outputFileName>")

   for opt,arg in opts:
      if opt in ["-i"]:
         print("Input file = ",arg)
         g_inputFileName = arg
      elif opt in ["-o"]:
         print("Output file = ",arg)
         g_outputFileName = arg


#------------------------------------------------------------------------------------------------------------#
#function for aggregate CSV dataset
#It reads CSV from input file, and write selected colums into new dataset per rows
#fileNameInput - string variable with name of file
#fileNameOutput - straing variable with output name of file

def aggregateCSVDataset(fileNameInput,fileNameOutput):
#   try:
      with open(fileNameInput,"r") as source:
         reader = csv.reader(source)
         with open(fileNameOutput,"w") as result:
            writer = csv.writer(result)
            for row_number, r in enumerate(reader,1):
               if (row_number == 1):
                   writer.writerow ((r[6], r[3], r[85], r[86], "numberofFWDBWDPackets", "numberOfFWDBWDBytes"))
               else:
                   # Vypsani hodnot v slupcich a jejich zapis
                   # den-hodina, IPdest,    L7ProtocolNumber, L7ProtocolName, numberOfFwdPackets,   numberOfFwdBytes
                   print( r[6],"\t", r[3],"    \t", r[85],"\t",  r[86].ljust(10," "),"\t",     int(r[8])+int(r[9]),"\t",   int(r[10])+int(r[11]) , "\n")
                   writer.writerow(( r[6], r[3],    r[85],       r[86],                        int(r[8])+int(r[9]),        int(r[10])+int(r[11])      ))
#   except:
#       print("Error in aggegatedCSVDataset \n")
#      print("Filename in :", fileNameInput, "\n")

#----MAIN--------------------------------------------------------------------------------------------------------#

readCLIArgs()
aggregateCSVDataset(g_inputFileName,g_outputFileName)



