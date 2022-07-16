import csv
import os
from platform import libc_ver
from pyparsing import line
with open('al092004_Ivan.csv') as file:
    reader=csv.DictReader(file)  
    for row in reader:
        shfile=row['INSTANCENAME']
        if os.path.exists(shfile+".sh"):
            os.remove(shfile+".sh")
        else:
            print("The file does not exist")
        f = open(shfile+".sh", "x")
        #Indicator for generated file that is a bash script.
        line1 ="#!/bin/sh \n"
        #Start writing static things
        line2="#N O T E: \n"
        line3="#This configuration file was generated automatically from a CSV file. \n"
        line4="#Any changes should probably be managed via the method of creation rather \n"
        line5="#than by manually editing this file ... unless you know what you're doing, \n"
        line6="#or don't :-) \n"
        line7="#-------------------------------------------------------------------\n"
        f.writelines([line1, line2, line3,line4,line5,line6,line7])
        #Start creating variables
        f.write("INSTANCENAME="+row['INSTANCENAME']+"\n")
        f.write("INSTANCENAME="+row['INSTANCENAME'])