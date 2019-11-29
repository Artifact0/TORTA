#!/usr/bin/python
######################################################################################
# TORTA - TOR Technical Assistant                                                    #
#   chatbot manager for TOR chats, and eventually forums, chans, VOIP, and more      #
#       after chats are well polished, chans will be next; forums are not priority.  #
#       call flooder AI is a distant goal, able to converse via TTS                  #
#                                                                                    #
#   ./modules/setup.py                                                               #
#       Artifact - 2019                                                              #
#                                                                                    #
######################################################################################
#                                                                                    #
#[o_o]< lines that start like this are comments for clarification of the code        #
#[o_o]< commented lines which do not start like this are lines of code which are     #
#[o_o]< commented out for reasons, but may have been left in for testing             #
##############################  END HEADER  ##########################################
#
#[o_o]< Setup file loads global modules, so all can be called with one include in other files
#
#
global IMPORTED_SETUP
IMPORTED_SETUP = 1
import os
if(os.path.exists('../data/verbose')): 
    print("...imported:['./modules/setup.py']...")


#[o_o]< core modules
global IMPORTED_CONFIG
global IMPORTED_IMPORTS
global IMPORTED_OPERATIONS
global IMPORTED_FUNCTIONS

#[o_o]< base modules
global IMPORTED_B65KTEST
global IMPORTED_BASE65536
global IMPORTED_BOORU
global IMPORTED_CAPTCHA
global IMPORTED_CHATBOT
global IMPORTED_COLOURS
global IMPORTED_IMAGEBOARD
global IMPORTED_LECHATPERL
global IMPORTED_LECHATPHP
global IMPORTED_SIX
global IMPORTED_SPIDER
global IMPORTED_TARGETS

#[o_o]< addon modules
#global IMPORTED_





#[o_o]< core modules
IMPORTED_CONFIG = 0
IMPORTED_IMPORTS = 0
IMPORTED_OPERATIONS = 0
IMPORTED_FUNCTIONS = 0

#[o_o]< base modules
IMPORTED_B65KTEST = 0
IMPORTED_BASE65536 = 0
IMPORTED_BOORU = 0
IMPORTED_CAPTCHA = 0
IMPORTED_CHATBOT = 0
IMPORTED_COLOURS = 0
IMPORTED_IMAGEBOARD = 0
IMPORTED_LECHATPERL = 0
IMPORTED_LECHATPHP = 0
IMPORTED_SIX = 0
IMPORTED_SPIDER = 0
IMPORTED_TARGETS = 0

#[o_o]< addon modules
#IMPORTED_ = 0




#[o_o]< one location to store update information
if(IMPORTED_CONFIG != 1): from config import *

#[o_o]< one location to store global imports
if(IMPORTED_IMPORTS != 1): from imports import *

#[o_o]< one location to manage Operations Control
if(IMPORTED_OPERATIONS != 1): from operations import *

#[o_o]< one location to define global functions
if(IMPORTED_FUNCTIONS != 1): from functions import *


