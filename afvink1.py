def main():
    zoekwoord = str(input("Op welk zoekwoord wilt u zoeken? "))

    headers, seqs = lees_inhoud()

    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print(headers[i])
            print(seqs[i])
            checkrna = is_dna(seqs[i])
            print("Is het RNA", checkrna)
            knipt(seqs[i])
    print("\n")



def lees_inhoud():
    """Deze functie leest het bestand en split de inhoud in 2 lijsten
    input: Bestand

    output:
    headers --> lijst van headers
    seq --> lijst van sequenties"""
    try:
        bestand = open("/home/sasnee/Documents/School Bio-informatica/Informatica/Blok 1/Week 6/2testseq.txt", "r")
        headers = []
        seqs = []
        seq = ""
        for line in bestand:
            line = line.strip()
            if ">" in line:
                if seq != "":
                    seqs.append(seq)  ##Stript de line en voegt de 2 stukken in 2 verschillende lijsten
                    seq = ""
                headers.append(line)
            else:
                seq += line.strip()
        seqs.append(seq)
        return headers, seqs
    except IOError:
        print("Kan het bestand niet vinden.")
    except ZeroDivisionError:
        print("Kan getal niet delen door 0.")
    except ValueError:
        print("Er zit een verkeerd getal in.")
    except:
        print("Onbekende error.")





def is_dna(seq):
    """Deze functie checked of de sequentie een RNA- of DNA sequentie is
    input: seq - lijst van sequenties

    output: boolean"""
    try:
        print("\n")
        rna = True
        for e in seq:
            if e not in "ATGNC":     ##kijkt of het een RNA of DNA sequentie is
                rna = False

        return rna
    except IOError:
        print("Kan het bestand niet vinden.")
    except ZeroDivisionError:
        print("Kan getal niet delen door 0.")
    except ValueError:
        print("Er zit een verkeerd getal in.")
    except:
        print("Onbekende error.")





def knipt(seq):
    """Deze functie kijkt waar enzymen knippen op de sequentie, ook laat het zien welke enzymen knippen
    input: seq, lijst van sequenties,
        bestand met enzymen

    output: print statement dat laat zien welk enzym knipt"""
    try:
        print("\n")
        enzymen = open(
                "/home/sasnee/Documents/School Bio-informatica/github/Blok 1/1718-owe1a-afvinkopdracht5-Saschadebruijn/enzymen.txt",
                "r")
        for line in enzymen:
            naam, code = line.split()
            code = code.replace("^", "")          ##opent een bestand met enzymen die dan wordt gebruikt bij het checken
            if code in seq:                       ## van de echte sequentie.
                print(naam, "is aanwezig")
            else:
                print(naam, "is niet aanwezig")
    except IOError:
        print("Kan het bestand niet vinden.")
    except ZeroDivisionError:
        print("Kan getal niet delen door 0.")
    except ValueError:
        print("Er zit een verkeerd getal in.")
    except:
        print("Onbekende error.")




main()