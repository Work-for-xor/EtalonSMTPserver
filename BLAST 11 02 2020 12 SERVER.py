
import textile
import base64
import codecs
import imaplib
import email
import urllib.request
import socket
import smtplib
import re
from threading import Thread
import time
import datetime
import os
from email.mime.text import MIMEText
import sys
import logging
import random

class global_params():
    cointer_sended_mail = 0
    contact_list_all = []
    senders = []



class myrun():
    sub = ''
    text = ''
class myflags():
    start_error = 1

reqmail = ["demo@getxor.com", "demo@getxor.today", "demo@getxorai.today", "demo@getxor.co", "demo@getxor.tech", "demo@xorte.ch"]

def check_point(vmail, servN): # куда отправлять и номер сервера
    server = '13.64.198.158'  # 10
    port = 25
    # smtp data & connect
    psmtp = os.getcwd() + "/settings/smtp.my"
    fsmtp = open(psmtp, 'r')
    smtpset = fsmtp.readlines()
    smtpset = [line.rstrip() for line in smtpset]
    # print(smtpset)
    fsmtp.close()
    server = smtpset[0]
    port = smtpset[1]
    domain = smtpset[2]
    #s = smtplib.SMTP(server, port)
    #s.ehlo()

    # subj = 'Merry X-Mas and Happy Holidays '
    subj = 'CHESK POINT  ' + str(servN)
    text = "\n \n \n CHESK POINT PRINT 'Y' IN PYCHARM"
    text_html = '<html>' + text + '</html>'
    s = smtplib.SMTP(server, port)
    # you = "vasilii.b@xor.ai"
    # you = 'seth.d@xor.ai'
    you = vmail
    msg = MIMEText(text_html, 'html', 'utf-8')
    mail_from = "cheskpoint" + " " + "mail" + "  <" + "cheskpoint" + "@" + domain + ">"
    reply_to = 'vasilii.b@xor.ai'
    # reply_to = 'seth.d@xor.ai'
    msg['Subject'] = subj
    msg['FROM'] = mail_from
    msg['TO'] = you
    msg['Reply-To'] = reply_to
    msg['List-Unsubscribe'] = "mailto:noreply@xorhr.com"
    msg['List-Unsubscribe-Post'] = 'List-Unsubscribe=One-Click'
    msg['X-Mailer'] = 'SenderXO'
    s.sendmail(mail_from, you, msg.as_string())
    s.quit()

