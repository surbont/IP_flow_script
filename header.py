


#Script to list all columns of dataset.csv

import csv

with open("dataset_in.csv") as file:
   reader = csv.reader(file)
   header = next(reader)
   i=0
   for h in header:
      print(i,"\t\t" ,h,"\n")
      i+=1


