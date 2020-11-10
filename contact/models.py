from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = _('Messages')

    def __str__(self):
        return self.name

    @property
    def notification(self):
        return (f'*Name:* _{self.name}_\n\n'
                f'*Email:* _{self.email}_\n\n'
                f'*Message:* _{self.message}_\n\n'
                f'*Posted at:* _{self.humanized_date}_')

    @property
    def humanized_date(self):
        return self.created_at.strftime("%d-%m-%Y")
