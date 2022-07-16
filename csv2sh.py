import csv
import os
from pyparsing import line
with open('al092004_Ivan.csv') as file:
    reader=csv.DictReader(file)  
    for row in reader:
        shfile=row['INSTANCENAME']
        if os.path.exists(shfile+".sh"):
            print("Rewriting file")
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
        f.write("ASGSADMIN="+row['ASGSADMIN']+"\n")
        #f.write("ACCOUNT="+row['ACCOUNT']+"\n") this need work to the csv
        f.write("RMQMessaging_Enable="+row['RMQMessaging_Enable']+"\n")
        f.write("RMQMessaging_Transmit="+row['RMQMessaging_Transmit']+"\n")
        #f.write("enablePostStatus="+row['enablePostStatus']+"\n") this need work to the csv
        #f.write("enableStatusNotify="+row['enableStatusNotify']+"\n") this need work to the csv
        #f.write("statusNotify="+row['statusNotify']+"\n") this need work to the csv
        f.write("# Input files and templates \n")
        f.write("GRIDNAME="+row['GRIDNAME']+"\n")
        f.write("source $SCRIPTDIR/config/mesh_defaults.sh \n")
        f.write("CONTROLTEMPLATE="+row['CONTROLTEMPLATE']+"\n")
        f.write("TRIGGER="+row['TRIGGER']+"\n")
        f.write("RSSSITE="+row['RSSSITE']+"\n")
        f.write("FTPSITE="+row['FTPSITE']+"\n")
        f.write("FDIR="+row['FDIR']+"\n")
        f.write("HDIR="+row['HDIR']+"\n")
        f.write("TIDEFAC="+row['TIDEFAC']+"\n")
        f.write("HINDCASTLENGTH="+row['HINDCASTLENGTH']+"\n")
        f.write("BACKGROUNDMET="+row['BACKGROUNDMET']+"\n")
        f.write("FORECASTCYCLE=00,06,12,18 \n")
        f.write("forecastSelection=strict \n")
        f.write("TROPICALCYCLONE="+row['TROPICALCYCLONE']+"\n")
        f.write("STORM="+row['STORM']+"\n")
        f.write("YEAR="+row['YEAR']+"\n")
        f.write("WAVES="+row['WAVES']+"\n")
        f.write("VARFLUX="+row['VARFLUX']+"\n")
        f.write("CYCLETIMELIMIT="+row['CYCLETIMELIMIT']+"\n")
        f.write("# Computational Resources (related defaults set in platforms.sh) \n")
        f.write("NCPU="+row['NCPU']+"\n")
        f.write("NUMWRITERS="+row['NUMWRITERS']+"\n")
        f.write("NCPUCAPACITY="+row['NCPUCAPACITY']+"\n")
        f.write("# Post processing and publication\n")
        f.write("EMAILNOTIFY="+row['EMAILNOTIFY']+"\n")
        f.write("INTENDEDAUDIENCE="+row['INTENDEDAUDIENCE']+"\n")
        f.write("OPENDAPPOST="+row['OPENDAPPOST']+"\n")
        f.write("POSTPROCESS="+row['POSTPROCESS']+"\n")
        f.write("OPENDAPNOTIFY="+row['OPENDAPNOTIFY']+"\n")
        f.write("NOTIFY_SCRIPT=cera_notify.sh \n")
        f.write("TDS=( lsu_tds ) \n")
        f.write("# Initial state (overridden by STATEFILE after ASGS gets going) \n")
        f.write("HINDCASTENDDATE="+row['HINDCASTENDDATE']+"\n")
        f.write("HINDCASTLENGTH="+row['HINDCASTLENGTH']+"\n")
        f.write("COLDSTARTDATE="+row['COLDSTARTDATE']+"\n")
        f.write("HOTORCOLD="+row['HOTORCOLD']+"\n")
        f.write("LASTSUBDIR="+row['LASTSUBDIR']+"\n")
        f.write("#\n")
        f.write("# Scenario package \n")
        f.write("#\n")
        f.write("PERCENT=default \n")
        f.write("SCENARIOPACKAGESIZE=0 \n")
        f.write("case $si in \n")
        f.write("   -2)\n")
        f.write("       ENSTORM=hindcast\n")
        f.write("       ;;\n")
        f.write("   -1)\n")
        f.write("      # do nothing ... this is not a forecast\n")
        f.write("       ENSTORM=nowcast\n")
        f.write("       ;;\n")
        f.write("    0)\n")
        f.write("       ENSTORM=nhcConsensusWind10m\n")
        f.write("      source $SCRIPTDIR/config/io_defaults.sh # sets met-only mode based on Wind10m suffix\n")
        f.write("      ;;\n")
        f.write("    1)\n")
        f.write("       ENSTORM=nhcConsensus\n")
        f.write("       ;;\n")
        f.write("    *)\n")
        conferror1=("       echo ")
        conferror2=(" CONFIGRATION ERROR: Unknown ensemble member number: \n ")  #this must be added to the csv file. there is conflict btween the character for strings from bash and python
        f.write(conferror1 + conferror2 )
        f.write("      ;;\n")
        f.write("esac\n")
        f.write("#\n")
        f.write("PREPPEDARCHIVE=prepped_${GRIDNAME}_${INSTANCENAME}_${NCPU}.tar.gz \n")
        f.write("HINDCASTARCHIVE=prepped_${GRIDNAME}_hc_${INSTANCENAME}_${NCPU}.tar.gz \n")