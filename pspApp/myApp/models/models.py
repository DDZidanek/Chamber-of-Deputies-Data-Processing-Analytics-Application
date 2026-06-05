from django.db import models

class TypyProjednavani(models.Model):
    id_typ = models.IntegerField(primary_key=True)
    text = models.TextField()

    class Meta:
        verbose_name = "Typ projednávání"
        verbose_name_plural = "Typy projednávání"
        db_table = "typy_projednavani"

class TypZakon(models.Model):
    id_navrh = models.IntegerField(primary_key=True)
    druh_navrhovatele = models.TextField()

    class Meta:
        verbose_name = "Typ zákona"
        verbose_name_plural = "Typy zákonů"
        db_table = "typ_zakon"
        
    def __str_(self):
        return self.id_navrh

class DruhTisku(models.Model):
    id_druh = models.IntegerField(primary_key=True)
    druh_t = models.TextField()
    nazev_druh = models.TextField(null = True)

    class Meta:
        verbose_name = "Druh tisku"
        verbose_name_plural = "Druhy tisků"
        db_table = "druh_tisku"

class TypStavu(models.Model):
    id_typ = models.IntegerField(primary_key=True)
    popis_stavu = models.TextField()

    class Meta:
        verbose_name = "Typ stavu"
        verbose_name_plural = "Typy stavů"
        db_table = "typ_stavu"

class Stavy(models.Model):
    id_stav = models.IntegerField(primary_key=True)
    id_typ = models.IntegerField()
    id_druh = models.IntegerField()
    popis = models.TextField()
    lhuta = models.IntegerField()
    lhuta_where = models.IntegerField()

    class Meta:
        verbose_name = "Stav"
        verbose_name_plural = "Stavy"
        db_table = "stavy"

class TypAkce(models.Model):
    id_akce = models.IntegerField(primary_key=True)
    popis_akce = models.TextField()

    class Meta:
        verbose_name = "Typ akce"
        verbose_name_plural = "Typy akcí"
        db_table = "typ_akce"

class Tisky(models.Model):
    id_tisk = models.IntegerField(primary_key=True)
    id_druh = models.IntegerField()
    id_stav = models.IntegerField()
    ct = models.IntegerField()
    cislo_za = models.IntegerField()
    id_navrh = models.IntegerField()
    id_org = models.IntegerField()
    id_org_obd = models.IntegerField()
    id_osoba = models.IntegerField()
    navrhovatel = models.TextField()
    nazev_tisku = models.TextField()
    predlozeno = models.TextField()
    rozeslano = models.TextField()
    dal = models.TextField()
    tech_nos_dat = models.IntegerField()
    uplny_nazev_tisku = models.TextField()
    zm_lhuty = models.IntegerField()
    lhuta = models.IntegerField()
    rj = models.IntegerField()
    t_url = models.TextField()
    is_eu = models.IntegerField()
    roz = models.TextField()
    is_sdv = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        verbose_name = "Tisk"
        verbose_name_plural = "Tisky"
        db_table = "tisky"

class Hist(models.Model):
    id_hist = models.IntegerField(primary_key=True)
    id_tisk = models.IntegerField()
    datum = models.TextField()
    id_hlas = models.IntegerField()
    id_prechod = models.IntegerField()
    id_bod = models.IntegerField()
    schuze = models.IntegerField()
    usnes_ps = models.IntegerField()
    orgv_id_posl = models.IntegerField()
    ps_id_posl = models.IntegerField()
    orgv_p_usn = models.IntegerField()
    zaver_publik = models.TextField()
    zaver_sb_castka = models.IntegerField()
    zaver_sb_cislo = models.IntegerField()
    poznamka = models.TextField()

    class Meta:
        verbose_name = "Historie"
        verbose_name_plural = "Historie"
        db_table = "hist"

class HistVybory(models.Model):
    id_tisku = models.IntegerField(primary_key=True)
    id_organ = models.IntegerField()
    typ = models.IntegerField()
    id_hist = models.IntegerField()
    id_posl = models.IntegerField()
    poradi = models.IntegerField()

    class Meta:
        verbose_name = "Historie výborů"
        verbose_name_plural = "Historie výborů"
        db_table = "hist_vybory"

class Vysledek(models.Model):
    id_vysledek = models.IntegerField(primary_key=True)
    druh_vysledek = models.TextField()

    class Meta:
        verbose_name = "Výsledek"
        verbose_name_plural = "Výsledky"
        db_table = "vysledek"

class TiskyZa(models.Model):
    id_tisk = models.IntegerField(primary_key=True)
    cislo_za = models.IntegerField()
    id_hist = models.IntegerField()
    id_druh = models.IntegerField()
    nazev_za = models.IntegerField()
    uplny_nazev_za = models.TextField()
    rozeslano = models.DateTimeField()
    id_org = models.IntegerField()
    usn_vybor = models.IntegerField()
    id_posl = models.IntegerField()
    t_url = models.TextField()
    id_vysledek = models.IntegerField()
    cislo_za_post = models.IntegerField()
    sort_it = models.IntegerField()
    roz = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        verbose_name = "Tisk následný"
        verbose_name_plural = "Tisky následující"
        db_table = "tisky_za"

class Prekladatel(models.Model):
    id_tisk = models.IntegerField(primary_key=True)
    id_osoba = models.IntegerField()
    poradi = models.IntegerField()
    typ = models.IntegerField()

    class Meta:
        verbose_name = "Překladatel"
        verbose_name_plural = "Překladatelé"
        db_table = "prekladatel"

class NavrhPodpis(models.Model):
    id_tisk = models.IntegerField(primary_key=True)
    id_osoba = models.IntegerField()
    stav = models.IntegerField()
    datum = models.DateField()

    class Meta:
        verbose_name = "Návrh podpisu"
        verbose_name_plural = "Návrhy podpisů"
        db_table = "navrh_podpis"

class Prechody(models.Model):
    id_prechod = models.IntegerField(primary_key=True)
    odkud = models.IntegerField()
    kam = models.IntegerField()
    id_akce = models.IntegerField()

    class Meta:
        verbose_name = "Přechod"
        verbose_name_plural = "Přechody"
        db_table = "prechody"
