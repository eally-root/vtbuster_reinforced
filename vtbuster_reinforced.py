# VTBUSTER REINFORCED FINAL PROJECT

# IMPORTS

import os
import re
import time
from selenium.webdriver import Chrome
from selenium import webdriver

# VARIABLES

thor_time_by_second = 601                #                           -Thor           = 10 Minutes
intezervt_time_by_second = 7201          #                           -intezervt      = 2 Hours
dnwls0719_time_by_second = 86401         #   DEFAULT TIME VAULE's    -dnwls0719      = 1 Day
sentoryn_time_by_second = 120961         #                           -Sentoryn       = 1.4 Days
alinvirusnever_time_by_second = 604801   #                           -Alinvirusnever = 3.5 Days

optional_Proxy = "0"

tagpool = []

# CHROMEDRIVER SETTINGS

print("""
This script uses selenium for python,
Before using this you need to install chromedriver.

Type chromedriver's location path
""")
wdriver = input("chromedriver location: ")
os.system('cls')

# USER INTERFACE

os.system('cls')

print("""
VIRUSTOTAL BUSTER REINFORCED

"start" for start.
"options" for see all options.
"exit" for exit.
""")

while True:
    first_input = input()

    if first_input == "start":
        os.system('cls')

        # PROXY CHECK
        if optional_Proxy == "0":
            os.system('cls')
        else:
            webdriver.DesiredCapabilities.CHROME['proxy']={
                "httpProxy":optional_Proxy,
                "ftpProxy":optional_Proxy,
                "sslProxy":optional_Proxy,
                "noProxy":None,
                "proxyType":"MANUAL",
                "autodetect":False
            }
            os.system('cls')
        
        # THOR SCRIPT STARTS #
        driver = Chrome(wdriver)
        f = open("./hash_list_busters.txt","a")

        x = 0
        looptime = 160

        driver.get("https://www.virustotal.com/en/user/thor/")

        while x < (looptime - 1):
            driver.execute_script("javascript:more('comments')")
            x += 1
        time.sleep(1)

        hashes = driver.find_elements_by_class_name("margin-left-1")
        comments = driver.find_elements_by_class_name("comment-text")
        time.sleep(1)

        for i in range(len(comments)):
            tagpool.append(re.findall(r'(?i)\#\w+', comments[i].text))

        num_pages_hashes = len(hashes)
        for i in range(num_pages_hashes):
            f.write("'hashtype':'sha256','hash':'" + hashes[i].text[5:] + "','source':'thor','tags':'"+ str(tagpool[i])[1:-1].lower().replace("'","") + "'\n")

        tagpool = []
        f.close()
        driver.close()
        # THOR SCRIPT ENDS #
        time.sleep(1)
        # INTEZERVT SCRIPT STARTS #
        driver = Chrome(wdriver)
        f = open("./hash_list_busters.txt","a")

        x = 0
        looptime = 2

        driver.get("https://www.virustotal.com/en/user/intezervt/")

        while x < (looptime - 1):
            driver.execute_script("javascript:more('comments')")
            x += 1
        time.sleep(1)

        hashes = driver.find_elements_by_class_name("margin-left-1")
        comments = driver.find_elements_by_class_name("comment-text")
        time.sleep(1)

        for i in range(len(comments)):
            tagpool.append(re.findall(r'(?i)\#\w+', comments[i].text))
            tagpool[i].pop(-1)


        num_pages_hashes = len(hashes)
        for i in range(num_pages_hashes):
            f.write("'hashtype':'sha256','hash':'" + hashes[i].text[5:] + "','source':'intezervt','tags':'"+ str(tagpool[i])[1:-1].lower().replace("'","") + "'\n")

        tagpool = []
        f.close()
        driver.close()
        # INTEZERVT SCRIPT ENDS #
        time.sleep(1)
        # DNWLS0719 SCRIPT STARTS #
        driver = Chrome(wdriver)
        f = open("./hash_list_busters.txt","a")

        x = 0
        looptime = 1

        driver.get("https://www.virustotal.com/en/user/dnwls0719/")

        while x < (looptime - 1):
            driver.execute_script("javascript:more('comments')")
            x += 1
        time.sleep(1)

        hashes = driver.find_elements_by_class_name("margin-left-1")
        comments = driver.find_elements_by_class_name("comment-text")
        time.sleep(1)

        for i in range(len(comments)):
            tagpool.append(re.findall(r'(?i)\#\w+', comments[i].text))

        num_pages_hashes = len(hashes)
        for i in range(num_pages_hashes):
            f.write("'hashtype':'sha256','hash':'" + hashes[i].text[5:] + "','source':'dnwls0719','tags':'"+ str(tagpool[i])[1:-1].lower().replace("'","") + "'\n")

        tagpool = []
        f.close()
        driver.close()
        # DNWLS0719 SCRIPT ENDS #
        time.sleep(1)
        # SENTORYN SCRIPT STARTS #
        driver = Chrome(wdriver)
        f = open("./hash_list_busters.txt","a")

        x = 0
        looptime = 1

        driver.get("https://www.virustotal.com/en/user/Sentoryn/")

        while x < (looptime - 1):
            driver.execute_script("javascript:more('comments')")
            x += 1
        time.sleep(1)

        hashes = driver.find_elements_by_class_name("margin-left-1")
        comments = driver.find_elements_by_class_name("comment-text")
        time.sleep(1)

        for i in range(len(comments)):
            tagpool.append(re.findall(r'(?i)\#\w+', comments[i].text))

        num_pages_hashes = len(hashes)
        for i in range(num_pages_hashes):
            f.write("'hashtype':'sha256','hash':'" + hashes[i].text[5:] + "','source':'sentoryn','tags':'"+ str(tagpool[i])[1:-1].lower().replace("'","") + "'\n")

        tagpool = []
        f.close()
        driver.close()
        # SENTORYN SCRIPT ENDS #
        time.sleep(1)
        # ALINVIRUSNEVER SCRIPT STARTS #
        driver = Chrome(wdriver)
        f = open("./hash_list_busters.txt","a")

        x = 0
        looptime = 1

        driver.get("https://www.virustotal.com/en/user/AlinVirusnever/")

        while x < (looptime - 1):
            driver.execute_script("javascript:more('comments')")
            x += 1
        time.sleep(1)

        hashes = driver.find_elements_by_class_name("margin-left-1")
        comments = driver.find_elements_by_class_name("comment-text")
        time.sleep(1)

        for i in range(len(comments)):
            tagpool.append(re.findall(r'(?i)\#\w+', comments[i].text))
            
        num_pages_hashes = len(hashes)
        for i in range(num_pages_hashes):
            f.write("'hashtype':'sha256','hash':'" + hashes[i].text[5:] + "','source':'Alinvirusnever','tags':'"+ str(tagpool[i])[1:-1].lower().replace("'","") + ", #Malware" + "'\n")


        tagpool = []
        f.close()
        driver.close()
        # ALINVIRUSNEVER SCRIPT ENDS #

        time.sleep(1)

        start_time = int(time.time()) # GET SYSTEM TIME NOW
        time.sleep(1)

        # LOOP TIME CHECKING

        if thor_time_by_second%2 == 0:
            thor_time_by_second += 1
        else:
            thor_time_by_second = thor_time_by_second

        if intezervt_time_by_second%2 == 0:
            intezervt_time_by_second += 1
        else:
            intezervt_time_by_second = intezervt_time_by_second

        if dnwls0719_time_by_second%2 == 0:
            dnwls0719_time_by_second += 1
        else:
            dnwls0719_time_by_second = dnwls0719_time_by_second

        if sentoryn_time_by_second%2 == 0:
            sentoryn_time_by_second += 1
        else:
            sentoryn_time_by_second = sentoryn_time_by_second

        if alinvirusnever_time_by_second%2 == 0:
            alinvirusnever_time_by_second += 1
        else:
            alinvirusnever_time_by_second = alinvirusnever_time_by_second

        # MAIN LOOP

        while True:
            instant_time = int(time.time())
            control_time = (start_time - instant_time)
            
            if control_time%thor_time_by_second == 0:
                # THOR SCRIPT START #
                driver = Chrome(wdriver)
                f = open("./hash_list_busters.txt","a")

                x = 0
                looptime = 160

                driver.get("https://www.virustotal.com/en/user/thor/")

                while x < (looptime - 1):
                    driver.execute_script("javascript:more('comments')")
                    x += 1
                time.sleep(1)

                hashes = driver.find_elements_by_class_name("margin-left-1")
                comments = driver.find_elements_by_class_name("comment-text")
                time.sleep(1)

                for i in range(len(comments)):
                    tagpool.append(re.findall(r'(?i)\#\w+', comments[i].text))

                num_pages_hashes = len(hashes)
                for i in range(num_pages_hashes):
                    f.write("'hashtype':'sha256','hash':'" + hashes[i].text[5:] + "','source':'thor','tags':'"+ str(tagpool[i])[1:-1].lower().replace("'","") + "'\n")

                tagpool = []
                f.close()
                driver.close()
                # THOR SCRIPT ENDS #
            
            elif control_time%intezervt_time_by_second == 0:
                # INTEZERVT SCRIPT STARTS #
                driver = Chrome(wdriver)
                f = open("./hash_list_busters.txt","a")
                
                x = 0
                looptime = 2

                driver.get("https://www.virustotal.com/en/user/intezervt/")

                while x < (looptime - 1):
                    driver.execute_script("javascript:more('comments')")
                    x += 1
                time.sleep(1)

                hashes = driver.find_elements_by_class_name("margin-left-1")
                comments = driver.find_elements_by_class_name("comment-text")
                time.sleep(1)

                for i in range(len(comments)):
                    tagpool.append(re.findall(r'(?i)\#\w+', comments[i].text))
                    tagpool[i].pop(-1)

                num_pages_hashes = len(hashes)
                for i in range(num_pages_hashes):
                    f.write("'hashtype':'sha256','hash':'" + hashes[i].text[5:] + "','source':'intezervt','tags':'"+ str(tagpool[i])[1:-1].lower().replace("'","") + "'\n")

                tagpool = []
                f.close()
                driver.close()
                # INTEZERVT SCRIPT ENDS #

            elif control_time%dnwls0719_time_by_second == 0:
                # DNWLS0719 SCRIPT STARTS #
                driver = Chrome(wdriver)
                f = open("./hash_list_busters.txt","a")

                x = 0
                looptime = 1

                driver.get("https://www.virustotal.com/en/user/dnwls0719/")

                while x < (looptime - 1):
                    driver.execute_script("javascript:more('comments')")
                    x += 1
                time.sleep(1)

                hashes = driver.find_elements_by_class_name("margin-left-1")
                comments = driver.find_elements_by_class_name("comment-text")
                time.sleep(1)

                for i in range(len(comments)):
                    tagpool.append(re.findall(r'(?i)\#\w+', comments[i].text))

                num_pages_hashes = len(hashes)
                for i in range(num_pages_hashes):
                    f.write("'hashtype':'sha256','hash':'" + hashes[i].text[5:] + "','source':'dnwls0719','tags':'"+ str(tagpool[i])[1:-1].lower().replace("'","") + "'\n")

                tagpool = []
                f.close()
                driver.close()
                # DNWLS0719 SCRIPT ENDS #

            elif control_time%sentoryn_time_by_second == 0:
                # SENTORYN SCRIPT STARTS #
                driver = Chrome(wdriver)
                f = open("./hash_list_busters.txt","a")

                x = 0
                looptime = 1

                driver.get("https://www.virustotal.com/en/user/Sentoryn/")

                while x < (looptime - 1):
                    driver.execute_script("javascript:more('comments')")
                    x += 1
                time.sleep(1)

                hashes = driver.find_elements_by_class_name("margin-left-1")
                comments = driver.find_elements_by_class_name("comment-text")
                time.sleep(1)

                for i in range(len(comments)):
                    tagpool.append(re.findall(r'(?i)\#\w+', comments[i].text))

                num_pages_hashes = len(hashes)
                for i in range(num_pages_hashes):
                    f.write("'hashtype':'sha256','hash':'" + hashes[i].text[5:] + "','source':'sentoryn','tags':'"+ str(tagpool[i])[1:-1].lower().replace("'","") + "'\n")

                tagpool = []
                f.close()
                driver.close()
                # SENTORYN SCRIPT ENDS #

            elif control_time%alinvirusnever_time_by_second == 0:
                # ALINVIRUSNEVER SCRIPT STARTS #
                driver = Chrome(wdriver)
                f = open("./hash_list_busters.txt","a")

                x = 0
                looptime = 1

                driver.get("https://www.virustotal.com/en/user/AlinVirusnever/")

                while x < (looptime - 1):
                    driver.execute_script("javascript:more('comments')")
                    x += 1
                time.sleep(1)

                hashes = driver.find_elements_by_class_name("margin-left-1")
                comments = driver.find_elements_by_class_name("comment-text")
                time.sleep(1)

                for i in range(len(comments)):
                    tagpool.append(re.findall(r'(?i)\#\w+', comments[i].text))
                    
                num_pages_hashes = len(hashes)
                for i in range(num_pages_hashes):
                    f.write("'hashtype':'sha256','hash':'" + hashes[i].text[5:] + "','source':'Alinvirusnever','tags':'"+ str(tagpool[i])[1:-1].lower().replace("'","") + ", #Malware" + "'\n")

                tagpool = []
                f.close()
                driver.close()
                # ALINVIRUSNEVER SCRIPT ENDS #
            
            time.sleep(1)

    elif first_input == "options":
        os.system('cls')
        print("""
Type "start" for start the program.

Type "options" for see this options

Type "back" in everywhere for go back.

Type "exit" in everywhere for exit.

Type "looptime" for setting optional looptime.
        After type bot number what you want to change
        and type how many second you want to loop.
        You can change all bots looptime typing "all"

Type "proxy" for use custom proxy.
        After type which proxy you want like example
        example: 123.45.678.910:80
                 ipaddress:port
        If you set new proxy and you want to cancel it,
        Just set proxy to "0"
""")

        options_input = input()

        if options_input == "back":
            os.system('cls')
            print("""
VIRUSTOTAL BUSTER REINFORCED

"start" for start.
"options" for see all options.
"exit" for exit.
""")
        elif options_input == "exit":
            os.system('cls')
            exit()

    elif first_input == "exit":
        os.system('cls')
        exit()

    # OPTIONS

    elif first_input == "looptime":
        os.system('cls')
        print("""
type "1" for editing "thor"s loop time.
type "2" for editing "intezervt"s loop time.
type "3" for editing "dnwls0719"s loop time.
type "4" for editing "Sentoryn"s loop time.
type "5" for editing "TheRealRookie"s loop time.
type "all" for editing all bots loop time.

type "reset" for reset all loop times.
type "back" for turn main menu.
""")

        while True:
            looptime_choose = input()

            if looptime_choose == "1":
                os.system('cls')
                print("""
Type time by second
Minimum 60 second for works stable!               
                """)
                thor_time_by_second = int(input("Set thor's loop time to: "))
                os.system('cls')
                print("""
type "1" for editing "thor"s loop time.
type "2" for editing "intezervt"s loop time.
type "3" for editing "dnwls0719"s loop time.
type "4" for editing "Sentoryn"s loop time.
type "5" for editing "TheRealRookie"s loop time.
type "all" for editing all bots loop time.

type "reset" for reset all loop times.
type "back" for turn main menu.
""")
           
            elif looptime_choose == "2":
                os.system('cls')
                print("""
Type time by second
Minimum 60 second for works stable!               
                """)
                intezervt_time_by_second = int(input("Set intezervt's loop time to: "))
                os.system('cls')
                print("""
type "1" for editing "thor"s loop time.
type "2" for editing "intezervt"s loop time.
type "3" for editing "dnwls0719"s loop time.
type "4" for editing "Sentoryn"s loop time.
type "5" for editing "TheRealRookie"s loop time.
type "all" for editing all bots loop time.

type "reset" for reset all loop times.
type "back" for turn main menu.
""")

            elif looptime_choose == "3":
                os.system('cls')
                print("""
Type time by second
Minimum 60 second for works stable!               
                """)
                dnwls0719_time_by_second = int(input("Set dnwls0719's loop time to: "))
                os.system('cls')
                print("""
type "1" for editing "thor"s loop time.
type "2" for editing "intezervt"s loop time.
type "3" for editing "dnwls0719"s loop time.
type "4" for editing "Sentoryn"s loop time.
type "5" for editing "TheRealRookie"s loop time.
type "all" for editing all bots loop time.

type "reset" for reset all loop times.
type "back" for turn main menu.
""")

            elif looptime_choose == "4":
                os.system('cls')
                print("""
Type time by second
Minimum 60 second for works stable!               
                """)
                sentoryn_time_by_second = int(input("Set Sentoryn's loop time to: "))
                os.system('cls')
                print("""
type "1" for editing "thor"s loop time.
type "2" for editing "intezervt"s loop time.
type "3" for editing "dnwls0719"s loop time.
type "4" for editing "Sentoryn"s loop time.
type "5" for editing "TheRealRookie"s loop time.
type "all" for editing all bots loop time.

type "reset" for reset all loop times.
type "back" for turn main menu.
""")

            elif looptime_choose == "5":
                os.system('cls')
                print("""
Type time by second
Minimum 60 second for works stable!               
                """)
                therealrookie_time_by_second = int(input("Set TheRealRookie's loop time to: "))
                os.system('cls')
                print("""
type "1" for editing "thor"s loop time.
type "2" for editing "intezervt"s loop time.
type "3" for editing "dnwls0719"s loop time.
type "4" for editing "Sentoryn"s loop time.
type "5" for editing "TheRealRookie"s loop time.
type "all" for editing all bots loop time.

type "reset" for reset all loop times.
type "back" for turn main menu.
""")

            elif looptime_choose == "all":
                os.system('cls')
                print("""
Type time by second
Minimum 60 second for works stable!               
                """)
                all_time = int(input("Set all loop times to: "))

                thor_time_by_second = all_time
                intezervt_time_by_second = all_time
                dnwls0719_time_by_second = all_time
                sentoryn_time_by_second = all_time
                therealrookie_time_by_second = all_time

                os.system('cls')
                print("""
type "1" for editing "thor"s loop time.
type "2" for editing "intezervt"s loop time.
type "3" for editing "dnwls0719"s loop time.
type "4" for editing "Sentoryn"s loop time.
type "5" for editing "TheRealRookie"s loop time.
type "all" for editing all bots loop time.

type "reset" for reset all loop times.
type "back" for turn main menu.
""")

            elif looptime_choose == "reset":
                os.system('cls')
                print("""
Type time by second
Minimum 60 second for works stable!               
                """)
                thor_time_by_second = 601
                intezervt_time_by_second = 7201
                dnwls0719_time_by_second = 86401
                sentoryn_time_by_second = 120961
                therealrookie_time_by_second = 302401
                os.system('cls')
                print("""
type "1" for editing "thor"s loop time.
type "2" for editing "intezervt"s loop time.
type "3" for editing "dnwls0719"s loop time.
type "4" for editing "Sentoryn"s loop time.
type "5" for editing "TheRealRookie"s loop time.
type "all" for editing all bots loop time.

type "reset" for reset all loop times.
type "back" for turn main menu.
""")

            elif looptime_choose == "back":
                os.system('cls')
                print("""
VIRUSTOTAL BUSTER REINFORCED

"start" for start.
"options" for see all options.
"exit" for exit.
""")
                break

            elif looptime_choose == "exit":
                os.system('cls')
                exit()

            else:
                print("Unknown command!")

    elif first_input == "proxy":
        os.system('cls')
        print("""
Type proxy with port, likes 123.45.678.910:8080

If you changed proxy,
Type "0" for don't use proxy.
        """)
        optional_Proxy = input("Set custom proxy: ")
        os.system('cls')
        print("""
VIRUSTOTAL BUSTER REINFORCED

"start" for start.
"options" for see all options.
"exit" for exit.
""")

    else:
        print("Unknown command!")
