from django.db import models

# Create your models here.
class Group(models.Model):
    title = models.TextField()
    number = models.SmallIntegerField()
    year = models.SmallIntegerField()


class Discipline(models.Model):
    title = models.TextField()
    group = models.ForeignKey("marks.Group", on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True)


class Lesson(models.Model):
    date = models.DateField()
    para = models.SmallIntegerField()
    discpline = models.ForeignKey("marks.Discipline", on_delete=models.CASCADE, null=True)


class Mark(models.Model):
    lesson = models.ForeignKey("marks.Lesson", on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True, related_name="teacher_marks")
    student = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True, related_name="student_marks")
