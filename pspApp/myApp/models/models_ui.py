from django.db import models

class Uitypv(models.Model):
    id_ui_stav = models.IntegerField(primary_key=True)
    nazev = models.TextField(null = True)
    priorita = models.IntegerField()
    class Meta:
        verbose_name = "UI Typ"
        verbose_name_plural = "UI Typy"
        db_table = "uitypv"

class TypInterpelace(models.Model):
    id_typ = models.IntegerField(primary_key=True)
    popis = models.TextField()

    class Meta:
        verbose_name = "Typ interpelace"
        verbose_name_plural = "Typ interpelací"
        db_table = 'typ_interpelace'
      
class LosInterpelaci(models.Model):
    id_los = models.IntegerField(primary_key=True)
    datum_los = models.DateField(null=True, blank=True)
    typ_los = models.CharField(max_length=1)
    cas_los = models.DateTimeField(null=True,blank = True)
    id_schuze = models.ForeignKey('Schuze', on_delete=models.CASCADE, db_column='id_schuze')
    id_bod = models.IntegerField()
    #id_bod = models.ForeignKey('Bod_schuze', on_delete=models.CASCADE, db_column='id_bod')
    schuze = models.IntegerField()
    id_org = models.ForeignKey('Organy', on_delete=models.CASCADE, db_column='id_org')

    class Meta:
        verbose_name = "Los interpelací"
        verbose_name_plural = "Losy interpelací"
        db_table = "los_interpelaci"
        
class Poradi(models.Model):
    id_poradi = models.IntegerField(primary_key=True)
    id_losovani = models.ForeignKey('LosInterpelaci', on_delete=models.CASCADE, db_column='id_losovani')
    id_poslanec = models.ForeignKey('Osoby', on_delete=models.CASCADE, db_column='id_poslanec', related_name='poslanec_poradi')
    id_ministr = models.ForeignKey('Osoby', on_delete=models.CASCADE, db_column='id_ministr', related_name='ministr_poradi')
    vec = models.CharField(max_length=255)
    poradi_l = models.IntegerField(null=True)
    priorita = models.IntegerField(null=True)
    vec32 = models.CharField(null=True,max_length=255)

    class Meta:
        verbose_name = "Pořadí"
        verbose_name_plural = "Pořadí"
        db_table = "poradi"

class Uistav(models.Model):
    id_poradi = models.ForeignKey("Poradi",on_delete=models.CASCADE,db_column='id_poradi')
    id_typ = models.ForeignKey("TypInterpelace",on_delete=models.CASCADE,db_column = 'id_typ')
    steno = models.IntegerField(null=True)
    class Meta:
        verbose_name = "UI Stav"
        verbose_name_plural = "UI Stavy"
        db_table = "ui_stav"