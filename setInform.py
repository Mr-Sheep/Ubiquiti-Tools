#!/usr/bin/python

# -------------------------------------------------------------------------------
#  "THE BEER-WARE LICENSE" (Revision 42):
#  <patrick@kerwood.dk> wrote this script. As long as you retain this notice you
#  can do whatever you want with this stuff. If we meet some day, and you think
#  this stuff is worth it, you can buy me a beer in return. 
#
#     - Patrick Kerwood @ LinuxBloggen.dk
# 
#  MrSheep modified some part of this script. You dont have to buy me a beer if me
#  meet, I prefer coffee lol.
# -------------------------------------------------------------------------------

import paramiko

informAddr = "http://<your-inform-ip>:8080/inform"
sshUser = "username"
sshPass = "password"

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


print("\nConnecting to devices....\n")

# use this if ur aps are in a specific range
for n in range(240,253): # specify the range here
    ip_addr = '192.168.88.'+ str(n) # change this one too, for example: 192.168.88.
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip_addr, username=sshUser, password=sshPass, allow_agent=False)
        stdin, stdout, stderr = client.exec_command("mca-cli <<EOF\nset-inform %s\nquit\nEOF" % informAddr)
        
        if stdout.channel.recv_exit_status() == 0:
            for line in stdout:
                if "Adoption request sent to" in line:
                    print(" %s[+] Adoption request sent to %s from %s %s" % (bcolors.OKGREEN, informAddr, ip_addr, bcolors.ENDC))
        
        
    except paramiko.AuthenticationException:
        print(" %s[-] Authentication failed on %s!%s" % (bcolors.FAIL, ip_addr, bcolors.ENDC))
    except:
        print(" %s[-]Something went wrong on %s!%s" % (bcolors.FAIL, ip_addr, bcolors.ENDC))

# use this if you want to mannually state AP's ip
# clients = [
# # CHANGE THIS
#     '192.168.88.240',
#     '192.168.88.241',
#     '192.168.88.40',
#     '192.168.88.36',
#     '192.168.88.54',
#     '192.168.88.55',
#     '192.168.88.55',
#     '192.168.88.53',
#     '192.168.88.23',
#     '192.168.88.29',
#     '192.168.88.25',
#     '192.168.88.39',
# ]
# for ip in clients:
#     try:
#         client = paramiko.SSHClient()
#         client.load_system_host_keys()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(ip, username=sshUser, password=sshPass, allow_agent=False)
#         stdin, stdout, stderr = client.exec_command("mca-cli <<EOF\nset-inform %s\nquit\nEOF" % informAddr)
        
#         if stdout.channel.recv_exit_status() == 0:
#             for line in stdout:
#                 if "Adoption request sent to" in line:
#                     print(" %s[+] Adoption request sent to %s from %s %s" % (bcolors.OKGREEN, informAddr, ip, bcolors.ENDC))
        
        
#     except paramiko.AuthenticationException:
#         print(" %s[-] Authentication failed on %s!%s" % (bcolors.FAIL, ip, bcolors.ENDC))
#     except:
#         print(" %s[-]Something went wrong on %s!%s" % (bcolors.FAIL, ip, bcolors.ENDC))
   
print
