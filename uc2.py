#Ultimate Calculator V2.5.0
#Shrek Calculator V8.2
#Soviet Union Calculator V2
#Hooters Freedom Registry V1.2
#Hooters Freedom Calculator V1
#Bruh Industries Terminal V2.4.5
#Basic Calculator V1.1
#Thanos Snap Calculator Alpha 1.2
#Fly To Horsepower Converter V1
#Big Chungus
#Clackk 2021
import sys
import time
import itertools
import threading
import random
shrekruntime = 95
soviet = 36291240
flyhorse=24950000
running = True
print (" _    _ _ _   _  _____      _       __      _____  ")
print ("| |  | | | | (_)/ ____|    | |      \ \    / /__ \ ")
print ("| |  | | | |_ _| |     __ _| | ___   \ \  / /   ) |")
print ("| |  | | | __| | |    / _` | |/ __|   \ \/ /   / / ")
print ("| |__| | | |_| | |___| (_| | | (__     \  /   / /_ ")
print (" \____/|_|\__|_|\_____\__,_|_|\___|     \/   |____|")
print ("--------------------------/")
print ("Warning: input is case sensitive, please put your answers in lowercase.")
print ("Thank you for using Ultimate Calculator V2.5.0!")
print (" ")
while running:
    print ("_______________________________________________________________________________")
    print ("| Enter 1 for Shrek Calculator                                                |")
    print ("| Enter 2 for Soviet Union Calculator                                         |")
    print ("| Enter 3 for an UwU                                                          |")
    print ("| Most, but not all programs have an info section, accessed by 'info' on start|")
    print ("| Enter cancel to end the program at any point                                |")
    print ("| Enter 4 for a list of world Hooters Freedom Index                           |")
    print ("| Enter back at the beginning of a program to go back                         |")
    print ("| Enter 5 for Hooters Freedom Index calculator                                |")
    print ("| Enter ul for the Software Usage License                                     |")
    print ("| Enter calc for a basic calculator                                           |")
    print ("| Enter thanos for the Thanos Snap Survival Calculator                        |")
    print ("| Enter var for a Variable Chart                                              |")
    print ("| Enter 6 for a Fly to Horsepower Conversion Calculator                       |")
    print ("| Enter 7                                                                     |")
    print ("-------------------------------------------------------------------------------")
    print (" ")
    calc_select = (input("Please choose what program you would like to use: "))
    if calc_select == '1':
     print (" ")
     print ("Shrek Calculator V8.2")
     print ("---------------------")
     time_selection = (input("Would You like To Calculate Shrek Time in Hours or Minutes?: "))
     if time_selection.lower() =='hours':
         timeinput_hours = float(input("How Many Hours Would You Like to Calculate?: "))
         hours_2 = 60 * timeinput_hours 
         final_hours_input = hours_2 / shrekruntime
         final_hours_input_rounded = round(final_hours_input,4)
         print ("The amount of times you could watch Shrek 1 in " + str(timeinput_hours) + " hours is")
         print (str(final_hours_input_rounded) + " playthroughs.")
         restart = (input("Would you like to calculate another number?: "))
         if restart.lower() == 'yes':
             running = True
         else: 
             print ("Aight bye chief")
             running = False
     elif time_selection.lower() == 'minutes':
         timeinput_hours = float(input("How Many Minutes Would You Like to Calculate?: "))
         min_1 = timeinput_hours / shrekruntime
         answer = round(min_1,4)
         print ("The amount of times you could watch Shrek 1 in " + str(timeinput_hours) + " minutes is")
         print (str(answer) + " playthroughs.")
         restart = (input("Would you like to calculate another number?: "))
         if restart.lower() == 'yes':
             running = True
         else: 
             print ("Aight bye chief")
             running = False
     elif time_selection.lower() == 'pp':
             print ("UwU")
     elif time_selection.lower() == 'cancel':
         running = False
     elif time_selection.lower() == 'info':
       print (" ")
       print ("Info")
       print ("---------------------")
       print (" ")
       print ("Created out of the boredom of 8th grade, used extensively in band class")
       print ("Inspired by a Cowbelly meme")
       print ("The first calculator")
       restart = (input("restart?: "))
       if restart.lower() == 'yes':
         running = True
       else:
         running = False
     elif time_selection.lower() == 'back':
         running = True
     else:
         print (" ")
         print (" what? ")
         print (" ")
         restart = (input("restart?: "))
         if restart.lower() == 'yes':
                running = True
         else:
               running = False
    elif calc_select.lower() == '2':
        print (" ")
        print ("Soviet Union Calculator V2")
        print ("--------------------------")
        time_selection = (input("Would You like To Calculate your Soviet Union time in Hours or Minutes?: "))
        if time_selection.lower() =='hours':
         timeinput_hours = float(input("How Many Hours Would You Like to Calculate?: "))
         hours_2 = 60 * timeinput_hours 
         final_hours_input = hours_2 / soviet
         final_hours_input_rounded = round(final_hours_input,8)
         print ("The amount of time the Soviet Union could have existed in " + str(timeinput_hours) + " hours is")
         print (str(final_hours_input_rounded) + " times")
         restart = (input("Would you like to calculate another number?: "))
         if restart.lower() == 'yes':
             running = True
         else: 
             print ("Aight bye comrade")
             running = False
        elif  time_selection.lower() == 'minutes':
         timeinput_hours = float(input("How Many Minutes Would You Like to Calculate?: "))
         min_1 = timeinput_hours / soviet
         answer = round(min_1,8)
         print ("The amount of times the Soviet Union could have existed through " + str(timeinput_hours) + " minutes is")
         print (str(answer) + " times")
         restart = (input("Would you like to calculate another number?: "))
         if restart.lower() == 'yes':
             running = True
         else: 
             print ("Aight bye comrade")
             running = False
    elif calc_select.lower() == '3':
        print (" ")
        print ("UwU")
        print ("")
        restart = (input("Restart?: "))
        if restart.lower() == 'yes':
          running = True
        else:
          print (" ")
          print ("See ya later bruh")
          running = False
    elif calc_select.lower() == 'cancel':
        print (" ")
        print ("                                          bruh                     ")
        running = False
    elif calc_select.lower() == '69':
        print (" ")
        print ("nice")
        print (" ")
        restart = (input("Restart?: "))
        if restart.lower() == 'yes':
          running = True
        else:
          running = False
    elif calc_select.lower() == 'info':
        print (" ")
        print ("Ultimate Calculator V2")
        print ("The very first iteration was a 20 or so lines of code that converted")
        print ("time input to the amount of times you could watch Shrek One in that time")
        print ("this new unit of time measurement was called 'Shrek Time'")
        print ("After I worked on the Shrek calculator for a bit I decided to expand, quite a lot")
        print (" Alas, always, ALWAYS! make copies of your work, I accidentially deleted")
        print ("Ultimate Calculator V1 about a year and a half ago, so I decided")
        print ("to rewrite a new, better, and cleaner version. So here we are")
        print (" ")
        print ("UwU")
        print (" ")
        restart = (input("Restart?: "))
        if restart.lower() == 'yes':
          print (" ")
          print ("Back to da show!")
          running = True
        else:
          print (" ")
          print ("Grassbird Nation")
          running = False
    elif calc_select.lower() == '4':
        print (" ")
        print ("Hooters Freedom Index Registry V1.2")
        print ("-----------------------------------")
        hfi = (input("Please enter the country (or Texas or Florida) you would like to view the Hooters Freedom Index: (for countries with multiple words, use capital letters of first letter of each word. e.g. United States of America = USA, type all for all entries: "))
        if hfi.lower() == 'usa':
            print (" ")
            print ("The Hooters Freedom Index of the United States of America is 5,940.1")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi.lower() == 'canada': 
            print (" ")
            print ("The Hooters Freedom Index of Canada is 69,923.67")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi.lower() == 'mexico': 
            print (" ")
            print ("Unfortunately, Mexico has not publically released the amount of employees work for the government. Therefore we cannot accurately measure their Hooters Freedom Index, though it can be inferred it is around 12000")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi.lower() == 'china': 
            print (" ")
            print ("The Hooters Freedom Index of China is 2,500,000")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi.lower() == 'uk': 
            print (" ")
            print ("The Hooters Freedom Index of The United Kingdom is 5,500,000")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi.lower() == 'thailand': 
            print (" ")
            print ("The Hooters Freedom Index of Thailand is 65,171.4")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi.lower() == 'germany': 
            print (" ")
            print ("The Hooters Freedom Index of Germany is 2,500,000")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi.lower() == 'texas': 
            print (" ")
            print ("The Hooters Freedom Index of Texas is 2601")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi.lower() == 'florida': 
            print (" ")
            print ("The Hooters Freedom Index of Florida is 22,630.61")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi.lower() == 'info': 
            print (" ")
            print ("The Hooters Freedom Index was devised in AP Gov while looking at China's civil freedoms index and Hooters merch at the same time, it is calculated by number of government employees divided by hooters location in a given country.")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi.lower() == 'california': 
            print (" ")
            print ("The Hooters Freedom Index of California is 87,083.34")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi.lower() == 'all':
            print (" ")
            print ("All Hooters Freedom Index Entries")
            print ("_________________________________")
            print (" ")
            time.sleep(1)
            print ("The Hooters Freedom Index of the United States of America is 5,940.1")
            time.sleep(1)
            print ("The Hooters Freedom Index of Canada is 69,923.67")
            time.sleep(1)
            print ("Unfortunately, Mexico has not publically released the amount of employees work for the government. Therefore we cannot accurately measure their Hooters Freedom Index, though it can be inferred it is around 12000")
            time.sleep(1)
            print ("The Hooters Freedom Index of China is 2,500,000")
            time.sleep(1)
            print ("The Hooters Freedom Index of The United Kingdom is 5,500,000")
            time.sleep(1)
            print ("The Hooters Freedom Index of Thailand is 65,171.4")
            time.sleep(1)
            print ("The Hooters Freedom Index of Germany is 2,500,000")
            time.sleep(1)
            print ("The Hooters Freedom Index of Texas is 2601")
            time.sleep(1)
            print ("The Hooters Freedom Index of Florida is 22,630.61")
            time.sleep(1)
            print (" ")
            print ("Updated Actively")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi.lower() == 'cancel':
            restart = (input("would you like to choose another program?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print (" ")
                print ("Chungus")
                running = False
        elif hfi.lower() == 'back':
            running = True
        else:
            restart = (input("Unfortunately your Hooter Freedom Index request was not on file or was completely illeterate -_-, do you want to try again?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
    elif calc_select.lower() == '5':
            print (" ")
            print ("Hooters Freedom Index Calculator")
            print ("--------------------------------")
            gov = float(input("Please input the amount of government employees in the institution you would like to analyze: "))
            hoot = float(input("Please input the number of Hooters locations within your institution: "))
            boobie = gov / hoot
            print (" ")
            print ("The Hooters Freedom Index of your institution is " + str(boobie))
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
    elif calc_select.lower() == 'qing dynasty':
            done = False
            #here is the animation
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    sys.stdout.write('\rEstablishing Secure Connection ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rConnection Established    ')

            t = threading.Thread(target=animate)
            t.start()

            #long process here
            time.sleep(10)
            done = True
            time.sleep(1)
            print (" ")
            print ("Bruh Industries V2.45")
            print (" ")
            print ("Please log in")
            user = (input("Username: "))
            pas = (input("Password: "))
            combo = user + pas
            time.sleep(.5)
            if combo == 'megamike':
                print ("Login Successful")
                time.sleep(3)
                print (" ")
                print ("Welcome To the Mainframe")
                print ("------------------------")
                print (" ")
                time.sleep(2)
                print ("1. Half-Life 3")
                time.sleep(2)
                print ("2. The Craig Documents")
                time.sleep(2)
                print ("3. Info")
                time.sleep(3)
                print ("you have 10 seconds to review your options")
                time.sleep(10)
                select = (input("Please Choose an option: "))
                if select.lower() == '1':
                    print (" ")
                    print ("Half-Life 3 Developer Controls")
                    time.sleep(2)
                    def animate():
                        for c in itertools.cycle(['|', '/', '-', '\\']):
                            if done:
                                break
                        sys.stdout.write('\rLoading, Please Wait |  ' + c)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    sys.stdout.write('\rLoad Failure (error code GAYBEN)    ')

                    t = threading.Thread(target=animate)
                    t.start()

                    #long process here
                    time.sleep(100000)
                    done = True
                    running = False
                elif select.lower() == '2':
                    print (" ")
                    time.sleep(2.5)
                    print ("SECURITY CLEARANCE: 1AAA")
                    time.sleep(5)
                    print ("FILENAME: DESCRIPT.txt")
                    time.sleep(4)
                    print (" EVENt-REDACTED is a REDACTED foundation staff  REDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTED D-3819 REDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTED among us REDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTED genitals were obliterated REDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTED")
                    running = False
                elif select.lower() == '3':
                    print (" ")
                    print ("REDACTED")
                    time.sleep(.2)
                    print ("genitals were obliterated")
                    time.sleep(.2)
                    print ("34.5553° N, 69.2075° E")
                    time.sleep(.2)
                    print (shrekruntime)
                    time.sleep(.2)
                    print (soviet)
                    time.sleep(5)
                    print (" ")
                    print ("got those coordinates down yet?")
                    time.sleep(.2)
                    
                    running = False
                else:
                    print ("Invalid Response")
                    time.sleep(2)
                    print ("Disconnecting, Have a good day")
                    running = True
            else:
                print (" ")
                print ("Invalid Credentials, Alerting Authorities")
                time.sleep(3)
                print ("Goodbye")
                time.sleep(1)
                running = False
                
    elif calc_select.lower() == 'fnafboobie':
            print (" ")
            print ("Congradulations, you found the secret chum!")
            restart = (input("Restart?: "))
            if restart == 'yes':
                print (" ")
                print ("How'd you even find this?")
                time.sleep(2)
                print ("Are you happy now Alex?")
                running = True
            else:
                print (" ")
                print ("Exotic Butters")
                running = False
    elif calc_select.lower() == 'loop':
            print (" ")
            time.sleep(3)
            print ("You asked for it")
            time.sleep(3)
            while True:
                print ("_")
                print (" _")
                print ("  _")
                print ("   _")
                print ("    _")
                print ("   _")
                print ("  _")
                print (" _")
                print ("_")
    elif calc_select.lower() == 'loop2':
            print (" ")
            time.sleep(3)
            print ("You know all the tricks huh")
            time.sleep(3)
            while True:
                print ("bruh")
                print ("chung")
                print ("legoo")
                print ("tryna crash?")
                print (" sex")
                print ("   gensi")
                print ("  10125")
                print (" mountaign gap")
                print ("qing dynasty")
    elif calc_select.lower() == 'loop3':
            print (" ")
            time.sleep(1)
            print ("nah")
            time.sleep(1)
            print ("No more loops rn")
            time.sleep(1)
            print ("go get some choccy milk or something")
            time.sleep(1)
            running = True
            
    elif calc_select.lower() == 'ul':
            print (" ")
            time.sleep(1)
            print ("Software Usage License")
            print ("----------------------")
            time.sleep(2)
            print ("This is free and unencumbered software released into the public domain.")
            print ("Anyone is free to copy, modify, publish, use, compile, sell, or")
            print ("distribute this software, either in source code form or as a compiled")
            print ("binary, for any purpose, commercial or non-commercial, and by any")
            print ("means.")
            print (" ")
            print ("In jurisdictions that recognize copyright laws, the author or authors")
            print ("of this software dedicate any and all copyright interest in the")
            print ("software to the public domain. We make this dedication for the benefit")
            print ("of the public at large and to the detriment of our heirs and")
            print ("successors. We intend this dedication to be an overt act of")
            print ("relinquishment in perpetuity of all present and future rights to this")
            print ("software under copyright law.")
            print (" ")
            print ("THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,")
            print ("EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF")
            print ("MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.")
            print ("IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR")
            print ("OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,")
            print ("ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR")
            print ("OTHER DEALINGS IN THE SOFTWARE.")
            print (" ")
            print ("For more information, please refer to <https://unlicense.org>")
            print (" ")
            restart = (input("Restart?: "))
            if restart.lower() == 'yes':
                print (" ")
                print ("Good read huh")
                running = True
            else:
                print (" ")
                print ("chumice")
                running = False
    elif calc_select.lower() == 'calc':
            print (" ")
            print ("Actual Calculator v1.1")
            print ("______________________")
            print (" ")
            op = (input("Enter your operation symbol +,-,*,/, "))
            if op == '+':
                a = float(input("Please enter your first number: "))
                b = float(input("Please enter your second number: "))
                ans = a + b
                print (" ")
                print (" = " + str(ans) )
                restart = (input("Restart?: "))
                if restart == 'yes':
                    print (" ")
                    print ("yuh")
                    running = True
                else:
                    print (" ")
                    print ("chumice")
                    running = False
            elif op == '-':
                a = float(input("Please enter your first number: "))
                b = float(input("Please enter your second number: "))
                ans = a - b
                print (" ")
                print (" = " + str(ans) )
                restart = (input("Restart?: "))
                if restart == 'yes':
                    print (" ")
                    print ("aight")
                    running = True
                else:
                    print (" ")
                    print ("chumice")
                    running = False
            elif op == '*':
                a = float(input("Please enter your first number: "))
                b = float(input("Please enter your second number: "))
                ans = a * b
                print (" ")
                print (" = " + str(ans) )
                restart = (input("Restart?: "))
                if restart == 'yes':
                    print (" ")
                    print ("OK boss")
                    running = True
                else:
                    print (" ")
                    print ("chumice")
                    running = False
            elif op == '/':
                a = float(input("Please enter your first number: "))
                b = float(input("Please enter your second number: "))
                chung = a + b
                if chung == 0 :
                    print (" ")
                    print ("bruh you can't divide by zero")
                    print (" ")
                    restart = (input("Restart?: "))
                    if restart.lower() == 'yes':
                        print (" ")
                        print ("sounds good")
                        running = True
                    else:
                        print (" ")
                        print ("chumice")
                        running = False
                else:
                    ans = a / b
                    print (" ")
                    print (" = " + str(ans) )
                    restart = (input("Restart?: "))
                    if restart.lower() == 'yes':
                        print (" ")
                        print ("sounds good")
                        running = True
                    else:
                        print (" ")
                        print ("chumice")
                        running = False
            else:
                print (" ")
                print (" Invalid input hehe")
                running = True
    elif calc_select.lower() == 'var':
        print (" ")
        print ("Variable Chart")
        print ("--------------")
        print (" ")
        print (running)
        print (shrekruntime)
        print (soviet)
        print (calc_select)
        print (" ")
        restart = (input("Restart?: "))
        if restart.lower() == 'yes':
            print (" ")
            print ("sounds good")
            running = True
        else:
            print (" ")
            print ("chumice")
            running = False
    elif calc_select.lower() == 'thanos':
        than = ['yes', 'no']
        print (" ")
        print ("THANOS SNAP Calculator")
        print ("______________________")
        time.sleep(2)
        print ("did you survive the snap?")
        print (" ")
        time.sleep(2)
        print ("calculating...")
        print (" ")
        time.sleep(3)
        print(random.choice(than))
        print (" ")
        restart = (input("Restart?: "))
        if restart == 'yes':
            print (" ")
            print ("sounds good")
            running = True
        else:
            print (" ")
            print ("chumice")
            running = False
              
    elif calc_select == 'davilos':
        print (" ")
        print ("your cute hehe <3")
        print ("                -Clackk")
        print (" ")
        running = False 
    elif calc_select.lower() == '6':
        print (" ")
        print ("Fly to Horsepower Converter v1")
        print ("______________________________")
        time.sleep(2)
        print ("Enter 1 for Fly to Horsepower Conversion")
        print ("Enter 2 for Horsepower to Fly Conversion")
        print (" ")
        time_selection = (input("Please Enter Here: "))
        print (" ")
        if time_selection.lower() =='1':
         timeinput_hours = float(input("How Many Flies Are Present?: "))
         print (" ")
         hours_2 = timeinput_hours / flyhorse
         print ("The amount of horsepower " + str(timeinput_hours) + " flies would make is")
         print (str(hours_2) + " horsepower")
         print (" ")
         restart = (input("Would you like to calculate another number?: "))
         if restart.lower() == 'yes':
             running = True
         else: 
             print ("Aight bye comrade")
             running = False
        elif  time_selection.lower() == '2':
         timeinput_hours = float(input("How Much horsepower Would You Like To Generate?: "))
         print ("")
         min_1 = timeinput_hours * flyhorse
         print ("The Amount Of Flies You Would Need To Generate " + str(timeinput_hours) + " Horsepower is")
         print (str(min_1) + " Flies")
         print (" ")
         restart = (input("Would you like to calculate another number?: "))
         if restart.lower() == 'yes':
             running = True
         else: 
             print ("Aight bye comrade")
             running = False
        elif time_selection.lower() == 'info':
            print (" ")
            print ("Info Section")
            print ("------------")
            print ("This calculator was one of the original additions")
            print ("to the first Ultimate Calculator, as such this updated")
            print ("edition would not be complete without it.")
            print (" ")
            print ("Methodology")
            print ("-----------")
            print ("You might be wondering how exactly the calculator figures out")
            print ("how much horsepower a fly can generate, this conversion")
            print ("is cheifly held on the figure 24950000, of which is the amount")
            print ("of flies needed to lift 550 pounds 'presuming it could be done in one minute'")
            print ("this figure was found by dividing 10 miligrams to the miligram equivalent")
            print ("of 550 lbs, I was originally going to use the rpm*tourqe /5252 method, however")
            print ("flies do not rotate at a fixed rpm, or at all really, and their torque surface,")
            print ("their wings, cannot really accurately be measured due to the fact we cannot")
            print ("calculate the weight being imparted across the wing under flight, loaded or otherwise")
            print ("Obviously this calculator uses data extrapolation and should be viewed with caution")
            print ("before you decide to buy millions of flies to start the next gen package carrier service.")
            print (" ")
            restart = (input("Would you like to calculate another number?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Aight bye comrade")
                running = False
        else:
            print ("Sorry bout dat chief but I aint sure what you entered")
            print (" ")
            restart = (input("Would you like to calculate another number?: "))
            if restart.lower() == 'yes':
                running = True
            else: 
                print ("Aight bye comrade")
                running = False
    elif calc_select.lower() == '7':
        print (" ")
        time.sleep(2)
        print ("q")
        time.sleep(1)
        print ("i")
        time.sleep(1)
        print ("n")
        time.sleep(1)
        print ("g")
        time.sleep(1)
        print (" ")
        time.sleep(1)
        print ("d")
        time.sleep(1)
        print ("y")
        time.sleep(1)
        print ("n")
        time.sleep(1)
        print ("a")
        time.sleep(1)
        print ("s")
        time.sleep(1)
        print ("t")
        time.sleep(1)
        print ("y")
        time.sleep(1)
        print (" ")
        time.sleep(1)
        print ("ERROR 254")
        print ("Connection Interrupted")
        running = False
    else:
        print ("------------------------------------------------------------------------------")
        print ("I'm not sure what you entered but it didnt match anything in this program UwU")
        print (" ")
        print ("I'm gonna restart the program so you can reenter UwU")
        running = True
#ADD elif inbetween if and else to add options for the calc
