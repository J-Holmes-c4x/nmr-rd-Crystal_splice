# -*- coding: utf-8 -*-
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
#import importlib
import Combined_all_v2
import angle_extractor_v4

#importlib.reload(Combined_all_v2)
#importlib.reload(angle_extractor_v4)


##############
parser = argparse.ArgumentParser(description="Goodday!\n\nThis is a gyrate editor script! \nThis script has been written to allow the comparsion of C4X models with crystal modes however before using it you must make some precauision, firstly back up your project, Although its undergone some rudimentary testing, its still may break your project. If this is done then please input parameters consistent with the list below, and run this script in the root directory of your project, i.e. /data/C4X_xxx/. if you only have the torsion list of the structure which you want to use, the please use the '-l' command")

parser.add_argument("gyrate_file_location", type=str,
                    help = "Please put the gyrate file location, relvent to your current location")

parser.add_argument("raw_ic_file", type=str,
                    help = "Please input the location of the currenIC file related to the gyrate file you wish to use, the list of torsion which contain the angle which you want")

parser.add_argument("crystal_sdf_file", type=str,
                    help = "Please input the location of the crystal file you wish to use")


args = parser.parse_args()

print(args.gyrate_file_location)
print(args.raw_ic_file)
print(args.crystal_sdf_file)

gyrate_file_location = args.gyrate_file_location
raw_data_ic = args.raw_ic_file
raw_data_sdf_angle = args.crystal_sdf_file


###############

###
# Testing
#gyrate_file_location= "/home/holmes/Desktop/Finished_Deletable/C4X_11162/project/structure/Round_86/SubRound_86_1/gyrateFile"
#raw_data_ic = "/home/holmes/Desktop/Finished_Deletable/C4X_11162/project/structure/Round_86/SubRound_86_1/currentIC"
#raw_data_sdf_angle = "Crystal_sdf/C4X_11162_test2.sdf"
###

###
# Testing
#raw_data_ic = "test_data/Control/currentIC"
#raw_data_sdf_angle = "test_data/Control/sim_bio_active_11_1_fixed.sdf"
#gyrate_file_location = "test_data/Control/gyrateFile"
###

##
#Torsion_change_list = "/home/holmes/Desktop/Methods folder/Project 32/Test_folder/Project 32/Torsions.txt"
##

Torsion_change_list = angle_extractor_v4.main(raw_data_ic, raw_data_sdf_angle,
                                       gyrate_file_location, [], [])


class running_script(object):
    """
    This is the main object needed to change the gyrate gile
    """
    def __init__(self):
        self.list_of_torsion = []
        self.input_ready_torsion = []
        self.count = []

    """
    Getters and setters
    """

    def get_list_of_torsion(self):
        return self.list_of_torsion

    def get_input_ready_torsion(self):
        return self.input_ready_torsion

    def set_list_of_torsion(self, a_list_of_torsion):
        if "\n----\n" not in a_list_of_torsion:
            print("\n**\nTorsion list does not contain torsion markers\n*\n")
            return None
        if len(a_list_of_torsion) == 0:
            print("\n**\nTorsion list is empty, or the SDF\n**\n")
            return None
        self.list_of_torsion = a_list_of_torsion

    def set_input_ready_torsions(self, a_input_ready_torsions):
        self.input_ready_torsion = a_input_ready_torsions


#####
    def opener(self, a_file_name):
        """
        This is a file opener
        @param a_file_name this is the file to be opened
        """
        output_list = []
        open_file = open(a_file_name, 'r')
        output_list = open_file.readlines()
        open_file.close()
        return output_list

    def torsions_extractor(self, a_list_of_torsion):
        """
        This extract the torsion information from the data
        @param a_list_of_torsion this is the list of torsion to be added
        @return None, this set the private member var internally
        """
        extracted_list = []
        check = 0

        for element in a_list_of_torsion:
            if check == 1:
                if '--' not in element:

                    element = element.strip()
                    element = element.split(',')

                    element = [float(element[0]), float(element[1]),
                               int(element[2])]
                    assert len(element) == 3
                    extracted_list.append(element)

            if '--' in element:
                check = 1
                print(element)

        new_list = []

        for element in extracted_list:
            new_list.append(element)

        self.input_ready_torsion = new_list
        print(new_list)
        return None

    def gyrate_runner(self, a_gyrate_location, a_torsion_change_list):
        """
        This is the main function runnner, it calls the combined script and
        then runs the main fuction
        @param a_gyrate_location, current location of the gyrate_file
        @param a_torsion_change_list current location of the torsion list
        @return None the main function works on the file directly
        """
        for element in a_torsion_change_list:
            print(element[0], element[1], element[2], gyrate_file_location)
            Combined_all_v2.main_combine(element[0], element[1],
                                         element[2], a_gyrate_location)
            self.count.append(element)
        return None

a_running_script = running_script()
print(Torsion_change_list)
a_running_script.set_list_of_torsion(Torsion_change_list)

a_running_script.torsions_extractor(a_running_script.get_list_of_torsion())
a_running_script.gyrate_runner(
    gyrate_file_location, a_running_script.get_input_ready_torsion())

print("This script has run, the torsion should of been added please check")
print("****Goodbye!****")
