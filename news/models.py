from django.db import models

class News(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Содержание")
    published_at = models.DateField("Дата публикации")
    author = models.ForeignKey("faculty.Teacher", on_delete=models.SET_NULL, null=True, related_name="news", verbose_name="Автор")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title