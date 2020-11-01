






def seePasses():
    f = open('passwords.txt', 'r')
    passwords = f.read()
    print(passwords)


def addPassword():
    webName = input('What would you like to name the set: ')
    Username = input('What is the user name for the set: ')
    Password = input('What is the password for this set: ')
    f = open('passwords.txt', 'a')
    f.write(webName + '; ' + Username + '; ' + Password + ',')
    f.write('\n')
    f.close()


seePasses()