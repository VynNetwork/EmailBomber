import os #line:1:import os
import time #line:2:import time
import smtplib #line:3:import smtplib
import colorama #line:4:import colorama
from colorama import Fore ,init #line:5:from colorama import Fore,init
colorama .init ()#line:6:colorama.init()
def TermuxBomber ():#line:10:def TermuxBomber():
        os .system ("clear")#line:11:os.system("clear")
        print (Fore .LIGHTBLUE_EX +"""███████╗███╗   ███╗ █████╗ ██╗██╗         ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██║██║         ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║██║         ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
              
                                    - Created By VynNetwork
            
          
                        1. Send Email               2. Add Credentials
                                    
                        3. Remove Credentials       4. View Credentials
              

""")#line:27:""")
        if not os .path .exists ('credentials.txt'):#line:29:if not os.path.exists('credentials.txt'):
            with open ('credentials.txt','w')as OOOO00O00OO0OO0OO :#line:31:with open('credentials.txt', 'w') as file:
                OO00OOOOO0O0O0O0O =""#line:32:saved_email = ""
                OO0O00OO00O0000OO =""#line:33:saved_password = ""
            OOOO00O00OO0OO0OO .close ()#line:34:file.close()
        else :#line:35:else:
            with open ('credentials.txt','r')as OOOO00O00OO0OO0OO :#line:37:with open('credentials.txt', 'r') as file:
                OO00OOOOO0O0O0O0O =OOOO00O00OO0OO0OO .readline ().strip ()#line:38:saved_email = file.readline().strip()
                OO0O00OO00O0000OO =OOOO00O00OO0OO0OO .readline ().strip ()#line:39:saved_password = file.readline().strip()
            OOOO00O00OO0OO0OO .close ()#line:40:file.close()
        OO00O0OOO00O0O00O ='smtp.gmail.com'#line:43:email_provider = 'smtp.gmail.com'
        OO0O0OO0O0O000O0O =OO00OOOOO0O0O0O0O #line:44:email_address = saved_email
        O0O0OO0OOO000OOOO =587 #line:45:email_port = 587
        O00OO0OOOO0OO000O =OO0O00OO00O0000OO #line:46:password = saved_password
        O00O0OO0O00OOO0OO =input (Fore .RESET +"Your Choice: ")#line:48:choice = input(Fore.RESET + "Your Choice: ")
        if O00O0OO0O00OOO0OO =="2":#line:50:if choice == "2":
            O00OO0O000000OOOO =input (Fore .RESET +"Your Email: ")#line:51:em = input(Fore.RESET + "Your Email: ")
            OOOO0O0000OO000O0 =input (Fore .RESET +"Your App Password: ")#line:52:pw = input(Fore.RESET + "Your App Password: ")
            if not "@"in O00OO0O000000OOOO :#line:53:if not "@" in em:
                input (Fore .RED +"Invalid Email! ")#line:54:input(Fore.RED + "Invalid Email! ")
                return TermuxBomber ()#line:55:return TermuxBomber()
            elif not O00OO0O000000OOOO :#line:56:elif not em:
                input (Fore .RED +"Type Something! ")#line:57:input(Fore.RED + "Type Something! ")
                return TermuxBomber ()#line:58:return TermuxBomber()
            elif not OOOO0O0000OO000O0 :#line:59:elif not pw:
                input (Fore .RED +"Type Something! ")#line:60:input(Fore.RED + "Type Something! ")
                return TermuxBomber ()#line:61:return TermuxBomber()
            else :#line:62:else:
                with open ("credentials.txt","w")as OOOO00O00OO0OO0OO :#line:63:with open("credentials.txt","w") as file:
                    OOOO00O00OO0OO0OO .write (O00OO0O000000OOOO +"\n")#line:64:file.write(em + "\n")
                    OOOO00O00OO0OO0OO .write (OOOO0O0000OO000O0 +"\n")#line:65:file.write(pw + "\n")
                    OOOO00O00OO0OO0OO .close ()#line:66:file.close()
                    input (Fore .GREEN +"""
Credentials Saved Successfully! """)#line:68:Credentials Saved Successfully! """)
                    return TermuxBomber ()#line:69:return TermuxBomber()
        elif O00O0OO0O00OOO0OO =="3":#line:71:elif choice == "3":
            with open ("credentials.txt","w")as OOOO00O00OO0OO0OO :#line:72:with open("credentials.txt","w") as file:
                OOOO00O00OO0OO0OO .write ("")#line:73:file.write("")
            OOOO00O00OO0OO0OO .close ()#line:74:file.close()
            input (Fore .GREEN +"""
Credentials Removed Successfully! """)#line:76:Credentials Removed Successfully! """)
            return TermuxBomber ()#line:77:return TermuxBomber()
        elif O00O0OO0O00OOO0OO =="4":#line:78:elif choice == "4":
            with open ('credentials.txt','r')as OOOO00O00OO0OO0OO :#line:80:with open('credentials.txt', 'r') as file:
                OO00OOOOO0O0O0O0O =OOOO00O00OO0OO0OO .readline ().strip ()#line:81:saved_email = file.readline().strip()
                OO0O00OO00O0000OO =OOOO00O00OO0OO0OO .readline ().strip ()#line:82:saved_password = file.readline().strip()
            print (Fore .GREEN +f"Saved Email: {OO00OOOOO0O0O0O0O}")#line:83:print(Fore.GREEN + f"Saved Email: {saved_email}")
            print (Fore .GREEN +f"Saved App Password: {OO0O00OO00O0000OO}")#line:84:print(Fore.GREEN + f"Saved App Password: {saved_password}")
            input ()#line:85:input()
            return TermuxBomber ()#line:86:return TermuxBomber()
        elif O00O0OO0O00OOO0OO =="1":#line:87:elif choice == "1":
            O00OOOO0OO0OOOO00 =input (Fore .RESET +"Target Email: ")#line:88:target_email = input(Fore.RESET + "Target Email: ")
            if "@"not in O00OOOO0OO0OOOO00 :#line:90:if "@" not in target_email:
                input (Fore .RED +"Invalid Email! ")#line:91:input(Fore.RED + "Invalid Email! ")
                return TermuxBomber ()#line:92:return TermuxBomber()
            elif not O00OOOO0OO0OOOO00 :#line:93:elif not target_email:
                input (Fore .RED +"Type Something! ")#line:94:input(Fore.RED + "Type Something! ")
                return TermuxBomber ()#line:95:return TermuxBomber()
            try :#line:96:try:
                O0O0OO00OO0OOOO0O =int (input (Fore .RESET +"Text Amount: "))#line:97:text_amount = int(input(Fore.RESET + "Text Amount: "))
                if not O0O0OO00OO0OOOO0O :#line:98:if not text_amount:
                    input (Fore .RED +"Type Something! ")#line:99:input(Fore.RED + "Type Something! ")
                    return TermuxBomber ()#line:100:return TermuxBomber()
            except ValueError :#line:101:except ValueError:
                input (Fore .RED +"Only Numbers! ")#line:102:input(Fore.RED + "Only Numbers! ")
                return TermuxBomber ()#line:103:return TermuxBomber()
            OOOOO00O00O0OOOO0 =input (Fore .RESET +"Message: ")#line:105:msg = input(Fore.RESET + "Message: ")
            if not OOOOO00O00O0OOOO0 :#line:106:if not msg:
                input (Fore .RED +"Type Something! ")#line:107:input(Fore.RED + "Type Something! ")
                return TermuxBomber ()#line:108:return TermuxBomber()
            try :#line:109:try:
                O0O00O0000O0OO0OO =smtplib .SMTP (OO00O0OOO00O0O00O ,O0O0OO0OOO000OOOO )#line:111:server = smtplib.SMTP(email_provider, email_port)
                O0O00O0000O0OO0OO .starttls ()#line:112:server.starttls()
                O0O00O0000O0OO0OO .login (OO0O0OO0O0O000O0O ,O00OO0OOOO0OO000O )#line:113:server.login(email_address, password)
            except :#line:114:except:
                input (Fore .RED +"""
Email Not Connected! """)#line:116:Email Not Connected! """)
                return TermuxBomber ()#line:117:return TermuxBomber()
            for _O00OOOO0O000OOO00 in range (0 ,O0O0OO00OO0OOOO0O ):#line:120:for _ in range(0,text_amount):
                O0O00O0000O0OO0OO .sendmail (OO0O0OO0O0O000O0O ,O00OOOO0OO0OOOO00 ,OOOOO00O00O0OOOO0 )#line:121:server.sendmail(email_address,target_email,msg)
                print (Fore .LIGHTYELLOW_EX +f"""
Message {OOOOO00O00O0OOOO0} Sent!""")#line:123:Message {msg} Sent!""")
                time .sleep (1 )#line:124:time.sleep(1)
            O0O00O0000O0OO0OO .quit ()#line:125:server.quit()
            input (Fore .GREEN +"{} Texts Were Sent. Hope You Had a Good Time ;)".format (O0O0OO00OO0OOOO0O ))#line:126:input(Fore.GREEN + "{} Texts Were Sent. Hope You Had a Good Time ;)".format(text_amount))
            return TermuxBomber ()#line:127:return TermuxBomber()
        else :#line:128:else:
            input (Fore .RED +"Invalid Choice! ")#line:129:input(Fore.RED + "Invalid Choice! ")
            return TermuxBomber ()#line:130:return TermuxBomber()
