
from django.db import models

# Create your models here.

class cc_type(models.Model):
    ##类型

    id = models.IntegerField
    type_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.id
    def __str__(self):
        return 'id=%s ,type=%s' % (self.id,self.type_name)
    def __getid__(self):
        return 'id=%s' % self.id