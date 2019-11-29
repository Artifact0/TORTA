#!/usr/bin/python
######################################################################################
# TORTA - TOR Technical Assistant                                                    #
#   chatbot manager for TOR chats, and eventually forums, chans, VOIP, and more      #
#       after chats are well polished, chans will be next; forums are not priority.  #
#       call flooder AI is a distant goal, able to converse via TTS                  #
#                                                                                    #
#   ./modules/colours.py                                                             #
#       Artifact - 2019                                                              #
#                                                                                    #
######################################################################################
#                                                                                    #
#[o_o]< lines that start like this are comments for clarification of the code        #
#[o_o]< commented lines which do not start like this are lines of code which are     #
#[o_o]< commented out for reasons, but may have been left in for testing             #
##############################  END HEADER  ##########################################
#
#
#
#
global IMPORTED_COLOURS
IMPORTED_COLOURS = 1
import os
if(os.path.exists('../data/verbose')): 
    print("...imported:['./modules/colours.py']...")

#[o_o]< default colour selection
global DfltClr_random
global DfltClr_Beige
global DfltClr_Blueviolet
global DfltClr_Brown
global DfltClr_Cyan
global DfltClr_Skyblue
global DfltClr_Gold
global DfltClr_Grey
global DfltClr_Green
global DfltClr_Hotpink
global DfltClr_Lightblue
global DfltClr_Lightgreen
global DfltClr_Limegreen
global DfltClr_Magenta
global DfltClr_Olive
global DfltClr_Orange
global DfltClr_Orangered
global DfltClr_Red
global DfltClr_Royalblue
global DfltClr_Seagreen
global DfltClr_Sienna
global DfltClr_Silver
global DfltClr_Tan
global DfltClr_Teal
global DfltClr_Violet
global DfltClr_White
global DfltClr_Yellow
global DfltClr_Yellowgreen




    #[o_o]< These colors are the login screen default choices for LEchat
    #[o_o]< any RGB/hex color value can be sent through login, even custom
DfltClr_random          =    ""
DfltClr_Beige           =    "F5F5DC"
DfltClr_Blueviolet      =    "8A2BE2"
DfltClr_Brown           =    "A52A2A"
DfltClr_Cyan            =    "00FFFF"
DfltClr_Skyblue         =    "00BFFF"
DfltClr_Gold            =    "FFD700"
DfltClr_Grey            =    "808080"
DfltClr_Green           =    "008000"
DfltClr_Hotpink         =    "FF69B4"
DfltClr_Lightblue       =    "ADD8E6"
DfltClr_Lightgreen      =    "90EE90"
DfltClr_Limegreen       =    "32CD32"
DfltClr_Magenta         =    "FF00FF"
DfltClr_Olive           =    "808000"
DfltClr_Orange          =    "FFA500"
DfltClr_Orangered       =    "FF4500"
DfltClr_Red             =    "FF0000"
DfltClr_Royalblue       =    "4169E1"
DfltClr_Seagreen        =    "2E8B57"
DfltClr_Sienna          =    "A0522D"
DfltClr_Silver          =    "C0C0C0"
DfltClr_Tan             =    "D2B48C"
DfltClr_Teal            =    "008080"
DfltClr_Violet          =    "EE82EE"
DfltClr_White           =    "FFFFFF"
DfltClr_Yellow          =    "FFFF00"
DfltClr_Yellowgreen     =    "9ACD32"







