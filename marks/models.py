from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Profile(models.Model):
    class Role(models.IntegerChoices):
        undefined = 0
        teacher = 1
        student = 2

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, null=True, blank=True)
    role = models.IntegerField("Роль", choices=Role, default=Role.undefined)
    group = models.ForeignKey("marks.Group", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username if self.user else f"Profile {self.id}"


@receiver(post_save, sender=User)
def on_user_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance, role=Profile.Role.undefined)


# Create your models here.
class Group(models.Model):
    title = models.TextField()
    number = models.SmallIntegerField()
    year = models.SmallIntegerField()


class Discipline(models.Model):
    title = models.TextField()
    group = models.ForeignKey("marks.Group", on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField("Картинка", null=True, upload_to='discipline')


class Lesson(models.Model):
    date = models.DateField()
    para = models.SmallIntegerField()
    discpline = models.ForeignKey("marks.Discipline", on_delete=models.CASCADE, null=True)


class Mark(models.Model):
    lesson = models.ForeignKey("marks.Lesson", on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True, related_name="teacher_marks")
    student = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True, related_name="student_marks")
