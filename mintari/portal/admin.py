from django.contrib import admin
from portal.models import RecordOrder, StockCategories, Stock, WishList


admin.site.register(RecordOrder)
admin.site.register(StockCategories)
admin.site.register(Stock)
admin.site.register(WishList)