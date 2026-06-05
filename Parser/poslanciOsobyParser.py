import csv
import sqlite3
from InputValidation import *


class PoslanciAosoby:

    def __init__(self):
        pass

    def typOrganuParser(self, path):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection succesfull!")

            cursor = connection.cursor()

            with open(path, "r", encoding="windows-1250") as infile:

                reader = csv.reader(infile, delimiter="|")

                osoby_list = []

                for row in reader:

                    row.pop()

                    (
                        id_typ_org,
                        organ_id_organ,
                        nazev_typ_org_cz,
                        nazev_typ_org_en,
                        id_typ_organu,
                        priorita,
                    ) = row

                    if len(row) != 6:
                        print(f"Invalid row length: {row}")
                        continue

                    if not is_valid_id(id_typ_org):
                        continue

                    osoby_list.append(
                        [
                            id_typ_org,
                            is_valid_int(organ_id_organ),
                            is_valid_int(id_typ_organu),
                            is_valid_char(nazev_typ_org_cz),
                            is_valid_char(nazev_typ_org_en),
                            is_valid_int(priorita),
                        ]
                    )

                try:
                    cursor.execute("DELETE FROM typ_organu")
                    connection.commit()
                    insert_query = "INSERT INTO typ_organu (id_typ_org, organ_id_organ, id_typ_organu,nazev_typ_org_cz,nazev_typ_org_en, priorita) VALUES(?,?,?,?,?,?)"
                    cursor.executemany(insert_query, osoby_list)
                    connection.commit()

                    try:
                        update_query = """
                        UPDATE typ_organu
                        SET organ_id_organ = NULL
                        WHERE organ_id_organ  IS NOT NULL AND organ_id_organ NOT IN (SELECT id_typ_org FROM typ_organu);
                        """
                        cursor.execute(update_query)
                        connection.commit()
                        print("Invalid foreign keys reset successfully")
                    except Exception as error:
                        connection.rollback()
                        print(
                            "Error occurred while resetting invalid foreign keys:",
                            error,
                        )

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

    def osobyParser(self, path):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection succesfull!")

            cursor = connection.cursor()

            with open(path, "r", encoding="windows-1250") as infile:

                reader = csv.reader(infile, delimiter="|")

                osoby_list = []

                for row in reader:

                    row.pop()

                    (
                        id_osoba,
                        pred,
                        prijmeni,
                        jmeno,
                        za,
                        narozeni,
                        pohlavi,
                        zmena,
                        umrti,
                    ) = row

                    if len(row) != 9:
                        print(f"Invalid row length: {row}")
                        continue

                    if not is_valid_id(id_osoba):
                        continue

                    if za == "" or za == " ":
                        za = None

                    if is_valid_date(narozeni) is False:
                        narozeni = "1900-01-01"
                    else:
                        narozeni = date_format(narozeni)

                    if pohlavi != "M":
                        pohlavi = "Ž"

                    if is_valid_date(zmena) is False:
                        zmena = None
                    else:
                        zmena = date_format(zmena)

                    if is_valid_date(umrti) is False:
                        umrti = None
                    else:
                        umrti = date_format(umrti)

                    osoby_list.append(
                        [
                            id_osoba,
                            is_valid_char(pred),
                            is_valid_char(jmeno),
                            is_valid_char(prijmeni),
                            is_valid_char(za),
                            narozeni,
                            pohlavi,
                            zmena,
                            umrti,
                        ]
                    )

                try:
                    cursor.execute("DELETE FROM osoby")
                    connection.commit()
                    insert_query = "INSERT INTO osoby (id_osoba,pred,jmeno,prijmeni,za,narozeni,pohlavi,zmena,umrti) VALUES(?,?,?,?,?,?,?,?,?)"
                    cursor.executemany(insert_query, osoby_list)
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

    def typFunkceParser(self, path):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection succesfull!")

            cursor = connection.cursor()

            with open(path, "r", encoding="windows-1250") as infile:

                reader = csv.reader(infile, delimiter="|")

                osoby_list = []

                for row in reader:

                    row.pop()

                    (
                        id_typ_funkce,
                        id_typ_org,
                        typ_funkce_cz,
                        typ_funkce_en,
                        priorita,
                        typ_funkce_obecny,
                    ) = row

                    if len(row) != 6:
                        print(f"Invalid row length: {row}")
                        continue

                    if (not id_typ_funkce.isdigit()) or (not id_typ_funkce):
                        print(f"Invalid id_typ_funkce: {id_typ_funkce}")
                        continue

                    if (not id_typ_org.isdigit()) or (not id_typ_org):
                        id_typ_org = None

                    if typ_funkce_cz == "" or typ_funkce_cz == " ":
                        typ_funkce_cz = None

                    if typ_funkce_en == "" or typ_funkce_en == " ":
                        typ_funkce_en = None

                    if not typ_funkce_obecny.isdigit() or (not typ_funkce_obecny):
                        typ_funkce_obecny = None
                    else:
                        if typ_funkce_obecny not in ["1", "2", "3"]:
                            typ_funkce_obecny = None

                    if (not priorita.isdigit()) or (not priorita):
                        priorita = None

                    osoby_list.append(
                        [
                            id_typ_funkce,
                            id_typ_org,
                            typ_funkce_cz,
                            typ_funkce_en,
                            priorita,
                            typ_funkce_obecny,
                        ]
                    )

                try:
                    cursor.execute("DELETE FROM typ_funkce")
                    connection.commit()
                    insert_query = "INSERT INTO typ_funkce (id_typ_funkce, id_typ_org, typ_funkce_cz,typ_funkce_en, priorita, typ_funkce_obecny) VALUES(?,?,?,?,?,?)"
                    cursor.executemany(insert_query, osoby_list)
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

    def funkceParser(self, path):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection succesfull!")

            cursor = connection.cursor()

            with open(path, "r", encoding="windows-1250") as infile:

                reader = csv.reader(infile, delimiter="|")

                osoby_list = []

                for row in reader:

                    row.pop()

                    id_funkce, id_organ, id_typ_funkce, nazev_funkce_cz, priorita = row

                    if len(row) != 5:
                        print(f"Invalid row length: {row}")
                        continue

                    if (not id_funkce.isdigit()) or (not id_funkce):
                        print(f"Invalid id_typ_funkce: {id_funkce}")
                        continue

                    if (not id_organ.isdigit()) or (not id_organ):
                        id_organ = None

                    if (not id_typ_funkce.isdigit()) or (not id_typ_funkce):
                        id_typ_funkce = None

                    if nazev_funkce_cz == "" or nazev_funkce_cz == " ":
                        nazev_funkce_cz = None

                    if not priorita.isdigit() or (not priorita):
                        priorita = None

                    osoby_list.append(
                        [id_funkce, id_organ, id_typ_funkce, nazev_funkce_cz, priorita]
                    )

                try:
                    cursor.execute("DELETE FROM funkce")
                    connection.commit()
                    insert_query = "INSERT INTO funkce (id_funkce, id_organ, id_typ_funkce,nazev_funkce_cz, priorita) VALUES(?,?,?,?,?)"
                    cursor.executemany(insert_query, osoby_list)
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

    def organyParser(self, path):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection succesfull!")

            cursor = connection.cursor()

            with open(path, "r", encoding="windows-1250") as infile:

                reader = csv.reader(infile, delimiter="|")

                osoby_list = []

                for row in reader:

                    row.pop()

                    [
                        id_organ,
                        organ_id_organ,
                        id_typ_organu,
                        zkratka,
                        nazev_organu_cz,
                        nazev_organu_en,
                        od_organ,
                        do_organ,
                        priorita,
                        cl_organ_base,
                    ] = row

                    if len(row) != 10:
                        print(f"Invalid row length: {row}")
                        continue

                    if not id_organ.isdigit() and not id_organ:
                        print(f"Invalid id_organ: {id_organ}")
                        continue

                    if not organ_id_organ.isdigit() and not organ_id_organ:
                        organ_id_organ = None

                    if not id_typ_organu.isdigit() and not id_typ_organu:
                        id_typ_organu = None

                    if zkratka == "" or zkratka == " ":
                        zkratka = None

                    if nazev_organu_cz == "" or nazev_organu_cz == " ":
                        nazev_organu_cz = None

                    if is_valid_date(od_organ) is False:
                        od_organ = None
                    else:
                        od_organ = date_format(od_organ)

                    if is_valid_date(do_organ) is False:
                        do_organ = None
                    else:
                        do_organ = date_format(do_organ)

                    if not priorita.isdigit() or (not priorita):
                        priorita = None

                    if cl_organ_base not in ["1", "0"]:
                        cl_organ_base = None

                    osoby_list.append(
                        [
                            id_organ,
                            organ_id_organ,
                            id_typ_organu,
                            zkratka,
                            nazev_organu_cz,
                            nazev_organu_en,
                            od_organ,
                            do_organ,
                            priorita,
                            cl_organ_base,
                        ]
                    )

                try:
                    cursor.execute("DELETE FROM organy")
                    connection.commit()
                    insert_query = "INSERT INTO organy (id_organ,organ_id_organ,id_typ_organu,zkratka,nazev_organu_cz,nazev_organu_en,od_organ,do_organ,priorita,cl_organ_base) VALUES(?,?,?,?,?,?,?,?,?,?)"
                    cursor.executemany(insert_query, osoby_list)
                    connection.commit()

                    print("Query executed successfully")

                    try:
                        update_query = """
                        UPDATE organy
                        SET organ_id_organ = NULL
                        WHERE organ_id_organ IS NOT NULL AND organ_id_organ NOT IN (SELECT id_organ FROM organy)
                        """
                        cursor.execute(update_query)
                        connection.commit()
                        print("Invalid foreign keys reset successfully")
                    except sqlite3.Error as error:
                        connection.rollback()
                        print(
                            "Error occurred while resetting invalid foreign keys:",
                            error,
                        )

                except sqlite3.Error as error:

                    connection.rollback()
                    print("Error occurred:", error)

        except sqlite3.Error as error:

            print("Connection unsuccesfull!", error)
        finally:

            if connection:
                connection.close()
                print("Connection successfully ended\n")

    def zarazeniParser(self, path):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection succesfull!")

            cursor = connection.cursor()

            with open(path, "r", encoding="windows-1250") as infile:

                reader = csv.reader(infile, delimiter="|")

                osoby_list_funkce = []
                osoby_list_organy = []

                for row in reader:

                    row.pop()

                    [
                        id_osoba,
                        id_of,
                        cl_funkce,
                        od_o,
                        do_o,
                        od_f,
                        do_f,
                    ] = row

                    if len(row) != 7:
                        print(f"Invalid row length: {row}")
                        continue

                    if not id_osoba.isdigit() and not id_osoba:
                        print(f"Invalid id_osoba: {id_osoba}")
                        continue

                    if not id_of.isdigit() and not id_of:
                        id_of = None

                    if not cl_funkce.isdigit() and not cl_funkce:
                        cl_funkce = None

                    if is_valid_datetime(od_o):
                        od_o = datetime_format_Y_H(od_o)
                    else:
                        od_o = None

                    if is_valid_datetime(do_o):
                        do_o = datetime_format_Y_H(do_o)
                    else:
                        do_o = None

                    if is_valid_date(od_f) is False:
                        od_f = None
                    else:
                        od_f = date_format(od_f)

                    if is_valid_date(do_f) is False:
                        do_f = None
                    else:
                        do_f = date_format(do_f)

                    if int(cl_funkce) == 1:
                        osoby_list_funkce.append(
                            [id_osoba, id_of, cl_funkce, od_o, do_o, od_f, do_f]
                        )
                    if int(cl_funkce) == 0:
                        osoby_list_organy.append(
                            [id_osoba, id_of, cl_funkce, od_o, do_o, od_f, do_f]
                        )

                try:
                    cursor.execute("DELETE FROM zarazeni")
                    connection.commit()
                    insert_query_funkce = "INSERT INTO zarazeni (id_osoba,id_funkce,cl_funkce,od_o,do_o,od_f,do_f) VALUES(?,?,?,?,?,?,?)"
                    insert_query_organy = "INSERT INTO zarazeni (id_osoba,id_organ,cl_funkce,od_o,do_o,od_f,do_f) VALUES(?,?,?,?,?,?,?)"
                    cursor.executemany(insert_query_funkce, osoby_list_funkce)
                    cursor.executemany(insert_query_organy, osoby_list_organy)
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

    def poslanecParser(self, path):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection succesfull!")

            cursor = connection.cursor()

            with open(path, "r", encoding="windows-1250") as infile:

                reader = csv.reader(infile, delimiter="|")

                osoby_list = []

                for row in reader:

                    row.pop()

                    [
                        id_poslanec,
                        id_osoba,
                        id_kraj,
                        id_kandidatka,
                        id_obdobi,
                        web,
                        ulice,
                        obec,
                        psc,
                        email,
                        telefon,
                        fax,
                        psp_telefon,
                        facebook,
                        foto,
                    ] = row

                    if len(row) != 15:
                        print(f"Invalid row length: {row}")
                        continue

                    if is_valid_int(id_poslanec) == False:
                        print(f"Id is not valid: {id_poslanec}")
                        continue
                    if is_valid_int(id_osoba) == False:
                        id_osoba = None
                    if is_valid_int(id_kraj) == False:
                        id_kraj = None
                    if is_valid_int(id_kandidatka):
                        id_kandidatka = int(id_kandidatka)
                    else:
                        id_kandidatka = None
                    if is_valid_int(id_obdobi) == False:
                        id_obdobi = None

                    web = is_valid_char(web)
                    ulice = is_valid_char(ulice)
                    obec = is_valid_char(obec)
                    psc = is_valid_char(psc)
                    email = is_valid_char(email)
                    telefon = is_valid_char(telefon)
                    fax = is_valid_char(fax)
                    psp_telefon = is_valid_char(psp_telefon)
                    facebook = is_valid_char(facebook)

                    if is_valid_int(foto) == False:
                        foto = None

                    osoby_list.append(
                        [
                            id_poslanec,
                            id_osoba,
                            id_kraj,
                            id_kandidatka,
                            id_obdobi,
                            web,
                            ulice,
                            obec,
                            psc,
                            email,
                            telefon,
                            fax,
                            psp_telefon,
                            facebook,
                            foto,
                        ]
                    )

                try:
                    cursor.execute("DELETE FROM poslanec")
                    connection.commit()
                    insert_query = "INSERT INTO poslanec (id_poslanec,id_osoba,id_kraj,id_kandidatka,id_obdobi,web,ulice,obec,psc,email,telefon,fax,psp_telefon,facebook,foto) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                    cursor.executemany(insert_query, osoby_list)
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

    def pkgpsParser(self, path):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection succesfull!")

            cursor = connection.cursor()

            with open(path, "r", encoding="windows-1250") as infile:

                reader = csv.reader(infile, delimiter="|")

                osoby_list = []

                for row in reader:

                    row.pop()

                    [id_poslanec, adresa, sirka, delka] = row

                    if len(row) != 4:
                        print(f"Invalid row length: {row}")
                        continue

                    if is_valid_int(id_poslanec) == False:
                        print(f"Id is not valid: {id_poslanec}")
                        continue
                    adresa = is_valid_char(adresa)
                    sirka = is_valid_char(sirka)
                    delka = is_valid_char(delka)
                    osoby_list.append([id_poslanec, adresa, sirka, delka])

                try:
                    cursor.execute("DELETE FROM pkgps")
                    connection.commit()
                    insert_query = "INSERT INTO pkgps (id_poslanec,adresa,sirka,delka) VALUES(?, ?, ?, ?)"
                    cursor.executemany(insert_query, osoby_list)
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

    def osobaExtraParser(self, path):
        try:
            connection = sqlite3.connect("/home/dd/BP_MLC0044/pspApp/db.sqlite3")
            print("Connection succesfull!")

            cursor = connection.cursor()

            with open(path, "r", encoding="windows-1250") as infile:

                reader = csv.reader(infile, delimiter="|")

                osoby_list = []

                for row in reader:

                    row.pop()

                    [id_osoba, id_org, typ, obvod, strana, id_external] = row

                    if len(row) != 6:
                        print(f"Invalid row length: {row}")
                        continue

                    if is_valid_int(id_osoba) == False:
                        print(f"Id is not valid: {id_osoba}")
                        continue
                    id_org = is_valid_int(id_org)
                    typ = is_valid_int(typ)
                    obvod = is_valid_int(obvod)
                    strana = is_valid_int(strana)
                    id_external = is_valid_int(id_external)
                    osoby_list.append(
                        [id_osoba, id_org, typ, obvod, strana, id_external]
                    )

                try:
                    cursor.execute("DELETE FROM osoba_extra")
                    connection.commit()
                    insert_query = "INSERT INTO osoba_extra (id_osoba,id_org,typ,obvod,strana,id_external) VALUES(?, ?, ?, ?, ? ,?)"
                    cursor.executemany(insert_query, osoby_list)
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
