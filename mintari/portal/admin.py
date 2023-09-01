from django.contrib import admin
from portal.models import RecordOrder, StockCategories, Stock, WishList, Cart


admin.site.register(RecordOrder)
admin.site.register(StockCategories)
admin.site.register(Stock)
admin.site.register(WishList)
admin.site.register(Cart)