def WindowsBomber ():#line:135:def WindowsBomber():
    os .system ("cls")#line:136:os.system("cls")
    print (Fore .LIGHTBLUE_EX +"""███████╗███╗   ███╗ █████╗ ██╗██╗         ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██║██║         ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║██║         ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║         ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

                                    - Created By VynNetwork
            
          
                        1. Send Email               2. Add Credentials
                                    
                        3. Remove Credentials       4. View Credentials
          

""")#line:152:""")
    if not os .path .exists ('credentials.txt'):#line:154:if not os.path.exists('credentials.txt'):
        with open ('credentials.txt','w')as O0OO00O00000O00O0 :#line:156:with open('credentials.txt', 'w') as file:
            O0OOO00O0OO00O0O0 =""#line:157:saved_email = ""
            OO000O0000OO0OOOO =""#line:158:saved_password = ""
        O0OO00O00000O00O0 .close ()#line:159:file.close()
    else :#line:160:else:
        with open ('credentials.txt','r')as O0OO00O00000O00O0 :#line:162:with open('credentials.txt', 'r') as file:
            O0OOO00O0OO00O0O0 =O0OO00O00000O00O0 .readline ().strip ()#line:163:saved_email = file.readline().strip()
            OO000O0000OO0OOOO =O0OO00O00000O00O0 .readline ().strip ()#line:164:saved_password = file.readline().strip()
        O0OO00O00000O00O0 .close ()#line:165:file.close()
    O000O0OO00O000OOO ='smtp.gmail.com'#line:168:email_provider = 'smtp.gmail.com'
    O0OOO00O0OO0OO00O =O0OOO00O0OO00O0O0 #line:169:email_address = saved_email
    OO0O0OOO00O0O00O0 =587 #line:170:email_port = 587
    O0O000O0000O0OOO0 =OO000O0000OO0OOOO #line:171:password = saved_password
    OO0OO0OOOOOO0OO00 =input (Fore .RESET +"Your Choice: ")#line:173:choice = input(Fore.RESET + "Your Choice: ")
    if OO0OO0OOOOOO0OO00 =="2":#line:175:if choice == "2":
        O0OOOO0O0O00OO000 =input (Fore .RESET +"Your Email: ")#line:176:em = input(Fore.RESET + "Your Email: ")
        O000OO0O0O000000O =input (Fore .RESET +"Your App Password: ")#line:177:pw = input(Fore.RESET + "Your App Password: ")
        if not "@"in O0OOOO0O0O00OO000 :#line:178:if not "@" in em:
            input (Fore .RED +"Invalid Email! ")#line:179:input(Fore.RED + "Invalid Email! ")
            return WindowsBomber ()#line:180:return WindowsBomber()
        elif not O0OOOO0O0O00OO000 :#line:181:elif not em:
            input (Fore .RED +"Type Something! ")#line:182:input(Fore.RED + "Type Something! ")
            return WindowsBomber ()#line:183:return WindowsBomber()
        elif not O000OO0O0O000000O :#line:184:elif not pw:
            input (Fore .RED +"Type Something! ")#line:185:input(Fore.RED + "Type Something! ")
            return WindowsBomber ()#line:186:return WindowsBomber()
        else :#line:187:else:
            with open ("credentials.txt","w")as O0OO00O00000O00O0 :#line:188:with open("credentials.txt","w") as file:
                O0OO00O00000O00O0 .write (O0OOOO0O0O00OO000 +"\n")#line:189:file.write(em + "\n")
                O0OO00O00000O00O0 .write (O000OO0O0O000000O +"\n")#line:190:file.write(pw + "\n")
                O0OO00O00000O00O0 .close ()#line:191:file.close()
                input (Fore .GREEN +"""
Credentials Saved Successfully! """)#line:193:Credentials Saved Successfully! """)
                return WindowsBomber ()#line:194:return WindowsBomber()
    elif OO0OO0OOOOOO0OO00 =="3":#line:196:elif choice == "3":
        with open ("credentials.txt","w")as O0OO00O00000O00O0 :#line:197:with open("credentials.txt","w") as file:
            O0OO00O00000O00O0 .write ("")#line:198:file.write("")
        O0OO00O00000O00O0 .close ()#line:199:file.close()
        input (Fore .GREEN +"""
Credentials Removed Successfully! """)#line:201:Credentials Removed Successfully! """)
        return WindowsBomber ()#line:202:return WindowsBomber()
    elif OO0OO0OOOOOO0OO00 =="4":#line:203:elif choice == "4":
        with open ('credentials.txt','r')as O0OO00O00000O00O0 :#line:205:with open('credentials.txt', 'r') as file:
            O0OOO00O0OO00O0O0 =O0OO00O00000O00O0 .readline ().strip ()#line:206:saved_email = file.readline().strip()
            OO000O0000OO0OOOO =O0OO00O00000O00O0 .readline ().strip ()#line:207:saved_password = file.readline().strip()
        print (Fore .GREEN +f"Saved Email: {O0OOO00O0OO00O0O0}")#line:208:print(Fore.GREEN + f"Saved Email: {saved_email}")
        print (Fore .GREEN +f"Saved App Password: {OO000O0000OO0OOOO}")#line:209:print(Fore.GREEN + f"Saved App Password: {saved_password}")
        input ()#line:210:input()
        return WindowsBomber ()#line:211:return WindowsBomber()
    elif OO0OO0OOOOOO0OO00 =="1":#line:212:elif choice == "1":
        O0OO0O0OOO000O0OO =input (Fore .RESET +"Target Email: ")#line:213:target_email = input(Fore.RESET + "Target Email: ")
        if "@"not in O0OO0O0OOO000O0OO :#line:215:if "@" not in target_email:
            input (Fore .RED +"Invalid Email! ")#line:216:input(Fore.RED + "Invalid Email! ")
            return WindowsBomber ()#line:217:return WindowsBomber()
        elif not O0OO0O0OOO000O0OO :#line:218:elif not target_email:
            input (Fore .RED +"Type Something! ")#line:219:input(Fore.RED + "Type Something! ")
            return WindowsBomber ()#line:220:return WindowsBomber()
        try :#line:221:try:
            O00OOO0OO000000OO =int (input (Fore .RESET +"Text Amount: "))#line:222:text_amount = int(input(Fore.RESET + "Text Amount: "))
            if not O00OOO0OO000000OO :#line:223:if not text_amount:
                input (Fore .RED +"Type Something! ")#line:224:input(Fore.RED + "Type Something! ")
                return WindowsBomber ()#line:225:return WindowsBomber()
        except ValueError :#line:226:except ValueError:
            input (Fore .RED +"Only Numbers! ")#line:227:input(Fore.RED + "Only Numbers! ")
            return WindowsBomber ()#line:228:return WindowsBomber()
        OOO0000OO0O0OO0OO =input (Fore .RESET +"Message: ")#line:230:msg = input(Fore.RESET + "Message: ")
        if not OOO0000OO0O0OO0OO :#line:231:if not msg:
            input (Fore .RED +"Type Something! ")#line:232:input(Fore.RED + "Type Something! ")
            return WindowsBomber ()#line:233:return WindowsBomber()
        try :#line:234:try:
            OOO0O0OO0O000OOOO =smtplib .SMTP (O000O0OO00O000OOO ,OO0O0OOO00O0O00O0 )#line:236:server = smtplib.SMTP(email_provider, email_port)
            OOO0O0OO0O000OOOO .starttls ()#line:237:server.starttls()
            OOO0O0OO0O000OOOO .login (O0OOO00O0OO0OO00O ,O0O000O0000O0OOO0 )#line:238:server.login(email_address, password)
        except :#line:239:except:
            input (Fore .RED +"""
Email Not Connected! """)#line:241:Email Not Connected! """)
            return WindowsBomber ()#line:242:return WindowsBomber()
        for _OO000O0OOOOO00O00 in range (0 ,O00OOO0OO000000OO ):#line:245:for _ in range(0,text_amount):
            OOO0O0OO0O000OOOO .sendmail (O0OOO00O0OO0OO00O ,O0OO0O0OOO000O0OO ,OOO0000OO0O0OO0OO )#line:246:server.sendmail(email_address,target_email,msg)
            print (Fore .LIGHTYELLOW_EX +f"""
Message {OOO0000OO0O0OO0OO} Sent!""")#line:248:Message {msg} Sent!""")
            time .sleep (1 )#line:249:time.sleep(1)
        OOO0O0OO0O000OOOO .quit ()#line:250:server.quit()
        input (Fore .GREEN +"{} Texts Were Sent. Hope You Had a Good Time ;)".format (O00OOO0OO000000OO ))#line:251:input(Fore.GREEN + "{} Texts Were Sent. Hope You Had a Good Time ;)".format(text_amount))
        return WindowsBomber ()#line:252:return WindowsBomber()
    else :#line:254:else:
        input (Fore .RED +"Invalid Choice! ")#line:255:input(Fore.RED + "Invalid Choice! ")
        return WindowsBomber ()#line:256:return WindowsBomber()
