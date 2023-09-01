from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


class Ticket(models.Model):
    title = models.fields.CharField(max_length=128, verbose_name="Titre")
    description = models.fields.TextField(max_length=2048, blank=True, verbose_name="Description")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(max_length=100, null=True, blank=True, verbose_name="Image")
    time_created = models.DateTimeField(auto_now_add=True)
    review = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.title}"


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, related_name="Ticket")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name="Note"
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128, verbose_name="Titre")
    body = models.TextField(max_length=8192, blank=True, verbose_name="Commentaire")
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.headline}"


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following",
    )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by", verbose_name="Taper les premières lettres du nom d'utilisateur"
    )

    def __str__(self):
        return f"{self.followed_user}"

    class Meta:
        # garantit que nous n’obtenons pas plusieurs instances UserFollows
        # pour les paires "utilisateur-utilisateur_suivi" uniques
        unique_together = ("user", "followed_user")
        