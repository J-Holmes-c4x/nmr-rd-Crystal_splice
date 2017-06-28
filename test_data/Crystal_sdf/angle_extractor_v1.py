# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 12:51:15 2017

@author: holmes
"""

import math
####
#globle test_var


def opener(a_file_name):
    """
    This is a file opener
    """

    file1 = open(a_file_name, 'r')
    raw_data = file1.readlines()
    file1.close()

    return raw_data

def writer(a_file_name, output_data):
    """
    This is a file closer
    """
    file1 = open(a_file_name, 'w')
    file1.writelines(output_data)
    file1.close()


raw_data_ic = opener("currentIC")
raw_data_sdf_angle = opener("C4X_11162_test1.sdf")
raw_gyrate_file = opener("gyrateFile_C4X_11162")
raw_maestro_file = opener("torsions_1.sbc")

####


class sdf_extractor(object):
    """

    """
    def __init__(self, a_raw_data):
        self.a_raw_data = a_raw_data
        self.a_key_values = self.key_values(self.a_raw_data)
        self.name = self.a_raw_data[0]
        self.coord = self.extract_values(self.a_raw_data, 0, self.a_key_values[0])
        self.connection = self.extract_values(self.a_raw_data, self.a_key_values[0], self.a_key_values[1])

        global test1
        test1 = self.coord

    def key_values(self, raw_data_1):
        """

        """
        key_value = raw_data_1[3]
        key_value = key_value.split()
        # print(key_value)
        return key_value

    def extract_values(self, raw_data_1, start_value, end_value):
        """

        """
        raw_data_2 = raw_data_1[4:]
        start_value = int(start_value)
        end_value = int(end_value) + int(start_value)

        new_list = raw_data_2[start_value:end_value]
        return new_list

class gyrate_extractor(object):
    """

    """
    def __init__(self,a_gyrate_file):
        self.a_gyrate_file = a_gyrate_file

        self.gyrate_dici = self.extact_torsion_data(self.a_gyrate_file, "dici")
        self.gyrate_list_key = self.extact_torsion_data(self.a_gyrate_file, "list_keys")

    def extact_torsion_data(self, a_gyrate_file_1, type_output):

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
            new_list  = []
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
                new_dict[new_key] = [ gyrate_dof_title[number], gyrate_name[number]]

            return new_dict

class sbc_extractor(object):
    """

    """
    def __init__(self, a_sbc_file):

        self.a_sbc_file = a_sbc_file
        self.a_sbc_file_processed = self.process_sbc_method(self.a_sbc_file)
        pass


    def process_sbc_method(self, a_sbc_file_1):
        new_list = []

        for element in a_sbc_file_1:
            element = element.split()
            element = [element[1], element[2], element[3], element[4], element[6]]
            new_list.append(element)

        return new_list

###

class ic_file_helper(object):
    """
    this is a helper class
    """
    def _init_(self):
        pass

    def ic_split_data(self, a_ic_file_list):
        """

        """
        new_list = []

        for element in a_ic_file_list:
            element = element.split()
            element = [int(element[0]), int(element[1]), int(element[2]), int(element[3])]
            new_list.append(element)
        return new_list


####
class ic_file_sdf_container(object):
    """
    This is the icfile class
    """

    def __init__(self, a_ic_raw_data, a_raw_data_sdf_angle, a_gyrate_dici, a_sbs_file, a_gyrate_list_key):
        self.a_ic_raw_data = a_ic_raw_data
        self.a_raw_data_sdf_angle = a_raw_data_sdf_angle
        self.a_gyrate_dici = a_gyrate_dici
        self.a_sbs_file = a_sbs_file
        self.a_gyrate_list_key = a_gyrate_list_key

    pass



####
class angle_measure(object):
    """

    """

    def measure_torsion(self, a_ic_file_list, a_sdf_angle_list, a_wanted_torsion):
        """

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

            #print (wanted_angle)

            a_wanted_angle_list.append(wanted_angle)

        #print(a_wanted_angle_list)

        crystal_dof_angle = []

        a = a_wanted_angle_list[0]
        b = a_wanted_angle_list[1]
        c = a_wanted_angle_list[2]
        d = a_wanted_angle_list[3]

        v1 = [(a[0]-b[0]), (a[1]-b[1]), (a[2]-b[2])]
        v2 = [(c[0]-b[0]), (c[1]-b[1]), (c[2]-b[2])]
        v3 = [(d[0]-c[0]), (d[1]-c[1]), (d[2]-c[2])]

        #print(v1)
        #print(v2)

        #v1_dot_v2 = (v1[0]*v2[0]) + (v1[1]*v2[1]) + (v1[2]*v2[2])


        def cross(a_v1, a_v2):

            x = ((a_v1[1] * a_v2[2]) - (a_v1[2] * a_v2[1]) )
            y = ((a_v1[2] * a_v2[0]) - (a_v1[0] * a_v2[2]) )
            z = ((a_v1[0] * a_v2[1]) - (a_v1[1] * a_v2[0]) )

            return [x, y, z]

        def dot(a_v1, a_v2):

            v1_dot_v2 = (a_v1[0]*a_v2[0]) + (a_v1[1]*a_v2[1]) + (a_v1[2]*a_v2[2])

            return v1_dot_v2

        v2_cross_v1 = cross(v2, v1)
        v2_cross_v3 = cross(v2, v3)

        v1_cross_v3 = cross(v1, v3)

        #print("This is the cross result: ", v2_cross_v1, v2_cross_v3)
        # v2_cross_v1_dot_v2_cross_v3 = (v2_cross_v1[0]*v2_cross_v3[0]) + (v2_cross_v1[1]*v2_cross_v3[1]) + (v2_cross_v1[2]*v2_cross_v3[2])
        # v1_dot_v1_sq = (v2_cross_v1[0]*v2_cross_v1[0]) + (v2_cross_v1[1]*v2_cross_v1[1]) + (v2_cross_v1[2]*v2_cross_v1[2])
        # v2_dot_v2_sq = (v2_cross_v3[0]*v2_cross_v3[0]) + (v2_cross_v3[1]*v2_cross_v3[1]) + (v2_cross_v3[2]*v2_cross_v3[2])


        #print ("This is the dot product", v2_cross_v1_dot_v2_cross_v3)

        v2_dot_v2_sq = dot(v2_cross_v3, v2_cross_v3)

        v2_cross_v1_dot_v2_cross_v3 = dot(v2_cross_v1, v2_cross_v3)

        v1_dot_v1_sq = dot(v2_cross_v1, v2_cross_v1)


        v1_mag = math.sqrt(v1_dot_v1_sq)

        v2_mag = math.sqrt(v2_dot_v2_sq)


        v1_cross_v3_dot_v2 = (v1_cross_v3[0]*v2[0]) + (v1_cross_v3[1]*v2[1]) + (v1_cross_v3[2]*v2[2])

        result = -((v2_cross_v1_dot_v2_cross_v3) / (v1_mag * v2_mag))

       # print(result)
        #result = round(result, 10)

       #v1_cross_v1 = cross(v1, v2)

       #v1_cross_v2_dot_v1_cross_v2 = (v1_cross_v1[0]*v1_cross_v1[0]) + (v1_cross_v1[1]*v1_cross_v1[1]) + (v1[2]*v2[2])

        #v2_cross_v1_mag = math.sqrt((v2_cross_v1[0]*v2_cross_v1[0]) + (v2_cross_v1[1]*v2_cross_v1[1]) + (v2_cross_v1[2]*v2_cross_v1[2]))

        #v2_cross_v3_mag = math.sqrt((v2_cross_v3[0]*v2_cross_v3[0]) + (v2_cross_v3[1]*v2_cross_v3[1]) + (v2_cross_v3[2]*v2_cross_v3[2]))

        #v1_mag = math.sqrt((v1[0]*v1[0]) + (v1[1]*v1[1]) + (v1[2]*v1[2]))
        #v2_mag = math.sqrt((v2[0]*v2[0]) + (v2[1]*v2[1]) + (v2[2]*v2[2]))

        # print("This is the scalar ", v1_dot_v2)
        # print("this is the mag v1 ", v1_mag)
        # print("this s the mag v2 ",v2_mag)

        #result = (v1[0]*v2[0])+(v1[1]*v2[1])+(v1[2]*v2[2])/(math.sqrt((v1[0]*v1[0])+(v1[1]*v1[1])+(v1[2]+v1[2])) * math.sqrt((v2[0]*v2[0])+(v2[1]*v2[1])+(v2[2]+v2[2])))

        #result = (v1_dot_v2/(v1_mag*v2_mag))

        #print("this is the ressult", result)
        result_1 = math.acos(result)
        result_2 = math.degrees(result_1)
        result_2 = result_2 - 180

        if (v1_cross_v3_dot_v2 > 0 ):
            result_2 = result_2 * -1

        #print(result_1)
        #print("this is the angle: ", result_2)
        print(a_wanted_torsion, result_2, v1_cross_v3_dot_v2)
        output =  [a_wanted_torsion, result_2]
        return output


