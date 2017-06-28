# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 12:51:15 2017
This is an angle measuring script, this will take a gyrate file, an currentIC
file, and give the angle for each torsion. This then then produce a torsion
table which can use and import for other scripts

@author: holmes
This script is now working and in the last alpha stage:
Things that need to be done:
1. minor refactoring
2. clearing up code
3. addition on of DbC

USE AT OWN RISH, IF UNSURE PLEASE SEE AJH
"""

import math


def opener(a_file_name):
    """
    This is a file opener
    @param a_file_name this file opener
    @return raw_data this is raw data output
    """

    file1 = open(a_file_name, 'r')
    raw_data = file1.readlines()
    file1.close()

    return raw_data


def writer(a_file_name, output_data):
    """
    This is a file closer
    @param a_file_name this is the file input
    @param output_data this is the file location
    """
    file1 = open(a_file_name, 'w')
    file1.writelines(output_data)
    file1.close()

####


class sdf_extractor(object):
    """
    This is a rudimentary SDF reader object, it will read the values and
    output create an object which attributes of a key value, name, connection
    matrix.
    """
    def __init__(self, a_raw_data):
        self.a_raw_data = a_raw_data
        self.a_key_values = self.key_values(self.a_raw_data)
        self.name = self.a_raw_data[0]
        self.coord = self.extract_values(self.a_raw_data, 0,
                                         self.a_key_values[0])
        self.connection = self.extract_values(
            self.a_raw_data, self.a_key_values[0], self.a_key_values[1])

        global test1
        test1 = self.coord

    def key_values(self, raw_data_1):
        """
        This method provides the key values
        @param raw_data_1 this provides the key values from the gyrate file
        @return key_values this is the key values
        """
        key_value = raw_data_1[3]
        key_value = key_value.split()
        # print(key_value)
        return key_value

    def extract_values(self, raw_data_1, start_value, end_value):
        """
        This extract the key values from the SDF
        @param raw_data_1 this extracts the atom coordinate values
        @param start_value where to start reading in the script
        @param end_value where to end reading in the script
        @return the script values
        """
        raw_data_2 = raw_data_1[4:]
        start_value = int(start_value)
        end_value = int(end_value) + int(start_value)

        new_list = raw_data_2[start_value:end_value]
        return new_list


class gyrate_extractor(object):
    """
    This is an object value, this extract the gyrate information creates an
    object with this data include,
    """
    def __init__(self, a_gyrate_file):
        self.a_gyrate_file = a_gyrate_file

        self.gyrate_dici = self.extact_torsion_data(
                                                self.a_gyrate_file, "dici")

        self.gyrate_list_key = self.extact_torsion_data(
                                            self.a_gyrate_file, "list_keys")

    def extact_torsion_data(self, a_gyrate_file_1, type_output):
        """
        This extract the torsion data from the gyrate file
        @param a_gyrate_file_1 this is the current gyrate file
        @param type_ouput this is used to explain the type of output which
        is being processed
        @return new_list this is the data in list format
        @return new_dic this is the data in a dici format
        """
        check = 0
        gyrate_dof_title = []
        gyrate_name = []
        new_dict = {}

        for element in a_gyrate_file_1:
            # print(element)
            if ("remark gyrates" in element):
                check = 1
            if (check == 1):
                if ("name" in element):
                    gyrate_dof_title.append(element.strip())

                element = element.split()
                if (len(element) > 1):
                    if (element[0] == "multigyrate"):
                        gyrate_name.append(element)
                    if (element[0] == "gyrate"):
                        gyrate_name.append(element)

        if (type_output == "list_keys"):
            # print(gyrate_name)
            new_list = []
            for element in gyrate_name:
                if (len(element) > 1):

                    if (element[0] == "multigyrate"):
                        new_list.append(element[1])

                    if (element[0] == "gyrate"):
                        new_list.append(element[1])

            # print(new_list)
            return new_list

        else:
            for number in range(len(gyrate_name)):
                assert len(gyrate_name) == len(gyrate_dof_title)

                new_key = gyrate_name[number]
                new_key = new_key[1]
                new_dict[new_key] = [gyrate_dof_title[number],
                                     gyrate_name[number]]

            return new_dict


class sbc_extractor(object):
    """
    This is a sbc_extractor, this uses to extract data from a SBC file
    from maestro. The main reason for this object is to provide data
    checking between this script and maestro
    """

    def __init__(self, a_sbc_file):
        self.a_sbc_file = a_sbc_file
        self.a_sbc_file_processed = self.process_sbc_method(self.a_sbc_file)

    def process_sbc_method(self, a_sbc_file_1):
        """
        This process the sbc method file
        @param a_sbc_file this is the current sbc file
        @return new_list this is the process sbc file
        """
        new_list = []

        for element in a_sbc_file_1:
            element = element.split()
            element = [element[1], element[2], element[3], element[4],
                       element[6]]

            new_list.append(element)

        return new_list

###


class ic_file_helper(object):
    """
    This is a helper class, which is called to help process the IC file.
    """
    def _init_(self):
        pass

    def ic_split_data(self, a_ic_file_list):
        """
        This splits the data into chuncks and changes their type.
        @param a_ic_file_list this is the current ic file list
        @return new_list this is the processed IC list file
        """
        new_list = []

        for element in a_ic_file_list:
            element = element.split()
            element = [int(element[0]), int(element[1]), int(element[2]),
                       int(element[3])]
            new_list.append(element)
        return new_list


####
class ic_file_sdf_container(object):
    """
    This is the icfile class
    This is the main contain for this script which contains the process SDF
    file and IC file information. In addition to this it also contains the
    SDB file information and the gyrate list
    """
    def __init__(self, a_ic_raw_data, a_raw_data_sdf_angle, a_gyrate_dici,
                 a_sbs_file, a_gyrate_list_key):
        self.a_ic_raw_data = a_ic_raw_data
        self.a_raw_data_sdf_angle = a_raw_data_sdf_angle
        self.a_gyrate_dici = a_gyrate_dici
        self.a_sbs_file = a_sbs_file
        self.a_gyrate_list_key = a_gyrate_list_key
    pass


####
class angle_measure(object):
    """
    This creates an object which measure the angle of key torsion and
    provides the correct dihedral angles.
    """

    def measure_torsion(self, a_ic_file_list, a_sdf_angle_list,
                        a_wanted_torsion):
        """
        This measures the wanted angle
        @param a_ic_file_list this is the current ic_file_list
        @param a_sdf_angle_list this is the current sdf angle list
        @return a_wanted_torsion this is the current wanted torsion
        """

        a_wanted_torsion_comps = a_ic_file_list[a_wanted_torsion-1]

        a_wanted_angle_list = []

        for element in a_wanted_torsion_comps:
            temp_list = a_sdf_angle_list[element]
            temp_list = temp_list.split()

            wanted_angle = []
            wanted_angle.append(float(temp_list[0]))
            wanted_angle.append(float(temp_list[1]))
            wanted_angle.append(float(temp_list[2]))

            # print (wanted_angle)

            a_wanted_angle_list.append(wanted_angle)

        # print(a_wanted_angle_list)

        crystal_dof_angle = []

        a = a_wanted_angle_list[0]
        b = a_wanted_angle_list[1]
        c = a_wanted_angle_list[2]
        d = a_wanted_angle_list[3]

        v1 = [(a[0]-b[0]), (a[1]-b[1]), (a[2]-b[2])]
        v2 = [(c[0]-b[0]), (c[1]-b[1]), (c[2]-b[2])]
        v3 = [(d[0]-c[0]), (d[1]-c[1]), (d[2]-c[2])]

        # print(v1)
        # print(v2)
        # v1_dot_v2 = (v1[0]*v2[0]) + (v1[1]*v2[1]) + (v1[2]*v2[2])

        def cross(a_v1, a_v2):
            """
            This provides the cross product between to vectors
            @param a_v1 this is the first vector
            @param a_v2 this is the second vector
            @return [x, y, z] this is the cross product result
            """
            x = ((a_v1[1] * a_v2[2]) - (a_v1[2] * a_v2[1]))
            y = ((a_v1[2] * a_v2[0]) - (a_v1[0] * a_v2[2]))
            z = ((a_v1[0] * a_v2[1]) - (a_v1[1] * a_v2[0]))

            return [x, y, z]

        def dot(a_v1, a_v2):
            """
            This provided the dot product result
            @param a_v1 this is the first vector
            @param a_v2 this is the second vector
            @return v1_dot_v2 this is the dot product
            """
            v1_dot_v2 = (a_v1[0]*a_v2[0])+(a_v1[1]*a_v2[1])+(a_v1[2]*a_v2[2])

            return v1_dot_v2

        v2_cross_v1 = cross(v2, v1)
        v2_cross_v3 = cross(v2, v3)
        v1_cross_v3 = cross(v1, v3)

        """
        print("This is the cross result: ", v2_cross_v1, v2_cross_v3)
        v2_cross_v1_dot_v2_cross_v3 = (v2_cross_v1[0]*v2_cross_v3[0])
        + (v2_cross_v1[1]*v2_cross_v3[1]) + (v2_cross_v1[2]*v2_cross_v3[2])
        v1_dot_v1_sq = (v2_cross_v1[0]*v2_cross_v1[0])
        + (v2_cross_v1[1]*v2_cross_v1[1]) + (v2_cross_v1[2]*v2_cross_v1[2])
        v2_dot_v2_sq = (v2_cross_v3[0]*v2_cross_v3[0])
        + (v2_cross_v3[1]*v2_cross_v3[1]) + (v2_cross_v3[2]*v2_cross_v3[2])
        """

        # print ("This is the dot product", v2_cross_v1_dot_v2_cross_v3)

        v2_dot_v2_sq = dot(v2_cross_v3, v2_cross_v3)

        v2_cross_v1_dot_v2_cross_v3 = dot(v2_cross_v1, v2_cross_v3)

        v1_dot_v1_sq = dot(v2_cross_v1, v2_cross_v1)

        v1_mag = math.sqrt(v1_dot_v1_sq)

        v2_mag = math.sqrt(v2_dot_v2_sq)

        v1_cross_v3_dot_v2 = (v1_cross_v3[0]*v2[0]) + (v1_cross_v3[1]*v2[1])
        + (v1_cross_v3[2]*v2[2])

        result = -((v2_cross_v1_dot_v2_cross_v3) / (v1_mag * v2_mag))

        """
        # print(result)
        # result = round(result, 10)

        # v1_cross_v1 = cross(v1, v2)

        # v1_cross_v2_dot_v1_cross_v2 = (v1_cross_v1[0]*v1_cross_v1[0])
            + (v1_cross_v1[1]*v1_cross_v1[1]) + (v1[2]*v2[2])

        # v2_cross_v1_mag = math.sqrt((v2_cross_v1[0]*v2_cross_v1[0])
            + (v2_cross_v1[1]*v2_cross_v1[1])
            + (v2_cross_v1[2]*v2_cross_v1[2]))

        # v2_cross_v3_mag = math.sqrt((v2_cross_v3[0]*v2_cross_v3[0])
        + (v2_cross_v3[1]*v2_cross_v3[1]) + (v2_cross_v3[2]*v2_cross_v3[2]))

        # v1_mag = math.sqrt((v1[0]*v1[0]) + (v1[1]*v1[1]) + (v1[2]*v1[2]))
        # v2_mag = math.sqrt((v2[0]*v2[0]) + (v2[1]*v2[1]) + (v2[2]*v2[2]))

        # print("This is the scalar ", v1_dot_v2)
        # print("this is the mag v1 ", v1_mag)
        # print("this s the mag v2 ",v2_mag)

        # result = (v1[0]*v2[0])+(v1[1]*v2[1])+(v1[2]*v2[2])/
        (math.sqrt((v1[0]*v1[0])+(v1[1]*v1[1])+(v1[2]+v1[2]))*
        math.sqrt((v2[0]*v2[0])+(v2[1]*v2[1])+(v2[2]+v2[2])))

        # result = (v1_dot_v2/(v1_mag*v2_mag))
        # print("this is the ressult", result)
        """

        result_1 = math.acos(result)
        result_2 = math.degrees(result_1)
        result_2 = result_2 - 180

        if (v1_cross_v3_dot_v2 > 0):
            result_2 = result_2 * -1

        # print(result_1)
        # print("this is the angle: ", result_2)

        print(a_wanted_torsion, result_2, v1_cross_v3_dot_v2,
              a_wanted_torsion_comps)
        output = [a_wanted_torsion, result_2]
        return output

####


class angle_measure_maestro(object):
        """
        This is for measure the angle using the maestro torsion information
        """

        def __init__(self, ic_file_list, gyrate_list, maestro_list,
                     gyrate_list_key):
            self.ic_file_list = ic_file_list
            self.gyrate_list = gyrate_list
            self.maestro_list = maestro_list
            self.gyrate_list_key = gyrate_list_key
            self.crystal_dof_angles = self.make_gyrate_file_list(
                self.ic_file_list, self.maestro_list, self.gyrate_list_key)

        def make_gyrate_file_list(self, a_ic_file_list, a_maestro_list,
                                  a_gyrate_list_key):
            """
            This script returns the a list of angle linked to torsion using the
            sbd file and also the gyrate file.
            @param a_ic_file_list this is the ic file list,
            @param a_maestro_list this is the maestro list
            @param a_gyrate_list this is the maestro list
            @return crystal_dof_angle this is the combined list
            """
            new_dici = {}
            for element in a_maestro_list:
                element_split = element
                element_angle = element[4]
                element_split = [(int(element[0])-1), (int(element[1])-1),
                                 (int(element[2])-1), (int(element[3])-1)]
                element_split_reverse = element_split.copy()
                element_split_reverse.reverse()

                if (element_split in a_ic_file_list):
                    tor_number_ic = a_ic_file_list.index(element_split)
                    element_split.append(element_angle)

                    new_dici[str(tor_number_ic)] = element_split

                if (element_split_reverse in a_ic_file_list):
                    tor_number_ic = a_ic_file_list.index(element_split_reverse)

                    element_split_reverse.append(element_angle)
                    new_dici[str(tor_number_ic)] = element_split_reverse

            global test_b
            test_b = new_dici

            global test_c
            test_c = a_gyrate_list_key

            crystal_dof_angle = []

            global maestro_measure

            maestro_measure = []

            # print(a_gyrate_list_key)

            counter = 0
            for element in a_gyrate_list_key:
                element_ic = (int(element))-1

                temp_result = (str(element), new_dici[(str(element_ic))])
                maestro_measure.append(temp_result)
                print(str(element), new_dici[(str(element_ic))])

                element_entry = new_dici[(str(element_ic))]
                element_entry = element_entry[-1]
                new_entry = "\n"+str(element_entry) + ", 0.0, " + str(counter)

                crystal_dof_angle.append(new_entry)
                counter = counter + 1
                pass

            return crystal_dof_angle

        def output_torsion_file(self):
            """
            This is an output function information, this takes the
            crystal_dof_angle and output them in to a torsion text.
            @return output_file this return the output file
            """
            a_crystal_dof_angles = self.crystal_dof_angles
            output_file = []
            header ="This is a list of torsion:\nPlease enter angle, jump size and torsion number between the markers\n\n----"
            output_file.append(header)
            for element in a_crystal_dof_angles:
                output_file.append(element)

            end = "\n----\n"
            output_file.append(end)

            return output_file

#######################################################


class gyrate_output(object):
    """
    This is the main measurement function, it takes a list of torsion and
    then measure the angle of them. It also output these values
    """
    def __init__(self, a_ic_raw_data, a_raw_data_sdf_angle, a_gyrate_list_key):
        self.a_ic_raw_data = a_ic_raw_data
        self.a_raw_data_sdf_angle = a_raw_data_sdf_angle
        self.a_gyrate_list_key = a_gyrate_list_key

        self.a_angle_measure = angle_measure()
        pass

    def run_angle(self, element,):
        """
        This take and element in a list and then calculated the angle
        between them. This places this directly into the data container.
        @param element this is the element list entry
        @result result this is the measured list
        """
        result = self.a_angle_measure.measure_torsion(
            self.a_ic_raw_data, self.a_raw_data_sdf_angle, element)
        return result

    def run_torsion_list(self, a_gyrate_list_key_1):
        """
        This take the a_gyrate_list_key_1 and the run the angle measurement.
        Then returns a angle list.
        @param a_gyrate_list_key_1 this is the gyrate key list
        @return new_list this is the amended gyrate list
        """
        new_list = []
        for element in a_gyrate_list_key_1:
            new_element = self.run_angle(int(element))
            new_list.append(new_element)
        return new_list

    def output(self, a_gyrate_list_key_1):
        """
        This process the angle list with and prepare it for export
        @param a_gyarte_list_key_1 this current gyrate_list key
        @return output this is the gyrate angle list ready to have its top
        and end added
        """
        global gyrate_measure

        gyrate_measure = []

        crystal_dof_angle = self.run_torsion_list(a_gyrate_list_key_1)
        output = []
        # print(a_gyrate_list_key)
        counter = 0
        for element_entry in crystal_dof_angle:
            element_entry = element_entry[-1]
            element_entry = round(element_entry, 4)  # need better precision
            new_entry = "\n"+str(element_entry) + ", 0.0, " + str(counter)

            gyrate_measure.append(new_entry)
            output.append(new_entry)

            counter = counter + 1
            pass

        return output

    def output_torsion_file(self):
        """
        This take the edited torsion file and then adds the top and end to
        it
        @return output this is the edited file
        """
        a_crystal_dof_angles = self.output(self.a_gyrate_list_key)
        output_file = []
        header ="This is a list of torsion:\nPlease enter angle, jump size and torsion number between the markers\n\n----"
        output_file.append(header)
        for element in a_crystal_dof_angles:
            output_file.append(element)

        end = "\n----\n"
        output_file.append(end)

        return output_file

# init var
# Test values
# raw_data_ic = opener("Crystal_sdf/currentIC")
# raw_data_sdf_angle = opener("Crystal_sdf/C4X_11162_test2.sdf")
# raw_gyrate_file = opener("Crystal_sdf/gyrateFile_C4X_11162")
# raw_maestro_file = opener("Crystal_sdf/torsions_2.sbc")
# output_file = "Crystal_sdf/Torsions_1.txt"


def main(raw_data_ic, raw_data_sdf_angle, raw_gyrate_file,
         raw_maestro_file, output_file):
    """
    This is the main loop used to access the this script
    @param raw_data_ic this is the raw data file
    @param raw_data_sdf_angle this is the raw sdf data
    @param raw_gyrate_fike this is the raw gyrate file
    @param raw_maestro_file this is the sbd file
    @result result1 this is the angle result
    """

    a_raw_data_ic = opener(raw_data_ic)
    a_raw_data_sdf_angle = opener(raw_data_sdf_angle)
    a_raw_gyrate_file = opener(raw_gyrate_file)
    # a_raw_maestro_file = opener(raw_maestro_file)
    a_raw_maestro_file = ""
    a_output_file = output_file

    a_sdf_extractor = sdf_extractor(a_raw_data_sdf_angle)
    a_ic_file_helper = ic_file_helper()
    a_gyrate_extractor = gyrate_extractor(a_raw_gyrate_file)
    a_sbc_extractor = sbc_extractor(a_raw_maestro_file)

    ##

    a_ic_file_sdf_container = ic_file_sdf_container(
        a_raw_data_ic, a_sdf_extractor.coord, a_gyrate_extractor.gyrate_dici,
        a_sbc_extractor.a_sbc_file_processed,
        a_gyrate_extractor.gyrate_list_key)

    a_ic_file_sdf_container.a_ic_raw_data = a_ic_file_helper.ic_split_data(a_ic_file_sdf_container.a_ic_raw_data)

    a_gyrate_output = gyrate_output(a_ic_file_sdf_container.a_ic_raw_data,
                                    a_ic_file_sdf_container.a_raw_data_sdf_angle,
                                    a_gyrate_extractor.gyrate_list_key)

    result_1 = a_gyrate_output.output_torsion_file()

    ####
    # Maestro comp
    #
    # writer(a_output_file, result_1)
    # a_angle_measure_maestro = angle_measure_maestro(a_ic_file_sdf_container.a_ic_raw_data, a_ic_file_sdf_container.a_gyrate_dici, a_ic_file_sdf_container.a_sbs_file, a_ic_file_sdf_container.a_gyrate_list_key)
    #writer("Crystal_sdf/mastro.txt", results)
    #writer("Crystal_sdf/tor1.txt", result_1)
    # results = a_angle_measure_maestro.output_torsion_file()
    ####

    return result_1

###
#testing info
#main(raw_data_ic, raw_data_sdf_angle, raw_gyrate_file,
#         raw_maestro_file, output_file)
#main(raw_data_ic, raw_data_sdf_angle, raw_gyrate_file,
#         [], output_file)
###