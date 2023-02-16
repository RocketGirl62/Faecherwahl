"""
Vorgehensweise:

- Erst wird "election" geöfnet, da dort steht welche Datein es überhaupt gibt
- In Variabel steht wie viele Zeilen alle weiteren Dateitypen haben --> aber dads brauche ich nicht, weil Python
- Jede Zeile wird einzeln gelesenund daraus halt ein Befehlt zur Erstellung eines Objekts in javascript gemacht

"""

import sys

#Methode zum öffnenen und lesen von Datein mit Rückgabe eines Arrays mit allen Zeilen
#--> daraufachten, dass das letzte wort ggf. noch ein \n hat
def openAndRead(filePath):
    try:
        file = open(filePath,"r")
    except:
        print("error")
        sys.exit(0)
    allLines = file.readlines()
    file.close()
    return allLines


def createString(txt):
    out = '["' +txt[0]
    for i in range (1, len(txt)):
        out = out + '","' + txt[i]
    out = out + '"]'
    return out

"""
def create(txt):
    out = "[" +txt[0]
    for i in range (1, len(txt)):
        out = out + "," + txt[i]
    out = out + "]"
    return out
"""

def create(txt):
    txt = txt[2:len(txt)-2]
    txt = txt.split('","')
    return txt



#Öffnen der Election Datei
lines = openAndRead("election/election.txt")
#Auslesen der Datei
profiles = lines[0].split(" ")[1]
profiles = profiles[:len(profiles)-1]
#profiles.remove(profiles[0])


kindOfSubjects = lines[1].split(" ")[1]
kindOfSubjects = kindOfSubjects[:len(kindOfSubjects)-1]
#kindOfSubjects.remove(kindOfSubjects[0])


taskfields = lines[2].split(" ")[1]
taskfields = taskfields[:len(taskfields)-1]
#taskfields.remove(taskfields[0])


subjects = lines[3].split(" ")[1]
subjects = subjects[:len(subjects)-1]
#subjects.remove(subjects[0])


#Schreiben des Javascripts
#print("election = new Election( "+ createString(profiles) + " , " + createString(kindOfSubjects) + " , "+ createString(taskfields) + " , "+ createString(subjects) + " );")
print("\t"+"election = new Election( "+ profiles + " , " + kindOfSubjects + " , "+ taskfields + " , "+ subjects + ") );")

profiles = create(profiles)
kindOfSubjects = create(kindOfSubjects)
taskfields = create(taskfields)
subjects = create(subjects)


#Bearbeiten aller Profil Datein
for i in range(0, len(profiles)):
    profile = profiles[i]
    lines = openAndRead("profiles/"+profile+".txt")
    txt = ""
    #Trennen aller Zeilen am Leerzeichen
    for j in range(0, len(lines)):
        tmp = lines[j].split(" ")
        tmp[1] = tmp[1][:len(tmp[1])-1]
        txt = txt + tmp[1]
        if (j < len(lines)-1):
            txt = txt + ", "
    #Schreiben und Ausgeben des javascripts
    print("\t"+"profiles.add( new Profile(" + txt + ") );")

#Bearbeiten aller Fachtypen Datein
for i in range(0, len(kindOfSubjects)):
    kindOfSubject = kindOfSubjects[i]
    lines = openAndRead("kindsOfSubjects/"+kindOfSubject+".txt")
    txt = ""
    #Trennen aller Zeilen am Leerzeichen
    for j in range(0, len(lines)):
        tmp = lines[j].split(" ")
        tmp[1] = tmp[1][:len(tmp[1])-1]
        txt = txt + tmp[1]
        if (j < len(lines)-1):
            txt = txt + ", "
    #Schreiben und Ausgeben des javascripts
    print("\t"+"kindOfSubjects.add( new KindOfSubject(" + txt + ") );")

#Bearbeiten aller Aufgabenbereichs Datein
for i in range(0, len(taskfields)):
    taskfield = taskfields[i]
    lines = openAndRead("taskfields/"+taskfield+".txt")
    txt = ""
    #Trennen aller Zeilen am Leerzeichen
    for j in range(0, len(lines)):
        tmp = lines[j].split(" ")
        tmp[1] = tmp[1][:len(tmp[1])-1]
        txt = txt + tmp[1]
        if (j < len(lines)-1):
            txt = txt + ", "
    #Schreiben und Ausgeben des javascripts
    print("\t"+"taskfields.add( new Taskfield(" + txt + ") );")

#Bearbeiten aller Fachdatein
for i in range(0, len(subjects)):
    subject = subjects[i]
    lines = openAndRead("subjects/"+subject+".txt")
    txt = ""
    #Trennen aller Zeilen am Leerzeichen
    for j in range(0, len(lines)):
        tmp = lines[j].split(" ")
        tmp[1] = tmp[1][:len(tmp[1])-1]
        txt = txt + tmp[1]
        if (j < len(lines)-1):
            txt = txt + ", "
    #Schreiben und Ausgeben des javascripts
    print("\t"+"subjects.add( new Subject(" + txt + ") );")

print("\t"+"//Fertig")
