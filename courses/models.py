from django.db import models

class Course(models.Model):
    name = models.CharField("Название курса", max_length=255)
    credits = models.IntegerField("Кредиты")
    description = models.TextField("Описание")
    program = models.ForeignKey("faculty.Program", on_delete=models.CASCADE, related_name="courses")
    teacher = models.ForeignKey("faculty.Teacher", on_delete=models.SET_NULL, null=True, related_name="courses")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"{self.name} ({self.program.name})"


class Enrollment(models.Model):
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name="enrollments")
    status = models.CharField("Статус", max_length=50)

    class Meta:
        verbose_name = "Запись на курс"
        verbose_name_plural = "Записи на курсы"

    def __str__(self):
        return f"{self.student.name} → {self.course.name}"


class Grade(models.Model):
    enrollment = models.ForeignKey("courses.Enrollment", on_delete=models.CASCADE, related_name="grades")
    value = models.FloatField("Оценка")
    date = models.DateField("Дата")

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

    def __str__(self):
        return f"{self.value} ({self.enrollment.student.name})"