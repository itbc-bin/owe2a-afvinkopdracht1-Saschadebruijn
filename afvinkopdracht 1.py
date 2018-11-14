def main():
    try:
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
    except IOError:
        print("Kan het bestand niet vinden.")
    except ZeroDivisionError:
        print("Kan getal niet delen door 0.")
    except ValueError:
        print("Er zit een verkeerd getal in.")
    except:
        print("Onbekende error.")



def lees_inhoud():
    try:
        bestand = open("/home/sasnee/Documents/School Bio-informatica/Informatica/Blok 1/Week 6/2testseq.txt", "r")
        headers = []
        seqs = []
        seq = ""
        for line in bestand:
            line=line.strip()
            if ">" in line:
                if seq != "":
                    seqs.append(seq)
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
    try:
        print("\n")
        rna = True
        for e in seq:
            if e not in "ATGNC":
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
    try:
        print("\n")
        enzymen = open("/home/sasnee/Documents/School Bio-informatica/github/1718-owe1a-afvinkopdracht5-Saschadebruijn/enzymen.txt", "r")
        for line in enzymen:
            naam, code = line.split()
            code = code.replace("^", "")
            if code in seq:
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

    

