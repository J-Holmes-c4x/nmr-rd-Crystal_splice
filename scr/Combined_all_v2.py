# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:47:26 2017
This is the main script for the addition of torsion script, this script this
made up of 3 parts, the tree builder, the addition of mode, and the gyrate
out put. A description of these is given at the beginning of each section.
@author: holmes
"""

#################
#
################


def main_combine(angle, jump, tor_number, gyrate_local):
    file1 = gyrate_local
    """
    Created on Tue Jan  3 10:55:28 2017
    tree builder
    This is 1st part of the crystal script. The scripts purpose is two fold, it
    sets up key environmental variables, need in later scripts, it creates a
    gyrate processor object, which process the initial  gyrate and places the
    process data into data container. It also creates an object which
    calculates a tree structure. Which is also placed in a data container
    @author: holmes
    This script is now working and in the last alpha stage:
    Things that need to be done:
    1. minor refactoring
    2.clearing up code
    3. addition on of DbC

    USE AT OWN RISH, IF UNSURE PLEASE SEE AJH
    """
    # imports file_data
    ####
    # file1= "/home/holmes/Desktop/Finished_Deletable/C4X_11162/project/structure/Round_86/SubRound_86_1/gyrateFile"
    # Angle and jump values
    # angle = 180
    # jump = 0.0
    # tor_number = 12
    #
    # Get the raw data from gyrate file
    gyrate_file = open(file1, 'r')
    raw_data = gyrate_file.readlines()
    gyrate_file.close()
    #
    # raw_data_copy = raw_data.copy()

    class gyrate_file_processor(object):
        """
        This is a processor object, designed to take the gyrate file extract
        key values which is needs to work with.
        @para a_raw_data  This is the raw data from the data file
        """
        def __init__(self, a_raw_data):
            """
            Object constructor
            this initialised the a collect of object variables, some of which
            are returned from member functions, these are: self.raw_data,
            self.raw_gyrate,  self.raw_multi_var, self.raw_var, self.raw_mode,
            which are all from the gyrate data.

            @param a_raw_data

            """
            self.raw_data = a_raw_data
            self.raw_gyrate = self.splitter("gyrate", "multigyrate",
                                            self.raw_data)
            self.raw_multi_var = self.splitter("multivar", "blank",
                                               self.raw_data)
            self.raw_var = self.splitter("var", "blank", self.raw_data)
            self.raw_mode = self.splitter("mode", "blank", self.raw_data)

        def splitter(self, keyword, keyword_2, a_raw_data):
            """
            This break up the list using keywords, and then adds key
            information
            @param keyword first keyword looking for
            @param keyword_2 second keyword looking for
            @param a_raw_data this is the raw gyrate file
            @@return a_list a list containing the lines from the raw data
            which has either keywork1 or keywork2.
            """
            a_list = []
            for element in a_raw_data:
                element_split = element.split()
                if keyword in element_split:
                    # print (element)
                    a_list.append(element)
                if keyword_2 in element_split:
                    # print (element)
                    a_list.append(element)
            return a_list

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

        def get_raw_gyrate(self):
            return self.raw_gyrate

        def get_raw_multi_var(self):
            return self.raw_multi_var

        def get_raw_var(self):
            return self.raw_var

        def get_raw_mode(self):
            return self.raw_mode

    # This initialised the gyrate_file_processor object
    a_gyrate_file_processor = gyrate_file_processor(raw_data)

    class data_container(object):
        """
        This is the main data repository, it works to hold all the key
        variables which are going to be used in the script. The constructor
        initialised all of the key data variables to either a empty string or
        an empty list.

        There are a selection of setter and getter which allow the access of
        these variables
        """
        def __init__(self):
            self.gyrate = []
            self.multi_var = []
            self.remaining_multi_var = []
            self.multi_var_list = []
            self.var = []
            self.mode = []

            self.type_tor = ''

            self.tree = []
            self.tor = []
            self.tor_mode = []

            self.out_put_multi_var = []

            """
            Here is a list of getting and setter, the general format used for
            getters and settes are:

            get_xxx
            @return self.xxx the private member variable

            set_xxx
            @param a_xxxx the new variable
            @return this return nothing
            """

            """
            Getters
            """
        def get_gyrate(self):
            return self.gyrate

        def get_multi_var(self):
            return self.multi_var

        def get_remaining_multi_var(self):
            return self.remaining_multi_var

        def get_multi_var_list(self):
            return self.multi_var_list

        def get_var(self):
            return self.var

        def get_mode(self):
            return self.mode

        def get_type_tor(self):
            return self.type_tor

        def get_tree(self):
            return self.tree

        def get_tor(self):
            return self.tor

        def get_tor_mode(self):
            return self.tor_mode

        def get_out_put_multi_var(self):
            return self.out_put_multi_var

            """
            Setters
            """
        def set_gyrate(self, a_gyrate):
            self.gyrate = a_gyrate
            return

        def set_multi_var(self, a_multi_var):
            self.multi_var = a_multi_var
            return

        def set_remaining_multi_var(self, a_remaining_multi_var):
            self.remaining_multi_var = a_remaining_multi_var
            return

        def set_multi_var_list(self, a_multi_var_list):
            self.multi_var_list = a_multi_var_list
            return

        def set_var(self, a_var):
            self.var = a_var
            return

        def set_mode(self, a_mode):
            self.mode = a_mode
            return

        def set_type_tor(self, a_type_tor):
            self.type_tor = a_type_tor
            return

        def set_tree(self, a_tree):
            self.tree = a_tree
            return

        def set_tor(self, a_tor):
            self.tor = a_tor
            return self.tor

        def set_tor_mode(self, a_tor_mode):
            self.tor_mode = a_tor_mode
            return

        def set_out_put_multi_var(self, a_out_put_multi_var):
            self.a_out_put_multi_var = a_out_put_multi_var
            return

    #####
    # this initalised the data container

    a_data_container = data_container()

    class gyrate_contain_constructor(object):
        """
        This is an object that will act upon the gyrate_file_processor object
        and process the relevant variables before depositing them into main
        data container object
        """

        def data_splitter(self, a_list, start, end):
            """
            This splits the data into section, then exports the information
            correctly
            @param a_list this the starting list
            @param start this at what line to start processing the data file
            @param end this is at what line to end the processing the data
            file
            @return this returns the output of extracted list
            """
            output_list = []

            for element in a_list:
                # print (element)
                element_split = element.split()
                # print(element_split)

                if (end == "all"):
                    end = (len(element_split))
                    # print(end)
                new_value = element_split[start:end]
                # print(new_value)
                temp_list = []

                for each_new_value in new_value:
                    temp_list.append(int(each_new_value))
                new_value = temp_list
                # print(new_value)
                if len(new_value) == 1:
                    output_list.append(new_value[0])
                else:
                    output_list.append(new_value)

            return output_list

        def multi_var_list_gen(self, a_input_list):
            """
            This generates the information for the gyrate file

            @param a_input_list this is the list which is being worked upon
            @return new_list this is the new list with just the first element
            of the input list
            """
            new_list = []
            for element in a_input_list:
                new_list.append(element[0])

            return new_list

        def remaining_multi_var_grouper(self, a_remaining_multi_var):
            """
            Makes key values string

            @param a_remaining_multi_var this is the input list
            @return this is the return list with the second item made into
            a string type
            """
            for element in a_remaining_multi_var:
                element[1] = str(element[1])

            return a_remaining_multi_var

        def grouper_multi(self, a_tree):  # Change from tree
            """
            This groups the key values togeather

            @param a_tree this is the input tree
            @return new_list this is the new tree with key values grouped
            together
            """
            new_list = []
            for element in a_tree:  # Changed from tree
                # print (element)
                temp_element = []
                temp_element.append(element[0])
                temp_element.append(str(element[1]))
                temp_element_1 = element[2:(len(element))]
                temp_element.append(temp_element_1)
                # print (temp_element)
                new_list.append(temp_element)

            return new_list

        def torsion_number_assigment(self, a_tor_number, a_gyrate):
            """
            This function gives a list of numbers which corresponds to gyrate
            of a torsion.

            @param a_tor_number this is the torsion in question
            @param a_gyrate this is a dici which contains all gyrate keyed by
            torsion
            @return a_gyrate this returns the gyrate in question
            """
            a_gyrate = a_gyrate[a_tor_number]
            return a_gyrate

        def torsion_type_assigment(self, a_gyrate):
            """
            This assigns the torsion type for a particular torsion

            @param a_gyrate this is the gyrate who's torsion type is being
            assigned
            @return type_tor this is a string containing the type of torsion
            """
            type_tor = ''
            if len(a_gyrate) < 4:
                type_tor = "gyrate"
            else:
                type_tor = "multigyrate"

            return type_tor

        def gyrate_assigment_for_uni(self, a_gyrate):
            """
            This give the gyrate values for unimode, to be zero.

            @param a_gyrate this is the gyrate entry,
            @return a_gyrate this is the changed value
            """
            if len(a_gyrate) < 4:
                a_gyrate.insert(1, '0')

            return a_gyrate

    ###
    # This is the gyrate values

    a_gyrate_contain_constructor = gyrate_contain_constructor()

    # These set the method values for gyrate files

    a_data_container.set_var(
        a_gyrate_contain_constructor.data_splitter(
            a_gyrate_file_processor.get_raw_var(), 1, 2))

    a_data_container.set_multi_var(
        a_gyrate_contain_constructor.data_splitter(
            a_gyrate_file_processor.get_raw_multi_var(), 1, 100))

    a_data_container.set_gyrate(
        a_gyrate_contain_constructor.data_splitter(
            a_gyrate_file_processor.get_raw_gyrate(), 1, 10))

    a_data_container.set_mode(
        a_gyrate_contain_constructor.data_splitter(
            a_gyrate_file_processor.get_raw_mode(), 1, 2))

    ###
    # multi_var_list = multi_var_list_gen(multi_var)
    ###

    a_data_container.set_multi_var_list(
        a_gyrate_contain_constructor.multi_var_list_gen(
            a_data_container.get_multi_var()))
    ###
    # remaining_multi_var = multi_var.copy()
    ###

    a_data_container.set_remaining_multi_var(
        a_data_container.get_multi_var().copy())  # note this might not work

    ###
    # remaining_multi_var = remaining_multi_var_grouper(remaining_multi_var)
    ###

    a_data_container.set_remaining_multi_var(
        a_gyrate_contain_constructor.remaining_multi_var_grouper(
            a_data_container.get_remaining_multi_var()))

    a_data_container.set_multi_var(
        a_gyrate_contain_constructor.grouper_multi(
            a_data_container.get_multi_var()))

    ###
    # multi_var = grouper_multi(multi_var)
    ###

    a_data_container.set_gyrate(
        a_gyrate_contain_constructor.torsion_number_assigment(
            tor_number, a_data_container.get_gyrate()))

    ###
    # gyrate = gyrate[tor_number]
    ###

    a_data_container.set_type_tor(
        a_gyrate_contain_constructor.torsion_type_assigment(
            a_data_container.get_gyrate()))

    a_data_container.set_gyrate(
        a_gyrate_contain_constructor.gyrate_assigment_for_uni(
            a_data_container.get_gyrate()))

    class tree_builder(object):
        """
        This is a tree class which created the main tree used to be changed,
        it works on the var, multi var and gyrate info. It take a collection
        of variables and sets them.
        """
        def __init__(self):
            self.tor = []
            self.gyrate = []
            self.tor_mode = []
            self.tree = []

        """
        Here is a list of getting and setter, the general format used for
        getters
        and settes are:

        get_xxx
        @return self.xxx the private member variable

        set_xxx
        @param a_xxxx the new variable
        @return this return nothing
        """

        """
        Setters and getters
        """

        def get_tor(self):
            return self.tor

        def get_gyrate(self):
            return self.gyrate

        def get_tor_mode(self):
            return self.tor_mode

        def get_tree(self):
            return self.tree

        def set_tor(self, a_tor):
            self.tor = a_tor

        def set_gyrate(self, a_gyrate):
            self.gyrate = a_gyrate

        def set_tree(self, a_tree):
            self.tree = a_tree

        def set_tor_mode(self, a_tor_mode):
            self.tor_mode = a_tor_mode
            return

        def tor_builder(self, a_gyrate):
            self.tor = a_gyrate.pop(0)
            self.tor_mode = a_gyrate.pop(0)
            self.gyrate = a_gyrate
            return

        def finder(self, a_tree, a_multi_var):  # this builds the tree
            """
            This takes the data from above and creates the tree

            @param a_tree this input in from the gyrate file
            @param a_multi_var this is the input from the multi_var information
            @return this will return the completed tree
            """
            temp_list = a_tree
            for entry_number in range(len(temp_list)):
                element_1 = temp_list[entry_number]
                # print (element_1)
                for element_2 in a_multi_var:
                    if element_1 in element_2:
                        # print (element_2)
                        a_tree[entry_number] = element_2
                        # print (element_2[-1])
                        self.finder(element_2[-1], a_multi_var)

            return a_tree

        def grouper(self, a_tree):
            """
            This add keep boths the libration and angles togreather

            @param a_tree this is the inpputed tree
            @return grouped_tree this is the outputted tree, with the
            libration and angles
            grouped togeather
            """
            grouped_tree = []
            # lenght_of_tree = len(tree)
            temp_value = []
            for element in a_tree:
                temp_value.append(element)
                if len(temp_value) > 1:
                    grouped_tree.append(temp_value)
                    temp_value = []
            return grouped_tree

        def first_level_tree_fix(self):
            """
            This function fixes the first level of the tree with a key
            identifying values

            This function  need to be looked at again, as it works on the
            private member variable. This should not happen.

            @return “” this function works purely on refferences.
            """
            local_tree = self.get_tree()
            local_tree.insert(0, self.get_tor())
            local_tree.insert(1, str(self.get_tor_mode()))
            self.set_tree(local_tree)

    a_tree_builder = tree_builder()

    a_tree_builder.tor_builder(a_data_container.get_gyrate())

    a_tree_builder.set_tree(
        a_tree_builder.finder(
            a_tree_builder.get_gyrate(), a_data_container.get_multi_var()))

    a_tree_builder.set_tree(
        a_tree_builder.grouper(a_tree_builder.get_tree()))

    # tree = finder(tree)
    # tree = grouper(tree)
    # print(tree)

    a_tree_builder.first_level_tree_fix()

    # tree.insert(0, tor)
    # tree.insert(1, str(tor_mode))
    # print(tree)

    a_data_container.set_tree(a_tree_builder.get_tree())
    a_data_container.set_tor(a_tree_builder.get_tor())
    a_data_container.set_tor_mode(a_tree_builder.get_tor_mode())

    # a_var_list, a_multi_var_list, a_tree, a_mode_list

    a_data_container.get_var()
    a_data_container.get_multi_var_list()
    a_data_container.get_tree()
    a_data_container.get_mode()
    a_data_container.get_multi_var_list()

    a_data_container.get_tor()

    # multi_var = out_put_multi_var.copy()

    a_data_container.get_gyrate().copy(),
    a_data_container.get_multi_var().copy(),
    a_data_container.get_mode().copy(),
    a_data_container.get_tree().copy(),
    a_data_container.get_var().copy()

    """
    Created on Tue Dec 20 11:28:41 2016
    tree implmention
    @author: holmes
    This is the 2nd part of the crystal script, it purpose is to work on the
    data container object and work to add a key mode to the torsion in
    question.
    This script is now working and in the last alpha stage:
    Things that need to be done:
    1. minor refactoring
    2.clearing up code
    3. addition on of DbC

    Please note:
    This during the writing of this script, several points python programming
    points have become quite clear, the main one is the that python works be a
    pass by argument system for whether a values is passed by value or pass by
    reference. So several function which has been written do not take this into
    account as such. With this said some work is need to improve the
    syntactic of quite a few function in this script

    USE AT OWN RISH, IF UNSURE PLEASE SEE AJH
    """
    # These are copys of variables

    class orginal_data_container(object):
        """
        This is a object which contains the remaining original value from the
        data container
        """
        def __init__(self, old_gyrate, old_multi_var, old_mode_list, old_tree,
                     old_var_list):
                            self.old_gyrate = old_gyrate
                            self.old_multi_var = old_multi_var  # repeated?
                            # self.old_var_list = old_var_list
                            self.old_mode_list = old_mode_list
                            self.old_tree = old_tree
                            self.old_var_list = old_var_list

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

        def set_old_gyrate(self, a_old_gyrate):
            self.old_gyrate = a_old_gyrate
            return

        def set_old_multi_var(self, a_old_multi_var):
            self.old_multi_var = a_old_multi_var
            return

        def set_old_mode_list(self, a_old_mode_list):
            self.old_mode_list = a_old_mode_list
            return

        def set_old_tree(self, a_old_tree):
            self.old_tree = a_old_tree
            return

        def set_old_var_list(self, a_old_var_list):
            self.old_var_list = a_old_var_list
            return

        def get_old_gyrate(self):
            return self.old_gyrate

        def get_old_multi_var(self):
            return self.old_multi_var

        def get_old_mode_list(self):
            return self.old_mode_list

        def get_old_tree(self):
            return self.old_tree

        def get_old_var_list(self):
            return self.old_var_list

    ###
    # a_orginal_data_container(gyrate.copy(), multi_var.copy(),
    #                         multi_var_list.copy(), mode.copy(), tree.copy(),
    #                         var.copy())
    ###
    a_orginal_data_container = orginal_data_container(
                                      a_data_container.get_gyrate().copy(),
                                      a_data_container.get_multi_var().copy(),
                                      a_data_container.get_mode().copy(),
                                      a_data_container.get_tree().copy(),
                                      a_data_container.get_var().copy())

    class add_base_branch_helper(object):
        """
        This is an object which holds all of the necessary helper functions
        which are need for the add branch object
        """
        def renamer(self, a_tree, a_number, counter):
            """
            This just updates multigyrate numbers

            @param a_tree this is the tree which is being worked upon
            @param a_number this is the level which is being looked at
            @param counter this is the level which is being avoided from being
            changed
            """
            counter = counter + 1

            if type(a_tree) != list:
                return

            for element in a_tree:
                if type(a_tree) != list:
                    return

                if (counter > 1):
                    # print (element)
                    if ((type(element) == list)):
                        # print (element)
                        if(type(a_tree[1]) != str):
                            # print(element)
                            new_value = element[0] + 1
                            element[0] = new_value
                            pass
                self.renamer(element, a_number, counter)

        def var_muli_var_list_update(self, a_new_entry, a_var_list,
                                     a_multi_var, a_tree):
            """
            This function, add a new var and updates the multigyrate numbers
            @param a_new_entry this the new entry being added to the multi_var
            list
            @param a_var_list this is the current var list
            @param a_multi_var this is the current multi var list
            @param a_tree this is the current tree
            """
            a_var_list.append(a_new_entry)
            if(a_new_entry in a_multi_var):
                a_new_value = (a_multi_var[-1]) + 1
                a_multi_var.append(a_new_value)
                a_multi_var.pop(0)
                self.renamer(a_tree, 3, 0)  # This is when it rename the tree
            pass

        def multi_var_update(self, a_multi_var, a_var_list):
            """
            This adds a new entry into the multigyrate values
            @param a_mutli_var
            @param a_var_list
            @return a_multi_var
            """
            if (len(a_multi_var) == 0):
                new_value = (a_var_list[-1]) + 1
                a_multi_var.append(new_value)
                return a_multi_var

            else:
                new_value = (a_multi_var[-1]) + 1
                a_multi_var.append(new_value)
                return a_multi_var
            pass

        def make_mode(self, mode_list):
            """
            This add new mode information to the mode list
            @param mod_list this works to make a new mode in the mode list
            @return this give back the amended mode list
            """
            current_number = mode_list[-1]
            mode_list.append((current_number+1))
            return mode_list

        def find_libration(self, a_tree, out_value):
            """
            This get the main data and then returns the libration value used
            for the new variable
            @param a_tree this is the current tree
            @param out_value this is the returned list of values of librations
            @return None This list works on referencing of lists
            """
            if (type(a_tree) != list):
                print(a_tree)
                out_value.append(a_tree)
                return None  # This might not work
            else:
                # print(a_tree[-1])
                self.find_libration(a_tree[-1], out_value)
                # return out_value

        def build_branch(self, a_tree, a_branch, a_value):
            """
            This function get the highlighted branch and places it into a
            branch list.
            @param a_tree this is the current tree
            @param a_branch this is the current branch
            @param a_value this the node which the branch is need to be added
            @return None this function works on references
            """
            temp_list = []
            for element in a_tree:
                temp_list.append(element[a_value])
            a_branch.append(temp_list)
            return None

        def muli_var_update(self, a_tree, output_list):
            """
            This update the multivar list to give the correct value
            @param a_tree this is the current tree
            @param output_list this is the output list being used
            @return None this function works on references
            """
            if (type(a_tree) != list):
                return None

            for element in a_tree:
                if (type(element) == list):
                    # print (element)
                    if (len(element) > 2):
                        # print (element)
                        if (type(element[1]) == str):
                            print(element)
                            output_list.append(element)

                self.muli_var_update(element, output_list)
                # This might be a problem
            return None

        # This is need to make the other values

        def old_multi_var_update(self, a_input_list, a_var_list):
            """
            This updates the old multi var values
            @param a_inputlist this is the muli_var list which is being updated
            @param a_var_list this is the current var_list
            @return this gives a list of mulit var which are not being acted up
            """
            temp_list = []
            # print (a_input_list)

            for element in a_input_list:

                # print (element)
                temp_list1 = []
                for element_entry in element:

                    if (type(element_entry) != str):
                        if element_entry not in a_var_list:
                            element_entry = element_entry + 1

                    print(element_entry)
                    temp_list1.append(element_entry)

                temp_list.append(temp_list1)

            print(temp_list)
            return temp_list

        def combine_old_new_multi_var(self, a_multi_var, a_remaining_multi_var,
                                      a_multi_var_list):
            """
            This works on combining the old and new values from the old and
            new multigyrate,
            @param a_multi_var this is the current a multi_var being changed
            @param a_remaining_multi_var this is the current  remaining multi
            varlist
            @param a_multi_var_list this is the list of remaining updated by
            order unchanged
            @return new_list this returns a list of the updated values
            """
            temp_list_1 = []
            if (len(a_multi_var) != 0):
                for element in a_multi_var:
                    temp_list_1.append(element[0])

            temp_list_2 = []
            if (len(a_remaining_multi_var) != 0):
                for element in a_remaining_multi_var:
                    temp_list_2.append(element[0])

            print(temp_list_1)
            print(temp_list_2)

            new_list = []

            for element in a_multi_var_list:
                if element in temp_list_1:
                    index = temp_list_1.index(element)
                    new_list.append(a_multi_var[index])

                elif element in temp_list_2:
                    index = temp_list_2.index(element)
                    new_list.append(a_remaining_multi_var[index])

                else:
                    new_list.append("entry not found")

            return new_list

    a_add_base_branch_helper = add_base_branch_helper()

    # this is the main function

    class add_branch(object):
        """
        This class is build an add branch object which carry out the process
        of change the tree to fit the addition of a branch at each root
        """

        def __init__(self, a_var_list, a_multi_var_list, a_tree, a_mode_list,
                     a_out_put_multi_var):
            self.a_var_list = a_var_list
            self.a_multi_var_list = a_multi_var_list
            self.a_tree = a_tree
            self.a_mode_list = a_mode_list
            self.a_out_put_multi_var = a_out_put_multi_var

            assert a_data_container.get_var() == self.a_var_list
            assert a_data_container.get_multi_var_list() == self.a_multi_var_list
            assert a_data_container.get_tree() == self.a_tree
            assert a_data_container.get_mode() == self.a_mode_list

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

        def set_a_var_list(self, a_var_list):
            self.a_var_list = a_var_list
            return

        def set_a_multi_var_list(self, a_multi_var_list):
            self.a_multi_var_list = a_multi_var_list
            return

        def set_a_tree(self, a_tree):
            self.a_tree = a_tree
            return

        def set_a_mode_list(self, a_mode_list):
            self.a_mode_list = a_mode_list
            return

        def set_a_out_put_multi_var(self, a_out_put_multi_var):
            self.a_out_put_multi_var = a_out_put_multi_var
            return

        def get_a_var_list(self):
            return self.a_var_list

        def get_a_multi_var_list(self):
            return self.a_multi_var_list

        def get_a_tree(self):
            return self.a_tree

        def get_a_mode_list(self):
            return self.a_mode_list

        def get_a_out_put_multi_var(self):
            return self.a_out_put_multi_var

        def joint_tree_auto(self, a_add_base_branch_helper):
            """
            This is a function which automatically runs the join tree
            function with the necessary argument based on the object in
            question private member variables
            @return self.join_tree(...) this calls the join_tree function
            """
            return self.join_tree(self.get_a_tree(),
                                  self.get_a_var_list(),
                                  self.get_a_multi_var_list(),
                                  self.get_a_mode_list(),
                                  a_add_base_branch_helper)

        def join_tree(self, a_tree, a_var_list, a_multi_var_list,
                      a_mode_list, a_add_base_branch_helper):
            """
            This is the main join tree function, this take the currently
            unchanged tree, var list, multi var list, mode list with the
            add_base_branch help object and changes the tree, var list multi
            var list and mode list to the correct values.

            @param a_tree this is the current tree
            @param a_var_list this is the current var list
            @param a_multi_var_list, this is the current multi_var_list
            @param a_mode_list this is the current mode list
            @param a_add_base_branch_helper this is the current base branch
            helper
            @return this is the change new tree
            """

            print(a_tree)
            new_entry = (a_var_list[-1] + 1)
            print(a_var_list)
            # print ("this one ", a_multi_var_list)

            a_add_base_branch_helper.var_muli_var_list_update(new_entry,
                                                              a_var_list,
                                                              a_multi_var_list,
                                                              a_tree)
            print(a_tree)
            print(a_var_list)

            # print("this one ", a_multi_var_list)

            if (a_tree[1] == '0'):

                # print("this one ", a_multi_var_list)

                a_mode_list = a_add_base_branch_helper.make_mode(a_mode_list)
                value = []
                a_add_base_branch_helper.find_libration(a_tree, value)
                # value = a_add_base_branch_helper.find_libration(a_tree,value)
                value = value[0]

                new_branch = [a_var_list[-1], value]

                print(new_branch)

                tor = a_tree.pop(0)  # this needs to be looked at
                old_mode = a_tree.pop(0)

                new_right_branch = new_branch
                new_left_branch = a_tree[0]

            else:
                # multi_var_update = multi_var_update(a_multi_var_list,
                #                                        a_var_list)
                # print("this one ", a_multi_var_list)

                a_mode_list = a_add_base_branch_helper.make_mode(a_mode_list)
                value = []
                a_add_base_branch_helper.find_libration(a_tree, value)

                # value = a_add_base_branch_helper.find_libration(a_tree,
                #                                                 value)
                value = value[0]

                new_branch = [a_var_list[-1], value]

                print(new_branch)

                tor = a_tree.pop(0)  # this need to be looked at
                old_mode = a_tree.pop(0)

                new_right_branch = []
                new_left_branch = []

                # a_add_base_branch_helper.multi_var_update(a_multi_var_list,
                #                        a_var_list)  # this has been moved

                a_multi_var_list = a_add_base_branch_helper.multi_var_update(
                                                          a_multi_var_list,
                                                          a_var_list)

                print("object: ", a_tree)

                a_add_base_branch_helper.build_branch(a_tree,
                                                      new_left_branch, 0)

                new_left_branch.insert(0, old_mode)
                new_left_branch.insert(0, a_multi_var_list[-1])

                a_add_base_branch_helper.build_branch(a_tree,
                                                      new_right_branch, 1)

                # a_add_base_branch_helper.multi_var_update(a_multi_var_list,
                #                                          a_var_list)

                a_multi_var_list = a_add_base_branch_helper.multi_var_update(
                                                          a_multi_var_list,
                                                          a_var_list)

                new_right_branch.insert(0, old_mode)
                new_right_branch.insert(0, a_multi_var_list[-1])

                # print (new_left_branch)
                # print(new_right_branch)

            # print("this one ", a_multi_var_list)

            new_tree = []

            new_tree.append(tor)
            new_tree.append(str(a_mode_list[-1]))

            print("-----")

            print(new_left_branch)
            print(new_right_branch)

            new_trunk = [new_left_branch, new_right_branch]

            if (old_mode == '0'):
                new_tree.append(new_trunk)
            else:
                new_tree.append(new_trunk)
                new_tree.append(new_branch)

            print("------------")
            print(new_tree)
            print("------------")

            # a_add_base_branch_helper.muli_var_update(new_tree,
            #                                         a_out_put_multi_var)
            # print (multi_var)
            # multi_var = out_put_multi_var.copy()
            # print (multi_var)
            # multi_var.sort()

            return new_tree

    # instance of the a_add_branch object

    a_add_branch = add_branch(a_data_container.get_var(),
                              a_data_container.get_multi_var_list(),
                              a_data_container.get_tree(),
                              a_data_container.get_mode(),
                              a_data_container.get_out_put_multi_var())

    ####
    # assert a_data_container.get_var() == var
    # assert a_data_container.get_multi_var_list() == multi_var_list
    # assert a_data_container.get_tree() == tree
    # assert a_data_container.get_mode() == mode_list
    ####

    # tree = join_tree(tree)
    #
    # tree_1 = a_add_branch.joint_tree_auto(a_add_base_branch_helper)
    #
    # a_data_container.set_tree(tree_1.copy())

    # this update the tree

    a_data_container.set_tree(
        a_add_branch.joint_tree_auto(
            a_add_base_branch_helper).copy())

    # sorting out the mulit_var
    # out_put_multi_var = []
    # a_data_container.set_out_put_multi_var([])

    # muli_var_update(tree, out_put_multi_var)
    # print (multi_var)

    # this update date the multivar information

    a_data_container.set_out_put_multi_var(
        a_add_base_branch_helper.muli_var_update(
                                    a_data_container.get_tree(),
                                    a_data_container.get_out_put_multi_var()))

    # multi_var = out_put_multi_var.copy()

    # this set the multi var infomation

    a_data_container.set_multi_var(
        a_data_container.get_out_put_multi_var().copy())

    # print (multi_var)
    # multi_var.sort()

    print("----------")

    # a_data_container.set_multi_var(a_data_container.get_multi_var().sort())

    a_data_container.get_multi_var().sort()  # this is working be reference

    # this set the remaining multivar information to work

    a_data_container.set_remaining_multi_var(
        a_add_base_branch_helper.old_multi_var_update(
            a_data_container.get_remaining_multi_var(),
            a_orginal_data_container.get_old_var_list()))

    # this set the remaining multi_var values to work

    a_data_container.set_remaining_multi_var(
        a_gyrate_contain_constructor.grouper_multi(
            a_data_container.get_remaining_multi_var()))

    # this set the remaining multi_var

    a_data_container.set_multi_var(
        a_add_base_branch_helper.combine_old_new_multi_var(
            a_data_container.get_multi_var(),
            a_data_container.get_remaining_multi_var(),
            a_data_container.get_multi_var_list()))

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

            self.raw_conf = []
            self.raw_multiconf = []
            self.raw_setconf = []

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

            self.splitter(self.get_raw_conf(), "conf", "blank",
                          self.get_raw_data())

            self.splitter(self.get_raw_multiconf(), "multiconf",
                          "multiconfroot", self.get_raw_data())

            self.splitter(self.get_raw_setconf(), "setconf", "blank",
                          self.get_raw_data())

            self.gyrate_name_splitter(self.get_raw_gyrate_name(), "gyrate",
                                      "multigyrate", self.get_raw_data())

            self.set_raw_mode(self.mode_name_jointer(self.get_raw_mode_names(),
                                                     self.get_raw_mode()))

        # getters and setters

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

        def set_raw_conf(self, a_raw_conf):
            self.raw_conf = a_raw_conf
            return

        def set_multiconf(self, a_multiconf):
            self.raw_multiconf = a_multiconf
            return

        def set_raw_setconf(self, a_setconf):
            self.raw_setconf = a_setconf

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

        def get_raw_conf(self):
            return self.raw_conf

        def get_raw_multiconf(self):
            return self.raw_multiconf

        def get_raw_setconf(self):
            return self.raw_setconf

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
                              a_raw_gyrate, a_raw_conf, a_raw_multi_conf,
                              a_raw_setconf):
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
            a_new_gyrate_file = a_new_gyrate_file + a_raw_conf
            a_new_gyrate_file = a_new_gyrate_file + a_raw_var
            a_new_gyrate_file.append("endsection\n")

            a_new_gyrate_file.append("probabilities:\n")
            a_new_gyrate_file = a_new_gyrate_file + a_raw_mode
            a_new_gyrate_file.append("\nendsection\n")

            a_new_gyrate_file.append("variables2:\n")
            a_new_gyrate_file = a_new_gyrate_file + a_raw_multi_var
            a_new_gyrate_file = a_new_gyrate_file + a_raw_multi_conf


            a_new_gyrate_file.append("\nendsection\n")

            a_new_gyrate_file.append("dynamics:\n")
            a_new_gyrate_file.append("remark ring\n")

            a_new_gyrate_file.append("remark gyrates")
            a_new_gyrate_file = a_new_gyrate_file + a_raw_gyrate
            if len(a_raw_setconf) == 0:
                a_new_gyrate_file.append("\nendsection")
            else:
                a_new_gyrate_file = a_new_gyrate_file + a_raw_setconf
                a_new_gyrate_file.append("endsection")

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
                              a_combine_gyrate_output.get_raw_gyrate(),
                              a_combine_gyrate_output.get_raw_conf(),
                              a_combine_gyrate_output.get_raw_multiconf(),
                              a_combine_gyrate_output.get_raw_setconf()))

    a_gyrate_output.set_export_new_line(
        a_combine_gyrate_output.export_update(a_gyrate_output.get_export()))

    export_file1 = a_gyrate_output.get_export_new_line()

    out_file = open("/home/holmes/Desktop/Methods folder/Project 32/Test_folder/Project 32/gyrate_test/Out_file.txt", 'w')

    # out_file.writelines(export_file)
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
        #out_file.writelines(export_file)
        out_file.writelines(a_gyrate_output.get_export_new_line())
        out_file.close()

    gyrate_out()
    # for element in a_gyrate_output.get_export_new_line():
    #     print(element)



    return
