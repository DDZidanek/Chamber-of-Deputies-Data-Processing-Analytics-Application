import csv
import sqlite3
from InputValidation import *

class UstniInterpelaceParser:
    def __init__(self):
        pass
    def uitypvParser(self, path):
        try:
            connection = sqlite3.connect('/home/dd/BP_MLC0044/pspApp/db.sqlite3')
            print("Connection successful!")
            
            cursor = connection.cursor()

            with open(path, 'r', encoding='windows-1250') as infile:
                
                reader = csv.reader(infile, delimiter="|")
                
                uitypv_list = []
                
                for row in reader:
                    
                    row.pop()

                    id_ui_stav, nazev, priorita = row
                    
                    if len(row) != 3:
                        print(f"Invalid row length: {row}")
                        continue
                    
                    if not is_valid_id(id_ui_stav): continue
                    
                    uitypv_list.append([
                        is_valid_int(id_ui_stav),
                        is_valid_char(nazev),
                        is_valid_int(priorita)
                    ])
                
                try:
                    cursor.execute("DELETE FROM uitypv")
                    connection.commit()
                    insert_query = "INSERT INTO uitypv (id_ui_stav, nazev, priorita) VALUES(?,?,?)"
                    cursor.executemany(insert_query, uitypv_list)
                    connection.commit()
                    
                    print("Query executed successfully")
                        
                except sqlite3.Error as error:
                    
                    connection.rollback()
                    print("Error occurred:", error)
                    
        except sqlite3.Error as error:
            
            print("Connection unsuccessful!", error)
            
        finally:
            
            if connection:
                connection.close()
                print("Connection successfully ended\n")
    def losInterpelaciParser(self, path):
        try:
            connection = sqlite3.connect('/home/dd/BP_MLC0044/pspApp/db.sqlite3')
            print("Connection successful!")

            cursor = connection.cursor()

            with open(path, 'r', encoding='windows-1250') as infile:

                reader = csv.reader(infile, delimiter="|")

                los_interpelaci_list = []

                for row in reader:

                    row.pop()

                    id_los, datum_los, typ_los, cas_los, id_schuze, id_bod, schuze, id_org = row

                    if len(row) != 8:
                        print(f"Invalid row length: {row}")
                        continue

                    if not is_valid_id(id_los): continue

                    los_interpelaci_list.append([
                        is_valid_int(id_los),
                        date_format(datum_los) if is_valid_date(datum_los) else None,
                        is_valid_char(typ_los),
                        convert_to_sqlite_datetime(cas_los) if is_valid_datetime_fraction(cas_los) else None,
                        is_valid_int(id_schuze),
                        is_valid_int(id_bod),
                        is_valid_int(schuze),
                        is_valid_int(id_org)
                    ])

                try:
                    cursor.execute("DELETE FROM los_interpelaci")
                    connection.commit()
                    insert_query = "INSERT INTO los_interpelaci (id_los, datum_los, typ_los, cas_los, id_schuze, id_bod, schuze, id_org) VALUES(?,?,?,?,?,?,?,?)"
                    cursor.executemany(insert_query, los_interpelaci_list)
                    connection.commit()

                    print("Query executed successfully")

                    try:
                        delete_query = """
                        DELETE FROM los_interpelaci
                        WHERE id_bod IS NOT NULL AND id_bod NOT IN (SELECT id_bodu FROM bod_schuze)
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

            print("Connection unsuccessful!", error)

        finally:

            if connection:
                connection.close()
                print("Connection successfully ended\n")
    def poradiParser(self, path):
        try:
            connection = sqlite3.connect('/home/dd/BP_MLC0044/pspApp/db.sqlite3')
            print("Connection successful!")

            cursor = connection.cursor()

            with open(path, 'r', encoding='windows-1250') as infile:

                reader = csv.reader(infile, delimiter="|")

                poradi_list = []

                for row in reader:

                    row.pop()

                    id_poradi, id_losovani, id_poslanec, id_ministr, vec, poradi_l, priorita, vec32 = row

                    if len(row) != 8:
                        print(f"Invalid row length: {row}")
                        continue

                    if not is_valid_id(id_poradi): continue

                    poradi_list.append([
                        is_valid_int(id_poradi),
                        is_valid_int(id_losovani),
                        is_valid_int(id_poslanec),
                        is_valid_int(id_ministr),
                        is_valid_char(vec),
                        is_valid_int(poradi_l),
                        is_valid_int(priorita),
                        is_valid_char(vec32)
                    ])

                try:
                    cursor.execute("DELETE FROM poradi")
                    connection.commit()
                    insert_query = "INSERT INTO poradi (id_poradi, id_losovani, id_poslanec, id_ministr, vec, poradi_l, priorita, vec32) VALUES(?,?,?,?,?,?,?,?)"
                    cursor.executemany(insert_query, poradi_list)
                    connection.commit()

                    print("Query executed successfully")

                except sqlite3.Error as error:

                    connection.rollback()
                    print("Error occurred:", error)

        except sqlite3.Error as error:

            print("Connection unsuccessful!", error)

        finally:

            if connection:
                connection.close()
                print("Connection successfully ended\n")
    def uiStavParser(self, path):
        try:
            connection = sqlite3.connect('/home/dd/BP_MLC0044/pspApp/db.sqlite3')
            print("Connection successful!")

            cursor = connection.cursor()

            with open(path, 'r', encoding='windows-1250') as infile:

                reader = csv.reader(infile, delimiter="|")

                ui_stav_list = []

                for row in reader:

                    row.pop()

                    id_poradi, id_typ, steno = row

                    if len(row) != 3:
                        print(f"Invalid row length: {row}")
                        continue

                    if not is_valid_id(id_poradi): continue

                    ui_stav_list.append([
                        is_valid_int(id_poradi),
                        is_valid_int(id_typ),
                        is_valid_int(steno)
                    ])

                try:
                    cursor.execute("DELETE FROM ui_stav")
                    connection.commit()
                    insert_query = "INSERT INTO ui_stav (id_poradi, id_typ, steno) VALUES(?,?,?)"
                    cursor.executemany(insert_query, ui_stav_list)
                    connection.commit()

                    print("Query executed successfully")

                except sqlite3.Error as error:

                    connection.rollback()
                    print("Error occurred:", error)

        except sqlite3.Error as error:

            print("Connection unsuccessful!", error)

        finally:

            if connection:
                connection.close()
                print("Connection successfully ended\n")
    def TypInterpelaceParser(self):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection successful!")

            cursor = connection.cursor()
            try:
                cursor.execute("DELETE FROM typ_interpelace ")
                connection.commit()
                insert_query = """INSERT INTO typ_interpelace (id_typ, popis) VALUES
                                    (1, 'Interpelace přednesena, interpelující využil doplňující otázku a interpelovaný na ni odpověděl.'),
                                    (2, 'Interpelace přednesena, interpelovaný neodpověděl na doplňující otázku nebo doplňující otázka nebyla položena.'),
                                    (3, 'Interpelace přednesena, interpelovaný nebyl přítomen a podle JŘ bude interpelovanému odpovězeno písemně do 30 dnů.'),
                                    (4, 'Interpelace nepřednesena, interpelující nepřítomen.'),
                                    (5, 'Interpelace nepřednesena, interpelující vzal interpelaci zpět.'),
                                    (6, 'Interpelace nepřednesena, interpelovaný nebyl přítomen a interpelace propadla.'),
                                    (7, 'Interpelace přednesena, interpelovaný odpoví písemně (např. z důvodů rozsáhlosti odpovědi a podobně; oproti typu 3 byl interpelovaný přítomen nebo byla domluva interpelujícího s interpelovaným o písemné odpovědi).'),
                                    (8, 'Interpelace nepřednesena, nejsou známy důvody nepřednesení.'),
                                    (9, 'Interpelace nepřednesena, interpelující se domluvil s interpelovaným na písemné odpovědi.'),
                                    (10, 'Interpelace nepřednesena, projednávání bodu ústních interpelací bylo ukončeno (na projednávání interpelace nedošlo, neboť uplynula lhůta k projednávání bodu).'),
                                    (11, 'Interpelace nepřednesena, interpelující nebyl přítomen, ale byl omluven.')
                                    """
                cursor.execute(insert_query)
                connection.commit()

                print("Query executed successfully")

            except sqlite3.Error as error:

                connection.rollback()
                print("Error occurred:", error)

        except sqlite3.Error as error:

            print("Connection unsuccessful!", error)

        finally:

            if connection:
                connection.close()
                print("Connection successfully ended\n")