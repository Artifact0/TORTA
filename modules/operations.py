#!/usr/bin/python
######################################################################################
# TORTA - TOR Technical Assistant                                                    #
#   chatbot manager for TOR chats, and eventually forums, chans, VOIP, and more      #
#       after chats are well polished, chans will be next; forums are not priority.  #
#       call flooder AI is a distant goal, able to converse via TTS                  #
#                                                                                    #
#   ./modules/operations.py                                                          #
#       Artifact - 2019                                                              #
#                                                                                    #
######################################################################################
#                                                                                    #
#[o_o]< lines that start like this are comments for clarification of the code        #
#[o_o]< commented lines which do not start like this are lines of code which are     #
#[o_o]< commented out for reasons, but may have been left in for testing             #
##############################  END HEADER  ##########################################
#
#[o_o]< Operations Command Center (OPCOMCEN) will integrate with server and reporters
#
#
#[o_o]< SCRIPT_HEADER:START
#
global IMPORTED_OPERATIONS
IMPORTED_OPERATIONS = 1
import os
if(os.path.exists('../data/verbose')): 
    print("...imported:['./modules/operations.py']...")
#
#[o_o]< SCRIPT_HEADER:END
#

import sys
import time

from config import *
from imports import *
from functions import *

global OP_Uncertain
global OP_NetCheck
global OP_ChatBot
global OP_CAPTCHA
global OP_Search
global OP_Spider
global OP_LEchatPERL
global OP_LEchatPHP
global OP_Chan
global OP_Booru
global OP_Vids

global OP_NetCheck_desc
global OP_ChatBot_desc
global OP_CAPTCHA_desc
global OP_Search_desc
global OP_Spider_desc
global OP_LEchatPERL_desc
global OP_LEchatPHP_desc
global OP_Chan_desc
global OP_Booru_desc
global OP_Vids_desc

###[o_o]<  operations  ##
OP_Uncertain = "uncertain"
OP_NetCheck = "NetCheck"
OP_ChatBot = "ChatBot"
OP_CAPTCHA = "CAPTCHA"
OP_Search = "Search"
OP_Spider = "Spider"
OP_LEchatPERL = "LEchatPERL"
OP_LEchatPHP = "LEchatPHP"
OP_Chan = "Chan / Image Boards"
OP_Booru = "Booru / Image Boards"
OP_Vids = "Videos / Streams"
#[o_o]<  descriptions
OP_NetCheck_desc = "Network Status Checker"
OP_ChatBot_desc = "Local or Remote ChatBot"
OP_CAPTCHA_desc = "CAPTCHA generator and solver"
OP_Search_desc = "Search Scraper"
OP_Spider_desc = "Website / Link Crawler"
OP_LEchatPERL_desc = "Lucky Eddie's Chat - include support for multiple versions"
OP_LEchatPHP_desc = "Daniel's adaptation of Lucky Eddie's PERL chat"
OP_Chan_desc = "image scraper / mass downloader & Conversation like ChatBot"
OP_Booru_desc = "image scraper / mass downloader"
OP_Vids_desc = "video scraper / mass downloader"













############# GLOBALS #############

global perseq
global RUNNING

#[o_o]< Used currently for managing logins easier, will eventually include memory and personality
global Persona
#[o_o]< logs in during runtime if set to 0, skips login if set to 1+ (already logged in)
global LOGGED_IN
#[o_o]< Operation to perform, used for mode management
global OP

#[o_o]<  OPERATIONS and rough progress towards completion of beta version for each module
global uncertain # N/A
global NetCheck # 50%
global ChatBot # 20%
global CAPTCHA # 10%
global Search # 10%
global Spider # 10%
global LEchatPERL # 20%
global LEchatPHP # 60%
global Chan # 0%
global Booru  # 10%
global Vids # 0%

#[o_o]< Log Sequence - sequential log recorder, let's Torta know how many logs have been made so far.
#[o_o]< this feature will change once logging becomes more polished. it will become a rolling log which
#[o_o]< appends new messages, and notes which messages were deleted & when
global logseq

#[o_o]< which website is lucky enough to have us as a visitor ;)
global target
#[o_o]< whether or not CAPTCHAs are in use on [target_site]
global USE_CAPTCHA
#[o_o]< pointer used for fetching page scrape data to parse
global content
#[o_o]< used for building a request to send the server
global send_action
#[o_o]< typically equals target
global url

#[o_o]< Data used for login and authentication while posting or requesting admin frames
global nic # nickname
global pas # password
global val # nc/value ~=npid? 
global cap # CAPTCHA solving
global col # personal text colour
#[o_o]< User Agent can be used to track a target across time and/or space. be careful about changing this from default
global User_Agent
#[o_o]< session ID string
global session
#[o_o]< next post ID, used to verify/identify posts and sometimes seems required
global npid

#[o_o]< frames used by the LEchat frameset
global frame_post
global frame_view
global frame_cntrl
global frame_help
global frame_profile
global frame_admin

#[o_o]< variables for handling waiting room
global WAITING
#[o_o]< Let's the script know that waiting occured before entry. could be used as a sort of yellow light
global HAD_TO_WAIT
#[o_o]< used during waiting room for determining how long to wait between checks, could be used elsewhere also
global wait_time
#[o_o]< used during waiting room routine, to know whether to wait one time and check back in, or keep looping.
global MOD_APPROVAL_ON

global Error
global ErrType
global ErrNum

global perseqdir
global datadir
global livedir

global USE_CAPTCHA
global CAPTCHA_SOLVED
global DONECHOOSING
global AvailPersonae

