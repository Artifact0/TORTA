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
#[o_o]< hold all general purpose functions in one location
#
#
global IMPORTED_FUNCTIONS
IMPORTED_FUNCTIONS = 1
import os
if(os.path.exists('../data/verbose')): 
    print("...imported:['./modules/functions.py']...")


from setup import *

############# FUNCTIONS #############


def b65ke(xyz):
    yzx = xyz.encode()
    zyx = base65536.encode(yzx)
#    b65k=open('data\\b65k.log','a')
#    a = type(zyx)
#    print(a)
#    b65k.write(zyx)
#    b65k.close()
    return zyx
#


def b65kd(zyx):
    xzy = base65536.decode(zyx)
#    print(xzy)
    xyz = xzy.decode()
#    print(xyz)
    return xyz
#


#[o_o]< check availability of the target without doing anything else to the data
def network_check(url):
    READY = 0
    TESTING_NETWORK = 1
    ERRORS = 0
    while(TESTING_NETWORK == 1):
        if(READY==0):
            while(READY==0):
                confirm = input("would you like to test the connection with "+url+"?: ")
                if(confirm=="n"):
                    target = input("What website would you like to check?: ")
                    if(target==""):
                        print("you didn't enter anything. if you want to cancel, type Exit")
                    confirm = input("would you like to test the connection with "+target+"?: ")
                    if(confirm=="n"):
                        target = input("What website would you like to check?: ")
                        if(target==""):target = url
                    elif(confirm=="y"):
                        target = url
                        READY = 1
                elif(confirm=="y"):
                    target = url
                    READY = 1
        print("testing internet connection")
        print(("target is: " + target))
        try:
            urllib.request.urlopen(target, timeout = 300)
            print("success!")
            return 1
        except (IOError, http.client.HTTPException):
            ERRORS = ERRORS + 1
            if(ERRORS==5):
                TESTING_NETWORK = 0
                FAILED = 1
                print("Failled a fifth time.. giving up for now")
                return 0
            print(("Failed... with " + ERRORS + " errors so far..."))
    return
#


def random_name(gender):
    CHOSEN=0
    while(CHOSEN==0):
        print("")
        print("RANDOM NAME SELECTOR: (a=any, f=female, m=male, r=robots, t=testing) ")
        print("If you do not type any input here it will default to 'any'")
        gender = input("which gender(s) would you like to choose from? >> ")
        if(gender==''): 
            gender = 'a'
        if(gender=='a') or (gender=='any'):
            CHOSEN = 1
            with open("data\\names\\female.txt", "r") as namefile:
                names = []
                lines  = 0
                for line in namefile:
                    names.append(line)
                    lines=lines+1
            with open("data\\names\\male.txt", "r") as namefile:
                for line in namefile:
                    names.append(line)
                    lines=lines+1
        elif(gender=='f'):
            CHOSEN = 1
            with open("data\\names\\female.txt", "r") as namefile:
                names = []
                lines  = 0
                for line in namefile:
                    names.append(line)
                    lines=lines+1
        elif(gender=='m'):
            CHOSEN = 1
            with open("data\\names\\male.txt", "r") as namefile:
                names = []
                lines  = 0
                for line in namefile:
                    names.append(line)
                    lines=lines+1
        elif(gender=='r'):
            CHOSEN = 1
            with open("data\\names\\robots.txt", "r") as namefile:
                names = []
                lines  = 0
                for line in namefile:
                    names.append(line)
                    lines=lines+1
        elif(gender=='t'):
            CHOSEN = 1
            with open("data\\names\\testing.txt", "r") as namefile:
                names = []
                lines  = 0
                for line in namefile:
                    names.append(line)
                    lines=lines+1
        else:
            print("error.. try again.")
    d2 = ''
    i=3
    CHOSEN=0
    j=0
    while(CHOSEN==0):
        d2 = names[random.randint(1, (lines-1))]
        d2 = d2.replace('\r', '')
        d2 = d2.replace('\n', '')
        random_name=d2
        if(random_name.find("#") == -1): 
            print("")
            print(("chose "+random_name+" as a random name."))
            user_choice = input("use this name? y or * >> ")
            if(user_choice=='y'): CHOSEN=1
    return random_name
#



def NYI(stated):
    global OP
    print(("Sorry, " + stated + " is not yet workable."))
    print("")
    time.sleep(1)
    OP = OP_Uncertain
    return OP
#






