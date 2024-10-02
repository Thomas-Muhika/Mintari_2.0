from django.contrib import admin
from portal.models import RecordOrder, StockCategories, Stock, WishList, Cart, Order, CustomOrder, BlogArticle


admin.site.register(RecordOrder)
admin.site.register(StockCategories)
admin.site.register(Stock)
admin.site.register(WishList)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(CustomOrder)
admin.site.register(BlogArticle)