# функция отправки
def part_blast():
    #me = email_sender
    logging.info(u'Enter run    ' + datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
    #me = email_sender
    # загрузить список контактов
    cl_for_mail = global_params.contact_list_all
    cl_for_mail = [line.split(',') for line in cl_for_mail]
    # print(name_sender + " otpravit " + str(len(cl_for_mail)) + " emeylov " + cl_for_mail[57][6] )
    # data email
    f_sub = open(os.getcwd() + "/subj.mail", "r")
    subject_mail1 = f_sub.readlines()

    f_sub.close()
    subject_mail1 = [line.rstrip() for line in subject_mail1]
    subject_mail = subject_mail1[0]
    #print(subject_mail)

    #sign_email = '\n\nBest, {MYNAME}.\n\nXOR Inc. 540 Howard Street, 2nd Floor #11|San Francisco, CA 94105\n'

    # print(name_sender + " otpravit " + str(len(cl_for_mail)) + " emeylov s temoy '" + subject_mail + "' i podpisyu " + sign_email)

    f_text = open(os.getcwd() + "/text.mail", "r")
    text_mail1 = f_text.readlines()
    # text_mail1 = [line.rstrip() for line in text_mail1]
    f_sub.close()
    text_email = ''
    tm = 0
    while tm < len(text_mail1):
        text_email = text_email + text_mail1[tm]
        tm += 1




    # smtp data & connect
    psmtp = os.getcwd() + "/settings/smtp.my"
    fsmtp = open(psmtp, 'r')
    smtpset = fsmtp.readlines()
    smtpset = [line.rstrip() for line in smtpset]
    # print(smtpset)
    fsmtp.close()
    server = smtpset[0]
    port = smtpset[1]
    domain = smtpset[2]
    s = smtplib.SMTP(server, port)
    #s.ehlo()


    # цикл отправки

    f1name = open(os.getcwd() + '/first_names.all.txt')

    firstnamebase = f1name.readlines()
    f1name.close()

    f2name = open(os.getcwd() + '/last_names.all.txt')

    lastnamebase = f2name.readlines()
    f2name.close()
    # no '\n'
    firstnamebase = [line.rstrip() for line in firstnamebase]
    lastnamebase = [line.rstrip() for line in lastnamebase]
    # title
    firstnamebase = [line.title() for line in firstnamebase]
    lastnamebase = [line.title() for line in lastnamebase]
    print(str(len(cl_for_mail)))
    cocl = 0
    while cocl < len(cl_for_mail):

        #print(cl_for_mail[cocl])


        #me = ""


        rand_1name = random.randint(0, len(firstnamebase))
        rand_2name = random.randint(0, len(lastnamebase))

        me = firstnamebase[rand_1name] + lastnamebase[rand_2name] + "@" + domain


        name_sender = firstnamebase[rand_1name] + " " + lastnamebase[rand_2name]

        randdemo = random.randint(0, 5)
        demomail = reqmail[randdemo]

        # составить письмо

        # тема письма
        subject_mail = subject_mail
        subject_mail = subject_mail.replace('{FirstName}', cl_for_mail[cocl][1])
        subject_email = subject_mail.replace('{Company}', cl_for_mail[cocl][4])
        subject_email = subject_email.replace('{MYNAME}', name_sender)
        # текст письма
        text_mail = text_email
        text_mail = text_mail.replace('{FirstName}', cl_for_mail[cocl][1])
        text_mail = text_mail.replace('{Company}', cl_for_mail[cocl][4])
        text_mail = text_mail.replace('{MYNAME}', name_sender)
        # print("*****    TEXT  :\n" + text_mail)
        text_mail_html = textile.textile(text_mail)

        text_mail_html = text_mail_html + "<p>Request a demo  <a href=" + "'mailto:" + demomail + "?subject=Request a demo&body=Helo, Request a demo'" + ">here</a>.</p>"
        sign_email = '\n\nWith best regards, \n' + name_sender + '.\nXOR Inc.  \n1161 Mission Street, #424, San Francisco, CA 94103 United States\n'
        sign_email_html = textile.textile(sign_email)
        text_mail_html = text_mail_html + sign_email_html
        text_mail_html = text_mail_html + "<p>If you would like to unsubscribe and stop receiving these emails click  <a href=" + "'mailto:noreply@getxorai.today?subject=Unsubscribe me&body=Helo, Unsubscribe me'" + ">here</a>.</p>"

        file3000 = open(os.getcwd() + '/3000 words', "r")
        words300 = file3000.readlines()
        words300 = [line.rstrip() for line in words300]
        file3000.close()
        rand = random.randint(50, 100)

        rand_text = ''

        w = 0
        while w < rand:
            r = random.randint(0, len(words300) - 1)
            rand_text = rand_text + words300[r] + '  '
            w += 1
        # print(rand)
        # print(rand_text)

        text_mail_html = text_mail_html + '<p style="display:none;"> ' + rand_text + ' </p> '

        text_mail_html = '<html>' + text_mail_html + '</html>'
        #print(subject_email)
        dt = datetime.datetime.now()
        t = str(email.utils.format_datetime(dt))

        msg = MIMEText(text_mail_html, 'html', 'utf-8')
        msg['Date'] = t
        msg['Subject'] = subject_email
        msg['From'] = name_sender + "<" + me + ">"
        msg['Reply-To'] = demomail
        msg['To'] = cl_for_mail[cocl][1] + "<" + cl_for_mail[cocl][6] + ">"
        msg['List-Unsubscribe'] = "mailto:noreply@getxorai.today"
        msg['List-Unsubscribe-Post'] = 'List-Unsubscribe=One-Click'
        try:
            # print(msg.as_string())
            s.sendmail(me, cl_for_mail[cocl][6], msg.as_string())

            print(f'\033[0;1;92m' + "    Successful: " + me + " to " + cl_for_mail[cocl][6] + "  " + cl_for_mail[cocl][1] + '\033[0m')
            logging.info(u"Successful: " + me + " to " + cl_for_mail[cocl][6] + cl_for_mail[cocl]
                [1] + datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))

            #chesk_point
            global_params.cointer_sended_mail += 1
            if global_params.cointer_sended_mail == 1000:
                check_point("vasilii.b@xor.ai", 12)
                check_point("seth.d@xor.ai", 12)
                global_params.cointer_sended_mail = 0
                print("Test time " + datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
                answer = input("Press Y to continue...")
                if answer == "y":
                    print("OK work")

                else:
                    print("Xuevo")
                    break


        except:
            print('\x1b[31m' + me + " Ошибка отправки на  : " + cl_for_mail[cocl][6] + '\033[0m')
            logging.info(u"Successful: " + me + " Ошибка отправки на  : " + cl_for_mail[cocl]
                [6] + datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
        cocl += 1

    print(f'\033[0;1;92m' + "    Successful: " + " end send " + '\033[0m')

# получить список контактов in contact_list_all
def load_params():
    try:
        #f_contact_list_all = open(os.getcwd() + '/10k send 11 02 2020', 'r')
        f_contact_list_all = open(os.getcwd() + '/test_c-list(svoy).csv', 'r')

        global_params.contact_list_all = f_contact_list_all.readlines()

        f_contact_list_all.close()

        # contact_list_all = [line.rstrip() for line in contact_list_all]

        print(str(len(global_params.contact_list_all)))
    except:
        myflags.start_error = 0  # error - true
        print('\x1b[31m' + "Ошибка получения списка контактов" + '\033[0m')

    """# получить список почт
    try:
        f_senders = open(os.getcwd() + '/senders', 'r')

        senders = f_senders.readlines()

        f_senders.close()

        senders = [line.rstrip() for line in senders]

        # print(senders)
    except:
        myflags.start_error = 0 # error - true
        print('\x1b[31m' + "Ошибка получения списка отправителей" + '\033[0m')
    """

    # Логи

    date_now = str(datetime.date.today())
    pa = os.getcwd() + "/log/" + date_now + ".log"
    F = open(pa, 'a')
    F.close()
    logging.basicConfig(filename=pa, level=logging.INFO)



def main():
    t_ = str(datetime.datetime.today())
    print(t_)

    load_params()

    part_blast()

    t = str(datetime.datetime.today())
    print(t_ + "  -  " + t)



if __name__ == '__main__':
    main()



