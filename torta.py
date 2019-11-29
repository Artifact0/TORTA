#!/usr/bin/python
######################################################################################
# TORTA - TOR Technical Assistant                                                    #
#   chatbot manager for TOR chats, and eventually forums, chans, VOIP, and more      #
#       after chats are well polished, chans will be next; forums are not priority.  #
#       call flooder AI is a distant goal, able to converse via TTS                  #
#                                                                                    #
#   ./Torta.py                                                                       #
#       Artifact - 2019                                                              #
#                                                                                    #
######################################################################################
#                                                                                    #
#[o_o]< lines that start like this are comments for clarification of the code        #
#[o_o]< commented lines which do not start like this are lines of code which are     #
#[o_o]< commented out for reasons, but may have been left in for testing             #
##############################  END HEADER  ##########################################
# TO DO LIST
# 
# - build support into waiting room handler for changes in waiting room type
# -   such as moderator approval changing to simple wait time while waiting
# - 
# - 
#  features to add:
#   threads:
#       core logic thread, controls managers, which control personae/bots/workers
#       sessman: captcha/login , session management for all personae
#       messenger: reads, logs, parses, and feeds pertinent info to personae/bots
#       personae: new threads for each persona launched, the chatbot modules
#   check for expired session
#   make folder for each persona and manage datfiles for each one separately
#
#
import sys
import time
print("...starting TORTA...")




sys.path.insert(0, 'modules/')
from setup import *
if(IMPORTED_CHATBOT != 1): from chatbot import *
if(IMPORTED_LECHATPHP != 1): from lechatphp import *
if(IMPORTED_LECHATPERL != 1): from lechatperl import *
if(IMPORTED_BOORU != 1): from booru import *



#RUNNING=1


#while(RUNNING==1): test()


#a = "bWF5YmUgdHJ5IHRoaXMgb25l"
#b = b64decode(a)
#print(b)

#e = '陣啮𐙡靹饯啹驲饡𓈠鹨瑳'
#f = b65kd(e)
#print(f)


#[o_o]< this is where the magic happens
def main():
    RUNNING = 1
    global target
    global LOGGED_IN
    print("You are running "+SoftName+", developed by "+SoftDev)
    print("")
    print("")
#    setup_threads()
#    setup_netchat()
#    start_threads()
    condition = greenlight
    OP = Operations("start")
    while(RUNNING==1):
        if(OP==""):
#            print("did you not enter anything?")
#            time.sleep(1)
#            OP = OP_Uncertain
            OP = OP_LEchatPHP
        elif(OP==OP_NetCheck):
            network_check(target)
            OP = OP_Uncertain
        elif(OP==OP_ChatBot):
            OP = NYI(OP)
        elif(OP==OP_CAPTCHA):
            OP = NYI(OP)
        elif(OP==OP_Search):
            OP = NYI(OP)
        elif(OP==OP_Spider):
            OP = NYI(OP)
        elif(OP==OP_LEchatPERL):
            print("LEchatPERL not yet reimplemented")
            time.sleep(2)
            OP = OP_Uncertain
        elif(OP==OP_LEchatPHP):
            LEchatPHP()
        elif(OP==OP_Chan):
            OP = NYI(OP)
        elif(OP==OP_Booru):
            OP = NYI(OP)
        elif(OP==OP_Vids):
            OP = NYI(OP)
        elif(OP=="Exit"):
            print("Take Care and Stay Safe")
            time.sleep(2)
            break    
        else:
            OP = Operations("error")
    return
#



main()



#[o_o]< end of file
