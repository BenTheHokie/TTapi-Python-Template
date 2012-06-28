# This is a template for future LSK Python bots

from ttapi import Bot
from printnesteddictionary import print_dict
import re
import random
from time import localtime, strftime
import sys
import os
import unicodedata
import threading
import pickle

bot_auth       = 'auth+live+xxxxxx'
bot_userid     = 'xxxx'

lsk_userid     = '4e7c70bc4fe7d052ef034402'

AUTH   = ''
USERID = ''
ROOM   = ''

bot = Bot(AUTH,USERID,ROOM)

userList = []
snags = 0

def speak(data):
   name = data['name']
   userid = data['userid']
   text = data['text']
   userid = data['userid']
   print(strftime('%I:%M:%S %p',localtime())+'  '+strpAcc(name) + ':'+ ' '*(21-len(strpAcc(name)))+ strpAcc(text))
   if re.match('/((h(ello|i|ey))|(sup))', strpAcc(text)):
      bbot.speak('Hey! How are you %s?' % atName(name))

def roomChanged(data):
   print 'Moderators:      %s' % (', '.join(data['room']['metadata']['moderator_id']))
   global userList
   for i in range(len(data['users'])):
      userList.append({'name':data['users'][i]['name'],'userid':data['users'][i]['userid'],'avatarid':data['users'][i]['avatarid']})
   print '\nCurrent Users:'
   for i in range(len(userList)):
      print(strpAcc(userList[i]['name'])+ ' '*(30-len(strpAcc(userList[i]['name']))) + userList[i]['userid']) #when we enter the room we print the current users in the I/O
   print '\nCurrent DJs:'
   for i in range(len(userList)):
      if userList[i]['userid'] in data['room']['metadata']['djs']:
         print strpAcc(userList[i]['name'])
   print '\n'

def userReg(data):
   userid = data['user'][0]['userid']
   name   = data['user'][0]['name']
   print '%s  %s has entered the room. %s' % (strftime('%I:%M:%S %p',localtime()),strpAcc(name),userid)
   if not(userid == bot_userid):
      userList.append({'name':data['user'][0]['name'],'userid':data['user'][0]['userid'],'avatarid':data['user'][0]['avatarid']})
   
def userDereg(data):
   userid = data['user'][0]['userid']
   name   = data['user'][0]['name']
   print '%s  %s has left the room. %s' % (strftime('%I:%M:%S %p',localtime()),strpAcc(name),userid)
   for i in range(len(userList)):
      if userList[i]['userid']==userid: userList.remove(userList[i])

def recSnag(data):
   global snags
   snags += 1

def strpAcc(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def atName(name): # This is so we don't get @@twittername which looks weird. If the user has a twitter name, one @ should still ping them
   if name[0]=='@':
      return name
   else:
      return '@%s' % name

bot.on('snag',recSnag)
bot.on('deregistered',userDereg)
bot.on('roomChanged',roomChanged)
bot.on('registered',userReg)
bot.on('speak',speak)
bot.start()