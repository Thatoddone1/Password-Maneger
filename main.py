import os
import random
import string

while True:
    def seeSets():
        f = open('passwords.txt', 'r')
        passwords = f.read()
        print(passwords)


    def addSet():
        randomPass = input('Do you want a randomly genarated password (y/n)')
        if randomPass == 'y':

            length = input('Enter The Length Of the Password(s): ')
            wantLower = input('Do you want lower case letters in the password(s) (y/n)')
            wantUpper = input('Do you want upper case lestters in the password(s) (y/n)')
            wantNum = input('Do you want numbers in the password(s) (y/n)')
            wantPunc = input('Do you want punctuation in the password(s (y/n))')

            i = 0
            c = random.randint(1,4)
            Password = ''
            while i < int(length):
                if c == 1 and wantLower == 'y':
                    Password + random.choice(string.ascii_lowercase)
                    i = i+1
                elif c == 2 and wantNum == 'y':
                    print(random.randint(1,9), end='')
                    i = i+1
                elif c == 3 and wantUpper == 'y':
                    print(random.choice(string.ascii_uppercase), end='')
                    i = i+1
                elif c == 4 and wantPunc == 'y':
                    print(random.choice(string.punctuation), end='')
                    i = i+1
                elif wantPunc == 'n' or wantNum == 'n' or wantUpper == 'n' or wantLower == 'n':
                    pass
                else:
                    print('error invalid value')
                c = random.randint(1,4)
            
            webName = input('What would you like to name the set: ')
            Username = input('What is the user name for the set: ')
            f = open('passwords.txt', 'a')
            f.write(webName + '; ' + Username + '; ' + Password + ',')
            f.write('\n')
            f.close()
        else:
            webName = input('What would you like to name the set: ')
            Username = input('What is the user name for the set: ')
            Password = input('What is the password for this set: ')
            f = open('passwords.txt', 'a')
            f.write(webName + '; ' + Username + '; ' + Password + ',')
            f.write('\n')
            f.close()







    choiseAnOpi = input("Do You Want to add a set or look at sets ('a' to add a set and 's' to see sets or 'q' to quit or 'rmas' to delete all sets)")
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







