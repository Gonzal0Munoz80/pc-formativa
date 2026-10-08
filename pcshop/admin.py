from django.contrib import admin
from pcshop.models import Producto,Categoria

admin.site.site_header = "Administración PCSHOP"
admin.site.site_title = "Administración PCSHOP"
admin.site.index_title = "Panel de administración de PCSHOP"
# Register your models here.



@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio_formateado', 'stock']
    list_filter = ['stock']
    search_fields = ['nombre', 'descripcion']
    search_help_text = "Buscar productos por nombre o descripción"

    @admin.display(description='Precio')
    def precio_formateado(self, obj):
        return f"${obj.precio:,.0f}".replace(',', '.')


class PccategoriaInline(admin.TabularInline):
    model = Producto
    extra = 1
    fields = ['nombre', 'precio', 'stock']
    show_change_link = True

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre_categoria', 'descripcion_categoria']
    inlines = [PccategoriaInline]


@admin.display(description='Productos en esta categoría')
def productos_en_categoria(self, obj):
    return obj.producto_set.count()

