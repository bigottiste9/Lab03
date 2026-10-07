from deposito_strumenti import DepositoStrumenti
from datetime import datetime

#funzione che visualizza il menu
def menu():

    #stampo il titolo del menu
    print("\n--- MENU DEPOSITO STRUMENTI ---")

    #stampo tutte le operazioni disponibii
    print("1. Modifica nome del responsabile del deposito")
    print("2. Carica strumenti da file")
    print("3. Aggiungi un nuovo strumento (da tastiera)")
    print("4. Visualizza strumenti ordinati per marca")
    print("5. Presta uno strumento")
    print("6. Termina prestito strumento")
    print("7. Esci")

    #chiedo all'utente di scegliere un'opzione
    return input("Scegli un'opzione >> ")

#funzione principale del programma
def main():

    #creo il deposito con nome e responsabile iniziali
    deposito = DepositoStrumenti(
        "Deposito Strumenti Civico",
        "Alessandro Visconti"
    )

    #mantengo il programma attivo finchè l'utente non sceglie 7
    while True:

        #mostro il menu e salvo la scelta
        scelta = menu()

        #modifica del responsabile
        if scelta == "1":

            #chiedo il nuovo nome del responsabile
            nuovo_responsabile = input(
                "Inserisci il nuovo responsabile: "
            )

            #modifico direttamente l'attributo
            deposito.responsabile = nuovo_responsabile

            #comunico la modifica fatta
            print ("Responsabile modificato correttamente.")

        #caricamento degli strumenti del file
        elif scelta == "2":

            #continuo a chiedere il file finchè non viene trovato
            while True:
                try:

                    #chiedo il percorso del file
                    file_path = input(
                        "Inserisci il path del file da caricare: "
                    ).strip()

                    #cerco gli strumenti
                    deposito.carica_file_strumenti(file_path)

                    #se tutto va bene usciamo dal ciclo
                    print("File caricato correttamente.")
                    break

                #gestisco il caso in cui il file non esiste
                except FileNotFoundError:
                    print("Errore: file non trovato")

                #gestisco possibili altri errori
                except Exception as e:
                    print("Errore:", e)

        #aggiunta di un nuovo strumento
        elif scelta == "3":

            #chiedo il tipo dello strumento
            tipo = input("Tipo di strumento: ")

            #chiedo la marca
            marca = input("Marca: ")
            try:

                #chiedo l'anno e lo trasformo in intero
                anno_acquisto = int(
                    input("Anno di acquisto: ").strip()
                )

                #chiedo il valore e lo trasformo in float
                valore = float(
                    input("Valore (euro): ").strip()
                )

            #gestisco l'inserimento di valori numerici
            except ValueError:
                print(
                    "Errore: inserire valori numerici validi per anno e valore."
                )

                #torno all'inizio del ciclo
                continue

            #aggiungo lo strumento al deposito
            strumento = deposito.aggiungi_strumento(
                tipo,
                marca,
                anno_acquisto,
                valore
            )

            #mostro lo strumento appena creato
            print(f"Strumento aggiunto: {strumento}")


        #visualizzo gli strumenti ordinati
        elif scelta == "4":

            #ottengo la lista ordinata per marca
            strumenti_ordinati = deposito.strumenti_ordinati_per_marca()

            #controllo se la lista è vuota
            if len(strumenti_ordinati) == 0:
                print("Non ci sono strumenti nel deposito.")
            else:
                #stampo uno alla volta gli strumenti
                for s in strumenti_ordinati:
                    print(f'- {s}')

        #creazione di un nuovo prestito
        elif scelta == "5":

            #chiedo il codice dello strumento
            id_strumento = input(
                "ID strumento: "
            )

            #chiedo il cognome dell'alievo
            cognome_allievo = input(
                "Cognome allievo: "
            )

            #ottengo la data di oggi
            data = datetime.now().date()
            try:

                #creo il nuovo prestito
                prestito = deposito.nuovo_prestito(
                    data,
                    id_strumento,
                    cognome_allievo
                )

                #mostro il prestito creato
                print(f"Prestito andato a buon fine: {prestito}")

            #gestisco gli errori del metodo
            except Exception as e:
                print(e)

        #terminazione di un prestito
        elif scelta == "6":

            #chiediamo il codice del prestito
            id_prestito = input(
                "ID prestito da terminare: "
            )
            try:

                #termino il prestito
                deposito.termina_prestito(id_prestito)

                #comunico il successo dell'operzione
                print(
                    f"Prestito {id_prestito} terminato con successo."
                )

            #gestisco gli errori
            except Exception as e:
                print(e)

        #esco dal programma
        elif scelta == "7":

            #stampo il mess di uscita
            print("Uscita dal programma...")

            #interrompo il ciclo
            break

        #gestione di una scelta non valida
        else:
            print("Opzione non valida!")

#avvio il programma solo se questo file viene eseguito corretamente
if __name__ == "__main__":
    main()
