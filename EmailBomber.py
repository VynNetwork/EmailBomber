import os
import time
import smtplib
import colorama
from colorama import Fore,init
colorama.init()



def TermuxBomber():
        os.system("clear")
        print(Fore.LIGHTBLUE_EX + """███████╗███╗   ███╗ █████╗ ██╗██╗         ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██║██║         ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║██║         ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
              
                                    - Created By VynNetwork
            
          
                        1. Send Email               2. Add Credentials
                                    
                        3. Remove Credentials       4. View Credentials
              

""")    
        
        if not os.path.exists('credentials.txt'):
            # Crea il file vuoto se non esiste
            with open('credentials.txt', 'w') as file:
                saved_email = ""
                saved_password = ""
            file.close()
        else:
            # Leggi l'email e la password dal file
            with open('credentials.txt', 'r') as file:
                saved_email = file.readline().strip()
                saved_password = file.readline().strip()
            file.close()

        #Settings Per Collegare l'Email.
        email_provider = 'smtp.gmail.com'
        email_address = saved_email
        email_port = 587
        password = saved_password

        choice = input(Fore.RESET + "Your Choice: ")

        if choice == "2":
            em = input(Fore.RESET + "Your Email: ")
            pw = input(Fore.RESET + "Your App Password: ")
            if not "@" in em:
                input(Fore.RED + "Invalid Email! ")
                return TermuxBomber()
            elif not em:
                input(Fore.RED + "Type Something! ")
                return TermuxBomber()
            elif not pw:
                input(Fore.RED + "Type Something! ")
                return TermuxBomber()
            else:
                with open("credentials.txt","w") as file:
                    file.write(em + "\n")
                    file.write(pw + "\n")
                    file.close()
                    input(Fore.GREEN + """
Credentials Saved Successfully! """)
                    return TermuxBomber()
        
        elif choice == "3":
            with open("credentials.txt","w") as file:
                file.write("")
            file.close()
            input(Fore.GREEN + """
Credentials Removed Successfully! """)
            return TermuxBomber()
        elif choice == "4":
            # Leggi l'email e la password dal file e visualizzale
            with open('credentials.txt', 'r') as file:
                saved_email = file.readline().strip()
                saved_password = file.readline().strip()
            print(Fore.GREEN + f"Saved Email: {saved_email}")
            print(Fore.GREEN + f"Saved App Password: {saved_password}")
            input()
            return TermuxBomber()
        elif choice == "1":
            target_email = input(Fore.RESET + "Target Email: ")

            if "@" not in target_email:
                input(Fore.RED + "Invalid Email! ")
                return TermuxBomber()
            elif not target_email:
                input(Fore.RED + "Type Something! ")
                return TermuxBomber()
            try:
                text_amount = int(input(Fore.RESET + "Text Amount: "))
                if not text_amount:
                    input(Fore.RED + "Type Something! ")
                    return TermuxBomber()
            except ValueError:
                input(Fore.RED + "Only Numbers! ")
                return TermuxBomber()
            
            msg = input(Fore.RESET + "Message: ")
            if not msg:
                input(Fore.RED + "Type Something! ")
                return TermuxBomber()
            try:
                #Connessione Alla Email.
                server = smtplib.SMTP(email_provider, email_port)
                server.starttls()
                server.login(email_address, password)
            except:
                input(Fore.RED + """
Email Not Connected! """)
                return TermuxBomber()

            #Mandare Email.
            for _ in range(0,text_amount):
                server.sendmail(email_address,target_email,msg)
                print(Fore.LIGHTYELLOW_EX + f"""
Message {msg} Sent!""")
                time.sleep(1)
            server.quit()
            input(Fore.GREEN + "{} Texts Were Sent. Hope You Had a Good Time ;)".format(text_amount))
            return TermuxBomber()
        else:
            input(Fore.RED + "Invalid Choice! ")
            return TermuxBomber()




