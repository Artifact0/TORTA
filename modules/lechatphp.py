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
global IMPORTED_LECHATPHP
IMPORTED_LECHATPHP = 1
import os
if(os.path.exists('../data/verbose')): 
    print("...imported:['./modules/lechatphp.py']...")

############# IMPORTS #############

from setup import *
from functions import *
from colours import *
from targets import *

############# GLOBALS #############

global Kill_Signal


############# SETUP #############

#[o_o]< CAPTCHA check
#[o_o]< this should be turned into a one time front page scraper and parser
#[o_o]< which determines captcha presence based on known captcha form values
#[o_o]< rather than requiring the hard coding of a captcha use table

if(target==dans_v3):
    USE_CAPTCHA = 1
#
if(target==dans_v2):
    USE_CAPTCHA = 1
#
if(target==dans_clear):
    USE_CAPTCHA = 1
#
if(target==blackhatchat):
    USE_CAPTCHA = 1
#

USE_CAPTCHA = 1

USE_PROXY = 1

#[o_o]< PROXY SETUP
#[o_o]< useful if running on a machine where TOR is not enabled for all traffic by default
#[o_o]< recommended setup should be covered in the README
if(USE_PROXY==1):
    proxy_support = urllib.request.ProxyHandler({"http":"http://127.0.0.1:9150"})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
#


############# DIALOGUE #############





############# FUNCTIONS #############



def b65ke(xyz):
    yzx = xyz.encode()
    zyx = base65536.encode(yzx)
#    b65k=open('data/b65k.log','a')
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


def random_post(type_of_speech='null',volume='null'):
    CHOSEN=0
    while(CHOSEN==0):
        if(type_of_speech=='null'): 
            print("")
            print("RANDOM POST SELECTOR: ")
            print(" (n=nuetral, s=shitpost, q=question, f=fact, c=conspiracy) ")
            print("If you do not type any input here it will default to 'nuetral'")
            type_of_speech = input("which set would you like to choose from? >> ")
        if(type_of_speech==''): 
            type_of_speech = 'n'
        if(type_of_speech=='n') or (type_of_speech=='N') or (type_of_speech=='nuetral'):
            CHOSEN = 1
            with open("data/posts/nuetral.txt", "r") as postsfile:
                posts = []
                lines  = 0
                for line in postsfile:
                    posts.append(line)
                    lines=lines+1
        elif(type_of_speech=='s') or (type_of_speech=='S') or (type_of_speech=='shitpost'):
            CHOSEN = 1
            with open("data/posts/shitpost.txt", "r") as postsfile:
                posts = []
                lines  = 0
                for line in postsfile:
                    posts.append(line)
                    lines=lines+1
        elif(type_of_speech=='q') or (type_of_speech=='Q') or (type_of_speech=='question'):
            CHOSEN = 1
            with open("data/posts/question.txt", "r") as postsfile:
                posts = []
                lines  = 0
                for line in postsfile:
                    posts.append(line)
                    lines=lines+1
        elif(type_of_speech=='s') or (type_of_speech=='F') or (type_of_speech=='fact'):
            CHOSEN = 1
            with open("data/posts/fact.txt", "r") as postsfile:
                posts = []
                lines  = 0
                for line in postsfile:
                    posts.append(line)
                    lines=lines+1
        elif(type_of_speech=='c') or (type_of_speech=='C') or (type_of_speech=='conspiracy'):
            CHOSEN = 1
            with open("data/posts/conspiracy.txt", "r") as postsfile:
                posts = []
                lines  = 0
                for line in postsfile:
                    posts.append(line)
                    lines=lines+1
        else:
            print("error.. try again.")
    d2 = ''
    i=3
    CHOSEN=0
    j=0
    if(volume=="silent"):
        while(CHOSEN==0):
            d2 = posts[random.randint(1, (lines-1))]
            d2 = d2.replace('\r', '')
            d2 = d2.replace('\n', '')
            random_post=d2
            if(len(random_post) >=3):
                if(random_post.find("#") == -1):
                    CHOSEN=1
    else:
        while(CHOSEN==0):
            d2 = posts[random.randint(1, (lines-1))]
            d2 = d2.replace('\r', '')
            d2 = d2.replace('\n', '')
            random_post=d2
            if(len(random_post) >=3):
                if(random_post.find("#") == -1):
                    print("")
                    print(("choose "+random_post+" as a random name."))
                    user_choice = input("use this name? y or * >> ")
                    if(user_choice=='y'): CHOSEN=1
    return random_post
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
            with open("data/names/female.txt", "r") as namefile:
                names = []
                lines  = 0
                for line in namefile:
                    names.append(line)
                    lines=lines+1
            with open("data/names/male.txt", "r") as namefile:
                for line in namefile:
                    names.append(line)
                    lines=lines+1
        elif(gender=='f'):
            CHOSEN = 1
            with open("data/names/female.txt", "r") as namefile:
                names = []
                lines  = 0
                for line in namefile:
                    names.append(line)
                    lines=lines+1
        elif(gender=='m'):
            CHOSEN = 1
            with open("data/names/male.txt", "r") as namefile:
                names = []
                lines  = 0
                for line in namefile:
                    names.append(line)
                    lines=lines+1
        elif(gender=='r'):
            CHOSEN = 1
            with open("data/names/robots.txt", "r") as namefile:
                names = []
                lines  = 0
                for line in namefile:
                    names.append(line)
                    lines=lines+1
        elif(gender=='t'):
            CHOSEN = 1
            with open("data/names/testing.txt", "r") as namefile:
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
        if(len(random_name) >=3):
            if(random_name.find("#") == -1):
                print("")
                print(("choose "+random_name+" as a random name."))
                user_choice = input("use this name? y or * >> ")
                if(user_choice=='y'): CHOSEN=1
    return random_name
