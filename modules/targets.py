#!/usr/bin/python
######################################################################################
# TORTA - TOR Technical Assistant                                                    #
#   chatbot manager for TOR chats, and eventually forums, chans, VOIP, and more      #
#       after chats are well polished, chans will be next; forums are not priority.  #
#       call flooder AI is a distant goal, able to converse via TTS                  #
#                                                                                    #
#   ./modules/targets.py                                                             #
#       Artifact - 2019                                                              #
#                                                                                    #
######################################################################################
#                                                                                    #
#[o_o]< lines that start like this are comments for clarification of the code        #
#[o_o]< commented lines which do not start like this are lines of code which are     #
#[o_o]< commented out for reasons, but may have been left in for testing             #
##############################  END HEADER  ##########################################
#
#[o_o]< designation of targets
#
#
global IMPORTED_TARGETS
IMPORTED_TARGETS = 1
import os, time
if(os.path.exists('../data/verbose')): 
    print("...imported:['./modules/targets.py']...")




#######[o_o]<  TARGETS  #######

global targets
targets = []

    #[o_o]< hacker chats
blackhatchat = 'http://blkh4ylofapg42tj6ht565klld5i42dhjtysvsnnswte4xt4uvnfj5qd.onion/index.php'

    #[o_o]< Daniel chats
dans_v3 = 'http://danschat356lctri3zavzh6fbxg2a7lo6z3etgkctzzpspewu7zdsaqd.onion/chat.php'
dans_v2 = ''
dans_clear = 'https://chat.danwin1210.me/chat.php'

    #[o_o]< search engines - this will become much more useful, later on..
    #[o_o]< the script could eventually be given a search topic, and it would
    #[o_o]< prompt user with a list of search engines (defined below) to choose from
    #[o_o]< Torta could then scrape the search results for xyz and parse/save data
    #[o_o]< for AI models to train on. such as images with certain keywords (like 'pikachu')
searx = 'http://searchb5a7tmimez.onion/'

    #[o_o]< Forums

    #[o_o]< Image Boards / Chans
ch8clear = "http://8ch.net"
ch8onion = "http://oxwugzccvk3dk6tj.onion/"
    #[o_o]< Booru type image sites

    #[o_o]< Handlers will be built in for each site type, so far only chat has been worked on
    #[o_o]< and search sites so far have been used only to test network connection
    #[o_o]< as a diagnostic step if a chat target is unavailable




marianaschat = "http://krduknstksgqwphwzanwvlx3kpnbbhtxatmfduqcdn3n7cfbsjjiw2qd.onion/chat/index.php"


infowarschat = "http://lnemtg57t7tivkp26okie5ywpb2w7rcjesrwozrrtfwcj22qnxtlwkyd.onion/chat/index.php"


target = dans_v3
target = dans_clear
#target = searx


#target = marianas
target = infowarschat

url = target


def Targetting(choice='null'):
    global DONECHOOSING
    global target
    DONECHOOSING = 0
    CHOSEN = 0
    Target = choice
    TimesRan = 0
    while(DONECHOOSING==0):
        if(TimesRan==0): Targets = []
        print("")
        if(TimesRan>1):
            print("")
            print(("Available Targete include: " + str(Targets)))
            print("also you can enter 'c' or 'custom' to choose your own url")
            print("")
            print("default is Daniel's clearnet gateway if nothing else is typed")
            print("")
            time.sleep(1)
            Target = input("What is the target? ")
        if(Target=="custom") or (Target=="c"):
            while(CHOSEN==0):
                print("")
                user_url = input("please enter your custom url> http:\\")
                user_choice = input("target is http:\\"+user_url+" ? y or * >> ")
                if(user_choice=='y'): CHOSEN=1
            target = user_url
            DONECHOOSING = 1
        #[o_o]< ACCOUNTS
        #
        #
        # INFOWARS
        if(TimesRan==0): Targets.append("INFOWARS CHAT (infowars)")
        if(Target=="infowars"):
            target = infowarschat
            DONECHOOSING = 1
        #
        # target_xyz
        if(TimesRan==0): Targets.append("Mariana's Web (mariana)")
        if(Target=="mariana"):
            target = marianaschat
            DONECHOOSING = 1
        #
        # target_xyz
        if(TimesRan==0): Targets.append("Daniel's Chat Clear (danclear)")
        if(Target=="danclear"):
            target = dans_clear
            DONECHOOSING = 1
        #
        # target_xyz
        if(TimesRan==0): Targets.append("Daniel's Chat TOR (dantor)")
        if(Target=="dantor"):
            target = dans_v3
            DONECHOOSING = 1
        #
        # Blackhat Chat
        if(TimesRan==0): Targets.append("Blackhat Chat (blackhat)")
        if(Target=="Blackhat"):
            target = blackhatchat
            DONECHOOSING = 1
        #
        #
        # blank
        if(Target==""):
            target = dans_clear
            DONECHOOSING = 1
        #
        #
        #
        TimesRan = TimesRan + 1
        time.sleep(1)
    return target
#
