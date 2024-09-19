from django.contrib import admin


from .models import Article, Category, Service, Location, Employer, User, InventaireItem

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Location)
admin.site.register(Employer)
admin.site.register(User)
admin.site.register(InventaireItem)
