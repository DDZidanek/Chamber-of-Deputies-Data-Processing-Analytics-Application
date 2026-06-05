from .models.models_PaO import *
from .models.models_hl import *
from django.db.models.functions import ExtractYear
from django.db.models import F, Q, Count
import json
from datetime import date
from collections import Counter
from .forms import VolebniObdobiForm
import numpy as np

def getVolebniObdobi(request):
    form = VolebniObdobiForm(request.GET)
    if form.is_valid():
        return form.cleaned_data['id_obdobi']
    return 173

def getNazvyVolebnichObdobi():
    volebni_obdobi = (
        Poslanec.objects.annotate(
            od_o=ExtractYear("id_obdobi__od_organ"),
            do_o=ExtractYear("id_obdobi__do_organ"),
        )
        .values("id_obdobi", "id_obdobi__zkratka", "od_o", "do_o")
        .distinct()
    )
    return volebni_obdobi


def getVek(id_poslanec):

    narozeniQuery = (
        Poslanec.objects.filter(id_poslanec=id_poslanec)
        .annotate(narozeni=F("id_osoba__narozeni"), umrti=F("id_osoba__umrti"))
        .values("narozeni", "umrti")
    )

    if narozeniQuery:
        vysledek = list(narozeniQuery)[0]

        narozeni = vysledek["narozeni"]
        umrti = vysledek["umrti"]

        if narozeni == date(1900,1,1):
            return None
        
        dnes = date.today() if umrti is None else umrti

        vek = (
            dnes.year
            - narozeni.year
            - ((dnes.month, dnes.day) < (narozeni.month, narozeni.day))
        )

        return vek

    return None


def getAdresa(id_poslanec):
    adresa = Pkgps.objects.filter(id_poslanec=id_poslanec).values_list(
        "adresa", flat=True
    )

    prvni_adresa = " ".join((str(list(adresa)[0])).split("; ")) if adresa else None

    return prvni_adresa


def getPohlavi(id_osoba):
    pohlavi_query = Osoby.objects.filter(id_osoba=id_osoba).values_list(
        "pohlavi", flat="true"
    )

    pohlavi = "Žena"

    if len(pohlavi_query) != 0:
        if str(list(pohlavi_query)[0]) == "M":
            pohlavi = "Muž"

    return pohlavi


# query pro hlasovani pro poslande v danem volebnim obdobi
def zpracuj_hlasovani(poslanec_id):
    hlasovaniPoslanci = (
        hl_poslanec.objects.filter(id_poslanec=poslanec_id)
        .values("vysledek")
        .annotate(pocet=Count("vysledek"))
    )

    vysledky = {
        "ano": 0,
        "ne": 0,
        "zdrzel": 0,
        "neprihlasen": 0,
        "pred_slibem": 0,
    }

    for item in hlasovaniPoslanci:
        vysledek = item.get("vysledek")
        pocet = int(item.get("pocet", 0))

        if vysledek == "A":
            vysledky["ano"] += pocet
        elif vysledek in ["B", "N"]:
            vysledky["ne"] += pocet
        elif vysledek in ["C", "K", "F"]:
            vysledky["zdrzel"] += pocet
        elif vysledek == "@":
            vysledky["neprihlasen"] += pocet

    return vysledky


def getZarazeniOrgany(id_osoba, typZarazeni, od_roku, do_roku):

    conditions = Q(zarazeni__od_o__year__gte=od_roku)

    if do_roku is not None:
        conditions &= Q(zarazeni__od_o__year__lt=do_roku)

    podvybory_poslanci = (
        Organy.objects.filter(
            conditions,
            zarazeni__id_osoba=id_osoba,
            id_typ_organu__nazev_typ_org_cz=typZarazeni,
        )
        .values("nazev_organu_cz","zkratka")
        .distinct()
    )

    podvybory = {"pocet": 0, "nazev": "", "zkratka" : ""}

    podvybory["pocet"] = len(podvybory_poslanci)

    podvybory["zkratka"] = "; ".join(
        [prvek["zkratka"] for prvek in (list(podvybory_poslanci))]
    )
    podvybory["nazev"] = "; ".join(
        [prvek["nazev_organu_cz"] for prvek in (list(podvybory_poslanci))]
    )


    return podvybory