#


def Personae(choice):
    global nic
    global pas
    global User_Agent
    global col
    global DONECHOOSING
    DONECHOOSING = 0
    CHOSEN = 0
    Persona = choice
    TimesRan = 0
    while(DONECHOOSING==0):
        if(TimesRan==0): AvailPersonae = []
        print("")
        if(TimesRan>1):
            print("")
            print(("Available Personae include: " + str(AvailPersonae)))
            print("also you can enter 'c' or 'custom' to choose your own name")
            print("")
            print("default is Random if nothing else is typed")
            print("")
            time.sleep(1)
            Persona = input("Who would you like to be? ")
        if(Persona=="custom") or (Persona=="c"):
            pas = 'CHANGE_THIS'
            User_Agent = UA_tor
            while(CHOSEN==0):
                print("")
                user_name = input("please enter your custom name: ")
                user_choice = input("use this name("+user_name+")? y or * >> ")
                if(user_choice=='y'): CHOSEN=1
            nic = user_name
            DONECHOOSING = 1
        #[o_o]< MY ACCOUNTS
        #
        #
        #
        #
        # 025 - Pikachu
        if(TimesRan==0): AvailPersonae.append("Pikachu")
        if(Persona=="Pikachu"):
            nic = 'Pikachu'
            pas = 'h!ghv0lt4ge'
            User_Agent = UA_pkmn
            col = DfltClr_Yellow
            DONECHOOSING = 1
        #
        #
        #[o_o]< RANDOM
        #
        if(TimesRan==0): AvailPersonae.append("Random")
        if(Persona==""): Persona = "Random"
        if(Persona=="Random"):
            nic=random_name('choose')
            pas = 'changeme57475685676474'
            User_Agent = UA_tor
            col = DfltClr_random
            DONECHOOSING = 1
        TimesRan = TimesRan + 1
        time.sleep(1)
    return Persona
#


def frames_update(target,session):
    global LOGGED_IN
    meta_refresh = '<meta http-equiv="Refresh" content="15; URL=/chat.php?action=view&session='+session+'&lang=en">'
#    print(("session ["+session+"]"))
        #[o_o]< URLs for the LeChat frames
    frame_post = target + '?action=post&session=' + session
    frame_view = target + '?action=view&session=' + session
    frame_cntrl = target + '?action=control&session=' + session
    frame_help = target + '?action=help&session=' + session
    frame_profile = target + '?action=profile&session=' + session
    frame_admin = target + '?action=admin&session=' + session
    if(VERBOSE>2): 
        print(frame_post)
        print(frame_view)
        print(frame_cntrl)
        print(frame_help)
        print(frame_profile)
        print(frame_admin)
#    refresh_div_nc1 = frame_view.find('<div id="manualrefresh"><br>Manual refresh required<br><form action="/chat.php" enctype="multipart/form-data" method="post"><input type="hidden" name="lang" value="en"><input type="hidden" name="nc" value="')
#    refresh_div_nc2 = frame_view.find('"><input type="hidden" name="action" value="view"><input type="hidden" name="session" value="')
#    refresh_div_nc = frame_view[refresh_div_nc1:refresh_div_nc2]
#    refresh_div = '<div id="manualrefresh"><br>Manual refresh required<br><form action="/chat.php" enctype="multipart/form-data" method="post"><input type="hidden" name="lang" value="en"><input type="hidden" name="nc" value="'+refresh_div_nc+'"><input type="hidden" name="action" value="view"><input type="hidden" name="session" value="'+session+'"><input type="submit" value="Reload" ></form><br></div>'
    try:
        liveview = urllib.request.urlopen(frame_view, timeout = 300)
        frames_view = liveview.read().decode()
        frames_view.replace('<meta http-equiv="Refresh" content="15; URL=/chat.php?action=view&session=','<meta http-equiv="Refresh" content="15; URL=live.htm> <!-- ')
        frames_view.replace('&lang=en");}, 20000);</script>',' -->')
        frames_view.replace('<div id="manualrefresh"><br>Manual refresh required<br><form action=','<!-- ')
        frames_view.replace('"><input type="submit" value="Reload" ></form><br></div>',' -->')
#        viewframefile=codecs.open(livedir+'view.htm','w','utf-16')
#        viewframefile.write(str(frames_view))
#        viewframefile.close()
        logseqfile=open(datadir+'logseq.txt','r')
        logseq = int(logseqfile.read())
        logseqfile.close()
        frameset=codecs.open(datadir+'xLog'+str(logseq)+'.htm','w','utf-16')
        frameset.write(frames_view)
        frameset.close()
        livepost = urllib.request.urlopen(frame_post, timeout = 300)
        frames_post = livepost.read().decode()
        framepost=codecs.open(livedir+'post.htm','w','utf-16')
        framepost.write(frames_post)
        framepost.close()
        frames_view.replace(meta_refresh,'<meta http-equiv="Refresh" content="15; URL=live.htm>')
        frameset=codecs.open(livedir+'live.htm','w','utf-16')
        frameset.write(frames_view)
        frameset.close()
        logseq = logseq + 1
        logseqfile=open(datadir+'logseq.txt','w')
        logseqfile.write(str(logseq))
        logseqfile.close()
        print(("saved ["+datadir+"xLog"+str(logseq)+".htm]"))
