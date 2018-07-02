from django.db import models
from django.contrib.auth.models import Group

class Menu(models.Model):
    path    = models.CharField("目录名或文件名",max_length=100, default='/', help_text="目录名或文件名")
    icon    = models.CharField("图标名", max_length=32, null=True, help_text="图标名")
    title   = models.CharField("路由显示名", max_length=255, null=False, help_text="路由显示名")
    show    = models.BooleanField("该路由是否显示", default=False, help_text="该路由是否显示")
    parent  = models.ForeignKey("self", null=True, verbose_name="上级菜单", help_text="上级菜单")
    groups  = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name="menu_set",
        related_query_name="menu",
        help_text="所属组",
    )

    class Meta:
        ordering = ["title"]
        db_table = "view_menu"

    def __str__(self):
        return "{} {}".format(self.title, self.path)