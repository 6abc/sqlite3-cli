#5_3.sql.py
import sqlite3
from colorama import Fore, Back

try:
    #App Message
    print(Fore.GREEN + "\nWelcome to Python SQLite-CLI\nPlease create .sql script:\n\n" + Fore.RESET)
    print(Fore.BLUE + "Enter Database file name with location\nWindow : C:\\\db\\\sql.db\nLinux  : /home/db/sql.db\n" + Fore.RESET)
    print(Fore.BLUE + "Enter Script file name with location\nWindow : C:\\\scripts\\\command.sql\nLinux  : /home/scripts/command.sql" + Fore.RESET)
    #Database and Script Selection
    db_slct = input(Fore.YELLOW + "\n🟧 Enter DB : " + Fore.RESET)
    tb_slct = input(Fore.YELLOW + "\n🟧 Enter script file : " + Fore.RESET)
    #Connect(create a new file)
    conn = sqlite3.connect(db_slct)
    curs = conn.cursor()
    #Load SQL Script from file
    with open(tb_slct) as file:
        sql_script = file.read()
    #Execute script
    curs.executescript(sql_script)
    print(Fore.GREEN + "\n🚀 Script Executed" + Fore.RESET)
except FileNotFoundError as file_not_found_error:
    print(Back.RED + f"\n🐞 File error: {file_not_found_error}" + Back.RESET)
except sqlite3.Error as error_caught:
    print(Back.RED + f"\n🐞 SQLite error: {error_caught}" + Back.RESET)
finally:
    #Close Connection
    curs.close()
    conn.close()