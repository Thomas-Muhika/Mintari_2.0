from django import forms
from portal.models import Stock


class StockUploadForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['ProductTitle', 'ProductCode', 'ProductCategory', 'ProductWeight',
                  'ProductDimension', 'ProductPrice', 'ShortDescription', 'DetailedDescription',
                  'ProductBaseImage', 'ProductImageTopView', 'ProductImageLeftView', 'ProductImageRightView',
                  'ProductImageFrontView']