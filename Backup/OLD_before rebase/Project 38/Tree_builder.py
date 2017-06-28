# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 16:55:31 2017

@author: holmes
"""

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
#file1= "/home/holmes/Desktop/Finished_Deletable/C4X_11162/project/structure/Round_86/SubRound_86_1/gyrateFile"

file1 = "/home/holmes/Desktop/Methods folder/Project 38/Key_files/Round_7/SubRound_7_1/gyrateFile"

# Angle and jump values
angle = 180
jump = 0.0
tor_number = 3
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
test_1_data_container = data_container()



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

    def gyrate_assigment_for_mode(self, a_gyrate):
        """
        This has been added to make all mode values strings in the tree
        @param a_gyrate this is the current gyrate entry
        #TODO this should be removed is not being used at the end
        """
        a_gyrate[1] = str(a_gyrate[1])
        return None

    def gyrate_assigment_of_uni_all(self, a_gyrate):
        """
        This will run through the gyrate tree and will make uni mode
        consistent
        @param a_gyrate this is the full gyrate list form the raw data file
        @param None this works direcly on reffences
        """
        for element in a_gyrate:
            self.gyrate_assigment_for_uni(element)

        return None



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

a_gyrate_contain_constructor.gyrate_assigment_of_uni_all(
        a_data_container.get_gyrate())

####

test_1_data_container = data_container()

test_1_data_container.set_var(
    a_gyrate_contain_constructor.data_splitter(
        a_gyrate_file_processor.get_raw_var(), 1, 2))

test_1_data_container.set_multi_var(
    a_gyrate_contain_constructor.data_splitter(
        a_gyrate_file_processor.get_raw_multi_var(), 1, 100))

test_1_data_container.set_gyrate(
    a_gyrate_contain_constructor.data_splitter(
        a_gyrate_file_processor.get_raw_gyrate(), 1, 10))

test_1_data_container.set_mode(
    a_gyrate_contain_constructor.data_splitter(
        a_gyrate_file_processor.get_raw_mode(), 1, 2))

###
# multi_var_list = multi_var_list_gen(multi_var)
###

test_1_data_container.set_multi_var_list(
    a_gyrate_contain_constructor.multi_var_list_gen(
        test_1_data_container.get_multi_var()))
###
# remaining_multi_var = multi_var.copy()
###

test_1_data_container.set_remaining_multi_var(
    test_1_data_container.get_multi_var().copy())  # note this might not work

###
# remaining_multi_var = remaining_multi_var_grouper(remaining_multi_var)
###

test_1_data_container.set_remaining_multi_var(
    a_gyrate_contain_constructor.remaining_multi_var_grouper(
        test_1_data_container.get_remaining_multi_var()))

test_1_data_container.set_multi_var(
    a_gyrate_contain_constructor.grouper_multi(
        test_1_data_container.get_multi_var()))

a_gyrate_contain_constructor.gyrate_assigment_of_uni_all(
        test_1_data_container.get_gyrate())


###
# multi_var = grouper_multi(multi_var)
###
####

# Dont know if this will be needed
#
#a_data_container.set_gyrate(
#    a_gyrate_contain_constructor.torsion_number_assigment(
#        tor_number, a_data_container.get_gyrate()))
#
####
## gyrate = gyrate[tor_number]
####
#
#a_data_container.set_type_tor(
#    a_gyrate_contain_constructor.torsion_type_assigment(
#        a_data_container.get_gyrate()))
#
#a_data_container.set_gyrate(
#    a_gyrate_contain_constructor.gyrate_assigment_for_uni(
#        a_data_container.get_gyrate()))
#
#
#
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
        #print(a_tree)
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


    def multi_tree_build(self, a_tree_list):
        """
        This is a function which runs the a_gyate_list and builds the
        remaing tree from the gyrate file
        """
        temp_list = []

        for tree in a_tree_list:

            a_tree_builder.tor_builder(tree)

            a_tree_builder.set_tree(
                a_tree_builder.finder(
                    tree, a_data_container.get_multi_var()))

            a_tree_builder.set_tree(
                a_tree_builder.grouper(a_tree_builder.get_tree()))

            a_tree_builder.first_level_tree_fix()

            temp_list.append(a_tree_builder.get_tree().copy())

        return temp_list

a_tree_builder = tree_builder()

a_data_container.set_tree(a_data_container.get_gyrate().copy())

#for element in a_data_container.get_gyrate():
#
#
#    a_tree_builder.tor_builder(element)
#
#    a_tree_builder.set_tree(
#        a_tree_builder.finder(
#            element, a_data_container.get_multi_var()))
#
#    a_tree_builder.set_tree(
#        a_tree_builder.grouper(a_tree_builder.get_tree()))
#
#
##    tree = finder(tree)
##    tree = grouper(tree)
##    print(tree)
#
#    a_tree_builder.first_level_tree_fix()
#
#    temp_list.append(a_tree_builder.get_tree())
#    print(a_tree_builder.get_tree())
#print(temp_list)

a_data_container.set_tree(a_tree_builder.multi_tree_build(a_data_container.get_tree()))


#    tree.insert(0, tor)
#    tree.insert(1, str(tor_mode))
#    print(tree)

#    a_data_container.set_tree(a_tree_builder.get_tree())
#    a_data_container.set_tor(a_tree_builder.get_tor())
#    a_data_container.set_tor_mode(a_tree_builder.get_tor_mode())

# a_var_list, a_multi_var_list, a_tree, a_mode_list

#a_data_container.get_var()
#a_data_container.get_multi_var_list()
#a_data_container.get_tree()
#a_data_container.get_mode()
#a_data_container.get_multi_var_list()
#
#a_data_container.get_tor()

# multi_var = out_put_multi_var.copy()

#Current_gyrate = a_data_container.get_gyrate().copy()
#Current_multi_var = a_data_container.get_multi_var().copy()
#Current_mode = a_data_container.get_mode().copy()
#Current_tree = a_data_container.get_tree().copy()
#Current_var = a_data_container.get_var().copy()


#test_1_data_container.set_tree(a_data_container.get_gyrate().copy())

#test_1_data_container.set_tree(a_tree_builder.multi_tree_build(test_1_data_container.get_tree()))


###
class tree_node(object):
    """

    """
    var_list = []
    mode_list= []
    node_assigment_list = []

    def __init__(self, node_assigment, mode_assignment="var"):

        self.node_assigment = [node_assigment]

        self.node_assigment_list.append(self.node_assigment)



        if (mode_assignment == "var"):
            self.mode_assignment = mode_assignment
            self.var_list.append(self.node_assigment)
        else:
            self.mode_list = [mode_assignment]
            self.mode_list.append([mode_assignment])
            self.node_assigment_list = "node"

        self.node_join_list = []
        self.mode_assignment = mode_assignment

    def __repr__(self):
        output = str(self.node_assigment[0]) + " "+ str(self.mode_list[0]) + " " + str(self.node_join_list)

        return str(output)

    def insert_mode(self, location, tree_node):
        self.node_join_list.insert(location, tree_node)
        pass

    def get_tree_node(self, location):
        if location >= len(self.node_join_list):
            return "no nodes present"

        return self.node_join_list[location]

    def set_tree_node(self, a_list_of_connections):
        self.node_join_list = a_list_of_connections

    def get_node_assigement(self):
        return self.node_assigment

    def insert_trimode():
        pass

    def delete_bimode():
        pass

    def delete_trimode():
        pass


a_tree_obj = tree_node("Gyrate_base")
a_tree_obj.insert_mode(1, tree_node(4))
a_tree_obj.insert_mode(2, tree_node(6, "5"))
a_tree_obj.insert_mode(3, tree_node(8))

a_tree_obj.get_tree_node(1).insert_mode(1, tree_node(9))
a_tree_obj.get_tree_node(1).insert_mode(1, tree_node(10))

###

class tree_node_helper(object):
    """
    d
    """

    def __init__(self):
        self.tree_list = []
        self.node_list = []
        self.torsion_dici = {}
        self.var_list = []
        self.multi_gyrate_torsion_list_obj = []


    def set_multi_gyrate_torsion_list(self, a_mulit_gyrate):
        for element in a_mulit_gyrate:
            temp_object = tree_node(element[0], element[1])
            temp_object.set_tree_node(element[2])
            self.multi_gyrate_torsion_list_obj.append(temp_object)


"""
you need to add all of the data to refference itself



