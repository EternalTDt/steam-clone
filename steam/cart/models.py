# from django.db import models
# from django.contrib.auth.models import User

# class Cart(models.Model):
#     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
#     count = models.PositiveIntegerField(default=0, null=True, blank=True)
#     total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
#     updated = models.DateTimeField(auto_now_add=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return f"User: {self.user} has {self.count} items in their cart. Their total is ${self.total}"

#     class Meta:
#         db_table = "Cart"
#         verbose_name = "Корзина"
#         verbose_name_plural = "Корзины"

#     objects = models.Manager()