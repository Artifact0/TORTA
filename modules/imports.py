#!/usr/bin/python
######################################################################################
# TORTA - TOR Technical Assistant                                                    #
#   chatbot manager for TOR chats, and eventually forums, chans, VOIP, and more      #
#       after chats are well polished, chans will be next; forums are not priority.  #
#       call flooder AI is a distant goal, able to converse via TTS                  #
#                                                                                    #
#   ./modules/imports.py                                                             #
#       Artifact - 2019                                                              #
#                                                                                    #
######################################################################################
#                                                                                    #
#[o_o]< lines that start like this are comments for clarification of the code        #
#[o_o]< commented lines which do not start like this are lines of code which are     #
#[o_o]< commented out for reasons, but may have been left in for testing             #
##############################  END HEADER  ##########################################
#
#[o_o]< hold all global imports in one location
#
#
global IMPORTED_IMPORTS
IMPORTED_IMPORTS = 1
import os
if(os.path.exists('../data/verbose')): 
    print("...imported:['./modules/imports.py']...")




    #[o_o]< core functionality
# already imported in main script
#import sys
#import time
import subprocess
import os
from os.path import abspath, isabs, isdir, isfile, join

import codecs

import random
import string
import mimetypes
import re

#import aiml

    #[o_o]< threading
import queue
import threading
#import time #irrelevant, already called for AI

    #[o_o]< networking
import http.cookiejar
import http.client
import urllib
import ssl


import pytest
from six import int2byte

from base64 import b64encode, b64decode
#from base64 import *
#import base64


import six
import base65536
from colours import *

#[o_o]< FIND AND INSTALL BEAUTFUL SOUP - CALL FLOODERS USE IT ALSO
#import bs4

#import keras
#import opencv-python
#import 





