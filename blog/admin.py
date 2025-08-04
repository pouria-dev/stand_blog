from django.contrib import admin
from .models import Article , Category , Comment , Message


class FilterByTitle(admin.SimpleListFilter):
    title = "موارد پرتکرار"

    parameter_name = "title"

    def lookups(self, request, model_admin):
        return (
            ('django' , "جنگو"),
            ("python", 'پایتون')



        )
    
    def queryset(self, request, queryset):
        value = self.value()
        if  value:
            return queryset.filter(title__icontains=value)
        
        return queryset
       
        



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','created','updated', 'status')
    list_filter = ('status', 'created', FilterByTitle)
    list_editable = ('status',)
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created',)
    readonly_fields = ( 'created', 'updated')
    fieldsets = (
        ('کارهای مربوط به مقاله', {
            'fields': ('title', 'text', 'image', 'banner', 'category', 'status', 'slug')
        }),
        ('تاریخ', {
            'fields': ('updated', 'created'),
        }),
    )



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created', 'article')
    search_fields = ('author__username', 'text')
    list_filter = ('created', 'article')
    ordering = ('-created',)
    readonly_fields = ('created',)

    def post(self, obj):
        return obj.post.title if obj.post else "No Post"    
    

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'created')
    search_fields = ('name', 'text')
    ordering = ('-created',)

    def short_text(self, obj):
        return obj.text[:10]
    short_text.short_description = 'متن کوتاه'


