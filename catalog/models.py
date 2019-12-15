import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    class Meta():
        db_table = "article"
        
    # Работа с ООП. <Article> - модель. Обязательно ДОЛЖНА быть названа в единственном числе. Article - Article(s)
    article_title = models.CharField('name article', max_length = 200) 
    # <article_title> - <любая переменная_title>. 
    # <CharField> = <VarChar>, в MySQL. Поле для ввода текста в 200-300max символах.
    # <TextField> - поле для ввода текста, хранения очень большого кол-во текста.
    article_text = models.TextField('text article')
    pub_date = models.DateTimeField('date published')
    
    def __str__(self): # OOP
        return self.article_title
    
    def was_published_recently(self):
        # <timedelta> - позволяет от текущего времени отнять n-ко-во времени.
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7)) 
    

    
class Comment(models.Model):
    class Meta():
        db_table = "comment"
        
    comment_article = models.ForeignKey(Article, on_delete = models.CASCADE) 
    # привяка коментария к определенной статье. <models.ForeignKey(Article)> - <(Article)> - может быть толко один аргумент, это модель, к которой должна привязываться данная модель. В нашем случаи <Article> 
    # <on_delete = models.CASCADE> - <on_delete> - аргумент(команда), которая что-то сделает во время удаления комментария. <models.CASCADE> - команда говорит: Что, после удаления нужно применить *Каскад*. <CASCADE> - когда будет удалена, какая-либо статья, будет так же удалены и все комментарии когда-либо написанные и сохраненные в Базе данных для данной статье.
    author_name = models.CharField('author', max_length = 50) 
    comment_text = models.TextField('comment')
    
    def __str__(self): # OOP
        return self.author_name
