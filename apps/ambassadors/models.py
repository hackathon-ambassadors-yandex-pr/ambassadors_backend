from django.db import models


class Status(models.Model):
    """Модель статуса."""

    name = models.CharField(
        verbose_name="название статуса",
        max_length=20,
        unique=True,
    )

    class Meta:
        verbose_name = "статус"
        verbose_name_plural = "статусы"

    def __str__(self):
        return self.name


class Program(models.Model):
    """Модель программы."""

    name = models.CharField(
        verbose_name="название программы",
        max_length=30,
        unique=True,
    )

    class Meta:
        verbose_name = "программа"
        verbose_name_plural = "программы"

    def __str__(self):
        return self.name


class Target(models.Model):
    """Модель цели."""

    name = models.CharField(
        verbose_name="название цели",
        max_length=30,
        unique=True,
    )

    class Meta:
        verbose_name = "цель"
        verbose_name_plural = "цели"

    def __str__(self):
        return self.name


class Ambassador(models.Model):
    """Модель амбассадора."""

    CLOTHING_SIZE_CHOICES = [
        ("XS", "Extra Small"),
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
    ]
    EDUCATION_TARGET_CHOICES = [
        ("NEW_PROFESSION", "получение новой профессии, чтобы сменить работу"),
        (
            "DEEPEN_KNOWLEDGE",
            "углубление имеющихся знаний, чтобы использовать их в текущей работе",
        ),
        ("OTHER", "свой вариант"),
    ]
    GENDER_CHOICES = [
        ("М", "Male"),
        ("Ж", "Female"),
    ]
    first_name = models.CharField(
        verbose_name="имя",
        max_length=20,
    )
    middle_name = models.CharField(
        verbose_name="отчество",
        max_length=20,
    )
    last_name = models.CharField(
        verbose_name="фамилия",
        max_length=20,
    )
    gender = models.CharField(
        verbose_name="пол",
        max_length=5,
        choices=GENDER_CHOICES,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name="статус",
        related_name="ambassadors",
    )
    registration_date = models.DateField(
        verbose_name="дата регистрации",
        auto_now_add=True,
    )
    user_comment = models.TextField(
        verbose_name="комментарий пользователя",
        null=True,
        blank=True,
    )
    clothing_size = models.CharField(
        verbose_name="размер одежды",
        max_length=5,
        choices=CLOTHING_SIZE_CHOICES,
    )
    shoe_size = models.CharField(
        verbose_name="размер обуви",
        max_length=5,
    )
    telegram_login = models.CharField(
        verbose_name="имя пользователя телеграм",
        max_length=20,
    )
    email = models.EmailField(
        verbose_name="email",
    )
    mobile_phone = models.CharField(
        verbose_name="номер телефона",
        max_length=20,
    )
    blog_link = models.URLField(
        verbose_name="ссылка на блог",
    )
    education = models.TextField(
        verbose_name="образование",
    )
    work_place = models.TextField(
        verbose_name="место работы",
    )
    education_target = models.TextField(
        verbose_name="цель образования",
        choices=EDUCATION_TARGET_CHOICES,
    )
    education_target_own = models.TextField(
        verbose_name="своя цель образования",
        null=True,
        blank=True,
    )
    onboarding_date = models.DateField(
        verbose_name="дата онбординга",
        null=True,
        blank=True,
    )
    guide_date = models.DateField(
        verbose_name="дата прохождения гайда",
        null=True,
        blank=True,
    )
    comment_ambassador = models.TextField(
        verbose_name="комментарий амбассадора",
        null=True,
        blank=True,
    )
    program = models.ForeignKey(
        Program,
        on_delete=models.PROTECT,
        verbose_name="программа",
        related_name="ambassadors",
    )
    targets = models.ManyToManyField(
        Target,
        related_name="ambassadors",
    )

    class Meta:
        verbose_name = "амбассадор"
        verbose_name_plural = "амбассадоры"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Promocode(models.Model):
    """Модель промокода."""

    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        verbose_name="амбассадор",
        related_name="promocodes",
    )
    value = models.CharField(
        verbose_name="значение промокода",
        max_length=20,
    )
    replaced_at = models.DateField(
        verbose_name="дата замены",
        null=True,
        blank=True,
    )
    is_current = models.BooleanField(
        verbose_name="текущий",
        default=True,
    )

    class Meta:
        verbose_name = "промокод"
        verbose_name_plural = "промокоды"

    def __str__(self):
        return self.value


class Address(models.Model):
    """Модель адреса."""

    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        verbose_name="амбассадор",
        related_name="addresses",
    )
    country = models.CharField(
        verbose_name="страна",
        max_length=20,
    )
    city = models.CharField(
        verbose_name="город",
        max_length=20,
    )
    address = models.CharField(
        verbose_name="адрес",
        max_length=50,
    )
    code = models.CharField(
        verbose_name="почтовый индекс",
        max_length=10,
    )
    replaced_at = models.DateField(
        verbose_name="дата изменения",
        null=True,
        blank=True,
    )
    is_current = models.BooleanField(
        verbose_name="текущий",
        default=True,
    )

    class Meta:
        verbose_name = "адрес"
        verbose_name_plural = "адреса"

    def __str__(self):
        return f"{self.country}, {self.city}, {self.address}"
