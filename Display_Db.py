import sqlite3
from colorama import Fore, Back

try:
    # Database selection
    db_slct = input(Fore.YELLOW + "🟧 Enter db (ex: sql.db): " + Fore.RESET)
    tb_slct = input(Fore.YELLOW + "🟧 Enter table name : " + Fore.RESET)
    # Connect(create a new file)
    conn = sqlite3.connect(db_slct)
    curs = conn.cursor()
    # Display Data
    data = curs.execute("SELECT * FROM " + tb_slct)
    for row in data:
        print(row)
except FileNotFoundError as file_not_found_error:
    print(Back.RED + f"\n🐞 File error: {file_not_found_error}" + Back.RESET)
except sqlite3.Error as error_caught:
    print(Back.RED + f"🐞 SQLite error: {error_caught}" + Back.RESET)
finally:
    #Close Connection
    curs.close()
    conn.close()