from django.db import models


class Status(models.Model):
    name = models.CharField(
        verbose_name='Название статуса',
        max_length=20,
        unique=True,
        null=False,
    )

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(
        verbose_name='Название программы',
        max_length=30,
        unique=True,
        null=False,
    )

    class Meta:
        verbose_name = 'программа'
        verbose_name_plural = 'программы'

    def __str__(self):
        return self.name


class Ambassador(models.Model):
    first_name = models.CharField()
    middle_name = models.CharField()
    last_name = models.CharField()
    gender = models.CharField()
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
    )
    registration_date = models.DateField()
    user_comment = models.TextField()
    activity = models.Choices()
    clothing_size = models.CharField()
    shoe_size = models.CharField()
    telegram_login = models.CharField()
    email = models.EmailField()
    mobile_phone = models.CharField()
    blog_link = models.TextField()
    education = models.TextField()
    work_place = models.TextField()
    education_target = models.TextField()
    onboarding_date = models.DateField()
    guide_date = models.DateField()
    comment_ambassador = models.TextField()
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
    )


class Target(models.Model):
    pass


class Promocode(models.Model):
    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        verbose_name='Амбасадор',
    )
    value = models.CharField(
        verbose_name='Значение промокода',
        max_length=20,
        null=False,
    )
    replaced_at = models.DateField(
        verbose_name='Дата замены',
        null=True,
        blank=True,
    )
    is_current = models.BooleanField(
        verbose_name='Текущий',
        default=True,
        null=False,
    )

    class Meta:
        verbose_name = 'промокод'
        verbose_name_plural = 'промокоды'

    def __str__(self):
        return self.value


class Address(models.Model):
    pass