"""

a_tree_node_helper = tree_node_helper()

a_tree_node_helper.set_multi_gyrate_torsion_list(test_1_data_container.get_multi_var().copy())


for element in a_tree_node_helper.multi_gyrate_torsion_list_obj:
    print(element)


###

#a = a_data_container.get_tree().copy()
#for element in a:
#    print(element)
#    print("====")
#
#print("-------")
#
#class tree_node(object):
#    """
#
#    """
#    var_list = []
#    mode_list= []
#    node_assigment_list = []
#
#    def __init__(self, node_assigment, mode_assignment="var"):
#
#        self.node_assigment = [node_assigment]
#
#        self.node_assigment_list.append(self.node_assigment)
#
#        if (mode_assignment == "var"):
#            self.mode_assignment = mode_assignment
#            self.var_list.append(self.node_assigment)
#        else:
#            self.mode_list = [mode_assignment]
#            self.mode_list.append([mode_assignment])
#            self.node_assigment_list = "node"
#
#        self.node_join_list = []
#        self.mode_assignment = mode_assignment
#
#    def __repr__(self):
#        return str(self.node_assigment)
#
#    def insert_mode(self, location, tree_node):
#        self.node_join_list.insert(location, tree_node)
#        pass
#
#    def get_tree_node(self, location):
#        if location >= len(self.node_join_list):
#            return "no nodes present"
#
#        return self.node_join_list[location]
#
#    def get_node_assigement(self):
#        return self.node_assigment
#
#    def insert_trimode():
#        pass
#
#    def delete_bimode():
#        pass
#
#    def delete_trimode():
#        pass
#
#
#a_tree_obj = tree_node("Gyrate_base")
#a_tree_obj.insert_mode(1, tree_node(4))
#a_tree_obj.insert_mode(2, tree_node(6, "5"))
#a_tree_obj.insert_mode(3, tree_node(8))
#
#a_tree_obj.get_tree_node(1).insert_mode(1, tree_node(9))
#a_tree_obj.get_tree_node(1).insert_mode(1, tree_node(10))



