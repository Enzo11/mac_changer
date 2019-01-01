#! /usr/bin/env python

#First we will import the subprocess module
import subprocess
#below module is use for command line argumet
import optparse

##below module is for regular expression

import re

def getArg():
            parser= optparse.OptionParser()

            parser.add_option("-i","--interface",dest="interface",help="Interface to change the MAC Address")
            parser.add_option("-m","--mac",dest="mac",help="mac address to change the MAC Address")
            (options,arguments)=parser.parse_args()
            if not options.interface:
                print("[-]Please provide interface")
                exit()
            elif not options.mac:
                print("[-]Please provide new mac address")
                exit()
            return options



def change_mac(interface,new_mac):
            print("[+] changing the mac address of interface "+interface+" to "+new_mac)
            subprocess.call(["ifconfig", interface ,"down"])
            subprocess.call(["ifconfig", interface ,"hw", "ether",new_mac])
            subprocess.call(["ifconfig", interface ,"up"])

            print("[+] Congo Enzo your job is done")

def check_mac(interface):
        ifconfig_result=subprocess.check_output(["ifconfig",options.interface])
        res=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
        if res:
            return res.group(0)
        else:
            print("[-]Could not read the MAC address")


options=getArg()
change_mac(options.interface,options.mac)
cr=check_mac(options.interface)
if cr==options.mac:
    print("[+] Current MAC Address is "+cr)
else:
    print("[-]Some error has occur")
