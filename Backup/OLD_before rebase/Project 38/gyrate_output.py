# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 16:55:32 2017

@author: holmes
"""

"""
Created on Wed Jan  4 11:56:40 2017

@author: holmes
This is the 3rd part of the crystal script, it purpose is to take
the edited data container and produced a via gyrate file from this.

@author: holmes
This script is now working and in the last alpha stage:
Things that need to be done:
1. minor refactoring
2.clearing up code
3. addition on of DbC

Please note:
This during the writing of this script, several points python programming
points have become quite clear, the main one is the that python works be a
pass by argument system for whether a values is passed by value or pass by
reference. So several function which has been written do not take this
into account as such. With this said some work is need to improve the
syntactic of quite a few function in this script
"""

####
# These create the necesay var
# tree_copy = tree.copy()
# multi_var = tree.copy()
# multi_var.pop(0)
# multi_var.pop(0)
# multi_var
# var = var_list
####

# assert a_data_container.get_var() == var
# assert a_data_container.get_tree() == tree_copy
# assert raw_data_copy == raw_data

class gyrate_output_processor_helper(object):
    """
    This is a helper object, it contains all the major functions need
    output the gyrate file
    """
    def generate_gyrate(self, a_tree, a_output_list):
        """
        this is need to create a gyrate entry from tree values
        @param a_tree this is the current tree
        @param a_output_list this is the output list for the gyrate value
        @return “” this function works on references
        """
        if (type(a_tree) == int):
            return

        for element in a_tree:

            if (type(element) == list):
                self.generate_gyrate(element, a_output_list)

                if (len(element) > 2):
                    # print(element[0])
                    a_output_list.append(element[0])
####
#    gyrate_1 = []
#    gyrate_1.append(tree_copy.pop(0))
#    gyrate_1.append(tree_copy.pop(0))
#    generate_gyrate(tree_copy, gyrate_1)
#
#    gyrate = gyrate_1  # This create the gyrate values
#
####
# these functions work to find differences between the new and old data

    def difference(self, input_list, output_list):
        """
        This is a difference function
        It works by using sets of of the input list and output list, finds
        the differences and states the changes
        @param input_list this input list, in this cause it could be the
        var or mode input list
        @param output list in this case its the list from the orginal
        data container
        @return these are the changes
        """
        if (len(input_list) == 0):
            return output_list
        else:
            changes = set(input_list) - set(output_list)
            changes = list(changes)
            return changes

    # this finds the var changes
    # var_changes = difference(var, old_var_list)
    # mode changse
    # mode_list_changes = difference(mode_list, old_mode_list)
    # multi_var_ouput_list = []

    def multi_var_ouput(self, input_list, output_list):
        """
        This creates the multi_var_output
        @param input_list this is the current full multvar list
        @param outp_list this is the trucated list, ready for export into
        he main gyrate file
        @return None this script works on references
        """
        if (type(input_list[0]) == int):
            output_list.append(input_list)
            return None
        for element in input_list:
            if (type(element) == list):
                self.multi_var_ouput(element, output_list)
        return None

# multi_var_ouput(multi_var, multi_var_ouput_list)  # finds the multimode

    def mode_ouput_export(self, input_list):
        """
        This creates the mode output
        @param this is the current mode list ready to be exported
        @return temp_list this is the edited list
        """
        temp_list = []
        for element in input_list:
            # temp_list.append("remark ideal true")
            temp_list.append('remark ideal true name "Crystal torsion"\nmode ' + str(element) + ' 2 0.5 0.1')
            # print(temp_list)
        return temp_list
# this finds the mode
# mode_ouput_list = mode_ouput_export(mode_list_changes)

    def var_export(self, input_list):
        """
        this create the var export
        @param input_list this is the current input information for the
        var export
        @temp_list this is the corrected edited list
        """
        temp_list = []
        for element in input_list:
            temp_list.append("var " + str(element) + " fix " + str(angle) +" jump " + str(jump) + " start 0.0 rotor 0\n")
        # print(temp_list)
        return temp_list

#    var_export_list = var_export(var_changes) # this finds the var changes

    #####
    def reduce_level(self, a_list):
        """
        This reduces the level of the list, as in it removes a list
        @param a_list this is the current gyrate list, which needs
        the number if list reducing
        @return temp_list this is the reduced level gyrate list
        """
        temp_list = []
        for elements in a_list:
            if (type(elements) == list):
                for element1 in elements:
                    temp_list.append(element1)
            else:
                    temp_list.append(elements)
        return temp_list

    def multi_var_ouput_export(self, multi_var_ouput_list, multi_var_list):
        """
        This produces the multi_var export
        @param multi_var_output_list this is the current
        mult_var_output_list
        @param multi_var_list this the the current multi_var_list
        @return out_put_list_1 this is the main export
        """
        new_list = []
        for element in multi_var_ouput_list:
            element = self.reduce_level(element)
            new_list.append(element)

        out_put_list = []

        for element in new_list:
            new_entry = []

            # print(element)

            for element1 in element:

                if (type(element1) == list):
                    if element1[0] in multi_var_list:
                        new_entry.append(element1[0])
                else:
                    new_entry.append(element1)

            out_put_list.append(new_entry)

        out_put_list_1 = []
        # print(out_put_list_1)
        for element in out_put_list:
            element.insert(0, "multivar")
            element_string = str(element)
            element_string = element_string.replace("[", "")
            element_string = element_string.replace("]", "")
            element_string = element_string.replace(",", "")
            element_string = element_string.replace("'", "")
            out_put_list_1.append(element_string)

        return out_put_list_1

# multi_var_ouput_list = multi_var_ouput_export(multi_var_ouput_list,
# multi_var_list)

    ####

    def reduce_level_gyrate(self, a_list):
        """
        This reduce the list again
        @param a_list this is a list of gyrate
        @return temp_list this is the reduced list
        """
        temp_list = []
        for elements in a_list:
            if (type(elements) == list):
                for element1 in elements:
                    temp_list.append(element1)
            else:
                    temp_list.append(elements)
        return temp_list

    # print(tree_1)

#    gyrate = []

    def gyrate_generate(self, a_tree, level):
        """
        This generates the gyrate information
        @param a_tree this is the current tree
        @param level this argument is not used this will be removed
        @return this produces a list of number for each gyrate value
        """
        temp_list = []
        for element in a_tree:

            if(type(element) == list):
                # print(element[0])
                temp_list.append(element[0])
            else:
                # print(element)
                temp_list.append(element)
            pass
        # print(temp_list)
        # a_tree = temp_list
        return temp_list

    def gyrate_generate_bimode(self, a_tree, level, out_put):
        """
        This generate the bimode tree
        @param a_tree this is the current tree
        @param level this produces the leve which is needed
        @param out_put this is the gyrate level changed
        @return “” this script works on references
        """
        # temp_list = []

        for element in a_tree:

            if(type(element) == list):
                self.gyrate_generate_bimode(element, level, out_put)

            else:
                # print(element)
                out_put.append(element)
            pass
        # print(temp_list)
        # return temp_list

    def unimode_fix(self, a_type_tor, a_gyrate, a_gyrate_tree):
        """
        This convert unimode to bimodes
        @param a_type_tor this is the current gyrate values
        @param a_gyrate this is the gyrate
        @param a_gyrate_tree this is the current gyrate tree
        @return a_gyrate the changed gyrate value
        """
        if (a_type_tor == "gyrate"):
            a_gyrate = []
            # test9 = a_gyrate
            self.gyrate_generate_bimode(a_gyrate_tree, 0, a_gyrate)
            return a_gyrate  # need to be tested
        else:
            a_gyrate = self.gyrate_generate(a_gyrate_tree, 0)
            return a_gyrate

####
#    gyrate_tree = tree.copy()
#    gyrate_tree = reduce_level_gyrate(gyrate_tree)
#
#    if (type_tor == "gyrate"):
#
#        gyrate = []
#        gyrate_generate_bimode(gyrate_tree, 0, gyrate)
#
#    else:
#        gyrate = gyrate_generate(gyrate_tree, 0)
####

class gyrate_output_processor(object):
    """
    This class is effectively a container for for process gyrate data
    ready to be exported into a gyrate file
    """
    def __init__(self, a_tree, a_var):
        self.a_tree = a_tree
        self.var = a_var

        self.var_changes = []
        self.mode_list_changes = []
        self.var_export_list = []
        self.mode_ouput_list = []

        # These create the necesay var
        self.tree_copy = self.a_tree.copy()
        self.gyrate_tree = self.a_tree.copy()

        # multi_var
        # var = var_list

        self.gyrate_1 = []
        self.multi_var_ouput_list = []
        self.gyrate = []

        # gyrate_1 = []
        self.gyrate_1.append(self.tree_copy.pop(0))
        self.gyrate_1.append(self.tree_copy.pop(0))

        # self.generate_gyrate(tree_copy, gyrate_1)

        self.gyrate = self.gyrate_1  # This create the gyrate values

        # getter and setters

    """
    Getters
    Here is a list of getting and setter, the general format used for
    getters and settes are:

    get_xxx
    @return self.xxx the private member variable

    set_xxx
    @param a_xxxx the new variable
    @return this return nothing
    """

    def set_a_tree(self, a_tree_1):
        self.a_tree = a_tree_1
        return

    def set_var(self, a_set_var):
        self.var = a_set_var
        return

    def set_var_changes(self, a_var_changes):
        self.var_changes = a_var_changes
        return

    def set_mode_list_changes(self, a_mode_list_changes):
        self.mode_list_changes = a_mode_list_changes
        return

    def set_var_export_list(self, a_var_export_list):
        self.var_export_list = a_var_export_list
        return

    def set_tree_copy(self, a_tree_copy):
        self.tree_copy = a_tree_copy
        return

    def set_gyrate_tree(self, a_gyrate_tree):
        self.gyrate_tree = a_gyrate_tree
        return

    def set_gyrate_1(self, a_gyrate_1):
        self.gyrate_1 = a_gyrate_1
        return

    def set_multi_var_output_list(self, a_multi_var_output_list):
        self.multi_var_ouput_list = a_multi_var_output_list
        return

    def set_gyrate(self, a_gyrate):
        self.gyrate = a_gyrate
        return

    def set_mode_ouput_list(self, a_mode_ouput_list):
        self.mode_ouput_list = a_mode_ouput_list
        return

    def get_a_tree(self):
        return self.a_tree

    def get_var(self):
        return self.var

    def get_var_changes(self):
        return self.var_changes

    def get_mode_list_changes(self):
        return self.mode_list_changes

    def get_var_export_list(self):
        return self.var_export_list

    def get_tree_copy(self):
        return self.tree_copy

    def get_gyrate_tree(self):
        return self.gyrate_tree

    def get_gyrate_1(self):
        return self.gyrate_1

    def get_multi_var_output_list(self):
        return self.multi_var_ouput_list

    def get_gyrate(self):
        return self.gyrate

    def get_mode_ouput_list(self):
        return self.mode_ouput_list

######
# This is the gyrate output processor helper instance
a_gyrate_output_processor_helper = gyrate_output_processor_helper()

# This is the method calls for this object

a_gyrate_output_processor = gyrate_output_processor(
                                            a_data_container.get_tree(),
                                            a_data_container.get_var())

# a_gyrate_output_processor.set_gyrate_1(
# a_gyrate_output_processor_helper.generate_gyrate(
#                            a_gyrate_output_processor.tree_copy(),
#                            a_gyrate_output_processor.get_gyrate_1()))

a_gyrate_output_processor_helper.generate_gyrate(
                                a_gyrate_output_processor.get_tree_copy(),
                                a_gyrate_output_processor.get_gyrate_1())

# generate_gyrate(tree_copy, gyrate_1)
# a_gyrate_output_processor.set

a_gyrate_output_processor.set_var_changes(
    a_gyrate_output_processor_helper.difference(
        a_gyrate_output_processor.get_var(),
        a_orginal_data_container.get_old_var_list()))

# var_changes = difference(var, old_var_list)  # this finds the var changes
# assert var_changes == a_gyrate_output_processor.get_var_changes()

a_gyrate_output_processor.set_mode_list_changes(
    a_gyrate_output_processor_helper.difference(
        a_data_container.get_mode(),
        a_orginal_data_container.get_old_mode_list()))

# mode_list_changes = difference(mode_list, old_mode_list)  # mode changse

# global test1
# test1 = mode_list_changes
# global test2
# test2 = a_gyrate_output_processor.get_mode_list_changes()

# assert mode_list_changes == a_gyrate_output_processor.get_mode_list_changes()

a_gyrate_output_processor_helper.multi_var_ouput(
                a_data_container.get_multi_var(),
                a_gyrate_output_processor.get_multi_var_output_list())

#        multi_var_ouput_list = []

global multi_var_ouput_list_obj_1st_pass
multi_var_ouput_list_obj_1st_pass = a_gyrate_output_processor.get_multi_var_output_list()

# multi_var_ouput(multi_var, multi_var_ouput_list)  # finds the multimode
# assert multi_var_ouput_list == a_gyrate_output_processor.get_multi_var_output_list()

a_gyrate_output_processor.set_mode_ouput_list(
    a_gyrate_output_processor_helper.mode_ouput_export(
        a_gyrate_output_processor.get_mode_list_changes()))

# this finds the mode
# mode_ouput_list = mode_ouput_export(mode_list_changes)

# assert mode_ouput_list == a_gyrate_output_processor.get_mode_ouput_list()

a_gyrate_output_processor.set_var_export_list(
    a_gyrate_output_processor_helper.var_export(
        a_gyrate_output_processor.get_var_changes()))

# var_export_list = var_export(var_changes) # this finds the var changes
# assert var_export_list == a_gyrate_output_processor.get_var_export_list()

a_gyrate_output_processor.set_multi_var_output_list(
    a_gyrate_output_processor_helper.multi_var_ouput_export(
        a_gyrate_output_processor.get_multi_var_output_list(),
        a_data_container.get_multi_var_list()))

# multi_var_ouput_list = multi_var_ouput_export(multi_var_ouput_list,
# multi_var_list)

# assert multi_var_ouput_list == a_gyrate_output_processor.get_multi_var_output_list()

# gyrate = []
# gyrate_tree = tree.copy()

a_gyrate_output_processor.set_gyrate_tree(
    a_gyrate_output_processor_helper.reduce_level_gyrate(
        a_gyrate_output_processor.get_gyrate_tree()))

# gyrate_tree = reduce_level_gyrate(gyrate_tree)
# assert gyrate_tree == a_gyrate_output_processor.get_gyrate_tree()

# global test4
# test4 = a_gyrate_output_processor.get_gyrate()
#
# a_gyrate_output_processor.set_gyrate([])
#
# global test5
# test5 = a_gyrate_output_processor.get_gyrate()
#
# global test6
# test6 = a_data_container.get_type_tor()
#
# global test8
# test8 = a_gyrate_output_processor.get_gyrate_tree()

a_gyrate_output_processor.set_gyrate(
    a_gyrate_output_processor_helper.unimode_fix(
        a_data_container.get_type_tor(),
        a_gyrate_output_processor.get_gyrate(),
        a_gyrate_output_processor.get_gyrate_tree()))

# global test1
# test1 = a_gyrate_output_processor.get_gyrate()

# this extracts the data,
# file1 = "/home/holmes/Desktop/Methods folder/Project 32/Test_folder/Project 32/gyrateFile_8"

#
class combine_gyrate_output(object):
    """
    This is the main object file, which takes the processed output file and
    the produces a gyrate file at the end of it.
    """
    def __init__(self, a_raw_data):

        self.a_raw_data = a_raw_data
        self.raw_gyrate = []
        self.raw_multi_var = []
        self.raw_var = []
        self.raw_mode = []

        self.raw_mode_names = []

        self.raw_gyrate_name = {}

        ####
        self.splitter(self.get_raw_var(), "var", "blank",
                      self.get_raw_data())
        self.splitter(self.get_raw_multi_var(), "multivar", "blank",
                      self.get_raw_data())
        self.splitter(self.get_raw_gyrate(), "gyrate", "multigyrate",
                      self.get_raw_data())
        self.splitter(self.get_raw_mode(), "mode", "blank",
                      self.get_raw_data())
        self.splitter(self.get_raw_mode_names(), "ideal", "blank",
                      self.get_raw_data())

        self.gyrate_name_splitter(self.get_raw_gyrate_name(), "gyrate",
                                  "multigyrate", self.get_raw_data())

        self.set_raw_mode(self.mode_name_jointer(self.get_raw_mode_names(),
                                                 self.get_raw_mode()))

    # getters and setters

    """
    Getters
    Here is a list of getting and setter, the general format used for getters
    and settes are:

    get_xxx
    @return self.xxx the private member variable

    set_xxx
    @param a_xxxx the new variable
    @return this return nothing
    """

    def set_raw_gyrate(self, a_raw_gyrate):
        self.raw_gyrate = a_raw_gyrate
        return

    def set_raw_multi_var(self, a_raw_multi_var):
        self.raw_multi_var = a_raw_multi_var
        return

    def set_raw_var(self, a_raw_var):
        self.raw_var = a_raw_var
        return

    def set_raw_mode(self, a_raw_mode):
        self.raw_mode = a_raw_mode
        return

    def set_raw_mode_names(self, a_raw_mode_names):
        self.raw_mode_names = a_raw_mode_names
        return

    def set_raw_gyrate_name(self, a_raw_gyrate_name):
        self.raw_gyrate_name = a_raw_gyrate_name
        return

##
    def get_raw_data(self):
        return self.a_raw_data

    def get_raw_gyrate(self):
        return self.raw_gyrate

    def get_raw_multi_var(self):
        return self.raw_multi_var

    def get_raw_var(self):
        return self.raw_var

    def get_raw_mode(self):
        return self.raw_mode

    def get_raw_mode_names(self):
        return self.raw_mode_names

    def get_raw_gyrate_name(self):
        return self.raw_gyrate_name

    # class methods

    def splitter(self, a_list, keyword, keyword_2, a_raw_data):
        """
        this splits the data
        @param a_list this is a list of data to get information from the
        raw file
        @param keyword this is the first keyword to be looking form
        @param keyword this the second keywork to be looking for
        @param a_raw_data this is data from the raw file
        @return "" this works on references
        """
        for element in a_raw_data:
            element_split = element.split()
            if keyword in element_split:
                # print(element)
                a_list.append(element.strip())
            if keyword_2 in element_split:
                # print(element)
                a_list.append(element.strip())
####
#    splitter(raw_var, "var", "blank", raw_data)
#    splitter(raw_multi_var, "multivar", "blank", raw_data)
#    splitter(raw_gyrate, "gyrate", "multigyrate", raw_data)
#    splitter(raw_mode, "mode", "blank", raw_data)
#    splitter(raw_mode_names, "ideal", "blank", raw_data)
#####

####
#    raw_var = raw_var + var_export_list
#    raw_multi_var = multi_var_ouput_list
####

    def gyrate_name_splitter(self, a_dici, keyword, keyword_2, a_raw_data):
        """
        This splits the data
        @param a_dici this is the input data for the a_dici,
        @param keywork this is the first key word to be looked for
        @param a_raw_data this is the raw data which is being examined
        @return “” this works on references
        """

        for element_number in range(len(a_raw_data)):
            element = a_raw_data[element_number]

            element_split = element.split()

            if keyword in element_split:
                # print(element)
                # print(a_raw_data[element_number-1])
                new_value = a_raw_data[element_number-1]

                a_dici[(element_split[1])] = new_value.strip()

            if keyword_2 in element_split:
                # print(element)
                # print(a_raw_data[element_number-1])
                new_value = a_raw_data[element_number-1]

                a_dici[(element_split[1])] = new_value.strip()

#    raw_gyrate_name = {}
#    gyrate_name_splitter(raw_gyrate_name, "gyrate", "multigyrate",
#    raw_data)

    def mode_name_jointer(self, a_raw_mode_names, a_raw_mode):
        """
        This joints the names correctly
        @param a_raw_mode_names this is a list of raw mode names
        @param a_raw_mode this is the list of raw modes
        @return new_list this is a new list containing the amended list
        """
        assert len(a_raw_mode_names) == len(a_raw_mode)
        new_list = []

        for number in range(len(a_raw_mode)):
            new_element = str(a_raw_mode_names[number]) + "\n" + str(a_raw_mode[number])
            new_list.append(new_element)

        return new_list

#    raw_mode = mode_name_jointer(raw_mode_names, raw_mode)

#    raw_mode = raw_mode + mode_ouput_list

    def gyrate_number_update(self, a_gyrate_entry, a_var_list):
        """
        This updates the gyrate numbering system
        @param a_gyrate_entry this is the gyrate entry value
        @param a_var_list this is the current var list
        @return temp_list this updates the main list of gyrate values
        """
        temp_list = a_gyrate_entry[2:]
        print(temp_list)
        for number in range(len(temp_list)):

            element = temp_list[number]
            element = int(element)

            if (element not in a_var_list):
                element = element + 1
                temp_list[number] = str(element)

            if (element == a_var_list[-1]):
                element = element + 1
                temp_list[number] = str(element)

        temp_list.insert(0, a_gyrate_entry[1])
        temp_list.insert(0, a_gyrate_entry[0])

        print(temp_list)

        return temp_list

        pass


    def gyrate_update(self, input_list, a_raw_data, a_var_list):
        """
        This update the values within the gyrate file
        @param input_list this is the input list of the gyrate
        @param a_raw_data this is the raw data list
        @param a_var_list this is this is the raw var list
        @return “” this is works on references
        """
        print(input_list)
        print(a_raw_data)
        torsion_number = str(input_list[0])
        print(torsion_number)
        iter_list = a_raw_data

        for number in range(len(iter_list)):

            entry = iter_list[number]
            entry = entry.split()
            print(entry)

            if (entry[0] == "multigyrate"):
                entry = self.gyrate_number_update(entry, a_var_list)
                temp_string = ""

                for element in entry:
                    temp_string = temp_string + str(element) + " "
                    # print(entry)

                print(temp_string)
                a_raw_data[number] = temp_string

            if (entry[1] == torsion_number):
                temp_string = "multigyrate"

                for element in input_list:
                    temp_string = temp_string + " " + str(element)

                a_raw_data[number] = temp_string

    def join_string(self, method_1, method_2):
        """
        This is a string based method for fixing   for joining reference
        list. This is not currently in use.
        @param method_1 this is the first linked list
        @param method_2 this is the second linked list
        @return this is the joined list
        """
        temp1 = method_1.copy()
        temp2 = method_2.copy()
        temp1_2 = temp1 + temp2

        global test1
        test1 = temp1_2
        return temp1_2

    def gyrate_upate_names(self, a_gyrate, a_raw_gyrate_name):
        """
        This function updates the gyrates name information
        @a_gyrate this is a gyrate list which is being updates the gyrate
        names
        @ a_raw_gyrate_name this is the list of names which are being
        updated
        @return this is the list of gyrate elements being updated
        """
        new_list = []

        for element in a_gyrate:
            element_split = element.split()
            # print(raw_gyrate_name[1])
            # print(element_split)
            tor_number = element_split[1]
            new_list.append(a_raw_gyrate_name[tor_number])
            new_list.append(element)

        # print(new_list)
        # a_gyrate = new_list
        return new_list

    def export_update(self, a_new_gyrate_file):
        new_list = []
        for element in a_new_gyrate_file:
                element = str(element)+"\n"
                new_list.append(element)
        return new_list

####
# out of loop
# gyrate_file = open(file1, 'r')
# raw_data = gyrate_file.readlines()
# gyrate_file.close()
####

# This is the instance for a  combine gyrate output

a_combine_gyrate_output = combine_gyrate_output(raw_data)

a_combine_gyrate_output.set_raw_var(
    a_combine_gyrate_output.get_raw_var() +
    a_gyrate_output_processor.get_var_export_list())

#    raw_var = raw_var + var_export_list

# assert raw_var == a_combine_gyrate_output.get_raw_var()

a_combine_gyrate_output.set_raw_multi_var(
    a_gyrate_output_processor.get_multi_var_output_list())

#    raw_multi_var = multi_var_ouput_list

# assert raw_multi_var == a_combine_gyrate_output.get_raw_multi_var()

# a_combine_gyrate_output.set_raw_mode(
#    a_combine_gyrate_output.join_string(
#        a_combine_gyrate_output.get_raw_mode(),
#        a_gyrate_output_processor.get_mode_ouput_list()))

a_combine_gyrate_output.set_raw_mode(
        a_combine_gyrate_output.get_raw_mode() +
        a_gyrate_output_processor.get_mode_ouput_list())

# a_combine_gyrate_output.set_raw_mode(
#        a_combine_gyrate_output.get_raw_mode().copy() +
#        a_gyrate_output_processor.get_mode_ouput_list().copy())

# a_combine_gyrate_output.set_raw_mode(
#    a_combine_gyrate_output.get_raw_mode() +
#    a_gyrate_output_processor.get_mode_ouput_list)

#    raw_mode = raw_mode + mode_ouput_list

# assert raw_mode == a_combine_gyrate_output.get_raw_mode

a_combine_gyrate_output.gyrate_update(
    a_gyrate_output_processor.get_gyrate(),
    a_combine_gyrate_output.get_raw_gyrate(),
    a_gyrate_output_processor.get_var())  # this might not be right

#    gyrate_update(gyrate, raw_gyrate, var_list)

# assert raw_gyrate == a_combine_gyrate_output.get_raw_gyrate()

# these are the method calls

a_combine_gyrate_output.set_raw_gyrate(
    a_combine_gyrate_output.gyrate_upate_names(
        a_combine_gyrate_output.get_raw_gyrate(),
        a_combine_gyrate_output.get_raw_gyrate_name()))

####

class gyrate_output(object):
    """
    This is the main gyrate output class this take all of the gyrate
    information then produced a valid gyrate file.
    """
    def __init__(self):
        self.export = []
        self.export_new_line = []

    """
    Getters
    Here is a list of getting and setter, the general format used for
    getters
    and settes are:

    get_xxx
    @return self.xxx the private member variable

    set_xxx
    @param a_xxxx the new variable
    @return this return nothing
    """

    def set_export(self, a_export):
        self.export = a_export

    def set_export_new_line(self, a_export_new_line):
        self.export_new_line = a_export_new_line

    def get_export(self):
        return self.export

    def get_export_new_line(self):
        return self.export_new_line

####
#    def gyrate_upate_names(a_gyrate):
#        """
#        This function updates the gyrates name information
#        """
#        new_list = []
#
#        for element in a_gyrate:
#            element_split = element.split()
#            # print(raw_gyrate_name[1])
#            # print(element_split)
#            tor_number = element_split[1]
#            new_list.append(raw_gyrate_name[tor_number])
#            new_list.append(element)
#
#        # print(new_list)
#        # a_gyrate = new_list
#        return new_list
#
#    raw_gyrate = gyrate_upate_names(raw_gyrate)
####

    def build_gyrate_file(self, a_raw_var, a_raw_mode, a_raw_multi_var,
                          a_raw_gyrate):
        """
        This builds the gyrate file
        @param a_raw_var this is the raw var data
        @param this is the current raw mode
        @param this is the current raw multi var
        @param this is the raw gyrate
        @return this is the newly ready gyrate file, ready for export
        """
        a_new_gyrate_file = []
        a_new_gyrate_file.append("variables:\n")
        a_new_gyrate_file = a_new_gyrate_file + a_raw_var
        a_new_gyrate_file.append("endsection\n")

        a_new_gyrate_file.append("probabilities:\n")
        a_new_gyrate_file = a_new_gyrate_file + a_raw_mode
        a_new_gyrate_file.append("\nendsection\n")

        a_new_gyrate_file.append("variables2:\n")
        a_new_gyrate_file = a_new_gyrate_file + a_raw_multi_var
        a_new_gyrate_file.append("\nendsection\n")

        a_new_gyrate_file.append("dynamics:\n")
        a_new_gyrate_file.append("remark ring\n")

        a_new_gyrate_file.append("remark gyrates")
        a_new_gyrate_file = a_new_gyrate_file + a_raw_gyrate
        a_new_gyrate_file.append("\nendsection")

        return a_new_gyrate_file

    # new_gyrate_file = build_gyrate_file()
    # export_file = []

