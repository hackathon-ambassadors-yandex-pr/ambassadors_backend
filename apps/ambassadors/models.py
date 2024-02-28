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
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=20,
        null=False,
    )
    middle_name = models.CharField(
        verbose_name="Отчество",
        max_length=20,
        null=False,
    )
    last_name = models.CharField(
        verbose_name="Фамилия",
        max_length=20,
        null=False,
    )
    gender = models.CharField(
        verbose_name="Пол",
        max_length=5,
        null=False,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name="Статус",
        related_name="ambassadors",
    )
    registration_date = models.DateField(
        verbose_name="Дата регистрации",
        auto_now_add=True,
    )
    user_comment = models.TextField(
        verbose_name="Комментарий пользователся",
        null=True,
        blank=True,
    )
    activity = models.CharField(
        max_length=20,
        choices=[
            ("ACTIVE", "Активный"),
            ("INACTIVE", "Неактивный"),
        ],
        default="ACTIVE",
        verbose_name="Активность",
    )
    clothing_size = models.CharField(
        verbose_name="Размер одежды",
        max_length=5,
        null=False,
    )
    shoe_size = models.CharField(
        verbose_name="Размер обуви",
        max_length=5,
        null=False,
    )
    telegram_login = models.CharField(
        verbose_name="Имя пользователя телеграм",
        max_length=20,
        null=False,
    )
    email = models.EmailField(
        verbose_name="Email",
        null=False,
    )
    mobile_phone = models.CharField(
        verbose_name="Номер телефона",
        max_length=20,
        null=False,
    )
    blog_link = models.TextField(
        verbose_name="Ссылка на блог",
    )
    education = models.TextField(
        verbose_name="Образование",
        null=False,
    )
    work_place = models.TextField(
        verbose_name="Место работы",
        null=False,
    )
    education_target = models.TextField(
        verbose_name="Цель образования",
        null=False,
    )
    onboarding_date = models.DateField(
        verbose_name="Дата онбординга",
        null=True,
        blank=True,
    )
    guide_date = models.DateField(
        verbose_name="Дата прохождения гайда",
        null=True,
        blank=True,
    )
    comment_ambassador = models.TextField(
        verbose_name="Комментарий амбассадора",
        null=True,
        blank=True,
    )
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        verbose_name="программа",
        related_name="ambassadors",
    )

    class Meta:
        verbose_name = "амбассадор"
        verbose_name_plural = "амбассадоры"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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
        verbose_name="Амбассадоры",
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
        verbose_name="Амбассадор",
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
        verbose_name="Амбассадор",
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
        verbose_name="амбассадор",
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
