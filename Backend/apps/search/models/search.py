from django.db import models
class Search(models.Model):

  id = models.AutoField(primary_key=True)
  word = models.CharField("word searching", max_length=50)
  searchs = models.IntegerField("num searchs", default=1, null=True)
  result = models.JSONField()
  createSearch = models.DateTimeField(auto_now_add=True, null=True)
  lastSearch = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return self.word


