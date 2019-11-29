#!/usr/bin/python
######################################################################################
# TORTA - TOR Technical Assistant                                                    #
#   chatbot manager for TOR chats, and eventually forums, chans, VOIP, and more      #
#       after chats are well polished, chans will be next; forums are not priority.  #
#       call flooder AI is a distant goal, able to converse via TTS                  #
#                                                                                    #
#   ./modules/config.py                                                              #
#       Artifact - 2019                                                              #
#                                                                                    #
######################################################################################
#                                                                                    #
#[o_o]< lines that start like this are comments for clarification of the code        #
#[o_o]< commented lines which do not start like this are lines of code which are     #
#[o_o]< commented out for reasons, but may have been left in for testing             #
##############################  END HEADER  ##########################################
#
#[o_o]< Configurations file, to store important variables on development on runtime
#
#
global IMPORTED_CONFIG
IMPORTED_CONFIG = 1
import os
if(os.path.exists('../data/verbose')): 
    print("...imported:['./modules/config.py']...")



global SoftName
global SoftVer
global SoftDev

global VERBOSE

Software_Name = "Torta"
Software_Version = "0.6.8"
Software_ReleaseType = "a"
Software_Developer = "Artifact"

Software_Codename = '"Shatter"'

VERBOSE = 0
#[o_o]<  0 will be quiet operations, minimal notices, quick
#[o_o]<  1 will say when functions start and end, wait on module load, and so on
#[o_o]<  2 asks to displays html scrapes and more





SoftDev = Software_Developer
SoftVer = Software_Version + "-" + Software_ReleaseType
SoftName = Software_Name + "-v" + Software_Version + "-" + Software_ReleaseType
