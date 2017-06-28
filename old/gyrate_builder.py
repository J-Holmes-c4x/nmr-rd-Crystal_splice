# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 16:55:31 2017

@author: holmes
"""

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
