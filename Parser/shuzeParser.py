import csv
import sqlite3
from InputValidation import *


class ShuzeParser:
    def __init__(self):
        pass

    def schuzeParser(self, path):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection successful!")

            cursor = connection.cursor()

            with open(path, "r", encoding="windows-1250") as infile:

                reader = csv.reader(infile, delimiter="|")

                for row in reader:

                    row.pop()

                    if len(row) != 7:
                        print(f"Invalid row length: {row}")
                        continue

                    id_schuze, id_org, schuze, od_schuze, do_schuze, aktualizace, pozvanka = row

                    if not is_valid_id(id_schuze):
                        continue

                    cursor.execute("SELECT COUNT(*) FROM schuze WHERE id_schuze = ?", (id_schuze,))
                    if cursor.fetchone()[0] > 0:
                        #print(f"Record with primary key {id_schuze} already exists.")
                        continue

                    schuze_record = [
                        is_valid_int(id_schuze),
                        is_valid_int(id_org),
                        is_valid_int(schuze),
                        datetime_format(od_schuze) if is_valid_datetime_Year_to_Minute(od_schuze) else None,
                        datetime_format(do_schuze) if is_valid_datetime_Year_to_Minute(do_schuze) else None,
                        datetime_format(aktualizace) if is_valid_datetime_Year_to_Minute(aktualizace) else None,
                    ]

                    try:
                        insert_query = "INSERT INTO schuze (id_schuze, id_organ, schuze, od_schuze, do_schuze, aktualizace) VALUES(?,?,?,?,?,?)"
                        cursor.execute(insert_query, schuze_record)
                        connection.commit()

                        print(f"Record with primary key {id_schuze} inserted successfully.")

                    except sqlite3.Error as error:
                        connection.rollback()
                        print("Error occurred while inserting:", error)

        except sqlite3.Error as error:
            print("Connection unsuccessful!", error)

        finally:
            if connection:
                connection.close()
                print("Connection successfully ended\n")


    # def schuzeParser(self, path):
    #     try:
    #         connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
    #         print("Connection successful!")

    #         cursor = connection.cursor()

    #         with open(path, "r", encoding="windows-1250") as infile:

    #             reader = csv.reader(infile, delimiter="|")

    #             schuze_list = []

    #             for row in reader:

    #                 row.pop()

    #                 (
    #                     id_schuze,
    #                     id_org,
    #                     schuze,
    #                     od_schuze,
    #                     do_schuze,
    #                     aktualizace,
    #                     pozvanka,
    #                 ) = row

    #                 if len(row) != 7:
    #                     print(f"Invalid row length: {row}")
    #                     continue

    #                 if not is_valid_id(id_schuze):
    #                     continue

    #                 schuze_list.append(
    #                     [
    #                         is_valid_int(id_schuze),
    #                         is_valid_int(id_org),
    #                         is_valid_int(schuze),
    #                         (
    #                             datetime_format(od_schuze)
    #                             if is_valid_datetime_Year_to_Minute(od_schuze)
    #                             else None
    #                         ),
    #                         (
    #                             datetime_format(do_schuze)
    #                             if is_valid_datetime_Year_to_Minute(do_schuze)
    #                             else None
    #                         ),
    #                         (
    #                             datetime_format(aktualizace)
    #                             if is_valid_datetime_Year_to_Minute(aktualizace)
    #                             else None
    #                         ),
    #                         is_valid_int(pozvanka),
    #                     ]
    #                 )

    #             try:
    #                 cursor.execute("DELETE FROM schuze")
    #                 insert_query = "INSERT INTO schuze (id_schuze, id_org, schuze, od_schuze, do_schuze, aktualizace) VALUES(?,?,?,?,?,?)"
    #                 cursor.executemany(insert_query, schuze_list)
    #                 connection.commit()

    #                 print("Query executed successfully")

    #             except sqlite3.Error as error:

    #                 connection.rollback()
    #                 print("Error occurred:", error)

    #     except sqlite3.Error as error:

    #         print("Connection unsuccessful!", error)

    #     finally:

    #         if connection:
    #             connection.close()
    #             print("Connection successfully ended\n")

    def schuzeStavParser(self, path):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection successful!")

            cursor = connection.cursor()

            with open(path, "r", encoding="windows-1250") as infile:

                reader = csv.reader(infile, delimiter="|")

                schuze_stav_list = []

                for row in reader:

                    row.pop()

                    id_schuze, stav, typ, text_dt, text_st, tm_line = row

                    if len(row) != 6:
                        print(f"Invalid row length: {row}")
                        continue

                    if not is_valid_id(id_schuze):
                        continue

                    schuze_stav_list.append(
                        [
                            is_valid_int(id_schuze),
                            is_valid_int(stav),
                            is_valid_int(typ),
                            is_valid_char(text_dt),
                            is_valid_char(text_st),
                            is_valid_char(tm_line),
                        ]
                    )

                try:
                    cursor.execute("DELETE FROM schuze_stav")
                    connection.commit()
                    insert_query = "INSERT INTO schuze_stav (id_schuze, stav, typ, text_dt, text_st, tm_line) VALUES(?,?,?,?,?,?)"
                    cursor.executemany(insert_query, schuze_stav_list)
                    connection.commit()

                    print("Query executed successfully")
                    
                    try:
                        delete_query = """
                        DELETE FROM schuze_stav
                        WHERE id_schuze IS NOT NULL AND id_schuze NOT IN (SELECT id_schuze FROM schuze)
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

    def bodStavParser(self, path):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection successful!")

            cursor = connection.cursor()

            with open(path, "r", encoding="windows-1250") as infile:

                reader = csv.reader(infile, delimiter="|")

                bod_stav_list = []

                for row in reader:

                    row.pop()

                    id_bod_stav, popis = row

                    if len(row) != 2:
                        print(f"Invalid row length: {row}")
                        continue

                    if not is_valid_id(id_bod_stav):
                        continue

                    bod_stav_list.append(
                        [is_valid_int(id_bod_stav), is_valid_char(popis)]
                    )

                try:
                    cursor.execute("DELETE FROM bod_stav")
                    connection.commit()
                    insert_query = (
                        "INSERT INTO bod_stav (id_bod_stav, popis) VALUES(?,?)"
                    )
                    cursor.executemany(insert_query, bod_stav_list)
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

    def bodSchuzeParser(self, path):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection successful!")

            cursor = connection.cursor()

            with open(path, "r", encoding="windows-1250") as infile:

                reader = csv.reader(infile, delimiter="|")

                bod_schuze_list = []

                for row in reader:

                    row.pop()

                    (
                        id_bod,
                        id_schuze,
                        id_tisk,
                        id_typ,
                        bod,
                        uplny_naz,
                        uplny_kon,
                        poznamka,
                        id_bod_stav,
                        pozvanka,
                        rj,
                        pozn2,
                        druh_bodu,
                        id_sd,
                        zkratka,
                    ) = row

                    if len(row) != 15:
                        print(f"Invalid row length: {row}")
                        continue

                    if not is_valid_id(id_bod):
                        continue

                    bod_schuze_list.append(
                        [
                            is_valid_int(id_bod),
                            is_valid_int(id_schuze),
                            is_valid_int(id_tisk),
                            is_valid_int(id_typ),
                            is_valid_int(bod),
                            is_valid_char(uplny_naz),
                            is_valid_char(uplny_kon),
                            is_valid_char(poznamka),
                            is_valid_int(id_bod_stav),
                            is_valid_int(pozvanka),
                            is_valid_int(rj),
                            is_valid_char(pozn2),
                            is_valid_int(druh_bodu),
                            is_valid_int(id_sd),
                            is_valid_char(zkratka),
                        ]
                    )

                try:
                    cursor.execute("DELETE FROM bod_schuze")
                    connection.commit()
                    insert_query = "INSERT INTO bod_schuze (id_bod, id_schuze, id_tisk, id_typ, bod, uplny_naz, uplny_kon, poznamka, id_bod_stav, pozvanka, rj, pozn2, id_bodu, id_sd, zkratka) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                    cursor.executemany(insert_query, bod_schuze_list)
                    connection.commit()

                    print("Query executed successfully")

                    try:
                        update_query = """
                        UPDATE bod_schuze
                        SET id_typ = NULL
                        WHERE id_typ IS NOT NULL AND id_typ NOT IN (SELECT id_typ FROM typ_projednavani)
                        """
                        cursor = connection.cursor()
                        cursor.execute(update_query)
                        connection.commit()
                        print("Invalid foreign keys reset successfully")
                    except sqlite3.Error as error:
                        connection.rollback()
                        print("Error occurred while resetting invalid foreign keys:", error)
                    try:
                        update_query = """
                        UPDATE bod_schuze
                        SET id_bodu = NULL
                        WHERE id_bodu IS NOT NULL AND id_bodu NOT IN (SELECT id_bodu FROM druh_bodu)
                        """
                        cursor.execute(update_query)
                        connection.commit()
                        print("Invalid foreign keys reset successfully")
                    except Exception as error:
                        connection.rollback()
                        print("Error occurred while resetting invalid foreign keys:", error)
                except sqlite3.Error as error:

                    connection.rollback()
                    print("Error occurred:", error)

        except sqlite3.Error as error:

            print("Connection unsuccessful!", error)

        finally:

            if connection:
                connection.close()
                print("Connection successfully ended\n")

    def TypProjednavaniParser(self):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection successful!")

            cursor = connection.cursor()
            try:
                cursor.execute("DELETE FROM typ_projednavani;")
                connection.commit()
                insert_query = """INSERT INTO typ_projednavani (id_typ, text) VALUES
                                    (1, '1. čtení'),
                                    (7, '1. čtení'),
                                    (15, '1. čtení'),
                                    (17, '1. čtení'),
                                    (18, '1. čtení'),
                                    (40, '1. čtení'),
                                    (41, '1. čtení'),
                                    (2, '2. čtení'),
                                    (3, '2. čtení'),
                                    (4, '2. čtení'),
                                    (5, '3. čtení'),
                                    (13, 'vráceno prezidentem'),
                                    (14, 'vráceno Senátem'),
                                    (10, 'zkrácené jednání (stav legislativní nouze)')"""
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

    def DruhBoduParser(self):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection successful!")

            cursor = connection.cursor()
            try:
                cursor.execute("DELETE FROM druh_bodu")
                connection.commit()
                insert_query = """INSERT INTO druh_bodu (id_bodu, popis) VALUES
                                    (1, 'Zákony'),
                                    (2, 'Zákony'),
                                    (3, 'Smlouvy'),
                                    (4, 'Rozpočet'),
                                    (41, 'Záležitosti EU'),
                                    (45, 'Záležitosti EU'),
                                    (46, 'Záležitosti EU'),
                                    (47, 'Záležitosti EU')"""
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