####

class angle_measure_maestro(object):

    def __init__(self, ic_file_list, gyrate_list, maestro_list, gyrate_list_key):
        """
        f
        """
        self.ic_file_list = ic_file_list
        self.gyrate_list = gyrate_list
        self.maestro_list = maestro_list
        self.gyrate_list_key = gyrate_list_key
        self.crystal_dof_angles = self.make_gyrate_file_list(self.ic_file_list, self.maestro_list, self.gyrate_list_key)

        global test_b

    def make_gyrate_file_list(self, a_ic_file_list, a_maestro_list, a_gyrate_list_key):
        """
        """
        new_dici = {}
        for element in a_maestro_list:
            element_split = element
            element_angle = element[4]
            element_split = [(int(element[0])-1), (int(element[1])-1), (int(element[2])-1), (int(element[3])-1)]
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
            counter = counter +1
            pass

        return crystal_dof_angle


    def output_torsion_file(self):
        """

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
    """

    def __init__(self, a_ic_raw_data, a_raw_data_sdf_angle, a_gyrate_list_key):

        self.a_ic_raw_data = a_ic_raw_data
        self.a_raw_data_sdf_angle = a_raw_data_sdf_angle
        self.a_gyrate_list_key = a_gyrate_list_key

        self.a_angle_measure = angle_measure()

        pass

    def run_angle(self, element,):
        """
        """
        result = self.a_angle_measure.measure_torsion(
        self.a_ic_raw_data,
        self.a_raw_data_sdf_angle,
        element)
        return result


    def run_torsion_list(self, a_gyrate_list_key_1):
        """
        """
        new_list = []
        for element in a_gyrate_list_key_1:
            new_element = self.run_angle(int(element))
            new_list.append(new_element)
        return new_list

    def output(self, a_gyrate_list_key_1):
        """
        """

        global gyrate_measure

        gyrate_measure = []

        crystal_dof_angle = self.run_torsion_list(a_gyrate_list_key_1)
        output = []
        # print(a_gyrate_list_key)
        counter = 0
        for element_entry in crystal_dof_angle:
            #angle:
            element_entry = element_entry[-1]
            element_entry = round(element_entry, 4)#this need better precision
            new_entry = "\n"+str(element_entry) + ", 0.0, " + str(counter)

            gyrate_measure.append(new_entry)
            output.append(new_entry)

            counter = counter +1
            pass

        return output


    def output_torsion_file(self):
        """

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



#init var

a_sdf_extractor = sdf_extractor(raw_data_sdf_angle)
a_ic_file_helper = ic_file_helper()
a_gyrate_extractor = gyrate_extractor(raw_gyrate_file)
a_sbc_extractor = sbc_extractor(raw_maestro_file)

##

a_ic_file_sdf_container = ic_file_sdf_container(raw_data_ic, a_sdf_extractor.coord, a_gyrate_extractor.gyrate_dici, a_sbc_extractor.a_sbc_file_processed, a_gyrate_extractor.gyrate_list_key)

a_ic_file_sdf_container.a_ic_raw_data = a_ic_file_helper.ic_split_data(a_ic_file_sdf_container.a_ic_raw_data)

##
# speak to mike
#a_angle_measure = angle_measure()
#
#
#def run_angle(element):
#    a_angle_measure.measure_torsion(
#    a_ic_file_sdf_container.a_ic_raw_data,
#    a_ic_file_sdf_container.a_raw_data_sdf_angle,
#    element
#    )
#
#    return
#
#for element in a_ic_file_sdf_container.a_gyrate_list_key:
#
#    run_angle(int(element))
####

a_gyrate_output = gyrate_output(a_ic_file_sdf_container.a_ic_raw_data, a_ic_file_sdf_container.a_raw_data_sdf_angle, a_gyrate_extractor.gyrate_list_key)

result_1 = a_gyrate_output.output_torsion_file()
#
a_angle_measure_maestro = angle_measure_maestro(a_ic_file_sdf_container.a_ic_raw_data, a_ic_file_sdf_container.a_gyrate_dici, a_ic_file_sdf_container.a_sbs_file, a_ic_file_sdf_container.a_gyrate_list_key)

results = a_angle_measure_maestro.output_torsion_file()

a_writer = writer("Torsions.txt", result_1)
##

#for element in result_1:
#    print(element)


#test1_ic_file = a_ic_file_sdf_container.a_ic_raw_data
#test2_sdf_angle = a_ic_file_sdf_container.a_raw_data_sdf_angle
#test3_maestro = a_ic_file_sdf_container.a_sbs_file
#test4_gyrate_dici = a_ic_file_sdf_container.a_gyrate_dici
#test5_gyrate_list_key = a_gyrate_extractor.gyrate_list_key

#####
#class angle_measure(object):
#    """
#
#    """
#    def torsion_angles(self, a_wanted_torsion_dici, a_angle_list, a_torsion_list):
#
#        assert type(a_wanted_torsion_dici) == dict
#        assert type(a_angle_list) == list
#        assert type(a_torsion_list) == list
#
#
#        list_of_wanted_torsions = sorted(a_wanted_torsion_dici.keys())
#
#        global test4
#        test4 = list_of_wanted_torsions
#
#        a_wanted_torsion = int(list_of_wanted_torsions[19])
#
#        """
#        Notes the torsion list is one down as the torsion and
#        angle list starts at 0
#        """
#
#        a_wanted_torsion_list = a_torsion_list[a_wanted_torsion-1]
#
#        print (a_wanted_torsion_list)
#        a_wanted_angle_list = []
#
#        for element in a_wanted_torsion_list:
#            a_wanted_angle = a_angle_list[element]
#            a_wanted_angle = a_wanted_angle.split()
#
#            assert len(a_wanted_angle) == 10
#
#            a_wanted_angle = [float(a_wanted_angle[0]), float(a_wanted_angle[1]), float(a_wanted_angle[2]) ]
#            a_wanted_angle_list.append(a_wanted_angle)
#
#        for element in a_wanted_angle_list:
#            print(element)
#
#        print("this is the wanted angle", a_wanted_angle_list)
#
#        a = a_wanted_angle_list[0]
#        b = a_wanted_angle_list[1]
#        c = a_wanted_angle_list[2]
#        d = a_wanted_angle_list[3]
#
#        v1 = [(b[0]-a[0]), (b[1]-a[1]), (b[2]-a[2])]
#        v2 = [(d[0]-c[0]), (d[1]-c[1]), (d[2]-c[2])]
#
#        print(v1)
#        print(v2)
#
#        v1_dot_v2 = (v1[0]*v2[0]) + (v1[1]*v2[1]) + (v1[2]*v2[2])
#        v1_mag = math.sqrt((v1[0]*v1[0]) + (v1[1]*v1[1]) + (v1[2]*v1[2]))
#        v2_mag = math.sqrt((v2[0]*v2[0]) + (v2[1]*v2[1]) + (v2[2]*v2[2]))
#
#        print(v1_dot_v2)
#        print(v1_mag)
#        print(v2_mag)
#
#        #result = (v1[0]*v2[0])+(v1[1]*v2[1])+(v1[2]*v2[2])/(math.sqrt((v1[0]*v1[0])+(v1[1]*v1[1])+(v1[2]+v1[2])) * math.sqrt((v2[0]*v2[0])+(v2[1]*v2[1])+(v2[2]+v2[2])))
#
#        result = (v1_dot_v2/(v1_mag*v2_mag))
#        print(result)
#
#        result_1 = math.cos(result)
#        result_2 = math.degrees(result_1)
#        print(result_1)
#        print("this is the angle ", result_2)
#
#####

#a_angle_measure = angle_measure()
#
#
#def run_angle(element):
#    a_angle_measure.measure_torsion(
#    a_ic_file_sdf_container.a_ic_raw_data,
#    a_gyrate_extractor.gyrate_dici,
#    a_ic_file_sdf_container.a_gyrate_list_key,
#    a_ic_file_sdf_container.a_raw_data_sdf_angle,
#    element
#    )
#
#    return
#
#for element in a_ic_file_sdf_container.a_gyrate_list_key:
#
#    run_angle(int(element))
