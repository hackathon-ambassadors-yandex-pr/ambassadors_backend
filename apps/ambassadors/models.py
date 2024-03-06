from django.db import models

from apps.ambassadors.choice_classes import ClothingSize, EducationTarget, Gender


class Status(models.Model):
    """Модель статуса."""

    name = models.CharField(
        verbose_name="name",
        max_length=20,
        unique=True,
    )

    class Meta:
        verbose_name = "status"
        verbose_name_plural = "statuses"

    def __str__(self):
        return self.name


class Program(models.Model):
    """Модель программы."""

    name = models.CharField(
        verbose_name="name",
        max_length=30,
        unique=True,
    )

    class Meta:
        verbose_name = "program"
        verbose_name_plural = "programs"

    def __str__(self):
        return self.name


class Target(models.Model):
    """Модель цели."""

    name = models.CharField(
        verbose_name="name",
        max_length=30,
        unique=True,
    )

    class Meta:
        verbose_name = "target"
        verbose_name_plural = "targets"

    def __str__(self):
        return self.name


class Ambassador(models.Model):
    """Модель амбассадора."""

    first_name = models.CharField(
        verbose_name="first name",
        max_length=20,
    )
    middle_name = models.CharField(
        verbose_name="middle name",
        max_length=20,
    )
    last_name = models.CharField(
        verbose_name="last name",
        max_length=20,
    )
    gender = models.CharField(
        verbose_name="gender",
        max_length=6,
        choices=Gender.choices,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name="status",
        related_name="ambassadors",
    )
    registration_date = models.DateField(
        verbose_name="registration date",
        auto_now_add=True,
    )
    user_comment = models.TextField(
        verbose_name="comment",
        null=True,
        blank=True,
    )
    clothing_size = models.CharField(
        verbose_name="clothing size",
        max_length=5,
        choices=ClothingSize.choices,
    )
    shoe_size = models.CharField(
        verbose_name="shoe size",
        max_length=5,
    )
    telegram_link = models.URLField(
        verbose_name="telegram link",
        max_length=50,
        unique=True,
    )
    email = models.EmailField(
        verbose_name="email",
        unique=True,
    )
    mobile_phone = models.CharField(
        verbose_name="mobile phone",
        max_length=20,
        unique=True,
    )
    blog_link = models.URLField(
        verbose_name="blog link",
        unique=True,
    )
    education = models.TextField(
        verbose_name="education",
    )
    work_place = models.TextField(
        verbose_name="work place",
    )
    education_target = models.TextField(
        verbose_name="education target",
        choices=EducationTarget.choices,
    )
    education_target_own = models.TextField(
        verbose_name="own target of education",
        null=True,
        blank=True,
    )
    onboarding_date = models.DateField(
        verbose_name="onboarding date",
        null=True,
        blank=True,
    )
    guide_date = models.DateField(
        verbose_name="date of completion of guide",
        null=True,
        blank=True,
    )
    comment_ambassador = models.TextField(
        verbose_name="ambassador's comment",
        null=True,
        blank=True,
    )
    program = models.ForeignKey(
        Program,
        on_delete=models.PROTECT,
        verbose_name="program",
        related_name="ambassadors",
    )
    targets = models.ManyToManyField(
        Target,
        related_name="ambassadors",
    )

    class Meta:
        verbose_name = "ambassador"
        verbose_name_plural = "ambassadors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Promocode(models.Model):
    """Модель промокода."""

    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        verbose_name="ambassador",
        related_name="promocodes",
    )
    value = models.CharField(
        verbose_name="promocode value",
        max_length=20,
    )
    replaced_at = models.DateField(
        verbose_name="replacement date",
        null=True,
        blank=True,
    )
    is_current = models.BooleanField(
        verbose_name="current",
        default=True,
    )

    class Meta:
        verbose_name = "promocode"
        verbose_name_plural = "promocodes"

    def __str__(self):
        return self.value


class Address(models.Model):
    """Модель адреса."""

    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.CASCADE,
        verbose_name="ambassador",
        related_name="addresses",
    )
    country = models.CharField(
        verbose_name="country",
        max_length=20,
    )
    city = models.CharField(
        verbose_name="city",
        max_length=20,
    )
    address = models.CharField(
        verbose_name="address",
        max_length=50,
    )
    code = models.CharField(
        verbose_name="postal code",
        max_length=10,
    )
    replaced_at = models.DateField(
        verbose_name="replacement date",
        null=True,
        blank=True,
    )
    is_current = models.BooleanField(
        verbose_name="current",
        default=True,
    )

    class Meta:
        verbose_name = "address"
        verbose_name_plural = "addresses"

    def __str__(self):
        return f"{self.country}, {self.city}, {self.address}"
