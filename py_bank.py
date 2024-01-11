# SIMULACIJA BANKOVNOG RAČUNA


#IMPORT

import os
import datetime as dt
import random

#inicijalizacija

account_owner_data = {
    'Naziv Tvrtke': '',
    'Ulica i broj sjedišta Tvrtke': '',
    'Poštanski broj sjedišta Tvrtke': '',
    'Grad u kojem je sjedište Tvrtke': '',
    'OIB Tvrtke': '',
    'Ime i prezime odgovorne osobe Tvrtke': ''
}

#VARIJABLE
transaction_id = 0
transactions = { }

currency = ''
account_number = ''
account_balance = 0

def main_menu(message = 'Još niste otvorili račun. Molimo prvo kreirajte račun. Hvala!'):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print('*' * 65)
        print('PyBANK ALGEBRA\n'.center(65), '\n')
        print('GLAVNI IZBORNIK\n'.center(65))
        
        print('1. Kreiranje računa')
        print('2. Prikaz stanja računa')
        print('3. Prikaz prometa po računu')
        print('4. Polog novca na račun')
        print('5. Podizanje novca s računa')
        print('0. Izlaz')
        print()
        print(65 * '_')
        print(message)
        print(65 * '_')

        choice = int(input('Vaš izbor:\t'))

        if choice == 1:
            create_account()
        elif choice == 2 and account_owner_data['Naziv Tvrtke'] != '':
            show_account_balance()
        elif choice == 3 and account_owner_data['Naziv Tvrtke'] != '':
            show_transactions()
        elif choice == 4 and account_owner_data['Naziv Tvrtke'] != '':
            money_deposit()
        elif choice == 5 and account_owner_data['Naziv Tvrtke'] != '':
            money_withdrawal()
        elif choice == 0:
            exit()
            break
            # os.system('cls' if os.name == 'nt' else 'clear') 
            # print('*' * 65)
            # print('PyBANK ALGEBRA\n'.center(65), '\n')
            # print('Hvala što ste koristili aplikaciju. Doviđenja!')
            # False
        elif choice not in range(6):
            message = 'Pogrešan unos, pokušajte ponovno!'
        else:
            message = 'Prvo kreirajte korisnički račun.'
    


def create_account():
    while True:
        
        os.system('cls' if os.name == 'nt' else 'clear') 
        print('*' * 65)
        print('PyBANK ALGEBRA\n'.center(65), '\n')
        print('KREIRANJE RACUNA\n'.center(65))
        print('Podaci o vlasniku racuna\n'.center(65))
        
        for key in account_owner_data.keys():
            lenght = 40 - len(list(key))
            account_owner_data[key] = input (f'{key}: {'':<{lenght}}')
            if key == 'OIB Tvrtke':
                while len(account_owner_data[key]) != 11:
                    print('OIB mora imati 11 brojeva!')
                    account_owner_data[key] = input (f'{key}: {'':<{lenght}}')
        print()
        global currency
        while True: 
            currency = input('Upišite naziv valute računa (EUR ili HRK):\t')
            if currency.upper() == 'EUR' or currency.upper() == 'HRK':
                break
            else:
               print('Krivo ste unijeli!')
               continue
        while True:
            save = input('\nSPREMI? (Pritisnite bilo koju tipku)')
            if save != '':
                save_account_data()
            else:
                continue
            


       
        
def save_account_data():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('KREIRANJE RACUNA\n'.center(65))
    print(f'Podaci o vlasniku računa tvrtke {account_owner_data["Naziv Tvrtke"]} su uspješno spremljeni.'.center(65))
    print()
    ordinal_number = random.randint(1, 100000)
    for key, value in account_owner_data.items():
        lenght = 40 - len(list(key))
        print((f'{key}: {'':<{lenght}}{value}'))

    print('\n')
    global currency
    print(f'Valuta računa: {currency.upper()}')
    print('\n')
    formatted_ordinal_number = '{:04d}'.format(ordinal_number)
    global account_number
    account_number = f'BA-{dt.datetime.now().year}-{dt.datetime.now().month:02d}-{formatted_ordinal_number}'
    print(f'Broj računa:\t{account_number}')

    print('\nSada trebate položiti novac na račun.')
    while True:
            save = input('\nZa nastavak pritisnite bilo koju tipku)')
            if save != '':
                money_deposit('Polog kod otvaranja računa')





