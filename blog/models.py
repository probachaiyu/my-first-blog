from django.db import models
from django.urls import reverse
from django.utils import timezone
from suit_ckeditor.widgets import CKEditorWidget


class Category(models.Model):
    class Meta():
        db_table = 'category'
        #ordering = ['name']

    name = models.CharField(max_length=100)
    #slug = models.SlugField(default=name)

    def __str__(self):
            return self.name



class Tag(models.Model):
 name = models.CharField(blank=True, null=True, max_length=50, unique=True)

 def __str__(self):
  return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
    image = models.ImageField(upload_to='files', null=True, blank=True)
    likes = models.IntegerField(default=0)
    category = models.ForeignKey(Category, null = True, blank=True)
    tag = models.ManyToManyField(Tag, null = True, blank=True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.id})

    def __str__(self):
            return self.title

class Comments(models.Model):

    comments_text = models.CharField(max_length=500)
    comments_post = models.ForeignKey(Post)
    #author = models.ForeignKey('auth.User')
    #published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'comments'

