####Django Import CSV into Model demo

from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.translation import gettext as _

class UserDataModel(models.Model):
    # user_id = models.IntegerField(_("User ID"))
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    gender = models.CharField(_("Gender"), max_length=6, choices=GENDER, default='')
    age = models.SmallIntegerField(_("Age"),validators=[MaxValueValidator(100),MinValueValidator(18)])
    estimated_salary = models.SmallIntegerField(_("EstimatedSalary"))
    purchased = models.BooleanField(_("Purchased"))

