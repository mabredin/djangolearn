from django.contrib import admin

from catalog.models import Author, Genre, Language, Pub_house, Cover, Book, Status, Provider, Admission, BookInstance, \
    Booking, Advertisement


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'patronymic')


admin.site.register(Author, AuthorAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Genre, GenreAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Language, LanguageAdmin)


class Pub_houseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Pub_house, Pub_houseAdmin)


class CoverAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')


admin.site.register(Cover, CoverAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'isbn', 'genre', 'language', 'display_author', 'pub_house', 'cover')
    list_filter = ('genre', 'language', 'author', 'pub_house')


admin.site.register(Book, BookAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Status, StatusAdmin)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone')


admin.site.register(Provider, ProviderAdmin)


class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'name_prov', 'date')


admin.site.register(Admission, AdmissionAdmin)


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status', 'receipt', 'cost', 'order_num')
    list_filter = ('book', 'status', 'receipt', 'order_num')


admin.site.register(BookInstance, BookInstanceAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'price', 'full_name', 'address', 'order_date')
    list_filter = ('book', 'full_name', 'order_date')


admin.site.register(Booking, BookingAdmin)


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')


admin.site.register(Advertisement, AdvertisementAdmin)
