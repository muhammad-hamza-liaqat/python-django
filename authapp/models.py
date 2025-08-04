from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# user_wallet model
class UserWallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField(_("Balance"), max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    def __str__(self):
        return f"Wallet {self.id} - {self.balance}"

# custom_user manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, phone, gender, password=None):
        if not email:
            raise ValueError(_("Users must have an email address"))
        email = self.normalize_email(email)
        wallet = UserWallet.objects.create()
        user = self.model(email=email, name=name, phone=phone, gender=gender, wallet=wallet)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, gender, password):
        user = self.create_user(email, name, phone, gender, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# custom_user model
class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('male', _('Male')),
        ('female', _('Female')),
        ('other', _('Other')),
    )

    email = models.EmailField(_("Email"), unique=True)
    name = models.CharField(_("Name"), max_length=255)
    phone = models.CharField(_("Phone"), max_length=15, unique=True)
    gender = models.CharField(_("Gender"), max_length=10, choices=GENDER_CHOICES)
    is_active = models.BooleanField(_("Is active"), default=True)
    is_staff = models.BooleanField(_("Is staff"), default=False)
    is_admin = models.BooleanField(_("Is admin"), default=False)
    wallet = models.OneToOneField(UserWallet, verbose_name=_("Wallet"), on_delete=models.CASCADE, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'gender']

    def __str__(self):
        return self.email
