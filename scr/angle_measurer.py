# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:24:31 2017

@author: holmes
"""

"""
Created on Mon Feb  6 16:17:11 2017
This is an passer script, this will take the information from a gyrate file
and a torsion list and then add a mode at the base of each torsion.
For this script to run you need the combined gyrate addition script.

This script is now working and in the last alpha stage:
Things that need to be done:
1. minor refactoring
2.clearing up code
3. addition on of DbC

USE AT OWN RISH, IF UNSURE PLEASE SEE AJH
@author: holmes
"""

import argparse
import importlib
import angle_extractor_v4
importlib.reload(angle_extractor_v4)

##############
parser = argparse.ArgumentParser(description="Good day! This is a torsion angle measuring script! This script has been written to allow “yea old sea dogs” use a corresponding SDF and get out corresponding angle for different torsion values using the currentIC and gyrate file, before using it you must make some precaution, make sure the SDF, currentIC and gyrate file are all from the same molecule and back up these files, as although this script has undergone some rudimentary testing there is a risk these file might end up in Davie Jones' locker...,. When this is done then please input parameters consistent with the list below, and run this script in the folder it was given in, shiver my timbers...")

parser.add_argument("gyrate_file_location", type=str,
                    help = "Please put the gyrate file location, relvent to your current location")

parser.add_argument("raw_ic_file", type=str,
                    help = "Please input the location of the currenIC file related to the gyrate file you wish to use, the list of torsion which contain the angle which you want")

parser.add_argument("sdf_file", type=str,
                    help = "Please input the location of the crystal file you wish to use")

parser.add_argument("outp_file", type=str,
                    help = "Please input the location of where you would like the output file to be")


args = parser.parse_args()

print(args.gyrate_file_location)
print(args.raw_ic_file)
print(args.sdf_file)
print(args.outp_file)

gyrate_file_location = args.gyrate_file_location
raw_data_ic = args.raw_ic_file
raw_data_sdf_angle = args.sdf_file
out_put_file = args.outp_file

###############

###
# Testing
#gyrate_file_location= "/home/holmes/Desktop/Finished_Deletable/C4X_11162/project/structure/Round_86/SubRound_86_1/gyrateFile"
#raw_data_ic = "/home/holmes/Desktop/Finished_Deletable/C4X_11162/project/structure/Round_86/SubRound_86_1/currentIC"
#raw_data_sdf_angle = "Crystal_sdf/C4X_11162_test2.sdf"

#out_put_file = "Torsions_out.txt"

###

###
# Testing
# raw_data_ic = "Crystal_sdf/currentIC"
# raw_data_sdf_angle = "Crystal_sdf/C4X_11162_test2.sdf"
#gyrate_file_location = "Crystal_sdf/gyrateFile_C4X_11162"
###

##
#Torsion_change_list = "/home/holmes/Desktop/Methods folder/Project 32/Test_folder/Project 32/Torsions.txt"
##

Torsion_change_list = angle_extractor_v4.main(raw_data_ic, raw_data_sdf_angle,
                                       gyrate_file_location, [], [])

file_out = open(out_put_file, 'w')

try:
    file_out.writelines(Torsion_change_list)
except FileNotFoundError:
    print("File cannot be found")
finally:
    file_out.close()


print("Script has run, \n\n\nGoodbye!!\n\n")