class Bella :#line:259:class Bella:
    @staticmethod #line:260:@staticmethod
    def main ():#line:267:def main():
        OOO0O0O000O0OO00O =Bella .detect_environment ()#line:268:environment = Bella.detect_environment()
        if OOO0O0O000O0OO00O =="Termux":#line:270:if environment == "Termux":
            TermuxBomber ()#line:271:TermuxBomber()
        elif OOO0O0O000O0OO00O =="Windows":#line:272:elif environment == "Windows":
            WindowsBomber ()#line:273:WindowsBomber()
        else :#line:274:else:
            input (Fore .RED +"""Where Did You Launch This File From?
Unfortunately You Can Only Run It On Windows & Termux""")#line:276:Unfortunately You Can Only Run It On Windows & Termux""")
            exit ()#line:277:exit()
    @staticmethod #line:279:@staticmethod
    def detect_environment ():#line:285:def detect_environment():
        if os .name =="posix"and "termux"in os .environ .get ("SHELL","").lower ():#line:286:if os.name == "posix" and "termux" in os.environ.get("SHELL", "").lower():
            return "Termux"#line:287:return "Termux"
        elif os .name =="nt":#line:288:elif os.name == "nt":
            return "Windows"#line:289:return "Windows"
        else :#line:290:else:
            return "Sconosciuto"#line:291:return "Sconosciuto"
if __name__ =="__main__":#line:293:if __name__ == "__main__":
    Bella .main ()#line:294:Bella.main()
