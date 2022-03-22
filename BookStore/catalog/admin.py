from django.contrib import admin

from catalog.models import Department, Location, Author, Genre, Language, Pub_house, Book, Provider, Admission, \
    Employee, Check, Book_for_sale


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('num_dep', 'name')

admin.site.register(Department, DepartmentAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('num_shelf', 'num_rack', 'num_dep')


admin.site.register(Location, LocationAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Pub_house)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author', 'actual_cost')
    list_filter = ('genre', 'language', 'author')

admin.site.register(Book, BookAdmin)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')

admin.site.register(Provider, ProviderAdmin)


class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('number', 'name_prov', 'date')

admin.site.register(Admission, AdmissionAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'position', 'salary', 'phone')

admin.site.register(Employee, EmployeeAdmin)


class CheckAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'employee', 'display_book_for_sale')

admin.site.register(Check, CheckAdmin)


class Book_for_saleAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'admission', 'book', 'cost')

admin.site.register(Book_for_sale, Book_for_saleAdmin)