#"""
#Basic plan, you been to make a convetor which will take the list form and
#it a lost of actions for the refference form
#
#than a convetor back
#
#than work on make the addition of modes thing
#
#"""
#
#class tree_node_helper(object):
#    """
#    d
#    """
#    tree_list = []
#    node_list = []
#    torsion_dici = {}
#
#    def tree_list_conversion(self, a_tree):
#
#        # self.tree_list.append(a_tree.node_assigment[0])
#
#        #print(a_tree.mode_assignment)
#
#        if a_tree.mode_assignment == "var":
#            pass
#
#        else:
#            pass
#            #print(a_tree.node_assigment, a_tree.mode_assignment, a_tree.node_join_list)
#            #self.tree_list.append(a_tree.node_join_list)
#
#        for element in a_tree.node_join_list:
#            self.tree_list_conversion(element)
#
#    def list_examner(self, a_list):
#        for element in a_list:
##            print(element)
#            if type(element) != int:
#                return False
#        return True
#
#    def torsion_reader(self, a_branch):
#        if type(a_branch) != list:
#            return
#        else:
#            for element in a_branch:
#                if type(element) == list:
#                    #print(element)
#                    if (type(element[-1]) == list):
#                        if self.list_examner(element[-1]):
#                            # print("list all int", element)
#                            self.torsion_dici[element[0]] = element.copy()
#                            pass
#
#                    self.torsion_reader(element)
#
#    def gyrate_reader(self, a_branch):
#
#        if type(a_branch) != list:
#
#            return
#        else:
#
#            for element in a_branch:
#                if(type(element) == list):
#                    if element[0] in self.torsion_dici.keys():
#                        print(element[0])
#                    else:
#                        print(element)
#
#                    pass
#                else:
#                    #print(element)
#                    pass
#
#                self.gyrate_reader(element)
#
#
#
#
#
##        if type(a_branch[1][1]) != str:
##            print ("hit")
##            return
##        for element in a_branch:
##            print(element)
##            self.torsion_reader(element)
#
#a_tree_node_helper = tree_node_helper()
#
#a_tree_node_helper.tree_list_conversion(a_tree_obj)
#
##print(a_tree_node_helper.tree_list)
#
#a_tree_node_helper.torsion_reader(a[1])
#
#a_tree_node_helper.gyrate_reader(a[1])
#
#
#
##print(a[1][1])

