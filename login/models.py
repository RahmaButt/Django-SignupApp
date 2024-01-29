

# class user(models.Model):
#     email = models.EmailField(unique=True)
# Create your models here.

# class UserManager(BaseUserManager):

#     def create_user(self, username, email, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         user = self.model(
#             username=username,
#             email=self.normalize_email(email),
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self, username, email, password):
#         user = self.create_user(
#             username,
#             email,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser):
#     username = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#     def str__(self):

#         return self.username