from django.conf import settings
from django.db import models


class Course(models.Model):
    "Generated Model"
    author = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="course_author",
    )
    title = models.CharField(
        null=True,
        blank=True,
        max_length=256,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    categories = models.ManyToManyField(
        "course.Category",
        blank=True,
        related_name="course_categories",
    )


class Module(models.Model):
    "Generated Model"
    course = models.ForeignKey(
        "course.Course",
        on_delete=models.CASCADE,
        related_name="module_course",
    )
    title = models.CharField(
        max_length=256,
    )
    description = models.TextField()


class Event(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="event_user",
    )
    date = models.DateTimeField()


class Subscription(models.Model):
    "Generated Model"
    subscription_type = models.ForeignKey(
        "course.SubscriptionType",
        on_delete=models.CASCADE,
        related_name="subscription_subscription_type",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="subscription_user",
    )


class Enrollment(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="enrollment_user",
    )
    course = models.ForeignKey(
        "course.Course",
        on_delete=models.CASCADE,
        related_name="enrollment_course",
    )


class PaymentMethod(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="paymentmethod_user",
    )
    primary = models.BooleanField()
    token = models.CharField(
        max_length=256,
    )


class SubscriptionType(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )


class Category(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )


class Lesson(models.Model):
    "Generated Model"
    module = models.ForeignKey(
        "course.Module",
        on_delete=models.CASCADE,
        related_name="lesson_module",
    )
    title = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    media = models.URLField()


class Group(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )


class Recording(models.Model):
    "Generated Model"
    event = models.ForeignKey(
        "course.Event",
        on_delete=models.CASCADE,
        related_name="recording_event",
    )
    media = models.URLField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="recording_user",
    )
    published = models.DateTimeField()


# Create your models here.
