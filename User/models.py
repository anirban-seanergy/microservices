from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser
from User.managers import UserManager

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    phone = models.CharField(max_length=32, blank = True, validators=[MinLengthValidator(10)])
    email = models.EmailField(max_length=64, db_index=True, unique=True)
    last_login = models.DateTimeField(null=True, blank=True)
    all_regions = models.BooleanField(db_index=True, default=False)
    is_deleted = models.BooleanField(default=False)
    auth0_user_id = models.CharField(max_length = 64, blank=True, null=True)
    auth0_connection_name = models.CharField(max_length = 64, blank=True, null=True)
    password = models.CharField(max_length=140, default='password@123')
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
    objects = UserManager()
    

    class Meta:
        db_table = "models_mgmt_user"

# Before creating superuser for the first time the foreign key in the database shall be populated with initial data,
# otherwise the user cannot be created. And for initial migration the line `django.contrib.admin,` and `path('admin/', admin.site.urls),`
# from the INSTALLED_APPS and root urls .py shall be commented then migrated, then the lines shall be uncommented.

class UserRegions(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'models_mgmt_user_regions' 