#        time.sleep(1)
#        print("opening frameset log...")
#        time.sleep(1)
#        os.startfile(datadir+'xLog'+str(logseq-1)+'.htm')
#        if(VERBOSE >= 2): print(content)
    except (IOError, http.client.HTTPException):
        print("failed to save frames...")
#    if (LOGGED_IN == 2):
#        if frame_view.find('<body class="messages">') == -1:
#            LOGGED_IN = 0
#            Kill_Signal = 1
    return
#




def getframe_post(target,session):
    frame_post = target + '?action=post&session=' + session
    if(VERBOSE>2): 
        print(frame_post)
    try:
        liveview = urllib.request.urlopen(frame_post, timeout = 120)
        frames_post = liveview.read().decode()
        framedata=open(livedir+'post.htm','w')
        framedata.write(frames_post)
        framedata.close()
#        time.sleep(1)
    except (IOError, http.client.HTTPException):
        print("failed to save frames...")
    return
#



#[o_o]< this initial step gathers the login page data including CAPTCHA and nc/ verification value
def LEchatPHP_GetData(target):
    global content
    global LOGGED_IN
    LOGGED_IN = login_check('w',0)
    if(VERBOSE >= 2): print("------------- LEchatPHP_GetData start -------------")
    print(("Target = " + target))
        #[o_o]< Add our headers
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', User_Agent)]
        #[o_o]< Install our opener (note that this changes the global opener to the one
        #[o_o]< we just made, but you can also just call opener.open() if you want)
    urllib.request.install_opener(opener)
    req = urllib.request.Request(url)
        #[o_o]< Make the request and read the response
#    response = urllib.request.urlopen(req, timeout = 120
    FAILS = 0
    while(LOGGED_IN==0):
        if(FAILS == 5):
            return
        try:
            response = urllib.request.urlopen(req, timeout = 150)
            LOGGED_IN = login_check('w',1)
            print("grabbed login page successfully!")
        except (IOError, http.client.HTTPException):
#            print(httplib.HTTPException)
            FAILS = FAILS + 1
            print("failed... trying again...")
    content = response.read().decode()
    if(VERBOSE >= 2): print(content)
    #print("this should be an error handler ;p")
    print("attempting to isolate login data from page...")
    cbeft='<tr id="captcha"><td>Copy:<br>'
    cbef = content.find(cbeft,0)
    caft = content.find('</td><td><input type="hidden" name="challenge"')
    cap1 = content[len(cbeft):caft]
#    print(cap1)
    cap2 = cap1[cbef:caft]
    vbef = content.find('<input type="hidden" name="challenge" value="')
    vaft = content.find('<input type="text" name="captcha"')
    val1 = content[vbef:vaft]
    len1 = len(val1)
    len2 = len1 - 2
#    print("val1 = " + val1)
    val2 = val1[45:len2]
    cap = cap2
    val = val2
#    print("saved credentials")
    capfile=open(datadir+'cap.htm','w')
    captcha_header = "<html><head><title>"+nic+"'s CAPTCHA</title></head><body><center>"
    captcha_footer = "</center></body></html>"    
    captcha_page = captcha_header + cap + captcha_footer
    capfile.write(captcha_page)
    capfile.close()
    valfile=open(datadir+'val.txt','w')
    valfile.write(val)
    valfile.close()
    if(VERBOSE >= 2): print("------------- LEchatPHP_GetData end -------------")
    return
#width="55" height="24" 

#[o_o]< need to add a 'wrong CAPTCHA' event handler
#[o_o]<  using code from the waiting room check
def captcha_solve():
    if(VERBOSE >= 2): print("------------- captcha_solve start -------------")
    openerer = "open" if sys.platform == "darwin" else "xdg-open"
    text = input("solve the captcha:")
    cap3file=open(datadir+'sol.txt','w')
    cap3file.write(text)
    cap3file.close()
    subprocess.call([openerer, (datadir+'cap.htm')])
    if(VERBOSE >= 2): print("------------- captcha_solve end -------------")
#


