import sys

#Datei zum Schreiben öffnen
def openFile(filePath):
    try:
        return open(filePath,"w")
    except:
        print("error")
        sys.exit(0)



#Fragen+ was es so gibt
def ask(txt):
    inp = input("welche " + txt + " gibt es? (Bitte mit Leereichen getrennt und sonst als ein Wort)")
    a = inp.split()
    
    return a


#Fragen zu den Profilen

#--> ein Problem für später


#Fragen zu den Fachtypen
def minimumCountF(txt):
    anzahl = input("Minimale Anzahl der Fächer des Typen " + txt)
    return anzahl

#Fragen zu den Aufgabenbereichen
def minimumCountA(txt):
    anzahl = input("Minimale Anzahl der Fächer des Aufgabenbreiches " + txt)
    return anzahl
    
def shortName(txt):
    short = input("Kürzel des Aufgabenbereichs " + txt + "? ")
    return short

def create(txt):
    out = "[" +txt[0]
    for i in range (1, len(txt)):
        out = out + "," + txt[i]
    out = out + "]"
    return out

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
#eig muss ich hier in die election Datei auch schreiben, welche Fächer etc.es gibt, damit ich ide richtigen Datein öffne
#die anzählen wären dann aber nicht unnötig, da ich in js nur die zaählen brauche und es so nicht neu berechen muss
#done

#Informationen zu den Profilen
for elem in profile:
    print(elem)
    file = openFile("profiles/"+elem + ".txt")
    tmp = input("Fachtypen P1 (Index)")
    tmp = tmp.split("|")
    tmp2 = ""
    for each in tmp:
        tmp2 = tmp2 + create(each.split(" "))
    out = []
    out.append(tmp2)
    tmp = input("Fachtypen P2 (Index)")
    tmp = tmp.split("|")
    tmp2 = ""
    for each in tmp:
        tmp2 = tmp2 + create(each.split(" "))
    out.append(tmp2)
    
    tmp = input("Fachtypen P3 (Index)")
    tmp = tmp.split("|")
    tmp2 = ""
    for each in tmp:
        tmp2 = tmp2 + create(each.split(" "))
    out.append(tmp2)
    
    file.write("name: " + elem + "\n")
    file.write("kindOfSubject: " + create(out) + "\n")
    file.close()


#Informationen zu den Fachtypen
for elem in fachtypen:
    print(elem)
    file = openFile("kindsOfSubjects/" +elem + ".txt")
    file.write("name: " + elem + "\n")
    file.write("numberSubjects: " + minimumCountF(elem) + "\n")
    file.close()
    
#Informationen zu den Aufgabenbereichen
for elem in aufgabenbereiche:
    print(elem)
    file = openFile("taskfields/"+elem + ".txt")
    file.write("name: " + elem + "\n")
    file.write("shortName: " + shortName(elem) + "\n")
    file.write("numberSubjects: " + minimumCountA(elem) + "\n")
    file.close()

#Und jetzt am Ende noch die Fächer
for elem in faecher:
    print(elem)
    file = openFile("subjects/"+elem + ".txt")
    file.write("name: " + elem + "\n")
    tmp = input("Aufgabenbereich (Index):")
    file.write("taskfield: " + tmp + "\n")
    tmp = input("Fachtyp (Index): ")
    file.write("kindOfSubject: " + tmp + "\n")
    tmp = input ("kernfach (true/false)")
    file.write("kernfach: " + tmp + "\n")
    tmp = input("eA: ")
    file.write("eA: " + tmp + "\n")
    tmp = input("gA: ")
    file.write("gA: " + tmp +  "\n")
    tmp = input("prüfungsfachj (array): ")
    file.write ("pfach: " + tmp + "\n")
    tmp = input("eABand (Array): ")
    file.write("eABand: " + tmp + "\n")
    tmp = input("gABand (Array): ")
    file.write("gABand: " + tmp + "\n")
    tmp = input("belegungsverpflichtungen: ")
    file.write("belegungsverpflichtungen: " + tmp + "\n")
    tmp = input("stundeneA: ")
    file.write("stundeneA: " + tmp + "\n")
    tmp = input("stundengAP: ")
    file.write("stundengAP: " + tmp + "\n")
    tmp = input("stundengA: ")
    file.write("stundengA: " + tmp + "\n")
    tmp = input("eANichtWaehlbar: ")
    file.write("eANichtWaehlbar: " + tmp + "\n")
    tmp = input("gANichtWaehlbar: ")
    file.write("gANichtWaehlbar: " + tmp + "\n")
    file.close()