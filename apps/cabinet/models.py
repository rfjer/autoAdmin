from django.db import models
from idcs.models import Idc
# Create your models here.

class Cabinet(models.Model):
    name            = models.CharField("机柜名称", max_length=50, help_text="机柜名称")
    power_supply    = models.IntegerField("电源功率", help_text="电源功率")
    idc             = models.ForeignKey(Idc, verbose_name="所在机房", help_text="所在机房")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'resources_cabinet'
        permissions = (
            ("view_cabinet", "cat view cabinet"),
        )
        ordering = ["id"]