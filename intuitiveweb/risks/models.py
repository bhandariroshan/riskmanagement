from django.db import models

# Create your models here.
class RiskType(models.Model):
    # First Name and Last Name do not cover name patterns
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    # To add
    # created_by = models.ForeignKey(models.User)

    def __unicode__(self):
        return '%d: %s' % (self.name, self.name)

    def __str__(self):
        return "%s" % (self.name)

class RiskField(models.Model):
    FIELD_CHOICES = (
        ('Text', 'TEXT'),
        ('Number', 'NUMBER'),
        ('Date', 'DATE'),
        ('Enum', 'ENUM'),
    )

    id = models.AutoField(primary_key=True)
    risk_type = models.ForeignKey(RiskType, related_name='riskfields', on_delete=models.CASCADE)
    risk_field_name = models.TextField()
    risk_field_data_type = models.CharField(max_length=10,choices=FIELD_CHOICES)

    def __unicode__(self):
        return str(self.risk_type.name) + '::' + str(self.risk_field_name)

    def __str__(self):
        return str(self.risk_type.name) + '::' + str(self.risk_field_name)

class RiskFieldChoices(models.Model):
    risk_field_id = models.ForeignKey(RiskField)
    choice = models.CharField(max_length=100)

    def __unicode__(self):
        return '%d: %s' % (self.risk_field_id, self.choice)

    def __str__(self):
        return "%s" % (self.choice)

class RiskFieldValue(models.Model):
    id = models.IntegerField(primary_key=True)
    risk_field = models.ForeignKey(RiskField)
    risk_field_value = models.TextField()
