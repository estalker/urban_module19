from django.contrib import admin
from .models import Game, Buyer, News

# Register your models here.
# serge 12345678

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    search_fields = ('title', )
    list_filter = ('cost', 'size')
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    search_fields = ('name', )
    list_filter = ('balance', 'age')
    list_per_page = 30

    readonly_fields = ('balance', )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', )
    list_filter = ('date', )
    list_per_page = 10

    class Meta(object):
        verbose_name_plural = 'News'
