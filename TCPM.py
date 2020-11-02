import sys
import linecache
import os
import random
import string
import socket
hostname = socket.gethostname()
platform = sys.platform

if os.path.exists('passwords.txt'):
    f = open('passwords.txt')
    passtxt = f.readlines()
    if passtxt[0][:-1] == 'nolock' or passtxt[2][:-1] == 'nolock':
        pass
    elif passtxt[0][:-1] == hostname and passtxt[2][:-1] == platform: 
        print('Logged in as ' + passtxt[1])
        f.close()
    else:
        print('error hostname not valid')
        f.close()
        quit()
else:
    print('New User? if so welcome')
    username = input('What would you like your username to be: ')
    wantHostPro = input('Do you want Host Protection (stops this program from running on other computers when your set is loaded) (y/n): ')
    if wantHostPro == 'y':
        f = open('passwords.txt', 'w')
        f.write(hostname + '\n' + username + '\n' + platform + '\n')
        f.close()
    else:
        f = open('passwords.txt', 'w')
        f.write('nolock\n' + username)




while True:
    def seeSets():
        hostname = socket.gethostname()
        platform = sys.platformhos
        print('\n')
        if os.path.exists('passwords.txt'):
            f = open('passwords.txt')
            passtxt = f.readlines()
            if passtxt[0][:-1] == 'nolock' or passtxt[2][:-1] == 'nolock':
                f.close()
                f = open('passwords.txt', 'r')
                print(f.read())
            elif passtxt[0][:-1] == hostname and passtxt[2][:-1] == platform: 
                f.close()
                f = open('passwords.txt', 'r')
                passwordtxtseesets = f.readlines()
                print(passwordtxtseesets[3:])                

            else:
                print('error hostname not valid')
                f.close()
                quit()
        else:
            print("You have not made any sets yet try makeing one by typeing 'a'")



    def addSet():
        hostname = socket.gethostname()
        platform = sys.platform
        print('\n')
        if os.path.exists('passwords.txt'):
            f = open('passwords.txt')
            passtxt = f.readlines()
            if passtxt[0][:-1] == 'nolock' or passtxt[2][:-1] == 'nolock':
                randomPass = input('Do you want a randomly genarated password (y/n)')
                if randomPass == 'y':

                    length = input('Enter The Length Of the Password(s): ')
                    wantLower = input('Do you want lower case letters in the password(s) (y/n): ')
                    wantUpper = input('Do you want upper case lestters in the password(s) (y/n): ')
                    wantNum = input('Do you want numbers in the password(s) (y/n): ')
                    wantPunc = input('Do you want punctuation in the password(s (y/n): ')
                    setName = input('What would you like to name the set (if there is none just type none): ')
                    username = input('What is the user name for the set (if there is none just type none): ')
                    email = input('What is the email for this set (if there is none just type none): ')
            


                    if wantLower == 'n' and wantUpper == 'n' and wantNum == 'n' and wantPunc == 'n':
                        print('Cant have all digets and charecters set to no')
                        addSet()
            
                    f = open('passwords.txt', 'a')
                    f.write('Set Name {' + setName + '}, Username {' + username + '}, Password {')

                    i = 0
                    c = random.randint(1,4)
            
                    while i < int(length):
                        if c == 1 and wantLower == 'y':
                            randomval = (random.choice(string.ascii_lowercase))
                            f.write(randomval)
                            print(randomval, end='')
                            i = i+1
                        elif c == 2 and wantNum == 'y':
                            randomcal = (random.choice(['1', '2', '3', '4', '4', '5', '6', '7', '8', '9' ]))
                            f.write(randomcal)
                            print(randomcal, end='')
                            i = i+1
                        elif c == 3 and wantUpper == 'y':
                            randomval = (random.choice(string.ascii_uppercase))
                            f.write(randomval)
                            print(randomval, end='')
                            i = i+1
                        elif c == 4 and wantPunc == 'y':
                            randomval = (random.choice(string.punctuation))
                            f.write(randomval)
                            print(randomval, end='')
                            i = i+1
                        elif wantPunc == 'n' or wantNum == 'n' or wantUpper == 'n' or wantLower == 'n':
                           pass
                        else:
                             print('error invalid value')
                        c = random.randint(1,4)
                        print(' Is your Password')
                    f.write('}, Email {' + email + '},')
                    f.write('\n')
                    f.close()
                elif randomPass == 'n':
                    setName = input('What would you like to name the set: ')
                    username = input('What is the user name for the set (if there is none just type none): ')
                    password = input('What is the password for this set (if there is none just type none): ')
                    email = input('What is the email for this set (if there is none just type none): ')
                    f = open('passwords.txt', 'a')
                    f.write('Set Name {' + setName + '}, Username {' + username + '}, Password {' + password + '}, Email {' + email + '},')
                    f.write('\n')
                    f.close()
                elif randomPass == 'q':
                    pass
                else:
                    print('Error')  
            elif passtxt[0][:-1] == hostname and passtxt[2][:-1] == platform:                 
                    hostname = socket.gethostname()
                    platform = sys.platform
                    print('\n')
                    if os.path.exists('passwords.txt'):
                            f = open('passwords.txt')
            passtxt = f.readlines()
            if passtxt[0][:-1] == 'nolock' or passtxt[2][:-1] == 'nolock':
                randomPass = input('Do you want a randomly genarated password (y/n)')
                if randomPass == 'y':

                    length = input('Enter The Length Of the Password(s): ')
                    wantLower = input('Do you want lower case letters in the password(s) (y/n): ')
                    wantUpper = input('Do you want upper case lestters in the password(s) (y/n): ')
                    wantNum = input('Do you want numbers in the password(s) (y/n): ')
                    wantPunc = input('Do you want punctuation in the password(s (y/n): ')
                    setName = input('What would you like to name the set (if there is none just type none): ')
                    username = input('What is the user name for the set (if there is none just type none): ')
                    email = input('What is the email for this set (if there is none just type none): ')
            


                    if wantLower == 'n' and wantUpper == 'n' and wantNum == 'n' and wantPunc == 'n':
                        print('Cant have all digets and charecters set to no')
                        addSet()
            
                    f = open('passwords.txt', 'a')
                    f.write('Set Name {' + setName + '}, Username {' + username + '}, Password {')

                    i = 0
                    c = random.randint(1,4)
            
                    while i < int(length):
                        if c == 1 and wantLower == 'y':
                            randomval = (random.choice(string.ascii_lowercase))
                            f.write(randomval)
                            print(randomval, end='')
                            i = i+1
                        elif c == 2 and wantNum == 'y':
                            randomcal = (random.choice(['1', '2', '3', '4', '4', '5', '6', '7', '8', '9' ]))
                            f.write(randomcal)
                            print(randomcal, end='')
                            i = i+1
                        elif c == 3 and wantUpper == 'y':
                            randomval = (random.choice(string.ascii_uppercase))
                            f.write(randomval)
                            print(randomval, end='')
                            i = i+1
                        elif c == 4 and wantPunc == 'y':
                            randomval = (random.choice(string.punctuation))
                            f.write(randomval)
                            print(randomval, end='')
                            i = i+1
                        elif wantPunc == 'n' or wantNum == 'n' or wantUpper == 'n' or wantLower == 'n':
                           pass
                        else:
                             print('error invalid value')
                        c = random.randint(1,4)
                        print(' Is your Password')
                    f.write('}, Email {' + email + '},')
                    f.write('\n')
                    f.close()
                elif randomPass == 'n':
                    setName = input('What would you like to name the set: ')
                    username = input('What is the user name for the set (if there is none just type none): ')
                    password = input('What is the password for this set (if there is none just type none): ')
                    email = input('What is the email for this set (if there is none just type none): ')
                    f = open('passwords.txt', 'a')
                    f.write('Set Name {' + setName + '}, Username {' + username + '}, Password {' + password + '}, Email {' + email + '},')
                    f.write('\n')
                    f.close()
                elif randomPass == 'q':
                    pass
                else:
                    print('Error')  
            else:
                print('error hostname not valid')
                f.close()
                quit()
        else:
            pass

        
        
        
        
        
        randomPass = input('Do you want a randomly genarated password (y/n)')
        if randomPass == 'y':

            length = input('Enter The Length Of the Password(s): ')
            wantLower = input('Do you want lower case letters in the password(s) (y/n): ')
            wantUpper = input('Do you want upper case lestters in the password(s) (y/n): ')
            wantNum = input('Do you want numbers in the password(s) (y/n): ')
            wantPunc = input('Do you want punctuation in the password(s (y/n): ')
            setName = input('What would you like to name the set (if there is none just type none): ')
            username = input('What is the user name for the set (if there is none just type none): ')
            email = input('What is the email for this set (if there is none just type none): ')
            


            if wantLower == 'n' and wantUpper == 'n' and wantNum == 'n' and wantPunc == 'n':
                print('Cant have all digets and charecters set to no')
                addSet()
            
            f = open('passwords.txt', 'a')
            f.write('Set Name {' + setName + '}, Username {' + username + '}, Password {')

            i = 0
            c = random.randint(1,4)
            Password = ''
            while i < int(length):
                if c == 1 and wantLower == 'y':
                    randomval = (random.choice(string.ascii_lowercase))
                    f.write(randomval)
                    print(randomval, end='')
                    i = i+1
                elif c == 2 and wantNum == 'y':
                    randomcal = (random.choice(['1', '2', '3', '4', '4', '5', '6', '7', '8', '9' ]))
                    f.write(randomcal)
                    print(randomcal, end='')
                    i = i+1
                elif c == 3 and wantUpper == 'y':
                    randomval = (random.choice(string.ascii_uppercase))
                    f.write(randomval)
                    print(randomval, end='')
                    i = i+1
                elif c == 4 and wantPunc == 'y':
                    randomval = (random.choice(string.punctuation))
                    f.write(randomval)
                    print(randomval, end='')
                    i = i+1
                elif wantPunc == 'n' or wantNum == 'n' or wantUpper == 'n' or wantLower == 'n':
                    pass
                else:
                    print('error invalid value')
                c = random.randint(1,4)
            print(' Is your Password')
            f.write('}, Email {' + email + '},')
            f.write('\n')
            f.close()
        elif randomPass == 'n':
            setName = input('What would you like to name the set: ')
            username = input('What is the user name for the set (if there is none just type none): ')
            password = input('What is the password for this set (if there is none just type none): ')
            email = input('What is the email for this set (if there is none just type none): ')
            f = open('passwords.txt', 'a')
            f.write('Set Name {' + setName + '}, Username {' + username + '}, Password {' + password + '}, Email {' + email + '},')
            f.write('\n')
            f.close()
        elif randomPass == 'q':
            pass
        else:
            print('Error')







    choiseAnOpi = input("Control Center press 'a' to add a set or 's' to see sets or 'q' to quit or 'rmas' to delete all sets: ")
    if choiseAnOpi == 'a':
        print('Ok')
        addSet()
    elif choiseAnOpi == 's':
        print('Ok')
        seeSets()
    elif choiseAnOpi == 'q':
        quit()
    elif choiseAnOpi == 'rmas':
        if os.path.exists('passwords.txt'):
            os.remove('passwords.txt')
            print('Ok Done')
        else:
            print('Error')