#[o_o]< called after login, and will pass through silently if it doesn't detect
#[o_o]< a wating room screen. it looked for "your login has been delayed"
#[o_o]< and next checks for whether it has a time or says to wait for moderator
#[o_o]< both are currently handled by a different loop, but may be merged in an update
def waiting_room_handler(content):
    if(VERBOSE >= 2): print("------------- waiting_room_handler start -------------")
    MOD_APPROVAL_ON = 0
    WAITING = 0
    HAD_TO_WAIT = 0
    wait_time = 0
    session_found = 0
    pagedata = content    
    if pagedata.find("your login has been delayed") != -1:
        print("Waiting Room Handler engaged..")
        WAITING = 1
        HAD_TO_WAIT = 1
    if pagedata.find("moderator") != -1:
        MOD_APPROVAL_ON = 1
    if (MOD_APPROVAL_ON == 0): 
        while (WAITING == 1):
            print("")
                #[o_o]< find wait time
            wt_bef = content.find('you can access the chat in ')
            wt_aft = content.find(' seconds.</p>')
            wt_tmp = content[wt_bef:wt_aft]
            wt1 = len(wt_tmp)
            wt2 = wt1 - 13
            wt3 = wt_tmp[27:wt1]
            wait_time = int(wt3)
            print(("wait time set to: " + str(wait_time)))
                #[o_o]< waiting room session finder
            if(session_found==0):
                print("attempting to isolate sessionID from page...")
                sbef = content.find('<input type="hidden" name="session" value="')
                saft = content.find('"><input type="submit" value="Reload" >')
                sess1 = content[sbef:saft]
                len1 = len(sess1)
                len2 = len1 - 39
                sess2 = sess1[43:len1]
    #            print(sess1)
    #           print("sessionID is: " + sess2)
                session = sess2
                print(("sessionID is saved as: " + session))
                wsf=open(datadir+'wsess.txt','w')
                wsf.write(session)
                wsf.close()
                session_found = 1
                #[o_o]< NC/ Next PostID / post verification value finder
                #[o_o]<    if(VERBOSE >= 2): print(content)
#           print("this should be an error handler ;p")
            print("attempting to isolate next postID from post box...")
            string1 = '<input type="hidden" name="nc" value="'
            string2 = '"><input type="hidden" name="action" value='
            pid_bef = content.find(string1)
            pid_aft = content.find(string2)
            pid1 = content[pid_bef:pid_aft]
            len1 = len(pid1)
            len2 = len1 - len(string2)
            pid2 = pid1[38:len1]
#           print(pid1)
#           print("sessionID is: " + pid2)
            npid = pid2
#           print("next post ID is: " + npid)
            npidf=open(datadir+'wnpid.txt','w')
            npidf.write(session)
            npidf.close()
            time.sleep(wait_time+10)
            send_message = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
            post_data = urllib.parse.urlencode({
                                        'lang'  : 'en',
                                        'nc'  : npid,
                                        'action'  : 'wait',
                                        'session' : session})
            req = urllib.request.Request(url+"?action=post&session="+session+"&lang=en")
            content = send_message.open(url, post_data.encode()).read().decode()
            if content.find("your login has been delayed") < 1:
                WAITING = 0
    if (MOD_APPROVAL_ON == 1): 
        while (WAITING == 1):
            wait_time = 15
            print("waiting for moderator approval...")
            time.sleep(wait_time)
            print("checking back every 15 seconds or so...")
                #[o_o]< waiting room session finder
            if(session_found==0):
                print("attempting to isolate sessionID from page...")
                sbef = content.find('<input type="hidden" name="session" value="')
                saft = content.find('"><input type="submit" value="Reload" >')
                sess1 = content[sbef:saft]
                len1 = len(sess1)
                len2 = len1 - 39
                sess2 = sess1[43:len1]
                print(sess1)
#               print("sessionID is: " + sess2)
                session = sess2
                print(("sessionID is saved as: " + session))
                wsf=open(datadir+'wsess.txt','w')
                wsf.write(session)
                wsf.close()
                session_found = 1
                #[o_o]< NC/ Next PostID / post verification value finder
                #    if(VERBOSE >= 2): print(content)
#           print("this should be an error handler ;p")
            print("isolating next postID from page...")
            string1 = '<input type="hidden" name="nc" value="'
            string2 = '"><input type="hidden" name="action" value='
            pid_bef = content.find(string1)
            pid_aft = content.find(string2)
            pid1 = content[pid_bef:pid_aft]
            len1 = len(pid1)
            len2 = len1 - len(string2)
            pid2 = pid1[38:len1]
#           print(pid1)
#           print("sessionID is: " + pid2)
            npid = pid2
#           print("next post ID is: " + npid)
            npidf=open(datadir+'wnpid.txt','w')
            npidf.write(session)
            npidf.close()
            send_message = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
            post_data = urllib.parse.urlencode({
                                        'lang'  : 'en',
                                        'nc'  : npid,
                                        'action'  : 'wait',
                                        'session' : session})
            req = urllib.request.Request(url+"?action=post&session="+session+"&lang=en")
            content = send_message.open(url, post_data.encode()).read().decode()
            #[o_o]< add "you have been kicked" support
            #[o_o]< add timedout support
            if content.find("your login has been delayed") < 1:
                WAITING = 0
    if HAD_TO_WAIT == 1:
        print("had to wait")
    if(VERBOSE >= 2): print("------------- waiting_room_handler end -------------")
    return content
#


#[o_o]< once CAPTCHA is solved, and information is confirmed (confirmations not built in yet)
#[o_o]< then it is time to enter the data into the form and LOG IN - then write session info to a file
def LEchatPHP_login(target,nic,pas,cap,val,col):
    global LOGGED_IN
    global content
    LOGGED_IN = login_check('r', 0)
    if(VERBOSE >= 2): print("------------- LEchatPHP_login start -------------")
