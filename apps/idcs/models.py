from django.db import models

# Create your models here.


class Idc(models.Model):
    letter          = models.CharField("idc字母简称", max_length=10, unique=True, help_text="idc字母简称")
    name            = models.CharField("idc名称", max_length=30, help_text="idc名称")
    address         = models.CharField("idc具体地址", max_length=255, null=True, blank=True, help_text="idc具体地址")
    tel             = models.CharField("客服电话", max_length=15, null=True, blank=True, help_text="客服电话")
    mail            = models.EmailField("联系人邮箱", max_length=255, null=True, blank=True, help_text="联系人邮箱")
    remark          = models.CharField("备注说明", max_length=255, null=True, blank=True, help_text="备注说明")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'resources_idc'
        permissions = (
            ("view_idc", "cat view idc"),
        )
        ordering = ["id"]