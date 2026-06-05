from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class TypOrganu(models.Model):
    id_typ_org = models.IntegerField(primary_key=True)
    organ_id_organ = models.ForeignKey('self', on_delete=models.CASCADE, db_column='organ_id_organ', related_name='nadrazene_organy', null=True)
    id_typ_organu = models.ForeignKey('self', on_delete=models.CASCADE, db_column='id_typ_organu', related_name='podrizene_typy', null=True)
    nazev_typ_org_cz = models.TextField(null=True)
    nazev_typ_org_en = models.TextField(null=True)
    priorita = models.IntegerField(null=True)

    class Meta:
        db_table = 'typ_organu'
        verbose_name = "Typ orgánu"
        verbose_name_plural = "Typy orgánů"

class TypFunkce(models.Model):
    id_typ_funkce = models.AutoField(primary_key=True)
    id_typ_org = models.ForeignKey('TypOrganu', on_delete=models.CASCADE,db_column = 'id_typ_org')
    typ_funkce_cz = models.TextField(null = True)
    typ_funkce_en = models.TextField(null = True)
    priorita = models.IntegerField(null = True)
    typ_funkce_obecny = models.IntegerField(null = True)

    class Meta:
        db_table = 'typ_funkce'
        verbose_name = "Typ funkce"
        verbose_name_plural = "Typy funkcí"
        
class Funkce(models.Model):
    id_funkce = models.AutoField(primary_key=True)
    id_organ = models.ForeignKey('Organy', on_delete=models.CASCADE,db_column = "id_organ",null = True)
    id_typ_funkce = models.ForeignKey('TypFunkce', on_delete=models.CASCADE,db_column = "id_typ_funkce")
    nazev_funkce_cz = models.TextField()
    priorita = models.IntegerField()

    class Meta:
        db_table = 'funkce'
        verbose_name = "Funkce"
        verbose_name_plural = "Funkce"
        
class Organy(models.Model):
    id_organ = models.IntegerField(primary_key=True)
    organ_id_organ = models.ForeignKey('self', on_delete=models.CASCADE, null = True,db_column = 'organ_id_organ')
    id_typ_organu = models.ForeignKey('TypOrganu', on_delete=models.CASCADE,db_column = 'id_typ_organu')
    zkratka = models.TextField(null = True)
    nazev_organu_cz = models.TextField(null = True)
    nazev_organu_en = models.TextField(null = True)
    od_organ = models.DateField(null = True)
    do_organ = models.DateField(null = True)
    priorita = models.IntegerField(null = True)
    cl_organ_base = models.IntegerField(null = True)

    class Meta:
        db_table = 'organy'
        verbose_name = "Orgán"
        verbose_name_plural = "Orgány"

class Osoby(models.Model):
    id_osoba = models.AutoField(primary_key=True)
    pred = models.TextField(null=True)
    jmeno = models.TextField(null=True)
    prijmeni = models.TextField(null=True)
    za = models.TextField(null=True)
    narozeni = models.DateField(null=True)
    pohlavi = models.CharField(max_length=1, null=True)
    zmena = models.DateField(null=True)
    umrti = models.DateField(null=True)

    class Meta:
        db_table = 'osoby'
        verbose_name = "Osoba"
        verbose_name_plural = "Osoby"
        
class Zarazeni(models.Model):
    id_osoba = models.ForeignKey('Osoby', on_delete=models.CASCADE,db_column = 'id_osoba')
    id_organ = models.ForeignKey('Organy', on_delete=models.CASCADE, db_column='id_organ', null=True, blank=True)
    id_funkce = models.ForeignKey('Funkce', on_delete=models.CASCADE, db_column='id_funkce', null=True, blank=True)
    cl_funkce = models.IntegerField()
    od_o = models.DateTimeField(null=True)
    do_o = models.DateTimeField(null=True)
    od_f = models.DateField(null=True)
    do_f = models.DateField(null=True)

    class Meta:
        db_table = 'zarazeni'
        verbose_name = "Zařazení"
        verbose_name_plural = "Zařazení"
        
class Poslanec(models.Model):
    id_poslanec = models.AutoField(primary_key=True)
    id_osoba = models.ForeignKey('Osoby', on_delete=models.CASCADE,db_column = 'id_osoba')
    id_kraj = models.IntegerField()
    id_kandidatka = models.ForeignKey('Organy',on_delete=models.CASCADE,db_column = 'id_kandidatka',null = True)
    id_obdobi = models.ForeignKey('Organy', related_name='poslanci_obdobi', on_delete=models.CASCADE,db_column = 'id_obdobi',null = True)
    web = models.TextField(null = True)
    ulice = models.TextField(null = True)
    obec = models.TextField(null = True)
    psc = models.TextField(null = True)
    email = models.TextField(null = True)
    telefon = models.TextField(null = True)
    fax = models.TextField(null = True)
    psp_telefon = models.TextField(null = True)
    facebook = models.TextField(null = True)
    foto = models.IntegerField(null = True)

    class Meta:
        db_table = 'poslanec'
        verbose_name = "Poslanec"
        verbose_name_plural = "Poslanci"
        
class Pkgps(models.Model):
    id_poslanec = models.OneToOneField('Poslanec', on_delete=models.CASCADE, db_column = 'id_poslanec',primary_key = True)
    adresa = models.TextField()
    sirka = models.CharField(max_length=20)
    delka = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'pkgps'
        verbose_name = "GPS pozice"
        verbose_name_plural = "GPS pozice"
  
class OsobaExtra(models.Model):
    id_osoba = models.ForeignKey('Osoby', on_delete=models.CASCADE,db_column = 'id_osoba')
    id_org = models.ForeignKey('Organy', on_delete=models.CASCADE, db_column='id_org')
    typ = models.IntegerField()
    obvod = models.IntegerField()
    strana = models.TextField(null = True)
    id_external = models.IntegerField()

    class Meta:
        db_table = 'osoba_extra'
        verbose_name = "Extra info o osobě"
        verbose_name_plural = "Extra info o osobách"