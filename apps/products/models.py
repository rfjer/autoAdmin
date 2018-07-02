from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Product(models.Model):
    service_name    = models.CharField("业务线名称", max_length=32, help_text="业务线名称")
    pid             = models.IntegerField("上级业务线id", db_index=True, help_text="上级业务线id")
    module_letter   = models.CharField("业务线字母简称", max_length=32, help_text="业务线字母简称")
    dev_interface   = models.ManyToManyField(User, verbose_name="开发接口人", related_name="dev_interface", help_text="开发接口人")
    op_interface    = models.ManyToManyField(User, verbose_name="运维接口人", related_name="op_interface", help_text="运维接口人")

    def __str__(self):
        return self.service_name

    class Meta:
        db_table = 'resources_product'
        permissions = (
            ("view_product", "can view products"),
        )
        ordering = ["id"]
