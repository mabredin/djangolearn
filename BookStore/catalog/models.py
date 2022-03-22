from django.db import models


class Department(models.Model):
    num_dep = models.IntegerField()
    name = models.CharField(max_length=150, help_text="Введите название отдела", verbose_name="Название отдела")

    def __str__(self):
        return self.num_dep


class Location(models.Model):
    num_shelf = models.IntegerField()
    num_rack = models.IntegerField()
    num_dep = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.num_shelf


class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="Введите имя автора", verbose_name="Имя автора")
    last_name = models.CharField(max_length=100, help_text="Введите фамилию автора", verbose_name="Фамилия автора")

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Введите название книги", verbose_name="Название книги")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, help_text="Выберите жанр для книги",
                              verbose_name="Жанр книги", null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, help_text="Выберите язык книги",
                                 verbose_name="Язык книги", null=True)
    author = models.ManyToManyField('Author', help_text="Выберите автора книги", verbose_name="Автор книги")
    summary = models.TextField(max_length=1000, help_text="Введите краткое описание книги",
                               verbose_name="Аннотация книги")
    isbn = models.CharField(max_length=13, help_text="Должно содержать 13 символов", verbose_name="ISBN книги")
    year_of_pub = models.DateField()
    pub_house = models.CharField(max_length=150, help_text="Введите название издательства",
                                 verbose_name="Название издательства")
    actual_cost = models.IntegerField()
