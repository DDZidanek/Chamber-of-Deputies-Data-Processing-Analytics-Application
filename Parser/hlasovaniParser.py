import csv
import sqlite3
from InputValidation import *

class HlasovaniParser:
    
    def __init__(self):
        pass
    def hlhlasovaniParser(self,path):
        try:
            connection = sqlite3.connect('/home/dd/BP_MLC0044/pspApp/db.sqlite3')
            print("Connection succesfull!")
            
            cursor = connection.cursor()

            with open(path,'r',encoding='windows-1250') as infile:
                
                reader = csv.reader(infile, delimiter="|")
                
                data_list = []
                
                for row in reader:
                    
                    row.pop()

                    id_hlasovani,id_organ,schuze,cislo,bod,datum,cas,pro,proti,zdrzel,nehlasoval,prihlaseno,kvorum,druh_hlasovani,vysledek,nazev_dlouhy,nazev_kratky = row
                    
                    if len(row) != 17:
                        print(f"Invalid row length: {row}")
                        continue
                    
                    if is_valid_int(id_hlasovani) == False:
                        print(f"Id is not valid: {id_hlasovani}")
                        continue                
                    
                    if is_valid_date(datum):
                        datum = date_format(datum)
                    
                    data_list.append([id_hlasovani,is_valid_int(id_organ),is_valid_int(schuze),is_valid_int(cislo),is_valid_int(bod),datum,is_valid_datetime_Hour_to_Minute(cas),is_valid_int(pro),is_valid_int(proti),is_valid_int(zdrzel),is_valid_int(nehlasoval),is_valid_int(prihlaseno),is_valid_int(kvorum),is_valid_char(druh_hlasovani),is_valid_char(vysledek),is_valid_char(nazev_dlouhy),is_valid_char(nazev_kratky)])    
                try:
                    insert_query = "INSERT INTO hl_hlasovani (id_hlasovani,id_organ,schuze,cislo,bod,datum,cas,pro,proti,zdrzel,nehlasoval,prihlaseno,kvorum,druh_hlasovani,vysledek,nazev_dlouhy,nazev_kratky) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                    cursor.executemany(insert_query,data_list)
                    connection.commit()
                    
                    print("Query executed successfully")
                        
                except sqlite3.Error as error:
                    
                    connection.rollback()
                    print("Error occurred:", error)
                    
        except sqlite3.Error as error:
            
            print("Connection unsuccesfull!", error)
        finally:
             
            if connection:
                connection.close()
                print("Connection successfully ended\n")
    def hlhlasovaniDelete(self):
        try:
            connection = sqlite3.connect('/home/dd/BP_MLC0044/pspApp/db.sqlite3')
            print("Connection succesfull!")
            
            cursor = connection.cursor()

            try:
                cursor.execute("DELETE FROM hl_hlasovani")
                cursor.execute("DELETE FROM hl_poslanec")
                cursor.execute("DELETE FROM omluvy")
                cursor.execute("DELETE FROM hl_check")
                cursor.execute("DELETE FROM hl_zposlanec")
                cursor.execute("DELETE FROM hl_vazby")
                cursor.execute("DELETE FROM zmatecne")
                connection.commit()    
                print("Deleting hlasovani executed successfully")
                        
            except sqlite3.Error as error:
                    connection.rollback()
                    print("Error occurred:", error)
                    
        except sqlite3.Error as error:
            
            print("Connection unsuccesfull!", error)
        finally:
             
            if connection:
                connection.close()
                print("Connection successfully ended\n")
                
    def hlPoslanecParser(self,path):
        try:
            connection = sqlite3.connect('/home/dd/BP_MLC0044/pspApp/db.sqlite3')
            print("Connection succesfull!")
            
            cursor = connection.cursor()

            with open(path,'r',encoding='windows-1250') as infile:
                
                reader = csv.reader(infile, delimiter="|")
                
                data_list = []
                
                for row in reader:
                    
                    row.pop()

                    id_poslanec,id_hlasovani,vysledek = row
                    
                    if len(row) != 3:
                        print(f"Invalid row length: {row}")
                        continue
                    
                    if is_valid_int(id_poslanec) == False:
                        print(f"Id is not valid: {id_poslanec}")
                        continue                
                    
                    data_list.append([id_poslanec,is_valid_int(id_hlasovani),is_valid_char(vysledek)])    
                try:
                    insert_query = "INSERT INTO hl_poslanec (id_poslanec,id_hlasovani,vysledek) VALUES(?, ?, ?)"
                    cursor.executemany(insert_query,data_list)
                    connection.commit()
                    
                    print("Query executed successfully")
                        
                except sqlite3.Error as error:
                    
                    connection.rollback()
                    print("Error occurred:", error)
                    
        except sqlite3.Error as error:
            
            print("Connection unsuccesfull!", error)
        finally:
             
            if connection:
                connection.close()
                print("Connection successfully ended\n")
    def omluvyParser(self,path):
        try:
            connection = sqlite3.connect('/home/dd/BP_MLC0044/pspApp/db.sqlite3')
            print("Connection succesfull!")
            
            cursor = connection.cursor()

            with open(path,'r',encoding='windows-1250') as infile:
                
                reader = csv.reader(infile, delimiter="|")
                
                data_list = []
                
                for row in reader:
                    
                    row.pop()

                    id_organ,id_poslanec,den,od,do = row
                    
                    if len(row) != 5:
                        print(f"Invalid row length: {row}")
                        continue
                    
                    if is_valid_int(id_organ) == False:
                        print(f"Id is not valid: {id_organ}")
                        continue
                    
                    if is_valid_date(den):
                        den = date_format(den)                  
                    
                    data_list.append([id_organ,is_valid_int(id_poslanec),den,is_valid_datetime_Hour_to_Minute(od),is_valid_datetime_Hour_to_Minute(do)])    
                try:
                    insert_query = "INSERT INTO omluvy (id_organ,id_poslanec,den,od,do) VALUES(?, ?, ?, ?, ?)"
                    cursor.executemany(insert_query,data_list)
                    connection.commit()
                    
                    print("Query executed successfully")
                        
                except sqlite3.Error as error:
                    
                    connection.rollback()
                    print("Error occurred:", error)
                    
        except sqlite3.Error as error:
            
            print("Connection unsuccesfull!", error)
        finally:
             
            if connection:
                connection.close()
                print("Connection successfully ended\n")
                
    def hlCheckParser(self,path):
        try:
            connection = sqlite3.connect('/home/dd/BP_MLC0044/pspApp/db.sqlite3')
            print("Connection succesfull!")
            
            cursor = connection.cursor()

            with open(path,'r',encoding='windows-1250') as infile:
                
                reader = csv.reader(infile, delimiter="|")
                
                data_list = []
                
                for row in reader:
                    
                    row.pop()

                    id_hlasovani,turn,mode,id_h2,id_h3 = row
                    
                    if len(row) != 5:
                        print(f"Invalid row length: {row}")
                        continue
                    
                    if is_valid_int(id_hlasovani) == False:
                        print(f"Id is not valid: {id_hlasovani}")
                        continue
                    data_list.append([id_hlasovani,is_valid_int(turn),is_valid_int(mode),is_valid_int(id_h2),is_valid_int(id_h3)])    
                try:
                    insert_query = "INSERT INTO hl_check (id_hlasovani,turn,mode,id_h2,id_h3) VALUES(?, ?, ?, ?, ?)"
                    cursor.executemany(insert_query,data_list)
                    connection.commit()
                    
                    print("Query executed successfully")
                    try:
                        update_query = """
                        UPDATE hl_check
                        SET id_h3 = NULL, id_h2 = NULL
                        WHERE (id_h3 IS NOT NULL AND id_h3 NOT IN (SELECT id_hlasovani FROM hl_hlasovani))
                        OR (id_h2 IS NOT NULL AND id_h2 NOT IN (SELECT id_hlasovani FROM hl_hlasovani))
                        """
                        cursor.execute(update_query)
                        connection.commit()
                        print("Invalid foreign keys reset successfully")
                    except sqlite3.Error as error:
                        connection.rollback()
                        print("Error occurred while resetting invalid foreign keys:", error)
                    try:
                        delete_query = """
                        DELETE FROM hl_check
                        WHERE id_hlasovani IS NOT NULL AND id_hlasovani NOT IN (SELECT id_hlasovani FROM hl_hlasovani)
                        """
                        cursor.execute(delete_query)
                        connection.commit()
                        print("Rows with invalid foreign keys deleted successfully")
                    except sqlite3.Error as error:
                        connection.rollback()
                        print("Error occurred while deleting rows with invalid foreign keys:", error)

                except sqlite3.Error as error:
                    
                    connection.rollback()
                    print("Error occurred:", error)
                    
        except sqlite3.Error as error:
            
            print("Connection unsuccesfull!", error)
        finally:
             
            if connection:
                connection.close()
                print("Connection successfully ended\n")
    def hlzPoslanecParser(self,path):
        try:
            connection = sqlite3.connect('/home/dd/BP_MLC0044/pspApp/db.sqlite3')
            print("Connection succesfull!")
            
            cursor = connection.cursor()

            with open(path,'r',encoding='windows-1250') as infile:
                
                reader = csv.reader(infile, delimiter="|")
                
                data_list = []
                
                for row in reader:
                    
                    row.pop()

                    id_hlasovani,id_osoba,mode = row
                    
                    if len(row) != 3:
                        print(f"Invalid row length: {row}")
                        continue
                    
                    if is_valid_int(id_hlasovani) == False:
                        print(f"Id is not valid: {id_hlasovani}")
                        continue
                    data_list.append([id_hlasovani,is_valid_int(id_osoba),is_valid_int(mode)])    
                try:
                    insert_query = "INSERT INTO hl_zposlanec (id_hlasovani,id_osoba,mode) VALUES(?, ?, ?)"
                    cursor.executemany(insert_query,data_list)
                    connection.commit()
                    
                    print("Query executed successfully")
                    try:
                        update_query = """
                            DELETE FROM hl_zposlanec
                            WHERE id_hlasovani IS NOT NULL AND id_hlasovani NOT IN (SELECT id_hlasovani FROM hl_hlasovani)
                            """
                        cursor.execute(update_query)
                        connection.commit()
                        print("Not valid row deleted!")
                        
                    except sqlite3.Error as error:
                        connection.rollback()
                        print("Unable to fix foreign keys!",error)
                
                except sqlite3.Error as error:
                    
                    connection.rollback()
                    print("Error occurred:", error)
                    
        except sqlite3.Error as error:
            
            print("Connection unsuccesfull!", error)
        finally:
             
            if connection:
                connection.close()
                print("Connection successfully ended\n")
    def hlVazbyParser(self,path):
        try:
            connection = sqlite3.connect('/home/dd/BP_MLC0044/pspApp/db.sqlite3')
            print("Connection succesfull!")
            
            cursor = connection.cursor()

            with open(path,'r',encoding='windows-1250') as infile:
                
                reader = csv.reader(infile, delimiter="|")
                
                data_list = []
                
                for row in reader:
                    
                    row.pop()

                    id_hlasovani,turn,typ = row
                    
                    if len(row) != 3:
                        print(f"Invalid row length: {row}")
                        continue
                    
                    if is_valid_int(id_hlasovani) == False:
                        print(f"Id is not valid: {id_hlasovani}")
                        continue
                    data_list.append([id_hlasovani,is_valid_int(turn),is_valid_int(typ)])    
                try:
                    insert_query = "INSERT INTO hl_vazby (id_hlasovani,turn,typ) VALUES(?, ?, ?)"
                    cursor.executemany(insert_query,data_list)
                    connection.commit()
                    
                    print("Query executed successfully")
                        
                except sqlite3.Error as error:
                    
                    connection.rollback()
                    print("Error occurred:", error)
                    
        except sqlite3.Error as error:
            
            print("Connection unsuccesfull!", error)
        finally:
             
            if connection:
                connection.close()
                print("Connection successfully ended\n")
                
    def zmatecneParser(self,path):
        try:
            connection = sqlite3.connect('/home/dd/BP_MLC0044/pspApp/db.sqlite3')
            print("Connection succesfull!")
            
            cursor = connection.cursor()

            with open(path,'r',encoding='windows-1250') as infile:
                
                reader = csv.reader(infile, delimiter="|")
                
                data_list = []
                
                for row in reader:
                    
                    row.pop()

                    id_hlasovani = str(row[0])
                    
                    if len(row) != 1:
                        print(f"Invalid row length: {row}")
                        continue
                    
                    if not is_valid_id(id_hlasovani): continue
                        
                    data_list.append((id_hlasovani,))
                
                try:

                    insert_query = "INSERT INTO zmatecne (id_hlasovani) VALUES(?)"
                    cursor.executemany(insert_query,data_list)
                    connection.commit()
                    
                    print("Query executed successfully")
                    
                    try:
                        update_query  = """
                        DELETE FROM zmatecne
                        WHERE id_hlasovani IS NOT NULL AND id_hlasovani NOT IN (SELECT id_hlasovani FROM hl_hlasovani);
                        """
                        cursor.execute(update_query)
                        connection.commit()
                        print("Invalid foreign keys deleted successfully")
                        
                    except sqlite3.Error as error:
                        connection.rollback()
                        print("Unable to check foreign keys!", error)
                        
                except sqlite3.Error as error:
                    
                    connection.rollback()
                    print("Error occurred:", error)
                    
        except sqlite3.Error as error:
            
            print("Connection unsuccesfull!", error)
            
        finally:
            
            if connection:
                connection.close()
                print("Connection successfully ended\n")