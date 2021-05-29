
# Create your models here.
from django.db import models
from django.db.models import CASCADE,SET_NULL
from river.models.fields.state import StateField
from polls.company import Company
class MyModel(models.Model):
    my_state_field = StateField()
    company = models.ForeignKey(Company,related_name='company_id',on_delete=CASCADE,default=1
    )

# class NewModel(Workflow):
    
#     company =  models.ForeignKey(
#         Company,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="count_id")


#     class Meta:
#         unique_together = [("company",)]