global status

status = 'nominal'

PYTHONHTTPSVERIFY=0 


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context
#



############# DEFINITIONS #############
RUNNING = 0
Persona = ''
LOGGED_IN = 0
OP = ''


perseq = 'null'

try:
    perseqfile=open('data/perseq.txt','r')
    perseq = int(perseqfile.read())
    perseqfile.close()
    perseq = perseq + 1
    perseqfile=open('data/perseq.txt','w')
    perseqfile.write(str(perseq))
    perseqfile.close()
    perseq = str(perseq)
except(FileNotFoundError):
    perseqfile=open('data/perseq.txt','w')
    perseq = 0
    perseqfile.write(str(perseq))
    perseqfile.close()
    perseq = str(perseq)
#


def CreateDirs(perseq):
    os.makedirs(perseqdir)
    os.makedirs(datadir)
    os.makedirs(livedir)
    logseqfile=open(datadir+'logseq.txt','w')
    logseqfile.write("1")
    logseqfile.close()
    framesetfiile1 = open('data/frameset/index.htm', 'r')
    framesetfiile2 = open(livedir+'index.htm', 'w')
    framesetdata = framesetfiile1.read()
    framesetfiile2.write(framesetdata)
    framesetfiile2.readable()
    framesetfiile1.close()
    framesetfiile2.close()
    framesetfiile1 = open('data/frameset/controls.htm', 'r')
    framesetfiile1.readable()
    framesetfiile2 = open(livedir+'controls.htm', 'w')
    framesetdata = framesetfiile1.read()
    framesetfiile2.write(framesetdata)
    framesetfiile1.close()
    framesetfiile2.close()
    framesetdata = ''

perseqdir = "logs/perseq/"+perseq+"/"
datadir = perseqdir+"data/"
livedir = perseqdir+"live/"

if not os.path.exists(perseqdir): CreateDirs(perseq)

logseqfile=open(datadir+'logseq.txt','r')
logseq = int(logseqfile.read())
logseqfile.close()

target = ''

Error = ''
ErrType = ''
ErrNum = 0

#[o_o]< default settings
USE_PROXY = 0

#[o_o]< still testing file uploads, it needs to be encoded differently than a file.open()
sendfile = './data/fileshare/susieq.jpg'

working_dir = '' 

CAPTCHA_SOLVED = 0




AvailPersonae = []

nic = ''
pas = ''
val = ''
cap = ''
col = ''

npid = ''

MOD_APPROVAL_ON = 0
wait_time = 0
LOGGED_IN = 0

http.client.HTTPConnection.debuglevel = 1

content = ''
session = ''
send_action = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))

    #[o_o]< Torta's testing repository of phrases
manual_input = "Hello World"
msg01 = 'I am functioning within normal operational parameters.'
msg02 = ''
msg03 = ''
msg04 = ''
msg05 = ''
msg06 = ''
msg07 = ''
msg08 = ''
msg09 = ''
msg10 = ''

    #[o_o]< would effect how script operates, like DEFCON levels 1-5, the closer to a redlight
    #[o_o]< the more cautious the script could get about how to handle some things.
    #[o_o]< or rather than cautious, it 
bluelight    = 1
greenlight   = 2
yellowlight  = 3
orangelight  = 4
redlight     = 5

    #[o_o]< Settings most often changed could be saved and read from a text file, and translated by function
    #[o_o]< into proper variables, instead of using another .py file or editing configs a few hundred lines in
Persona = "Pikachu"








###[o_o]<  USER AGENTS  ###

UA_tor  = "Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0"
UA_os2  = "Warp/1.0 (IBM; OS/2)"
UA_fun  = "TimeMachine/1.0 (Nintendo; gameboy color) gopher/1999 Browser/1.0"
UA_pkmn = "Pokemon Transfer System / 1.1 (Bill's PC; box 11) PKMN Center, Viridian City"
User_Agent  = UA_tor
#User_Agent = UA_pkmn
User_Agent  = UA_fun











#OP = OP_NetCheck
#OP = OP_LEchatPHP
#OP = OP_Booru














#[o_o]<  This function will absorb much of the code currently in main()
def Operations(current):
    global OP
    tempOP1 = OP
    OP = OP_Uncertain
    print("")
    print("Options: NetCheck ChatBot CAPTCHA Search Spider")
    print("         LEchatPERL LEchatPHP Chan Booru Vids")
    print("")
    print("default is LEchatPHP if nothing else is typed")
    print("")
    while(OP==OP_Uncertain):
        typing = input("What is the current operation?: ")
        if(typing=="NetCheck"):
            OP = OP_NetCheck
        elif(typing=="ChatBot"):
            OP = OP_ChatBot
        elif(typing=="CAPTCHA"):
            OP = OP_CAPTCHA
        elif(typing=="Search"):
            OP = OP_Search
        elif(typing=="Spider"):
            OP = OP_Spider
        elif(typing=="LEchatPERL"):
            OP = OP_LEchatPERL
        elif(typing=="LEchatPHP"):
            OP = OP_LEchatPHP
        elif(typing=="Chan"):
            OP = OP_Chan
        elif(typing=="Booru"):
            OP = OP_Booru
        elif(typing=="Vids"):
            OP = OP_Vids
        elif(typing=="Exit"):
            OP = "Exit"
        elif(typing==""):
            OP = "LEchatPHP"
        else:
            print(("Sorry I didn't understand your input [" + typing + "], please try again."))
        time.sleep(1)
    return OP
#

