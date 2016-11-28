import email.parser
import os
import re
import time

<<<<<<< HEAD
def emailFields(name):
 try:
     fp = open(name)
     #filterBody = lambda body: body.replace("\\n"," ").replace("\\r"," ")
     emailMessage = email.message_from_file(fp)
     emailDict = dict(emailMessage.items())
     emailDict = dict((field,emailDict[field]) for field in ('CC','BCC','To','Subject','From') if field in emailDict)
     emailDict['Body'] = ""
     for part in emailMessage.walk():
         if(part.get_content_type() == "text/plain"):
             emailDict['Body'] = emailDict['Body'] + str(part.get_payload(decode=True))
     fp.close()
     fp = open(name[:-3] + ".txt", 'w')
     for key in emailDict:
         fp.write(key + ": " + emailDict[key] + "\n")
 except:
     print("file not processable: " + name)
 finally:
     fp.close()


def allFiles():
 files = os.listdir(os.getcwd() + "/emails")
 for file in files:
     if file[-4:] == ".eml":
         emailFields("emails/" + file)

allFiles()
=======
regex = re.compile("(\\r)+|(\\n)+|[\r\n\\><]+")

def processMessage(emailMessage):
    emailDict = dict(emailMessage.items())
    emailDict = dict(
        (field, emailDict[field]) for field in ('Date', 'CC', 'BCC', 'To', 'Subject', 'From') if field in emailDict)
    emailDict['Body'] = ""
    for part in emailMessage.walk():
        if (part.get_content_type() == "text/plain"):
            emailDict['Body'] = emailDict['Body'] + re.sub(regex, " ", str(part.get_payload(decode=True)))
    return emailDict

def emailFields(name, subdirSource, subdirSave):
    try:
        fp = open(subdirSource + name)
        emailDict = processMessage(email.message_from_file(fp))
        fp.close()
        fp = open(subdirSave + name[:-3] + "txt", 'w')
        for key in emailDict:
            fp.write(key + ": " + emailDict[key] + "\n")
    except:
        print("file not processable: " + name)
    finally:
        fp.close()


def allFiles():
    start = time.time()
    files = os.listdir(os.getcwd() + "/emails")
    for file in files:
        if file[-4:] == ".eml":
            emailFields(file, "emails/", "emailsProcessed/")
    print(time.time() - start)

allFiles()
>>>>>>> cfb12f288d4dc94db6a7236eb24803262d58bcea
