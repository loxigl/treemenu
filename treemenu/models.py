from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='childs', on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=50)

    def __str__(self):
        return self.title
