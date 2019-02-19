from django.db import models
import uuid
import datetime


def upload_image(instance, filename):
    extension = filename.split(".")[-1]
    return "images/{}/{}{}".format(datetime.datetime.today().year,
                                   datetime.datetime.now().strftime("%Y%m%d%H%M%S")+"_"+
                                   str(uuid.uuid4())+".",extension)


class myModel(models.Model):
    description = models.TextField(verbose_name="Description", max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True)
