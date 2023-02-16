# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:31:20 2023

@author: isabe
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

#Datei zum Schreiben öffnen
def openFile(filePath):
    try:
        return open(filePath,"w")
    except:
        print("error")
        sys.exit(0)
        
def create(txt):
    txt = txt[2:len(txt)-3]
    txt = txt.split('","')
    return txt


#Öffnen der Election Datei
lines = openAndRead("election/election.txt")
#Auslesen der Datei
profiles = lines[0].split(" ")[1]
#profiles.remove(profiles[0])


kindOfSubjects = lines[1].split(" ")[1]
#kindOfSubjects.remove(kindOfSubjects[0])


taskfields = lines[2].split(" ")[1]
#taskfields.remove(taskfields[0])


subjects = lines[3].split(" ")[1]
#subjects.remove(subjects[0])

profiles = create(profiles)
kindOfSubjects = create(kindOfSubjects)
taskfields = create(taskfields)
subjects = create(subjects)


#Bearbeiten aller Profil Datein
for i in range(0, len(profiles)):
    profile = profiles[i]
    lines = openAndRead("profiles/"+profile+".txt")
    #Trennen aller Zeilen am Leerzeichen
    tmp = lines[0].split(" ")
    txt = tmp[0] + ' "' + tmp[1][:len(tmp[1])-1] + '"\n'
    lines[0] = txt
    #Schreiben und Ausgeben des javascripts
    file = openFile("profiles/"+profile+".txt")
    for j in range (0, len(lines)):
        file.write(lines[j])
    file.close()

#Bearbeiten aller Fachtypen Datein
for i in range(0, len(kindOfSubjects)):
    kindOfSubject = kindOfSubjects[i]
    lines = openAndRead("kindsOfSubjects/"+kindOfSubject+".txt")
    #Trennen aller Zeilen am Leerzeichen
    tmp = lines[0].split(" ")
    txt = tmp[0] + ' "' + tmp[1][:len(tmp[1])-1] + '"\n'
    lines[0] = txt
    #Schreiben und Ausgeben des javascripts
    file = openFile("kindsOfSubjects/"+kindOfSubject+".txt")
    for j in range (0, len(lines)):
        file.write(lines[j])
    file.close()

#Bearbeiten aller Aufgabenbereichs Datein
for i in range(0, len(taskfields)):
    taskfield = taskfields[i]
    lines = openAndRead("taskfields/"+taskfield+".txt")
    #Trennen aller Zeilen am Leerzeichen
    tmp = lines[0].split(" ")
    txt = tmp[0] + ' "' + tmp[1][:len(tmp[1])-1] + '"\n'
    lines[0] = txt
    tmp = lines[1].split(" ")
    txt = tmp[0] + ' "' + tmp[1][:len(tmp[1])-1] + '"\n'
    lines[1] = txt
    #Schreiben und Ausgeben des javascripts
    file = openFile("taskfields/"+taskfield+".txt")
    for j in range (0, len(lines)):
        file.write(lines[j])
    file.close()

#Bearbeiten aller Fachdatein
for i in range(0, len(subjects)):
    subject = subjects[i]
    lines = openAndRead("subjects/"+subject+".txt")
    #Trennen aller Zeilen am Leerzeichen
    tmp = lines[0].split(" ")
    txt = tmp[0] + ' "' + tmp[1][:len(tmp[1])-1] + '"\n'
    lines[0] = txt
    #Schreiben und Ausgeben des javascripts
    file = openFile("subjects/"+subject+".txt")
    for j in range (0, len(lines)):
        file.write(lines[j])
    file.close()

