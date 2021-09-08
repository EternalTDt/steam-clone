from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField


class Company(models.Model):
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("Ссылка", max_length=130, unique=True, blank=True, null=True)
    year_of_foundation = models.PositiveSmallIntegerField("Год основания", default=2010)
    foundation_country = CountryField()
    ceo = models.CharField("Генеральный директор", max_length=40)
    employees_num = models.IntegerField("Количество сотрудников", default=0)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"



class Product(models.Model):
    name = models.CharField("Название", max_length=150, blank=True)
    slug = models.SlugField("Ссылка", max_length=130, unique=True, blank=True, null=True)
    description = RichTextField()
    release_date = models.DateField("Дата выхода", auto_now_add=True)
    price = models.DecimalField("Стоимость", max_digits=10, decimal_places=2, blank=True)
    title_image = models.ImageField("Главная картинка", default="default.jpg", upload_to="title_images", blank=True)
    company = models.ManyToManyField(Company, related_name="company", verbose_name="Компания")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"