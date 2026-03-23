from django.db import models

class Student(models.Model):
    name = models.CharField("Имя студента", max_length=255)
    email = models.EmailField("Email", unique=True)
    program = models.ForeignKey("faculty.Program", on_delete=models.CASCADE, related_name="students")
    enrollment_date = models.DateField("Дата поступления")

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return self.name