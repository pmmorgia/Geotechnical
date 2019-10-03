from django.db import models

class BlendSession(models.Model):
    session_id = models.CharField("Session ID", max_length = 200,blank=True,null=True)
    blend_date = models.DateTimeField('Blending Date',null=True)
    
    def __str__(self):
        return f'{self.session_id}'
    
class Stockpile(models.Model):
    pile_number = models.CharField("Stock Pile ID", max_length = 200,blank=True,null=True)
    
    #CHoice
    RockCodeChoice = (('200','Limonite'),('100','Saprolite'),('0','Waste')) 
    rockdescription = models.CharField("Description",choices=RockCodeChoice, max_length = 200,blank=False,null=True)
    blendsession = models.ForeignKey(BlendSession, on_delete=models.CASCADE)
    
    kWMT = models.CharField("Weight (kWMT)", max_length = 200,blank=False,null=False)
    ni_grade = models.FloatField("Nickel Grade (%)",default=0,blank=False,null=False)
    fe_grade = models.FloatField("Iron Grade (%)",default=0,blank=False,null=False)
    
    def __str__(self):
        return f'{self.pile_number}'
    
    
# Create your models here.
