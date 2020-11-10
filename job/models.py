from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    job = models.CharField(max_length=100)
    resume = models.FileField(upload_to='./uploads/resumes/',
                              max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Job applications')

    @property
    def humanized_date(self):
        return self.created_at.strftime("%d-%m-%Y")

    @property
    def notification(self):
        return (f'*Name:* _{self.name}_\n\n'
                f'*Email:* _{self.email}_\n\n'
                f'*Job role:* _{self.job}_\n\n'
                f'*Posted at:* _{self.humanized_date}_')
