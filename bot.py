from telegram.ext import* 
from telegram.constants import PARSEMODE_MARKDOWN_V2

updater= Updater(token='TOKEN')
dispatcher= updater.dispatcher


import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context) : 
    context.bot.send_message(chat_id=update.message.chat_id, text=''' 
   Welcome to our telegram bot .. How To Become A Bug Bounty Hunter:
    1_  /Introduction
    2_  /Who are the Bug Bounty Hunters?
    3_  /How to become a Bug Bounty Hunter?
    4_  /Skills required to be a bug bounty hunter
    5_  /Education & Training
    6_  /Bug Hunter Toolkit
    7_  /Resources
    8_  /Practice 
    9_  /Start Now
    10_ /Summary
    11_ /Thanks!
    
    
    ''')

def Introduction(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    In this article you will learn all the information that helps you to start as BugBounty Hunter,
    what are the necessary tools that you need to learn. Also we will discuss some of the prerequisites skills,
    training and certification in the correct order and how things work in the real world.
In the last few years, different companies including Google, Microsoft, Facebook, Yahoo and others started to offer significant rewards for helping them
uncover vulnerabilities in their own websites or software.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id,

def Who are the Bug Bounty Hunters?(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    Bug bounty hunters are individuals who know the nuts and bolts of cybersecurity and are well versed
    in finding flaws and vulnerabilities.
    There are various bug bounty platforms that allow them to be paid to find vulnerabilities in applications and software.
    Bug bounty programs allow hackers to detect and fix bugs before the public hears about them, in order to prevent incidents of widespread abuse. 
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id,

def How to become a Bug Bounty Hunter?(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
   Definitely before finding bugs in any platforms you need to understand how web applications work and understanding the architecture of these apps.
   Solid understanding of some network fundamentals ,SQL database , web components like HTML, CSS, php and Javascript will increase the opportunity
   of  analysing some vulnerabilities but you shouldn't be an expert for all of them.
Also if you have some knowledge in python , it will be an added value to create your own tools 
that will help you to achieve a specific goal that other tools won’t do it for you.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('img/voltarene.jpg', 'rb'))

def Skills required to be a bug bounty hunter(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    Some of the key areas to focus that are part of OWASP Top 10 which are:

Information gathering

SQL Injection

Cross-Site Scripting (XSS)

Server Side Request Forgery (SSRF)

Local & Remote file inclusion 

Information Disclosure 

Remote Code execution (RCE)

 

After understanding these vulnerabilities you can begin reading others reports ,POCs on the bug bounty platforms to figure out the common testing techniques 
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id,

def Education & Training(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
   Before starting the practical approach everyone needs to know the basics and the concepts of information security.
   One of the most effective learning methods is tutorials on watching free youtube channels or you can sign up for 
   any of the web application security training that is provided by CyberTalents, or other well-known courses like SANS, or elearn security 
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('img/salbutamol.jpg', 'rb'))


def Bug Hunter Toolkit(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
  There are no standard tools for the security researcher or the bughunter. However you need to be familiar with some common components like:

=> Web browser 

You can use your preferred version of a web browser “Google Chrome / Firefox” and you can weaponize it with some addons as well to make your testing journey easier.

=> Proxy

Using an interception proxy is required in order to trap all the traffic between your browser and the target website. Also you can automate some attacks or use some features like encoding/decoding on the fly.( burp suite can be your tool)

=> Virtual machine 

Using the Virtual machines is helpful for two reasons. First, it allows you to isolate your testing tools from your original operating system, Second, in order to practice on some vulnerable applications that already published online like VulnHub  you will need to download an ISO file and ready for virtualization 

 Resources

There are a lot of books, but this guide touches on how to get started with the bug bounty trend. This reading should give you a great start to become an ethical hacker and start your bug bounties journey.

 

Books

=> Web app hackers handbook

=>  Web hacking 101

=> Hacker's playbook 1,2,3

=> Hacking art of exploitation

=> Mastering modern web pen testing

=> OWASP Testing guide

=> Mobile application hacker's handbook

 

Youtube channels

=>  CyberTalents   

=>   Live Overflow

=>   Hackersploit

=>   Bugcrowd

=>   Hak5

=>   Hackerone

=>   PortSwigger

=>   thenewboston

=>   SANS Institute
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id,

def Practice(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
   Before jumping to the real bug bounties engagements you might need some web targets that have been made intentionally vulnerable, 
   there are many CTF platforms offering 24/7 web targets. 
   CyberTalents web security challenges can be your place to practice different web hacking techniques in different difficulty levels.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id,

def Start Now(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
   Now after discussing many topics and tools, this is the right time to talk about the bug bounty platform itself here is a list of the well known platforms that offer many programs.

=> HackerOne -:  world's largest community of hackers and bug hunters 

=> Bugcrowd -: powerful bug bounty platform and team of security researchers, one of the best platforms that connects organizations with ethical hackers .

=> Intigriti -: Europe's biggest community of security researchers that help companies to protect their assets

=> Synack -: American intelligence platform automates the discovery of vulnerable endpoints & assets .

=> YesWeHack -: Bug Bounty protects applications the agile way with a wide community of white hackers using private and public programs.

=> HackenProof -: vulnerability coordination platform , connects companies with the global security researchers community to uncover any security issues .
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id,
    
def Summary(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    You will find a lot of bug bounty platforms , differing from each other in some points but still doing the same target 
    which is helping corporates to secure their software assets and using the skills of security researchers in an ethical way.
    Sometimes bug bounty becomes very competitive with many people applying to the same bug on the same site or same program. 
    That's why private bug bounties which provide less hackers access to the target might be better.
    In addition, it might be better to go for freelance jobs where you can apply for a part time job to do full penetration testing.
 CyberTalents jobs section has a lot of freelancing jobs that you can apply on including web penetration testing and others which will 
 guarantee a fixed payment for your time despite the vulnerabilities you will find. However, you will need to pass through a tough
 process before starting receiving your first job.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id,
start_handler = CommandHandler('start', start)



    

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('Introduction', Introduction)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('Who are the Bug Bounty Hunters?', Who are the Bug Bounty Hunters?)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('How to become a Bug Bounty Hunter?', How to become a Bug Bounty Hunter?)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('Skills required to be a bug bounty hunter', Skills required to be a bug bounty hunter)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('Education & Training', Education & Training)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('Bug Hunter Toolkit ', Bug Hunter Toolkit )
dispatcher.add_handler(start_handler)

start_handler = CommandHandler(' Resources',  Resources)
dispatcher.add_handler(start_handler)
                           
start_handler = CommandHandler('Practice', Practice)
dispatcher.add_handler(start_handler)


start_handler = CommandHandler('Start Now', Start Now)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('Summary', Summary)
dispatcher.add_handler(start_handler)


updater.start_polling()