#    print("Attempting Login @ " + target)
    capfile=open(datadir+'sol.txt','r')
    cap = capfile.read()
    capfile.close()
    valfile=open(datadir+'val.txt','r')
    val = valfile.read()
    valfile.close()
    url = target
        #[o_o]< Add our headers
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', User_Agent)]
        #[o_o]< Install our opener (note that this changes the global opener to the one
        #[o_o]< we just made, but you can also just call opener.open() if you want)
    urllib.request.install_opener(opener)
    print("action    : login")
    print(("nickname  : " + nic))
    print(("password  : " + pas))
    print(("CAPTCHA   : " + cap))
    print(("challenge : " + val))
    print(("colour    : " + col))
        #[o_o]< Input parameters we are going to send
    authdat = {
      'action'    : 'login',
      'nick'      : nic,
      'pass'      : pas,
      'captcha'   : cap,
      'challenge' : val,
      'colour'    : col
      }
        #[o_o]< Use urllib to encode the payload
    login_data = urllib.parse.urlencode(authdat)
        #[o_o]< Build our Request object (supplying 'data' makes it a POST)
    req = urllib.request.Request(url, login_data.encode())
        #[o_o]< Make the request and read the response
#    response = urllib2.urlopen(req, timeout = 60)
    count = 0
    while(LOGGED_IN==1):
        try:
            response = urllib.request.urlopen(req, timeout = 120)
            print("checking for successful login")
            content = response.read().decode()
            count = count+1
            if(count==5): 
            	Exit
            if(VERBOSE >= 2): print(content)
            content = waiting_room_handler(content)
        except (IOError, http.client.HTTPException):
            print("failed... trying again...")
        if(content.find("your login has been delayed") == -1):
            if(content.find("Error") == -1):
                LOGGED_IN = login_check('w',2)
#    text = raw_input("turn this into a login restart option, y or n:")
    print("attempting to isolate sessionID from page...")
    sbef = content.find('?action=controls&session=')
    saft = content.find('<noframes>')
    sess1 = content[sbef:saft]
    len1 = len(sess1)
    len2 = len1 - 10
    sess2 = sess1[25:len1]    
    print(sess1)
#    print("sessionID is: " + sess2)
    session = sess2
#    print("sessionID is saved as: " + session)
#    if(VERBOSE>0):
    sf=open(datadir+'sess.txt','w')
    sf.write(session)
    sf.close()
    if(len(session)==32):
        LOGGED_IN = login_check('w',2)
    if(VERBOSE >= 2): print("------------- LEchatPHP_login end -------------")
    return
#


#[o_o]< scrapes the POST frame to look for "nc" value, which wasn't required in PERL
#[o_o]< and is not required for first post on PHP, but to post more than once, the
#[o_o]< "nc" value as the PHP calls it, or "npid"/"next post ID" as I call it, must
#[o_o]< be included with the post. this may also be needed for admin functions, etc- not sure
#[o_o]< probably used internally to prevent duplicate posts, etc. idk yet without looking at PHP
def find_next_postID(session):
    received = 0
    fails = 0
    req = urllib.request.Request(url+"?action=post&session="+session+"&lang=en")
    while (received == 0):
        try:
            response = urllib.request.urlopen(req, timeout = 300)
            received = 1
        except (IOError, http.client.HTTPException):
            print("failed to load the frame... trying again....")
            fails = fails + 1
        if (fails > 10):
            global Kill_Signal
            Kill_Signal = 1
            return
    content = response.read().decode()
#    if(VERBOSE >= 2): print(content)
#    print("this should be an error handler ;p")
    print("attempting to isolate next postID from post box...")
    string1 = '<input type="hidden" name="nc" value="'
    string2 = '"><input type="hidden" name="action" value="post">'
    pid_bef = content.find(string1)
    pid_aft = content.find(string2)
    pid1 = content[pid_bef:pid_aft]
    len1 = len(pid1)
    len2 = len1 - len(string2)
    pid2 = pid1[38:len1]
#    print(pid1)
#    print("sessionID is: " + pid2)
    npid = pid2
#    print("next post ID is: " + npid)
    sf=open(datadir+'npid.txt','w')
    sf.write(session)
    sf.close()
    return npid
#


#[o_o]< sends logout action, with sessionID
def netchat_logout():
    global session
    if(VERBOSE >= 2): print("-------------BEGIN netchat_logout-------------")
    send_action = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
        #[o_o]< retreive session info from sess.txt
    get_session()
    print(session)
        #[o_o]< Input parameters we are going to send
    post_data = urllib.parse.urlencode({  'action': 'logout',
                                    'session': session})
    content = send_action.open(url, post_data.encode()).read().decode()
#    if(VERBOSE >= 2): print(content)
    print("was logout successful?")
    if(VERBOSE >= 2): print("------------- END netchat_logout -------------")
    return
#


#[o_o]< pulls sessionID from file where it was saved during login
def get_session():
    global session
    if(VERBOSE >= 2): print("-------------BEGIN get_session-------------")
    sf = open(datadir+"sess.txt", "r")
    stemp = str(sf.read(32))
    session = stemp
    if(VERBOSE >= 1): print("")
    if(VERBOSE >= 1): print(("sessionID is: " + session))
    if(VERBOSE >= 2): print("------------- END get_session -------------")
    return session
#


