#Ultimate Calculator V2.4.1
import sys
import time
import itertools
import threading
shrekruntime = 95
soviet = 36291240
running = True
print (" _    _ _ _   _  _____      _       __      _____  ")
print ("| |  | | | | (_)/ ____|    | |      \ \    / /__ \ ")
print ("| |  | | | |_ _| |     __ _| | ___   \ \  / /   ) |")
print ("| |  | | | __| | |    / _` | |/ __|   \ \/ /   / / ")
print ("| |__| | | |_| | |___| (_| | | (__     \  /   / /_ ")
print (" \____/|_|\__|_|\_____\__,_|_|\___|     \/   |____|")
print ("--------------------------/")
print ("Warning: input is case sensitive, please put your answers in lowercase.")
print ("Thank you for using Ultimate Calculator V2.4.1!")
print (" ")
while running:
    print ("____________________________________________________________________________")
    print ("| Enter 1 for Shrek Calculator                                             |")
    print ("| Enter 2 for Soviet Union Calculator                                      |")
    print ("| Enter 3 for an UwU                                                       |")
    print ("| Enter info at the beginning of any program for that program's information|")
    print ("| Enter cancel to end the program at any point                             |")
    print ("| Enter 4 for a list of world Hooters Freedom Index                        |")
    print ("| Enter back at the beginning of a program to go back                      |")
    print ("| Enter 5 for Hooters Freedom Index calculator                             |")
    print ("| Enter ul for the Software Usage License                                  |")
    print ("---------------------------------------------------------------------------")
    print (" ")
    calc_select = (input("Please choose what program you would like to use: "))
    if calc_select == '1':
     print (" ")
     print ("Shrek Calculator V8.2")
     print ("---------------------")
     time_selection = (input("Would You like To Calculate Shrek Time in Hours or Minutes?: "))
     if time_selection =='hours':
         timeinput_hours = float(input("How Many Hours Would You Like to Calculate?: "))
         hours_2 = 60 * timeinput_hours 
         final_hours_input = hours_2 / shrekruntime
         final_hours_input_rounded = round(final_hours_input,4)
         print ("The amount of times you could watch Shrek 1 in " + str(timeinput_hours) + " hours is")
         print (str(final_hours_input_rounded) + " playthroughs.")
         restart = (input("Would you like to calculate another number?: "))
         if restart == 'yes':
             running = True
         else: 
             print ("Aight bye chief")
             running = False
     elif time_selection == 'minutes':
         timeinput_hours = float(input("How Many Minutes Would You Like to Calculate?: "))
         min_1 = timeinput_hours / shrekruntime
         answer = round(min_1,4)
         print ("The amount of times you could watch Shrek 1 in " + str(timeinput_hours) + " minutes is")
         print (str(answer) + " playthroughs.")
         restart = (input("Would you like to calculate another number?: "))
         if restart == 'yes':
             running = True
         else: 
             print ("Aight bye chief")
             running = False
     elif time_selection == 'pp':
             print ("UwU")
     elif time_selection == 'cancel':
         running = False
     elif time_selection == 'info':
       print (" ")
       print ("Info")
       print ("---------------------")
       print (" ")
       print ("Created out of the boredom of 8th grade, used extensively in band class")
       print ("Inspired by a Cowbelly meme")
       print ("The first calculator")
       restart = (input("restart?: "))
       if restart == 'yes':
         running = True
       else:
         running = False
     elif time_selection == 'back':
         running = True
     else:
         print (" ")
         print (" what? ")
         print (" ")
         restart = (input("restart?: "))
         if restart == 'yes':
                running = True
         else:
               running = False
    elif calc_select == '2':
        print (" ")
        print ("Soviet Union Calculator V2")
        print ("--------------------------")
        time_selection = (input("Would You like To Calculate your Soviet Union time in Hours or Minutes?: "))
        if time_selection =='hours':
         timeinput_hours = float(input("How Many Hours Would You Like to Calculate?: "))
         hours_2 = 60 * timeinput_hours 
         final_hours_input = hours_2 / soviet
         final_hours_input_rounded = round(final_hours_input,8)
         print ("The amount of time the Soviet Union could have existed in " + str(timeinput_hours) + " hours is")
         print (str(final_hours_input_rounded) + " times")
         restart = (input("Would you like to calculate another number?: "))
         if restart == 'yes':
             running = True
         else: 
             print ("Aight bye comrade")
             running = False
        elif  time_selection == 'minutes':
         timeinput_hours = float(input("How Many Minutes Would You Like to Calculate?: "))
         min_1 = timeinput_hours / soviet
         answer = round(min_1,8)
         print ("The amount of times the Soviet Union could have existed through " + str(timeinput_hours) + " minutes is")
         print (str(answer) + " times")
         restart = (input("Would you like to calculate another number?: "))
         if restart == 'yes':
             running = True
         else: 
             print ("Aight bye comrade")
             running = False
    elif calc_select == '3':
        print (" ")
        print ("UwU")
        print ("")
        restart = (input("Restart?: "))
        if restart == 'yes':
          running = True
        else:
          print (" ")
          print ("See ya later bruh")
          running = False
    elif calc_select == 'cancel':
        print (" ")
        print ("                                          bruh                     ")
        running = False
    elif calc_select == '69':
        print (" ")
        print ("nice")
        print (" ")
        restart = (input("Restart?: "))
        if restart == 'yes':
          running = True
        else:
          running = False
    elif calc_select == 'info':
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
        if restart == 'yes':
          print (" ")
          print ("Back to da show!")
          running = True
        else:
          print (" ")
          print ("Grassbird Nation")
          running = False
    elif calc_select == '4':
        print (" ")
        print ("Hooters Freedom Index Registry V1.2")
        print ("-----------------------------------")
        hfi = (input("Please enter the country (or Texas or Florida) you would like to view the Hooters Freedom Index: (for countries with multiple words, use capital letters of first letter of each word. e.g. United States of America = USA: "))
        if hfi == 'USA':
            print (" ")
            print ("The Hooters Freedom Index of the United States of America is 5,940.1")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi == 'Canada': 
            print (" ")
            print ("The Hooters Freedom Index of Canada is 69,923.67")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi == 'Mexico': 
            print (" ")
            print ("Unfortunately, Mexico has not publically released the amount of employees work for the government. Therefore we cannot accurately measure their Hooters Freedom Index, though it can be inferred it is around 12000")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi == 'China': 
            print (" ")
            print ("The Hooters Freedom Index of China is 2,500,000")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi == 'UK': 
            print (" ")
            print ("The Hooters Freedom Index of The United Kingdom is 5,500,000")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi == 'Thailand': 
            print (" ")
            print ("The Hooters Freedom Index of Thailand is 65,171.4")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi == 'Germany': 
            print (" ")
            print ("The Hooters Freedom Index of Germany is 2,500,000")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi == 'Texas': 
            print (" ")
            print ("The Hooters Freedom Index of Texas is 2601")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi == 'Florida': 
            print (" ")
            print ("The Hooters Freedom Index of Florida is 22,630.61")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi == 'info': 
            print (" ")
            print ("The Hooters Freedom Index was devised in AP Gov while looking at China's civil freedoms index and Hooters merch at the same time, it is calculated by number of government employees divided by hooters location in a given country.")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi == 'California': 
            print (" ")
            print ("The Hooters Freedom Index of California is 87,083.34")
            print (" ")
            restart = (input("Would you like to see another Hooters Freedom Index score?: "))
            if restart == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
        elif hfi == 'cancel':
            restart = (input("would you like to choose another program?: "))
            if restart == 'yes':
                running = True
            else: 
                print (" ")
                print ("Chungus")
                running = False
        elif hfi == 'back':
            running = True
        else:
            restart = (input("Unfortunately your Hooter Freedom Index request was not on file or was completely illeterate -_-, do you want to try again?: "))
            if restart == 'yes':
                running = True
            else: 
                print ("Hooder")
                running = False
    elif calc_select == '5':
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
    elif calc_select == 'qing dynasty':
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
            if combo == 'craigbruh':
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
                if select == '1':
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
                elif select == '2':
                    print (" ")
                    time.sleep(2.5)
                    print ("SECURITY CLEARANCE: 1AAA")
                    time.sleep(5)
                    print ("FILENAME: DESCRIPT.txt")
                    time.sleep(4)
                    print (" EVENt-REDACTED is a REDACTED foundation staff  REDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTED D-3819 REDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTED among us REDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTED genitals were obliterated REDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTEDREDACTED REDACTED")
                    running = False
                elif select == '3':
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
                
    elif calc_select == 'fnafboobie':
            print (" ")
            print ("Congradulations, you found the secret chum!")
            restart = (input("Restart?: "))
            if restart == 'yes':
                print (" ")
                print ("How'd you even find this?")
                running = True
            else:
                print (" ")
                print ("Exotic Butters")
                running = False
    elif calc_select == 'loop':
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
    elif calc_select == 'loop2':
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
    elif calc_select == 'loop3':
            print (" ")
            time.sleep(1)
            print ("nah")
            time.sleep(1)
            print ("No more loops rn")
            time.sleep(1)
            print ("go get some choccy milk or something")
            time.sleep(1)
            running = True
            
    elif calc_select == 'ul':
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
            if restart == 'yes':
                print (" ")
                print ("Good read huh")
                running = True
            else:
                print (" ")
                print ("chumice")
                running = False
    elif calc_select == 'calc':
            print (" ")
            print ("Actual Calculator v1.0")
            print ("______________________")
            print (" ")
            op = (input("Enter your operation symbol '+,-,*,/,'"))
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
                ans = a / b
                print (" ")
                print (" = " + str(ans) )
                restart = (input("Restart?: "))
                if restart == 'yes':
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
    else:
        print ("------------------------------------------------------------------------------")
        print ("I'm not sure what you entered but it didnt match anything in this program UwU")
        print (" ")
        print ("I'm gonna restart the program so you can reenter UwU")
        running = True
#ADD elif inbetween if and else to add options for the calc
