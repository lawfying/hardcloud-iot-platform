from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from device.models import Device
from scenario.models import Scenario,Collection,DevLink

class MyProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=20, blank=True)
    mugshot = models.ImageField(upload_to='upload',default = 'upload/none.jpg', blank=True)
    is_developer = models.BooleanField(default=True)
    is_custom_user = models.BooleanField(default=False)

    def __str__(self):  # Python 3: def __str__(self):
        return self.user.username  

@receiver(post_save, sender=User)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        profile, created = MyProfile.objects.get_or_create(user=instance)

class DevHolder(models.Model):
    dev_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    binding_dev = models.ForeignKey(Device,related_name='devholder', on_delete=models.CASCADE)
    bonding_date = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    user_dev_bind = models.CharField(max_length=100, blank=True,unique=True)

    def save(self, *args, **kwargs):
        self.user_dev_bind = str(self.dev_owner)+str(self.binding_dev_id) 
        super(DevHolder, self).save(*args, **kwargs)
        
    def __str__(self):  # Python 3: def __str__(self):
        return self.binding_dev.title  

class ScenarioHolder(models.Model):
    sce_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    binding_sce = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    bonding_date = models.DateTimeField(_(u"Creation date"), auto_now_add=True)
    user_sce_bind = models.CharField(max_length=100, blank=True,unique=True)

    #绑定场景时，自动绑定场景下面所有的设备
    def save(self, *args, **kwargs):
        self.user_sce_bind = str(self.sce_owner_id)+str(self.binding_sce_id) 
        super(ScenarioHolder, self).save(*args, **kwargs)
        query_tmp = Collection.objects.filter(scenario=self.binding_sce)
        for col in query_tmp:
            devtmp = DevLink.objects.filter(collection=col)
            for devtmp_s in devtmp:
                devholder = DevHolder(dev_owner=self.sce_owner,binding_dev=devtmp_s.device)
                devholder.save()
        return
        
    def __str__(self):  # Python 3: def __str__(self):
        return self.binding_sce.title  




#2022-12-27日修改
@receiver(post_save, sender=Device)
def create_own_devbinding(sender, instance=None, created=False, **kwargs):
    if created:
        tmp = DevHolder(dev_owner=instance.owner,binding_dev=instance)
        tmp.save()

@receiver(post_save, sender=Scenario)
def create_own_scebinding(sender, instance=None, created=False, **kwargs):
    if created:
        tmp = ScenarioHolder(sce_owner=instance.owner,binding_sce=instance)
        tmp.save()