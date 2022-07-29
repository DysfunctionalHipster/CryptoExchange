from django.db import models
from user.models import User

# Create your models here.
class Wire(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    withdrawal = models.BooleanField(default=False)

    def save(self, *args, **kwarg):
        user = User.objects.get(id=self.owner.id)
        wire = self.amount
        if self.withdrawal == True and user.balance >= self.amount:
            user.balance -= wire
        elif self.withdrawal == False:
            user.balance += wire
        else:
            raise ValueError('Insufficient Funds to make Wire transfer')
        user.save()
        super(Wire, self).save(*args, **kwarg)