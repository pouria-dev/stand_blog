
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from .manager import Model_Manager





class Category(models.Model):
    title = models.CharField(max_length=15 , unique=True, verbose_name='عنوان')

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['title']


class Article(models.Model):
    title = models.CharField(max_length=20, help_text="It should be unique", unique=True, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')
    image = models.ImageField(upload_to='article/image')
    category = models.ManyToManyField(Category, related_name='articles', verbose_name='دسته بندی')
    banner = models.ImageField(upload_to='article/banner', help_text='best size for banner:770x340')
    status = models.BooleanField(default=False)
    slug = models.SlugField(null=True, unique=True, blank=True, default=1) # slug field for SEO
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects =  models.Manager()  # Default manager 
    custom_manager = Model_Manager()  # Custom manager for additional functionality
    # If objects is null , the custom manager will be used by default
    # and change the base-query-set to filter articles with status=True in admin panel !!
    class Meta:
        verbose_name='بلاگ'
        verbose_name_plural = 'بلاگ ها'

        ordering = ['-created']
        


        
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={"slug": self.slug})

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.slug:

            self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments") # رابطه معکوس برای این فیلد
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments' , null=True , blank=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)


    def __str__(self):
        if self.author.username:
            return f"{self.author.username} - {self.text[:30]}"
        return f"Anonymous - {self.text[:30]}"
    
         
    
    class Meta:

        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'


class Message(models.Model):
    name = models.CharField(max_length=10)
    text = models.TextField()
    email = models.EmailField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}------{self.text[:30]}"
    
    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
