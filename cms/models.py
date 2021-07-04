from django.db import models


class Book(models.Model):
    """書籍"""
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharFiedld('出版社', max_length=255, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)
    price = models.IntegerField('書籍価格', blank=True, default=0)

    def __str__(self):
        return self.name


class Impression(models.Model):
    """感想"""
    book = models.ForignKey(Book, verbose_name='書籍', related_name='impressions', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def _str_(self):
        return self.comment


class AdsenseUrl(models.Model):
    """購入できるURL"""
    book = models.ForignKey(Book, verbose_name='書籍', related_name='impressions', on_delete=models.CASCADE)
    url = models.UrlField('URL', blank=True)