import os
import shutil

def check_string(listToComareTo):
    for filename in os.listdir(os.getcwd()+ "/emailsProcessed"):
        if filename[-4:] == ".txt":
            content = [line for line in open("emailsProcessed/" + filename[:-3] + "txt", 'r')]
            for line in content:
                if "Subject: " in line:
                    subject = line.replace("Subject: ", "")
                    if subject in listToComareTo:
                        shutil.copy("emailsProcessed/"+filename,"emailsFlagged/"+filename)
                    else:
                        shutil.copy("emailsProcessed/" + filename, "emailsNotFlagged/" + filename)

check_string([line for line in open("flaggedSubjects.csv")])