def WindowsBomber():
    os.system("cls")
    print(Fore.LIGHTBLUE_EX + """███████╗███╗   ███╗ █████╗ ██╗██╗         ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██║██║         ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║██║         ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

                                    - Created By VynNetwork
            
          
                        1. Send Email               2. Add Credentials
                                    
                        3. Remove Credentials       4. View Credentials
          

""")
    
    if not os.path.exists('credentials.txt'):
        # Crea il file vuoto se non esiste
        with open('credentials.txt', 'w') as file:
            saved_email = ""
            saved_password = ""
        file.close()
    else:
        # Leggi l'email e la password dal file
        with open('credentials.txt', 'r') as file:
            saved_email = file.readline().strip()
            saved_password = file.readline().strip()
        file.close()

    #Settings Per Collegare l'Email.
    email_provider = 'smtp.gmail.com'
    email_address = saved_email
    email_port = 587
    password = saved_password

    choice = input(Fore.RESET + "Your Choice: ")

    if choice == "2":
        em = input(Fore.RESET + "Your Email: ")
        pw = input(Fore.RESET + "Your App Password: ")
        if not "@" in em:
            input(Fore.RED + "Invalid Email! ")
            return WindowsBomber()
        elif not em:
            input(Fore.RED + "Type Something! ")
            return WindowsBomber()
        elif not pw:
            input(Fore.RED + "Type Something! ")
            return WindowsBomber()
        else:
            with open("credentials.txt","w") as file:
                file.write(em + "\n")
                file.write(pw + "\n")
                file.close()
                input(Fore.GREEN + """
Credentials Saved Successfully! """)
                return WindowsBomber()
    
    elif choice == "3":
        with open("credentials.txt","w") as file:
            file.write("")
        file.close()
        input(Fore.GREEN + """
Credentials Removed Successfully! """)
        return WindowsBomber()
    elif choice == "4":
        # Leggi l'email e la password dal file e visualizzale
        with open('credentials.txt', 'r') as file:
            saved_email = file.readline().strip()
            saved_password = file.readline().strip()
        print(Fore.GREEN + f"Saved Email: {saved_email}")
        print(Fore.GREEN + f"Saved App Password: {saved_password}")
        input()
        return WindowsBomber()
    elif choice == "1":
        target_email = input(Fore.RESET + "Target Email: ")

        if "@" not in target_email:
            input(Fore.RED + "Invalid Email! ")
            return WindowsBomber()
        elif not target_email:
            input(Fore.RED + "Type Something! ")
            return WindowsBomber()
        try:
            text_amount = int(input(Fore.RESET + "Text Amount: "))
            if not text_amount:
                input(Fore.RED + "Type Something! ")
                return WindowsBomber()
        except ValueError:
            input(Fore.RED + "Only Numbers! ")
            return WindowsBomber()
        
        msg = input(Fore.RESET + "Message: ")
        if not msg:
            input(Fore.RED + "Type Something! ")
            return WindowsBomber()
        try:
            #Connessione Alla Email.
            server = smtplib.SMTP(email_provider, email_port)
            server.starttls()
            server.login(email_address, password)
        except:
            input(Fore.RED + """
Email Not Connected! """)
            return WindowsBomber()

        #Mandare Email.
        for _ in range(0,text_amount):
            server.sendmail(email_address,target_email,msg)
            print(Fore.LIGHTYELLOW_EX + f"""
Message {msg} Sent!""")
            time.sleep(1)
        server.quit()
        input(Fore.GREEN + "{} Texts Were Sent. Hope You Had a Good Time ;)".format(text_amount))
        return WindowsBomber()
    
    else:
        input(Fore.RED + "Invalid Choice! ")
        return WindowsBomber()
        

class Bella:
    @staticmethod






    def main():
        environment = Bella.detect_environment()

        if environment == "Termux":
            TermuxBomber()
        elif environment == "Windows":
            WindowsBomber()
        else:
            input(Fore.RED + """Where Did You Launch This File From?
Unfortunately You Can Only Run It On Windows & Termux""")
            exit()

    @staticmethod





    def detect_environment():
        if os.name == "posix" and "termux" in os.environ.get("SHELL", "").lower():
            return "Termux"
        elif os.name == "nt":
            return "Windows"
        else:
            return "Sconosciuto"

if __name__ == "__main__":
    Bella.main()
