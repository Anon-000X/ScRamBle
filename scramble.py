from os import system, name
from time import sleep
import random as gen
import string as st
import colorama as cl
from colorama import Fore, Style, Back
def clear():
    if not name == 'nt':
        _ = system('clear')
    else:
        _ = system('cls')
def banner():
    print(f'''
    {Fore.GREEN}MP""""""`MM          MM"""""""`MM                     M#"""""""'M  dP          
    M  mmmmm..M          MM  mmmm,  M                     ##  mmmm. `M 88          
    {Fore.GREEN}{Style.BRIGHT}M.      `YM .d8888b. M'        .M .d8888b. 88d8b.d8b. #'        .M 88 .d8888b.
    MMMMMMM.  M 88'  `"" MM  MMMb. "M 88'  `88 88'`88'`88 M#  MMMb.'YM 88 88ooood8
    {Fore.BLUE}M. .MMM'  M 88.  ... MM  MMMMM  M 88.  .88 88  88  88 M#  MMMM'  M 88 88.  ... 
    Mb.     .dM `88888P' MM  MMMMM  M `88888P8 dP  dP  dP M#       .;M dP `88888P' 
    {Fore.CYAN}{Style.BRIGHT}MMMMMMMMMMM          MMMMMMMMMMMM                     M#########M              
    {Style.RESET_ALL}''')

def rerun():
    rerun = True
    while rerun:
        program()
        rerun == 'y' 
def run():
        clear()
        banner()
        choice = gen.randint (0,3)
        symbol = gen.choice(st.punctuation) *2
        numeral = gen.randint (0,9999)
        if choice == 0:
            clear()
            banner()
            print('Your PassPhrase is: ' + symbol + phrase + str(numeral))
            user_input = input('\nPress enter to continue or 0 to generate again! ')
            if user_input == '0':
                run()
            else:
                rerun()
        elif choice == 1:
            clear()
            banner()
            print('Your PassPhrase is: ' + phrase + str(numeral) + symbol)
            user_input = input('\nPress enter to continue or 0 to generate again! ')
            if user_input == '0':
                run()
            else:
                rerun()
        elif choice == 2:
                clear()
                banner()
                print('Your PassPhrase is: ' + phrase + symbol + str(numeral))
                user_input = input('\nPress enter to continue or 0 to generate again! ')
                if user_input == '0':
                    run()
        elif choice == 3:
                clear()
                banner()
                print('Your PassPhrase is: ' + str(numeral) + phrase + symbol)
                user_input = input('\nPress enter to continue or 0 to generate again! ')
                if user_input == '0':
                    run()
                else:
                    rerun()
def generate():
    clear()
    banner()
    counter_max = int(input('Enter number of passphrases to generate: '))
    file_name = str(input('\nEnter name of file for output: '))
    counter = 0
    text_file = open(file_name + ".txt", "wt")
    w = text_file.write('- - - SCrAmBLe ! - - - ')
    while counter < counter_max:
        clear()
        banner()
        choice = gen.randint (0,3)
        symbol = gen.choice(st.punctuation) *2
        numeral = gen.randint (0,9999)
        if choice == 0:
            w = text_file.write('\n' + str(numeral) + phrase + symbol)
            form = (str(numeral) + phrase + symbol)
            print('Phrase Generated: ' + form)
            counter += 1
            sleep(.1)
        if choice == 1:
            w = text_file.write('\n' + symbol + str(numeral) + phrase)
            form = (symbol + str(numeral) + phrase)
            print('Phrase Generated: ' + form)
            counter += 1
            sleep(.1)
        if choice == 2:
            w = text_file.write('\n' + phrase + symbol + str(numeral))
            form = (phrase + symbol + str(numeral))
            print('Phrase Generated: ' + form)
            counter += 1
            sleep(.1)
        if choice == 3:
            w = text_file.write('\n' + symbol + phrase + str(numeral))
            form = (symbol + phrase + str(numeral))
            print('Phrase Generated: ' + form)
            counter += 1
            sleep(.1)
        if counter >= counter_max:
            clear()
            banner()
            w = text_file.write('\n- - - ScRAmbLeD ! - - -')
            text_file.close()
            print('Finished Generating!')
            sleep(.8)
            rerun()
def pass_num():
    global digit_count
    max = int('9' * digit_count)
    passcode = gen.randint(0, max)
    check = len(str(abs(passcode)))
    if check != digit_count:
        pass_num()
    else:
        clear()
        banner()
        print('Your Passcode is: ' + passcode)
        user_input = input('\nPress enter to continue or 0 to generate again! ')
        if user_input == '0':
            pass_num()
        else:
            rerun()
phrase = 'ScRamble Me!'
def program():
    global phrase
    sleep(.3)
    clear()
    banner()
    print(f'     {Fore.GREEN}{Style.BRIGHT}SC{Style.RESET_ALL}{Fore.BLUE}rAm{Fore.CYAN}{Style.BRIGHT}bLE {Style.RESET_ALL}- - - {Fore.RED}PassPhrase Generator{Style.RESET_ALL}')
    print('\nCurrent phrase is ' + phrase + ' :')
    print('\n1) Create Passphrase\n\n2) Create Text File With List of Phrases\n\n3) Generate Passcodes\n\n4) Set Phrase\n\n0) Exit')
    user_input = input('\nEnter option: ')
    if user_input == '0':
        clear()
        exit()
    elif user_input == '1':
        run()
    elif user_input == '2':
        clear()
        generate()
    elif user_input == '3':
        clear()
        banner()
        digit_count = int(input('Enter number of digits for passcode: '))
        return digit_count
        pass_num()
    elif user_input == '4':
        clear()
        banner()
        phrase = input('Enter a word or phrase you can remember: ')
        return phrase
    else:
        print(user_input + '\n is not an option!')
        sleep(.5)
        rerun()
rerun()