def getZarazeniFunkce(id_osoba, od_roku, do_roku):

    conditions = Q(od_o__year__gte=od_roku)

    if do_roku is not None:
        conditions &= Q(od_o__year__lt=do_roku)

    funkce_poslanci = (
        Zarazeni.objects.filter(conditions, id_osoba=id_osoba, cl_funkce=1)
        .annotate(
            funkce=F("id_funkce__id_typ_funkce__typ_funkce_cz"),
            forgan=F("id_funkce__id_organ__nazev_organu_cz"),
        )
        .values("funkce", "forgan").distinct()
    )

    funkce = {"pocet": 0, "nazev": ""}

    funkce["pocet"] = len(funkce_poslanci)

    funkce["nazev"] = "; ".join(
        [prvek["funkce"] + " - " + prvek["forgan"] for prvek in funkce_poslanci]
    )
    return funkce


def dataPoslanci(selected_obdobi):

    # query pro vyber tabulek poslanec,osoba,pkgps

    if selected_obdobi:
        if selected_obdobi == -1:
            data = Poslanec.objects.all()
        else:
            data = Poslanec.objects.filter(id_obdobi=selected_obdobi).all()
    else:
        data = Poslanec.objects.all()

    return data


def getKraj(id_kraj):

    return Organy.objects.get(id_organ=id_kraj).nazev_organu_cz


def getVolebniStrana(is_strana):
    # query pro stranu v které je poslanec

    try:
        if is_strana:
            strana = Organy.objects.get(id_organ=is_strana).zkratka
        else:
            strana = None
    except Organy.DoesNotExist:
        strana = is_strana

    return strana


def getPoslanecFoto(id_osoba, rok):

    # mapovani fotek
    photoUrl = f"https://psp.cz/eknih/cdrom/{rok}ps/eknih/{rok}ps/poslanci/small/i{id_osoba}.jpg"

    if rok == 1992:
        photoUrl = (
            f"https://upload.wikimedia.org/wikipedia/commons/a/ac/Default_pfp.jpg"
        )

    return photoUrl


def getObdobiOrganu(id_org):

    zaznam = Organy.objects.filter(id_organ=id_org).annotate(
        od_roku=ExtractYear("od_organ"),
        do_roku=ExtractYear("do_organ")
    ).values("od_roku", "do_roku").first()
    
    od_roku = zaznam.get('od_roku') if zaznam else None
    do_roku = zaznam.get('do_roku') if zaznam else None

    return od_roku, do_roku

def getPoslanecVsechny():

    poslanci = Poslanec.objects.values("id_osoba_id").annotate(pocetObsazeni = Count("id_osoba_id")).order_by('pocetObsazeni')

    return list(poslanci)

def createPoslanciDict(poslanec):

    od_roku, do_roku = getObdobiOrganu(poslanec.id_obdobi_id)
    funkce = getZarazeniFunkce(poslanec.id_osoba_id, od_roku, do_roku)
    vybory = getZarazeniOrgany(poslanec.id_osoba_id, "Výbor", od_roku, do_roku)
    podvybory = getZarazeniOrgany(poslanec.id_osoba_id, "Podvýbor", od_roku, do_roku)
    vysledek_hlasovani = zpracuj_hlasovani(poslanec.id_poslanec)

    return {
        "foto": getPoslanecFoto(poslanec.id_osoba_id, od_roku),
        "id_poslanec": poslanec.id_poslanec,
        "id_osoba": poslanec.id_osoba_id,
        "pred": poslanec.id_osoba.pred,
        "jmeno": poslanec.id_osoba.jmeno,
        "prijmeni": poslanec.id_osoba.prijmeni,
        "za": poslanec.id_osoba.za,
        "kraj": getKraj(poslanec.id_kraj),
        "strana": getVolebniStrana(poslanec.id_kandidatka_id),
        "pohlavi": getPohlavi(poslanec.id_osoba_id),
        "vek": getVek(poslanec.id_poslanec),
        "funkce": funkce["nazev"],
        "pocet_funkci": funkce["pocet"],
        "vybory": vybory["nazev"],
        "vybory_kratky": vybory["zkratka"],
        "pocet_vyboru": vybory["pocet"],
        "podvybory": podvybory["nazev"],
        "pocet_podvyboru": podvybory["pocet"],
        "hlasovani_ano": vysledek_hlasovani.get("ano"),
        "hlasovani_ne": vysledek_hlasovani.get("ne"),
        "hlasovani_zdrzel": vysledek_hlasovani.get("zdrzel"),
        "hlasovani_neprihlasen": vysledek_hlasovani.get("neprihlasen"),
        "adresa": getAdresa(poslanec.id_poslanec),
    }

