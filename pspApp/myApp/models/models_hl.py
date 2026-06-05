from django.db import models

from django.db import models

class hl_hlasovani(models.Model):
    id_hlasovani = models.IntegerField(primary_key=True)
    id_organ = models.ForeignKey('Organy',on_delete=models.CASCADE,db_column = 'id_organ')
    schuze = models.IntegerField()
    cislo = models.IntegerField()
    bod = models.IntegerField(null=True)
    datum = models.DateField()
    cas = models.TimeField()
    pro = models.IntegerField()
    proti = models.IntegerField()
    zdrzel = models.IntegerField()
    nehlasoval = models.IntegerField(null=True)
    prihlaseno = models.IntegerField()
    kvorum = models.IntegerField()
    druh_hlasovani = models.CharField(max_length=1, choices=[
        ('N', 'Normální'),
        ('R', 'Ruční'),
        ('E', 'Technická závada'),
    ])
    vysledek = models.CharField(max_length=1, choices=[
        ('A', 'Přijato'),
        ('R', 'Zamítnuto'),
        ('X', 'Výsledek neznámý'),
        ('Q', 'Výsledek neznámý u neveřejného hlasování'),
        ('K', 'Nedosaženo kvóra'),
    ])
    nazev_dlouhy = models.TextField(null=True)
    nazev_kratky = models.TextField(null=True)
    class Meta:
        db_table = 'hl_hlasovani'
        verbose_name = "Hlasování"
        verbose_name_plural = "Hlasování"

    
class hl_poslanec(models.Model):
    id_poslanec = models.ForeignKey('Poslanec',on_delete=models.CASCADE,db_column = 'id_poslanec')
    id_hlasovani = models.ForeignKey('hl_hlasovani',on_delete=models.CASCADE,db_column = 'id_hlasovani')
    vysledek = models.TextField()
    class Meta:
        db_table = 'hl_poslanec'
        verbose_name = "Hlasování poslance"
        verbose_name_plural = "Hlasování poslanců"

class omluvy(models.Model):
    id_organ = models.ForeignKey('Organy', on_delete=models.CASCADE, db_column='id_organ')
    id_poslanec = models.ForeignKey('Poslanec', on_delete=models.CASCADE, db_column='id_poslanec')
    den = models.DateField()
    od = models.TimeField(null=True, blank=True)
    do = models.TimeField(null=True, blank=True)
    class Meta:
        db_table = 'omluvy'
        verbose_name = "Omluva"
        verbose_name_plural = "Omluvy"
        
class hl_check(models.Model):
    id_hlasovani = models.ForeignKey('hl_hlasovani', on_delete=models.CASCADE, db_column='id_hlasovani')
    turn = models.IntegerField()
    mode = models.IntegerField()
    id_h2 = models.ForeignKey('hl_hlasovani', on_delete=models.CASCADE, related_name='hlasovani_h2', db_column='id_h2',null=True)
    id_h3 = models.ForeignKey('hl_hlasovani', on_delete=models.CASCADE, related_name='hlasovani_h3', db_column='id_h3',null=True)
    class Meta:
        db_table = 'hl_check'
        verbose_name = "Hlasování kontrola"
        verbose_name_plural = "Hlasování kontroly"
    
class hl_zposlanec(models.Model):
    id_hlasovani = models.ForeignKey('hl_hlasovani', on_delete=models.CASCADE, db_column='id_hlasovani')
    id_osoba = models.ForeignKey('Osoby', on_delete=models.CASCADE, db_column='id_osoba')
    mode = models.IntegerField()
    class Meta:
        db_table = 'hl_zposlanec'
        verbose_name = "Zpochyb. hlas. poslancem"
        verbose_name_plural = "Zpochyb. hlas.poslanci"
        
class hl_vazby(models.Model):
    id_hlasovani = models.ForeignKey('hl_hlasovani', on_delete=models.CASCADE, db_column='id_hlasovani')
    turn = models.IntegerField()
    typ = models.IntegerField()
    class Meta:
        db_table = 'hl_vazby'
        verbose_name = "Hlasování vazby"
        verbose_name_plural = "Hlasování vazby"
        
class zmatecne(models.Model):
    id_hlasovani = models.ForeignKey('hl_hlasovani', on_delete=models.CASCADE, db_column='id_hlasovani')
    class Meta:
        db_table = 'zmatecne'
        verbose_name = "Zmatečné hlasování"
        verbose_name_plural = "Zmatečné hlasování"