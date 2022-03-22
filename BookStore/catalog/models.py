from django.db import models
from django.urls import reverse


class Department(models.Model):
    num_dep = models.IntegerField()
    name = models.CharField(max_length=150, help_text="Введите название отдела", verbose_name="Название отдела",
                            null=True)

    def __str__(self):
        return str(self.num_dep)


class Location(models.Model):
    num_shelf = models.IntegerField()
    num_rack = models.IntegerField()
    num_dep = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.num_shelf)


class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="Введите имя автора", verbose_name="Имя автора")
    last_name = models.CharField(max_length=100, help_text="Введите фамилию автора", verbose_name="Фамилия автора")

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Введите жанр книги", verbose_name="Жанр книги", null=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Введите язык книги", verbose_name="Язык книги", null=True)

    def __str__(self):
        return self.name


class Pub_house(models.Model):
    name = models.CharField(max_length=200, help_text="Введите издательство", verbose_name="Издательство книги")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Введите название книги", verbose_name="Название книги")
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, help_text="Выберите жанр для книги",
                              verbose_name="Жанр книги", null=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, help_text="Выберите язык книги",
                                 verbose_name="Язык книги", null=True)
    author = models.ManyToManyField('Author', help_text="Выберите автора книги", verbose_name="Автор книги")
    summary = models.TextField(max_length=1000, help_text="Введите краткое описание книги",
                               verbose_name="Аннотация книги", null=True)
    isbn = models.CharField(max_length=17, help_text="Должно содержать 17 символов", verbose_name="ISBN книги")
    year_of_pub = models.DateField(null=True)
    pub_house = models.ForeignKey('Pub_house', on_delete=models.SET_NULL, help_text="Введите название издательства",
                                  verbose_name="Название издательства", null=True)
    actual_cost = models.IntegerField()
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, help_text="Выберите полку в магазине",
                                 verbose_name="Полка", null=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     # Возвращает URL-адрес для доступа к определенному экземпляру книги
    #     return reverse('book-detail', args=[str(self.id)])

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Авторы'


class Provider(models.Model):
    name = models.CharField(max_length=200, help_text="Введите поставщика", verbose_name="Поставщик")
    address = models.CharField(max_length=200, help_text="Введите адрес поставщика", verbose_name="Адрес поставщика")
    phone = models.CharField(max_length=11, help_text="Введите номер телефона поставщика",
                             verbose_name="Номер телефона поставщика")

    def __str__(self):
        return self.name


class Admission(models.Model):
    number = models.IntegerField()
    name_prov = models.ForeignKey('Provider', on_delete=models.SET_NULL, help_text="Выберите поставщика поступления",
                                  verbose_name="Поставщик поступления", null=True)
    date = models.DateField()

    def __str__(self):
        return str(self.number)


class Employee(models.Model):
    first_name = models.CharField(max_length=100, help_text="Введите имя сотрудника", verbose_name="Имя сотрудника")
    last_name = models.CharField(max_length=100, help_text="Введите фамилию сотрудника",
                                 verbose_name="Фамилия сотрудника")
    patronymic = models.CharField(max_length=100, help_text="Введите отчество сотрудника",
                                  verbose_name="Отчество сотрудника")
    position = models.CharField(max_length=100, help_text="Введите должность сотрудника",
                                verbose_name="Должность сотрудника")
    salary = models.IntegerField(help_text="Введите зарплату сотрудника",
                                 verbose_name="Зарплата сотрудника")
    phone = models.CharField(max_length=11, help_text="Введите номер телефона сотрудника",
                             verbose_name="Номер телефона сотрудника")

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)


class Check(models.Model):
    number = models.CharField(max_length=20, help_text="Введите чек", verbose_name="Чек")
    date = models.DateTimeField()
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, help_text="Выберите сотрудника, пробившего чек",
                                 verbose_name="Сотрудника, пробивший чек")
    book_for_sale = models.ManyToManyField('Book_for_sale', help_text="Выберите книгу", verbose_name="Книга")

    def __str__(self):
        return str(self.number)


class Book_for_sale(models.Model):
    barcode = models.CharField(max_length=13, help_text="Введите штрих-код", verbose_name="Штрих-код")
    admission = models.ForeignKey('Admission', on_delete=models.PROTECT, help_text="Выберите номер поступления",
                                  verbose_name="Номер поступления")
    book = models.ForeignKey('Book', on_delete=models.PROTECT, help_text="Выберите книгу",
                             verbose_name="Книга")
    cost = models.IntegerField()

    def __str__(self):
        return self.barcode