#[o_o]< as it appears, sends message to staff - if it has that privilege
def netchat_msg_admin(msg):
    if(VERBOSE >= 2): print("-------------BEGIN netchat_msg_staff-------------")
    get_session()
  #[o_o]<  print(session)
    send_message = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
    post_data = urllib.parse.urlencode({  'action'  : 'post',
                                    'session' : session,
                                    'postid'  : '',
                                    'multi'   : '',
                                    'message' : msg,
                                    'sendto'  : 's &amp;'})
    content = send_message.open(url, post_data.encode()).read().decode()
  #  if(VERBOSE >= 2): print(content)
    if(VERBOSE >= 2): print("------------- END netchat_msg_staff -------------")
    return
#



#[o_o]< as it appears, sends message to staff - if it has that privilege
def netchat_msg_staff(msg):
    if(VERBOSE >= 2): print("-------------BEGIN netchat_msg_staff-------------")
    get_session()
  #[o_o]<  print(session)
    send_message = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
    post_data = urllib.parse.urlencode({  'action'  : 'post',
                                    'session' : session,
                                    'postid'  : '',
                                    'multi'   : '',
                                    'message' : msg,
                                    'sendto'  : 's #'})
    content = send_message.open(url, post_data.encode()).read().decode()
  #  if(VERBOSE >= 2): print(content)
    if(VERBOSE >= 2): print("------------- END netchat_msg_staff -------------")
    return
#


#[o_o]< sends message to members
def netchat_msg_members(msg):
    if(VERBOSE >= 2): print("-------------BEGIN netchat_msg_staff-------------")
    get_session()
  #[o_o]<  print(session)
    send_message = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
    post_data = urllib.parse.urlencode({  'action'  : 'post',
                                    'session' : session,
                                    'postid'  : '',
                                    'multi'   : '',
                                    'message' : msg,
                                    'sendto'  : 's ?'})
    content = send_message.open(url, post_data.encode()).read().decode()
  #  if(VERBOSE >= 2): print(content)
    if(VERBOSE >= 2): print("------------- END netchat_msg_staff -------------")
    return
#


#[o_o]< message to all
def netchat_msg_all(msg):
    if(VERBOSE >= 2): print("-------------BEGIN netchat_msg_all-------------")
    get_session()
    npid = find_next_postID(session)
#    print(session)
    send_message = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
    post_data = urllib.parse.urlencode({  'action'  : 'post',
                                    'session' : session,
                                    'postid'  : npid,
                                    'multi'   : '',
                                    'message' : msg,
                                    'sendto'  : 's *'})
    content = send_message.open(url, post_data.encode()).read().decode()
    if(VERBOSE >= 2): print(content)
    if(VERBOSE >= 2): print("------------- END netchat_msg_all -------------")
    return
#


#[o_o]< send a PM - in PERL version, everybody's name was assigned a unique numeric ID
#[o_o]< that numeral was used in the PM system on the original LEchat. on Daniel's PHP it
#[o_o]< is done with a case sensitive string. much easier to find the name anywhere it is used,
#[o_o]< including VIEW frame, rather than have to pull it from the list/menu options on the POST frame
def netchat_msg_PM(recip,msg,sendfile):
    fileshare = sendfile
    if(VERBOSE >= 2): print("-------------BEGIN netchat_msg_PM-------------")
    get_session()
    npid = find_next_postID(session)
    print(("attempting a pm to " + recip))
#    text = input("this could be a confirm/cancel check. but juts waits for enter")
    send_message = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
    post_data = urllib.parse.urlencode({  'action'  : 'post',
                                    'session' : session,
                                    'postid'  : npid,
                                    'multi'   : '',
                                    'message' : msg,
                                    'sendto'  : recip,
                                    'file'    : fileshare})
    content = send_message.open(url, post_data.encode()).read().decode()
    if(VERBOSE >= 3):     print(post_data)
    if(VERBOSE >= 2): print(content)
    if(VERBOSE >= 2): print("------------- END netchat_msg_PM -------------")
    return
#



#[o_o]< 
def Login_Daniels():
    global CAPTCHA_SOLVED
    global LOGGED_IN
    if(VERBOSE >= 2): print("------------- Login_Daniels start -------------")
    if(LOGGED_IN == 0):
        CAPTCHA_SOLVED = 0
        LEchatPHP_GetData(target)
    if(LOGGED_IN==1):
        if(USE_CAPTCHA==1):
            if(CAPTCHA_SOLVED==0): 
                captcha_solve()
                CAPTCHA_SOLVED = 1
            LEchatPHP_login(target,nic,pas,cap,val,col)
        if(USE_CAPTCHA==0):
            LEchatPHP_login(target,nic,pas,col)
    if(VERBOSE >= 2): print("------------- Login_Daniels end -------------")
#


#[o_o]< opens login file, in  read or write mode
def login_check(mode, current):
    if(VERBOSE >= 2): print("------------- login_check start -------------")
    filemode = mode
    LOGGED_IN = current
    logincheck = LOGGED_IN
    if(filemode=="r"):
        loginfile=open(datadir+'login.txt','r')
        logincheck = int(loginfile.read())
        loginfile.close()
    if(filemode=="w"):
        loginfile=open(datadir+'login.txt','w')
        loginfile.write(str(LOGGED_IN))
        loginfile.close()
#    os.startfile('data\\cap.htm')
#    text = raw_input("solve the captcha:")
    if(VERBOSE >= 2): print("------------- login_check end -------------")
    return logincheck
#









def netchat_delete(howmuch):
    get_session()
    npid = find_next_postID(session)
    if(howmuch=="last"):
        print("deleting last message...")