# This is the gyrate output instance

a_gyrate_output = gyrate_output()

a_gyrate_output.set_export(
    a_gyrate_output.build_gyrate_file(
                          a_combine_gyrate_output.get_raw_var(),
                          a_combine_gyrate_output.get_raw_mode(),
                          a_combine_gyrate_output.get_raw_multi_var(),
                          a_combine_gyrate_output.get_raw_gyrate()))

a_gyrate_output.set_export_new_line(
    a_combine_gyrate_output.export_update(a_gyrate_output.get_export()))

export_file1 = a_gyrate_output.get_export_new_line()

out_file = open("/home/holmes/Desktop/Methods folder/Project 32/Test_folder/Project 32/gyrate_test/Out_file.txt", 'w')

#out_file.writelines(export_file)
out_file.writelines(export_file1)
out_file.close()

####
# out_file = open("/home/holmes/Desktop/Methods folder/Project 32/Test_folder/Project 32/gyrate_test/Out_file.txt", 'w')
#
# out_file.writelines(export_file)
# out_file.close()
####

# This is the final method call for the gyrate output

def gyrate_out():
    """
    This outputs the gyrate file
    """
    out_file = open(file1, 'w')
#    out_file.writelines(export_file)
    out_file.writelines(a_gyrate_output.get_export_new_line())
    out_file.close()

gyrate_out()
