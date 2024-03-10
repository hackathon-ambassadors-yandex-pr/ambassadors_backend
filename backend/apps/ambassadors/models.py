from apps.ambassadors.choice_classes import (
    AmbassadorStatus,
    ClothingSize,
    EducationTarget,
    Gender,
)
from django.db import models


class Program(models.Model):
    """Модель программы."""

    name = models.CharField(
        "name",
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = "program"
        verbose_name_plural = "programs"

    def __str__(self):
        return self.name


class Target(models.Model):
    """Модель цели."""

    name = models.TextField(
        "name",
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
        "first name",
        max_length=20,
    )
    middle_name = models.CharField(
        "middle name",
        max_length=20,
    )
    last_name = models.CharField(
        "last name",
        max_length=20,
    )
    gender = models.CharField(
        "gender",
        max_length=6,
        choices=Gender.choices,
    )
    status = models.CharField(
        "status",
        max_length=20,
        choices=AmbassadorStatus.choices,
        default=AmbassadorStatus.NEW,
    )
    registration_date = models.DateField(
        "registration date",
        auto_now_add=True,
    )
    user_comment = models.TextField(
        "comment",
        blank=True,
    )
    clothing_size = models.CharField(
        "clothing size",
        max_length=5,
        choices=ClothingSize.choices,
    )
    shoe_size = models.CharField(
        "shoe size",
        max_length=5,
    )
    telegram_link = models.URLField(
        "telegram link",
        max_length=50,
        unique=True,
    )
    email = models.EmailField(
        "email",
        unique=True,
    )
    mobile_phone = models.CharField(
        "mobile phone",
        max_length=20,
        unique=True,
    )
    blog_link = models.URLField(
        "blog link",
        unique=True,
    )
    education = models.TextField(
        "education",
    )
    work_place = models.TextField(
        verbose_name="work place",
    )
    education_target = models.TextField(
        "education target",
        choices=EducationTarget.choices,
    )
    education_target_own = models.TextField(
        "own target of education",
        blank=True,
    )
    onboarding_date = models.DateField(
        "onboarding date",
        null=True,
        blank=True,
    )
    guide_date = models.DateField(
        "date of completion of guide",
        null=True,
        blank=True,
    )
    comment_ambassador = models.TextField(
        "ambassador's comment",
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
        verbose_name="targets",
        related_name="ambassadors",
    )

    class Meta:
        verbose_name = "ambassador"
        verbose_name_plural = "ambassadors"
        constraints = (
            models.CheckConstraint(
                check=(
                    (
                        models.Q(education_target=EducationTarget.OTHER)
                        & ~models.Q(education_target_own="")
                    )
                    | (
                        ~models.Q(education_target=EducationTarget.OTHER)
                        & models.Q(education_target_own="")
                    )
                ),
                name="education_target_and_education_target_own",
                violation_error_message=(
                    f"if education_target = {EducationTarget.OTHER.name}, "
                    f"then education_target_own field cannot be empty, and vice versa."
                ),
            ),
        )

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
        "promocode value",
        max_length=20,
    )
    replaced_at = models.DateField(
        "replacement date",
        null=True,
        blank=True,
    )
    is_current = models.BooleanField(
        "current",
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
        "country",
        max_length=20,
    )
    city = models.CharField(
        "city",
        max_length=20,
    )
    address = models.CharField(
        "address",
        max_length=100,
    )
    code = models.CharField(
        "postal code",
        max_length=10,
    )
    replaced_at = models.DateField(
        "replacement date",
        null=True,
        blank=True,
    )
    is_current = models.BooleanField(
        "current",
        default=True,
    )

    class Meta:
        verbose_name = "address"
        verbose_name_plural = "addresses"

    def __str__(self):
        return f"{self.country}, {self.city}, {self.address}"