#        text = input("this could be a confirm/cancel check. but juts waits for enter")
        delete_message = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
        post_data = urllib.parse.urlencode({  'action'  : 'delete',
                                            'session' : session,
                                            'nc'  : npid,
                                            'what' : 'last'})
        content = delete_message.open(url, post_data.encode()).read().decode()
    if(howmuch=="all"):
#        text = input("this could be a confirm/cancel check. but juts waits for enter")
        delete_message = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
        post_data = urllib.parse.urlencode({  'action'  : 'delete',
                                            'session' : session,
                                            'nc'  : npid,
                                            'what' : 'all'})
        content = delete_message.open(url, post_data.encode()).read().decode()
        time.sleep(1)
        confirmation = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
        post_data = urllib.parse.urlencode({  'action'  : 'delete',
                                            'confirm' : 'yes',
                                            'session' : session,
                                            'nc'  : npid,
                                            'what' : 'all'})
        content = confirmation.open(url, post_data.encode()).read().decode()
    time.sleep(1)
    return
#




def netchat_sendfile(whatfile):
    print("not yet implemented")
    time.sleep(1)
    return
#


















def send_admin():
    frame_admin = target + '?action=admin&session=' + session
    try:
        liveview = urllib.request.urlopen(frame_admin, timeout = 120)
        frames_admin = liveview.read().decode()
        framedata=open(livedir+'admin.htm','w')
        framedata.write(frames_admin)
        framedata.close()
    except (IOError, http.client.HTTPException):
        print("failed to save frames...")
    try:
#        frames_update(target,session)
        os.startfile(livedir+'admin.htm')
    except (IOError):
        print("failed to open frameset...")
    return
#    




def send_setup():
    frame_setup = target + '?action=setup&session=' + session
    try:
        liveview = urllib.request.urlopen(frame_setup, timeout = 120)
        frames_setup = liveview.read().decode()
        framedata=open(livedir+'setup.htm','w')
        framedata.write(frames_setup)
        framedata.close()
    except (IOError, http.client.HTTPException):
        print("failed to save frames...")
    try:
#        frames_update(target,session)
        os.startfile(livedir+'setup.htm')
    except (IOError):
        print("failed to open frameset...")
    return
#
    return
#






def send_profile():
    frame_profile = target + '?action=profile&session=' + session
    try:
        liveview = urllib.request.urlopen(frame_profile, timeout = 120)
        frames_profile = liveview.read().decode()
        framedata=codecs.open(livedir+'profile.htm','w','utf-16')
        framedata.write(frames_profile)
        framedata.close()
    except (IOError, http.client.HTTPException):
        print("failed to save frames...")
    try:
#        frames_update(target,session)
        os.startfile(livedir+'profile.htm')
    except (IOError):
        print("failed to open frameset...")
    return
#
    return
#






def send_help():
    frame_help = target + '?action=help&session=' + session
    try:
        liveview = urllib.request.urlopen(frame_help, timeout = 120)
        frames_help = liveview.read().decode()
        framedata=open(livedir+'help.htm','w')
        framedata.write(frames_help)
        framedata.close()
    except (IOError, http.client.HTTPException):
        print("failed to save frames...")
    try:
#        frames_update(target,session)
        os.startfile(livedir+'help.htm')
    except (IOError):
        print("failed to open frameset...")
    return
#
    return
#






def send_notes():
    frame_notes = target + '?action=notes&session=' + session
    try:
        liveview = urllib.request.urlopen(frame_notes, timeout = 120)
        frames_notes = liveview.read().decode()
        framedata=open(livedir+'notes.htm','w')
        framedata.write(frames_notes)
        framedata.close()
    except (IOError, http.client.HTTPException):
        print("failed to save frames...")
    try:
#        frames_update(target,session)
        os.startfile(livedir+'notes.htm')
    except (IOError):
        print("failed to open frameset...")
    return
#
    return
#






def logger():
    global logs
    return






def Concatenate_Logs():
    print("not yet implemented")
    return
# open all xLog files files in every perseq/data folder
# create new log file for every day, and append every non-duplicate post
# delete all posts from Bibu to Zorg and vice-versa
# create new dir for each month, and save each daily log in proper dir
# also add in all unique messages from logs saved into Dossier folders





# for multi line, add &"multi","on" /  &multi=on

def LEchatPHP(chosen='null'):
    global LOGGED_IN
    global url
    global target
    Kill_Signal = 0
    target = Targetting()
    url = target
#    reset_login = raw_input("reset login? (n or *): ")
    reset_login = 'y'
    if(reset_login=='n'): 
        LOGGED_IN = login_check('r',0)
    else:
        Personae("null")
        LOGGED_IN = login_check('w',0)
    while(LOGGED_IN<2):
        try:
            Login_Daniels()
