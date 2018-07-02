from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    vendor_name     = models.CharField("厂商名称", max_length=32, db_index=True, help_text="厂商名称")
    tel             = models.CharField("联系电话", null=True, max_length=20, help_text="联系电话")
    mail            = models.EmailField("email", null=True, blank=True, help_text="联系邮箱")
    remark          = models.CharField("备注", max_length=300, null=True, blank=True, help_text="备注")

    def __str__(self):
        return self.vendor_name

    class Meta:
        db_table = 'resources_manufacturer'
        permissions = (
            ("view_manufacturer", "cat view manufacturer"),
        )
        ordering = ["id"]

class ProductModel(models.Model):
    model_name      = models.CharField("型号名称", max_length=32, help_text="型号名称")
    vendor          = models.ForeignKey(Manufacturer, verbose_name="所属制造商", help_text="所属制造商")

    def __str__(self):
        return self.model_name

    class Meta:
        db_table = 'resources_productmodel'
        permissions = (
            ("view_productmodel", "cat view productmodel"),
        )
        ordering = ["id"]