# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:41:08 2023

@author: isabe
"""

import sys

#Methode zum öffnenen und lesen von Datein mit Rückgabe eines Arrays mit allen Zeilen
#--> daraufachten, dass das letzte wort ggf. noch ein \n hat
def openFile(filePath):
    try:
        file = open(filePath,"w")
    except:
        print("error")
        sys.exit(0)
    return file

#Fragen, was es so gibt
def ask(txt):
    inp = input("welche " + txt + " gibt es? (Bitte mit Leereichen getrennt und sonst als ein Wort)")
    a = inp.split()
    
    return a

def createString(txt):
    out = '["' +txt[0]
    for i in range (1, len(txt)):
        out = out + '","' + txt[i]
    out = out + '"]'
    return out


#Start Programm
print("Halt hier eine kleine Anleitung oder auch nicht weil fast")

#Allgemeine Informationen zu der Wahl

election = openFile("election/election.txt")

#Vielelicht hier erstmal abfragen welcher Fächer etc. es gibt
faecher = ask("Fächer")
aufgabenbereiche = ask("Aufgabenbereiche")
fachtypen = ask("Fachtypen")
profile = ask("Profile")

#Anzahlen oder Arrays seit neustem in Wahl Datei schreiben
election.write("profiles: "+ createString(profile)+ "\n")

election.write("kindOfSubject: " + createString(fachtypen) + "\n")

election.write("taskfields: " + createString(aufgabenbereiche) + "\n")

election.write("subjects: " + createString(faecher) + "\n")

election.close()