#            if(len(sess)==32):
#                print("login seems to have succeeded")
        except():
            print("failed login, try again?")
    session=get_session()
    frames_update(target,session)
    try:
        os.startfile(livedir+'index.htm')
    except (IOError):
        print("failed to open frameset...")
    time.sleep(1)
    while(LOGGED_IN==2):
        print("OPTIONS: config help profile admin notes links logout")
        print("a / all , p / pm , m / members , s / staff")
        print("all-b64 , all-b65k , pm-b64 , pm-b65k")
        print("delete-last, delete-all, send-file, r / refresh")
        print("")
        User_Input = input("What next?: ")
        if(User_Input=="config") or (User_Input=="Config") or (User_Input=="c") or (User_Input=="C"):
            print("config not implemented yet")
            time.sleep(1)
        elif(User_Input=="all") or (User_Input=="All") or (User_Input=="a") or (User_Input=="A"):
            netchat_msg_all(input("What do you want to say to [all]?: "))
            frames_update(target,session)
            time.sleep(1)
        elif(User_Input=="members") or (User_Input=="m") or (User_Input=="Members") or (User_Input=="M"):
            netchat_msg_members(input("What do you want to say to [members]?: "))
            frames_update(target,session)
            time.sleep(1)
        elif(User_Input=="staff") or (User_Input=="Staff") or (User_Input=="s") or (User_Input=="S"):
            netchat_msg_staff(input("What do you want to say to [staff]?: "))
            frames_update(target,session)
            time.sleep(1)
        elif(User_Input=="admin") or (User_Input=="Admin") or (User_Input=="adm") or (User_Input=="ADMIN"):
            netchat_msg_admin(input("What do you want to say to [Admin]?: "))
            frames_update(target,session)
            time.sleep(1)
        elif(User_Input=="pm") or (User_Input=="p") or (User_Input=="PM") or (User_Input=="P"):
            netchat_msg_PM(input("Who do you want to PM?: @"),input("What do you want to say to them?: "),sendfile)
            frames_update(target,session)
            time.sleep(1)
        elif(User_Input=="all-b64"):
            netchat_msg_all(b64encode(input("What do you want to say to all in base64?: ").encode()))
            frames_update(target,session)
            time.sleep(1)
        elif(User_Input=="all-b65k"):
            netchat_msg_all(b65ke(input("What do you want to say to all in base65536?: ")))
            frames_update(target,session)
            time.sleep(1)
        elif(User_Input=="pm-b64"):
            netchat_msg_PM(input("Who do you want to PM b64 encoded data to?: @"),b64encode(input("What do you want to say to them in b65k?: ").encode()),sendfile)
            frames_update(target,session)
            time.sleep(1)
        elif(User_Input=="pm-b65k"):
            netchat_msg_PM(input("Who do you want to PM b65k encoded data to?: @"),b65ke(input("What do you want to say to them in b65k?: ")),sendfile)
            frames_update(target,session)
            time.sleep(1)
        elif(User_Input=="delete-last"):
            print("delete last message")
            netchat_delete("last")
            frames_update(target,session)
            time.sleep(1)
        elif(User_Input=="delete-all"):
            print("delete all messages")
            netchat_delete("all")
            frames_update(target,session)
            time.sleep(1)
        elif(User_Input=="send-file"):
            netchat_sendfile("./null/")
            frames_update(target,session)
            time.sleep(1)
        elif(User_Input=="profile"):
            send_profile()
            time.sleep(1)
        elif(User_Input=="links"):
            get_links(target,session)
        elif(User_Input=="help") or (User_Input=="Help") or (User_Input=="h") or (User_Input=="H"):
            send_help()
            time.sleep(1)
        elif(User_Input=="admin"):
            send_admin()
            time.sleep(1)
        elif(User_Input=="setup"):
            send_setup()
            time.sleep(1)
        elif(User_Input=="notes") or (User_Input=="Notes") or (User_Input=="n") or (User_Input=="N"):
            send_notes()
            time.sleep(1)
        elif(User_Input=="logout"):
            LOGGED_IN = 0
            netchat_logout()
            time.sleep(1)
        elif(User_Input=="refresh") or (User_Input=="Refresh") or (User_Input=="r") or (User_Input=="R"):
            frames_update(target,session)
            time.sleep(1)
        elif(User_Input=="test") or (User_Input=="TEST") or (User_Input=="Test") or (User_Input=="t") or (User_Input=="T"):
            troll_test(input("\* (p)m or (a)ll :: "),input("\* (c)onspiracy, (f)act, (n)uetral, (s)hitpost, (q)uestion :: "))
            LOGGED_IN = 0
            netchat_logout()
            time.sleep(1)
        elif(User_Input=="logbot"):
            minutes = 0
            cycles = 0
            hours = 0
            days = 0
            whotopm = input("who will be your anti-timout pm recipient?: @")
            print("starting chat monitoring process")
#            netchat_msg_all("Hello World")
            while(Kill_Signal == 0):
                time.sleep(30)
                frames_update(target,session)
                time.sleep(30)
                frames_update(target,session)
                minutes = minutes + 1
                if(minutes == 10):
                    minutes = 0
                    cycles = cycles + 1
                    if(cycles == 6):
                        hours = hours + 1
                        cycles = 0
                        netchat_msg_PM(whotopm,".",sendfile)
                        netchat_delete("last")
                    else:
                        netchat_msg_PM(".",".",sendfile)
                        netchat_delete("last")
                if(hours == 24):
                    hours = 0
                    days = days + 1
                #add a divider to change time into hours and minutes
                print("has been running for ~" + str(days) + " days, " + str(hours) + " hours, and " + str((cycles * 10) + minutes) + " minutes.")
        else:
            print("sorry, I didn't understand that command")
    return status












# Add Morse Code module
