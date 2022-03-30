from django.db import models
from django.urls import reverse
from datetime import date


# Автор
class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="Введите имя автора", verbose_name="Имя автора")
    last_name = models.CharField(max_length=100, help_text="Введите фамилию автора", verbose_name="Фамилия автора")
    patronymic = models.CharField(max_length=100, help_text="Введите отчество автора", verbose_name="Отчество автора",
                                  null=True, blank=True)

    def __str__(self):
        return '{0} {1} {2}'.format(self.last_name, self.first_name, self.patronymic)


# Жанр
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Введите жанр книги", verbose_name="Жанр книги", null=True)

    def __str__(self):
        return self.name


# Язык
class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Введите язык книги", verbose_name="Язык книги", null=True)

    def __str__(self):
        return self.name


# Издательство
class Pub_house(models.Model):
    name = models.CharField(max_length=200, help_text="Введите издательство", verbose_name="Издательство книги",
                            null=True)

    def __str__(self):
        return self.name


# Переплёт
class Cover(models.Model):
    type = models.CharField(max_length=50, help_text="Введите тип переплета", verbose_name="Тип переплета", null=True,
                            blank=True)

    def __str__(self):
        return self.type


# Книга
class Book(models.Model):
    title = models.CharField(max_length=350, help_text="Введите название книги", verbose_name="Название книги")
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, help_text="Выберите жанр для книги",
                              verbose_name="Жанр книги", null=True, blank=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, help_text="Выберите язык книги",
                                 verbose_name="Язык книги", null=True, blank=True)
    author = models.ManyToManyField('Author', help_text="Выберите автора книги", verbose_name="Автор книги")
    summary = models.TextField(max_length=1750, help_text="Введите краткое описание книги",
                               verbose_name="Аннотация книги", null=True, blank=True)
    isbn = models.CharField(max_length=17, help_text="Должно содержать 17 символов", verbose_name="ISBN книги")
    year_of_pub = models.DateField(null=True, blank=True)
    pub_house = models.ForeignKey('Pub_house', on_delete=models.SET_NULL, help_text="Введите название издательства",
                                  verbose_name="Название издательства", null=True, blank=True)
    cover = models.ForeignKey('Cover', on_delete=models.SET_NULL, help_text="Выберите переплет",
                              verbose_name="Переплет", null=True, blank=True)
    image = models.ImageField(verbose_name="Картинка книги", null=True, blank=True)

    def __str__(self):
        return self.title

    # Необходимо добавить url в urls!!!!!!
    def get_absolute_url(self):
        # Возвращает URL-адрес для доступа к определенному экземпляру книги
        return reverse('book-detail', args=[str(self.id)])

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Авторы'


# Статус
class Status(models.Model):
    name = models.CharField(max_length=20, help_text="Введите статус экземпляра книги",
                            verbose_name="Статус экземпляра книги", blank=True, null=True)

    def __str__(self):
        return self.name


# Поставщик
class Provider(models.Model):
    name = models.CharField(max_length=200, help_text="Введите поставщика", verbose_name="Поставщик")
    address = models.CharField(max_length=200, help_text="Введите адрес поставщика", verbose_name="Адрес поставщика")
    phone = models.CharField(max_length=18, help_text="Введите номер телефона поставщика",
                             verbose_name="Номер телефона поставщика")

    def __str__(self):
        return self.name


# Поступление
class Admission(models.Model):
    number = models.IntegerField(verbose_name="Номер поступления")
    name_prov = models.ForeignKey('Provider', on_delete=models.SET_NULL, help_text="Выберите поставщика поступления",
                                  verbose_name="Поставщик поступления", null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return str(self.number)


# Экземпляр книги
class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.PROTECT, help_text="Выберите книгу",
                             verbose_name="Название книги")
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, help_text="Выберите статус", verbose_name="Статус",
                               null=True, blank=True)
    receipt = models.ForeignKey('Admission', on_delete=models.PROTECT, help_text="Выберите номер поступления",
                                verbose_name="Номер поступления")
    cost = models.IntegerField(help_text="Введите стоимость книги", verbose_name="Стоимость книги")
    order_num = models.ForeignKey('Booking', on_delete=models.SET_NULL, verbose_name="Номер заказа",
                                  help_text="Выберите номер заказа", null=True, blank=True)

    def __str__(self):
        return self.book.title


# Заказ
class Booking(models.Model):
    book = models.ForeignKey('Book', on_delete=models.PROTECT, help_text="Выберите книгу",
                             verbose_name="Название книги")
    price = models.IntegerField(help_text="Введите стоимость заказа", verbose_name="Стоимость заказа")
    full_name = models.CharField(max_length=150, help_text="Введите ФИО заказчика", verbose_name="ФИО заказчика")
    address = models.CharField(max_length=200, help_text="Введите адрес заказчика", verbose_name="Адрес заказчика")
    order_date = models.DateField(default=date.today, help_text="Выберите дату заказа", verbose_name="Дата заказа")

    def __str__(self):
        return str(self.id)


# Реклама
class Advertisement(models.Model):
    name = models.CharField(max_length=100, help_text="Введите описание к картинке", verbose_name="Картинка", null=True,
                            blank=True)
    image = models.ImageField(verbose_name="Акция")

    def __str__(self):
        return self.name
