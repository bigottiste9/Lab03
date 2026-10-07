import csv
from operator import attrgetter

#classe che rappresenta un singolo strumento musicale
class Strumento:

    #costruttore dello strumento
    def __init__(self, id_strumento, tipo, marca, anno_acquisto, valore):
        self.id_strumento = id_strumento
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    #rappresentazione testuale dello strumento
    def __str__ (self):
        return f"{self.id_strumento}-{self.tipo}-{self.marca}-{self.anno_acquisto}-{self.valore: .2f} euro"

#classe che rappresenta un prestito
class Prestito:

    #costruttore del prestito
    def __init__(self, id_prestito, data, id_strumento, cognome_alievo):
        self.id_prestito = id_prestito
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_alievo = cognome_alievo
        self.terminato = False

    #rappresentazione testuale del prestito
    def __str__ (self):
        if self.terminato:
            stato= "terminato"
        else:
            stato = "in corso"

        return f"{self.id_prestito}- {self.data} - {self.id_strumento} - {self.cognome_alievo} - {stato}"

#classe che gestisce tutto il deposito
class DepositoStrumenti:

    #costruttore del deposito
    def __init__(self, nome, responsabile):
        #salvo il nome del deposito
        self.nome = nome
        #salvo il nome del responsabile
        self.responsabile = responsabile
        #lista che contiene tutti gli strumenti
        self.strumenti = []
        #lista che contiene tutti i prestiti
        self.prestiti = []

    #metodo che carica gli strumenti dal file CSV
    def carica_file_strumenti(self,file_path):

        #apro il file in modalità lettura
        with open(file_path, "r", newline = "", encoding ="utf-8") as file:

            #creo il lettore del file CSV
            lettore= csv.reader(file)

            #analizzo una riga alla volta
            for riga in lettore:

                #prendo i datipresenti nella riga
                id_strumento = riga[0]
                tipo = riga[1]
                marca = riga[2]
                anno_acquisto = riga[3]
                valore = float(riga[4])

                #creo un nuovo oggetto Strumento
                strumento= Strumento(
                    id_strumento,
                    tipo,
                    marca,
                    anno_acquisto,
                    valore
                )

                #inserisco lo strumento nella lista
                self.strumenti.append(strumento)

    #metodo che aggiunge un nuovo strumento
    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):

        #parto dal numero 1
        numero = 1

        #cerco il primo numero libero
        while True:

            #creo il codice dello strumento
            nuovo_id = "S" + str(numero)

            #controllo se il codice esiste già
            esiste = False

            for strumento in self.strumenti:
                if strumento.id_strumento == nuovo_id:
                    esiste = True

            #se non esiste posso utilizzare questo codice
            if not esiste:
                break

            #altrimenti passo al numero succesivo
            numero += 1

        #creo il nuovo oggetto Strumento
        strumento = Strumento(
            nuovo_id,
            tipo,
            marca,
            anno_acquisto,
            valore
        )

        #inserisco il nuovo strumento nella lista
        self.strumenti.append(strumento)

        #restituisco lo strumento creato
        return strumento

    #metodo che ordina gli strumenti in base alla marca
    def strumenti_ordinati_per_marca(self):

        #creo una nuova lista ordinata per marca
        strumenti_ordinati = sorted(
            self.strumenti,
            key = attrgetter('marca'),
        )

        #restituisco la lista ordinata
        return strumenti_ordinati

    #metodo che crea un nuovo prestito
    def nuovo_prestito(self, data, id_strumento, cognome_allievo):

        #cerco lo strumento richiesto
        strumento_trovato = None

        for strumento in self.strumenti:
            if strumento.id_strumento == id_strumento:
                strumento_trovato = strumento

        #se lo strumento non esiste lancio un'eccezione
        if strumento_trovato is None:
            raise Exception("Lo strumento non è presente nel deposito.")

        #controllo se lo strumento è gia in prestito
        for prestito in self.prestiti:

            if prestito.id_strumento == id_strumento and prestito.terminato == False:
                raise Exception("Lo strumento è già in prestito.")

        #calcolo il prossimo numero del prestito
        numero = len(self.prestiti) + 1

        #creo il codice del prestito
        id_prestito = "P" + str(numero)

        #creo il nuovo prestito
        prestito = Prestito(
            id_prestito,
            data,
            id_strumento,
            cognome_allievo
        )

        #inserisco il prestito nella lista
        self.prestiti.append(prestito)

        #restituisco il prestito creato
        return prestito

    #metodo che termina un prestito
    def termina_prestito(self, id_prestito):

        #cerco il prestito nella lista
        for prestito in self.prestiti:

            #controlloil codice del prestito
            if prestito.id_prestito == id_prestito:

                #controllo che non sia terminato
                if prestito.terminato :
                    raise Exception("Il prestito è già terminato.")

                #modifico lo stato del prestito
                prestito.terminato = True

                #restituisco il prrstito terminato
                return prestito

        #se non ho trovato il prestito lancio un'eccezione
        raise Exception("Il prestito non esiste.")