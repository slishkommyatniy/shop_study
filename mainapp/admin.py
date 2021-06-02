from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm
from django.utils.safestring import mark_safe

from .models import *


class BeardsAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(BeardsAdminForm, self).__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """<span style="color: red; font-size:15px;">Загружайте изображение с минимальным разрешением {}x{}</span>
            """.format(
                *Product.MIN_RESOLUTION
            )
        )


class BeadsAdmin(admin.ModelAdmin):
    form = BeardsAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='beads'))
        return _super().formfield_for_foreignkey(db_field, request, **kwargs)


class FlossAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='floss'))
        return _super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Beads, BeadsAdmin)
admin.site.register(Floss, FlossAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
