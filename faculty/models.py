from django.db import models

class Faculty(models.Model):
    name = models.CharField("Название факультета", max_length=255)
    description = models.TextField("Описание")
    head = models.CharField("Заведующий", max_length=255)

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультеты"

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField("Название программы", max_length=255)
    duration = models.IntegerField("Длительность (лет)")
    description = models.TextField("Описание")
    faculty = models.ForeignKey("faculty.Faculty", on_delete=models.CASCADE, related_name="programs")

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"

    def __str__(self):
        return f"{self.name} ({self.faculty.name})"


class Teacher(models.Model):
    name = models.CharField("Имя преподавателя", max_length=255)
    title = models.CharField("Должность", max_length=255)
    faculty = models.ForeignKey("faculty.Faculty", on_delete=models.CASCADE, related_name="teachers")
    research_area = models.CharField("Область исследований", max_length=255)

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self):
        return f"{self.title} {self.name}"


class Event(models.Model):
    title = models.CharField("Название события", max_length=255)
    description = models.TextField("Описание")
    date = models.DateField("Дата")
    faculty = models.ForeignKey("faculty.Faculty", on_delete=models.CASCADE, related_name="events")

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return f"{self.title} ({self.date})"


class Document(models.Model):
    title = models.CharField("Название документа", max_length=255)
    file_url = models.URLField("Файл")
    faculty = models.ForeignKey("faculty.Faculty", on_delete=models.CASCADE, related_name="documents")

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title