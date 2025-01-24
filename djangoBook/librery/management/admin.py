from django.contrib import admin
from .models import Book, User, Rental
from django.contrib.auth.admin import UserAdmin


# admin.site.register(UserAdmin)


admin.site.site_header = "Управление ,библиотекой"
admin.site.site_title = "Админка librery"
admin.site.index_title = "Добро пожаловать в librery"



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'published_year', 'genre','is_available')  # Поля для отображения в списке
  list_filter = ('genre', 'is_available')  # Фильтры в правой части админки
  search_fields = ('title', 'author')  # Поля для поиска
#   ordering = ('due_date',)  # Сортировка записей


@admin.register(Rental)
class ProjectAdmin(admin.ModelAdmin):
  list_display = ('user', 'book')  # Поля для отображения в списке


@admin.register(User)
class UserAdmin(UserAdmin):
  list_display = ('username', 'email')
  fieldsets = UserAdmin.fieldsets + (
    ('Дополнительная информация', {'fields': ('firstname', 'lastname')}),
  )


