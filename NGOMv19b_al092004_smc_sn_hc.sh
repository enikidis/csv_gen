#!/bin/sh 
#N O T E: 
#This configuration file was generated automatically from a CSV file. 
#Any changes should probably be managed via the method of creation rather 
#than by manually editing this file ... unless you know what you're doing, 
#or don't :-) 
#-------------------------------------------------------------------
INSTANCENAME=NGOMv19b_al092004_smc_sn_hc
ASGSADMIN=archcomputerservice@gmail.com
RMQMessaging_Enable=off
RMQMessaging_Transmit=off
# Input files and templates 
GRIDNAME=NGOMv19b
source $SCRIPTDIR/config/mesh_defaults.sh 
CONTROLTEMPLATE=
TRIGGER=rssembedded
RSSSITE=filesystem
FTPSITE=filesystem
FDIR=/ddnA/work/$USER/fordir
HDIR=/ddnA/work/$USER/bestdir
TIDEFAC=on
HINDCASTLENGTH=30.0
BACKGROUNDMET=off
FORECASTCYCLE=00,06,12,18 
forecastSelection=strict 
TROPICALCYCLONE=on
STORM=09
YEAR=2004
WAVES=on
VARFLUX=off
CYCLETIMELIMIT=99:00:00
# Computational Resources (related defaults set in platforms.sh) 
NCPU=959
NUMWRITERS=1
NCPUCAPACITY=9999
# Post processing and publication
EMAILNOTIFY=yes
INTENDEDAUDIENCE=general
OPENDAPPOST=opendap_post2.sh
POSTPROCESS=includeWind10m.sh createOPeNDAPFileList.sh $OPENDAPPOST
OPENDAPNOTIFY=asgs.cera.lsu@coastalrisk.live,archcomputerservice@gmail.com
NOTIFY_SCRIPT=cera_notify.sh 
TDS=( lsu_tds ) 
# Initial state (overridden by STATEFILE after ASGS gets going) 
HINDCASTENDDATE=2004091100
HINDCASTLENGTH=30.0
COLDSTARTDATE=2004081200
HOTORCOLD=coldstart
LASTSUBDIR=null
#
# Scenario package 
#
PERCENT=default 
SCENARIOPACKAGESIZE=0 
case $si in 
   -2)
       ENSTORM=hindcast
       ;;
   -1)
      # do nothing ... this is not a forecast
       ENSTORM=nowcast
       ;;
    0)
       ENSTORM=nhcConsensusWind10m
      source $SCRIPTDIR/config/io_defaults.sh # sets met-only mode based on Wind10m suffix
      ;;
    1)
       ENSTORM=nhcConsensus
       ;;
    *)
       echo  CONFIGRATION ERROR: Unknown ensemble member number: 
       ;;
esac
#
PREPPEDARCHIVE=prepped_${GRIDNAME}_${INSTANCENAME}_${NCPU}.tar.gz 
HINDCASTARCHIVE=prepped_${GRIDNAME}_hc_${INSTANCENAME}_${NCPU}.tar.gz 
