
# Create your models here.
from django.db import models

from river.models.fields.state import StateField

class MyModel(models.Model):
    my_state_field = StateField()



# class NewModel(Workflow):
    
#     company =  models.ForeignKey(
#         Company,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="count_id")


#     class Meta:
#         unique_together = [("company",)]