def show_account_balance():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('Stanje računa\n'.center(65), '\n')
    print(f'Broj računa {account_number}')
    print(f'\nTrenutno stanje računa:\t{account_balance:.2f} {currency.upper()}\n')
    input('Za povratak na glavni meni pritisnite bilo koju tipku.')
    main_menu(f'Račun br. {account_number}')

def show_transactions():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('TRANSAKCIJE\n'.center(65), '\n')
    print(f'Broj računa {account_number}')
    for key, value in transactions.items():
        print(f'{key}' + 65 *'-')
        print(f'\tDatum i vrijeme transakcije:\t{value[1]}')
        print(f'\tOpis:\t{value[2]}')
        print(f'\tValuta:\t{value[3]}')
        print(f'\tIznos:\t{value[4]}')
        print(f'\tStanje računa:\t{value[5]}')
        print(f'\tBroj računa:\t{value[6]}')

    input('\n\nZa povratak na glavni meni pritisnite bilo koju tipku.')
    main_menu(f'Račun br. {account_number}')

def money_deposit(description = 'Polog'):
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('POLOG NOVCA NA RAČUN\n'.center(65))
    print('\n')
    global account_number
    print(f'Broj racuna {account_number}')

    global account_balance
    global currency
    print(f'Trenutno stanje računa:\t{account_balance:.2f} {currency.upper()}\n')

    print('Molimo Vas upišite iznos koji želite položiti na račun.\nNAPOMENA Molimo Vas koristite decimalnu točku, a ne zarez.\n')
    amount = input('Iznos: \t')
    global transaction_id
    global transactions
    if amount != '':
        amount = float(amount)

        transaction = ['']
        account_balance += amount
            # transakcija - datum, vrijeme, opis, iznos, stanje, broj racuna
        date_of_transaction = dt.datetime.now()

        transaction.append(date_of_transaction)
        transaction.append(description)
        transaction.append(currency)
        transaction.append(amount)
        transaction.append(account_balance)
        transaction.append(account_number)
        transaction_id += 1
        transactions[transaction_id] = transaction

    else:
        amount = 0.00
    input('Za povratak na glavni meni pritisnite bilo koju tipku.')
    main_menu(f'Račun br. {account_number}')
    
def money_withdrawal(description = 'Podizanje sredstava'):
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('PODIZANJE NOVCA SA RAČUNA\n'.center(65))
    print('\n')
    global account_number
    print(f'Broj racuna {account_number}')

    global account_balance
    global currency
    print(f'Trenutno stanje računa:\t{account_balance:.2f} {currency.upper()}\n')
    while True:
        print('Molimo Vas upišite iznos koji želite podignuti sa računa.\nNAPOMENA Molimo Vas koristite decimalnu točku, a ne zarez.\n')
        amount = input('Iznos: \t')
        if amount != '':
            amount = float(amount)
        if amount <= account_balance:
            break
        else:
            print('\nNemate dovoljno sredstava za podizanje unesenog iznosa.')

    global transaction_id
    global transactions

    transaction = ['']
    account_balance -= amount
        # transakcija - datum, vrijeme, opis, iznos, stanje, broj racuna
    date_of_transaction = dt.datetime.now()

    transaction.append(date_of_transaction)
    transaction.append(description)
    transaction.append(currency)
    transaction.append(amount)
    transaction.append(account_balance)
    transaction.append(account_number)
    transaction_id += 1
    transactions[transaction_id] = transaction

    input('Za povratak na glavni meni pritisnite bilo koju tipku.')
    main_menu(f'Račun br. {account_number}')

def exit():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('Hvala što ste koristili aplikaciju. Doviđenja!')
    
    

main_menu()