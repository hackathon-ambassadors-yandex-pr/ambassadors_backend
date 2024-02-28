from django.db import models


class Status(models.Model):
    name = models.CharField(
        verbose_name="Название статуса",
        max_length=20,
        unique=True,
        null=False,
    )

    class Meta:
        verbose_name = "статус"
        verbose_name_plural = "статусы"

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(
        verbose_name="Название программы",
        max_length=30,
        unique=True,
        null=False,
    )

    class Meta:
        verbose_name = "программа"
        verbose_name_plural = "программы"

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
        related_name="ambassadors",
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
        related_name="ambassadors",
    )


class Target(models.Model):
    name = models.CharField(
        verbose_name="Название цели",
        max_length=30,
        unique=True,
        null=False,
    )
    ambassadors = models.ManyToManyField(
        Ambassador,
        through="AmbassadorTarget",
        verbose_name="Амбасадоры",
        related_name="targets",
    )

    class Meta:
        verbose_name = "цель"
        verbose_name_plural = "цели"

    def __str__(self):
        return self.name


class AmbassadorTarget(models.Model):
    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        verbose_name="Амбасадор",
        related_name="ambassador_target",
    )
    target = models.ForeignKey(
        Target,
        on_delete=models.CASCADE,
        verbose_name="Цель",
        related_name="ambassador_target",
    )

    class Meta:
        unique_together = (
            "ambassador",
            "target",
        )

    def __str__(self):
        return f"{self.ambassador.first_name} {self.ambassador.last_name} - {self.target.name}"


class Promocode(models.Model):
    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        verbose_name="Амбасадор",
        related_name="promocodes",
    )
    value = models.CharField(
        verbose_name="Значение промокода",
        max_length=20,
        null=False,
    )
    replaced_at = models.DateField(
        verbose_name="Дата замены",
        null=True,
        blank=True,
    )
    is_current = models.BooleanField(
        verbose_name="Текущий",
        default=True,
        null=False,
    )

    class Meta:
        verbose_name = "промокод"
        verbose_name_plural = "промокоды"

    def __str__(self):
        return self.value


class Address(models.Model):
    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        verbose_name="амбасадор",
        related_name="addresses",
    )
    country = models.CharField(
        verbose_name="Страна",
        max_length=20,
        null=False,
    )
    city = models.CharField(
        verbose_name="Город",
        max_length=20,
        null=False,
    )
    address = models.CharField(
        verbose_name="Адрес",
        max_length=50,
        null=False,
    )
    code = models.CharField(
        verbose_name="Почтовый индекс",
        max_length=10,
        null=False,
    )
    replaced_at = models.DateField(
        verbose_name="Дата замены",
        null=True,
        blank=True,
    )
    is_current = models.BooleanField(
        verbose_name="Текущий",
        default=True,
        null=False,
    )

    class Meta:
        verbose_name = "адрес"
        verbose_name_plural = "адреса"

    def __str__(self):
        return f"{self.country}, {self.city}, {self.address}"
