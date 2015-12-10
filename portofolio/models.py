from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField('Category', max_length=100)
    category_slug = models.SlugField('Slug', max_length=100, unique=True)
    category_desc = models.TextField('Description')
    publish_date = models.DateTimeField('date published', auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.category_name

class Article(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_author = models.CharField(max_length=100)
    article_title = models.CharField('Title', max_length=255)
    article_slug = models.CharField('Slug', max_length=255)
    article_content = models.TextField('Content')
    publish_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    modify_date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.article_title

class Project(models.Model):
    project_name = models.CharField('Name', max_length=100)
    project_date = models.DateField('Date')
    project_url = models.URLField('Project URL', max_length=225)
    project_thumb = models.ImageField('Thumbnail', upload_to='uploads/%Y/%m/%d/')
    project_desc = models.TextField('Description')

    def __str__(self):
        return self.project_name

class Setting(models.Model):
    setting_name = models.CharField(max_length=100)
    setting_value = models.CharField(max_length=100)

    def __str__(self):
        return self.setting_name

class Experience(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.company
