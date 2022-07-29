from django.db import models
from django.utils import timezone
from .crypto_api import get_trade
from user.models import User

# Create your models here.
class Trade(models.Model):

    symbol_options = (
    ("BTC", "Bitcoin"),
    ("ETH", "Ethereum"),
    ("USDT", "Tether"),
    ("ADA", "Cardano"),
    ("SOL", "Solana"),
    ("DOGE", "Dogecoin"),
    ("MATIC", "Polygon"),
    ("USDC", "USD Coin")
)

    class OpenTrades(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(open=True) # ? Shows only open trades
        
    class ClosedTrades(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(open=False)
    
    trader = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    symbol = models.CharField(max_length=10, choices=symbol_options, default='Bitcoin')
    quantity = models.FloatField()
    open_price = models.FloatField(blank=True, null=True)
    close_price = models.FloatField(blank=True, null=True)
    open_date = models.DateField(blank=True, null=True)
    close_date = models.DateField(blank=True, null=True)
    open = models.BooleanField(default=True)

    objects = models.Manager()
    opentrades = OpenTrades()
    closedtrades = ClosedTrades()

    class Meta:
        ordering = ('-open_date', ) # ? Sorts trades by most recent
        
    @property
    def trade_price(self):
        price = get_trade(self.symbol)
        total = self.quantity * price
        return total
    
    def save(self, *args, **kwarg):
        user = User.objects.get(id=self.trader.id)
        
        if self.open == True and user.balance >= self.trade_price:
            self.open_price = self.trade_price
            self.open_date = timezone.now()
            user.balance -= self.trade_price
        elif self.open == False:
            self.close_price = self.trade_price
            self.close_date = timezone.now()
            user.balance += self.trade_price
        else:
            raise ValueError('Insufficient funds to open position')
        user.save()
        super(Trade, self).save(*args, **kwarg)