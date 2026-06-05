from django.db import models

class Schuze(models.Model):
    id_schuze = models.IntegerField(primary_key=True)
    id_org = models.ForeignKey('Organy', on_delete=models.CASCADE,db_column = 'id_organ')
    schuze = models.IntegerField()
    od_schuze = models.DateTimeField()
    do_schuze = models.DateTimeField(null=True, blank=True)
    aktualizace = models.DateTimeField()

    class Meta:
        db_table = 'schuze'
        verbose_name = "Schůze"
        verbose_name_plural = "Schůze"
        
class Schuze_stav(models.Model):
    id_schuze = models.ForeignKey('Schuze', on_delete=models.CASCADE,db_column = 'id_schuze')
    stav = models.IntegerField()
    typ = models.IntegerField()
    text_dt = models.TextField(null=True)
    text_st = models.TextField(null=True)
    tm_line = models.TextField(null=True)
    class Meta:
        db_table = 'schuze_stav'
        verbose_name = "Stav schůze"
        verbose_name_plural = "Stavy schůze"
        
class Bod_stav(models.Model):
    id_bod_stav = models.IntegerField(primary_key=True)
    popis = models.TextField()
    class Meta:
        db_table = 'bod_stav'
        verbose_name = "Stav bodu"
        verbose_name_plural = "Stavy bodu"

class Bod_schuze(models.Model):
    id_bod = models.IntegerField()
    id_schuze = models.ForeignKey('Schuze', on_delete=models.CASCADE, db_column='id_schuze')
    id_tisk = models.IntegerField(null=True, blank=True)
    id_typ = models.ForeignKey('TypProjednavani', on_delete=models.CASCADE, db_column='id_typ',null=True)
    bod = models.IntegerField(null=True)
    uplny_naz = models.CharField(max_length=255,null=True, blank=True)
    uplny_kon = models.CharField(max_length=255, null=True, blank=True)
    poznamka = models.CharField(max_length=255, null=True, blank=True)
    id_bod_stav = models.ForeignKey('Bod_stav', on_delete=models.CASCADE, db_column='id_bod_stav')
    pozvanka = models.IntegerField(null=True)
    rj = models.IntegerField(null=True)
    pozn2 = models.CharField(max_length=255, null=True, blank=True)
    druh_bodu = models.ForeignKey('druh_bodu', on_delete=models.CASCADE, null=True,db_column='id_bodu')
    id_sd = models.IntegerField(null=True, blank=True)
    zkratka = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'bod_schuze'
        verbose_name = "Bod schůze"
        verbose_name_plural = "Body schůze"
        
class druh_bodu(models.Model):
    id_bodu = models.IntegerField(primary_key = True)
    popis = models.TextField()
    class Meta:
        db_table = 'druh_bodu'
        verbose_name = "Druh bodu"
        verbose_name_plural = "Druhy bodu"

class TypProjednavani(models.Model):
    id_typ = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=255)

    class Meta:
        db_table = 'typ_projednavani'
        verbose_name = "Typ projednávání"
        verbose_name_plural = "Typy projednávání"