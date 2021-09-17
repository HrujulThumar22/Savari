from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db.models.fields import DateTimeField
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
	def create_user(self,username, email,first_name,last_name,dob,mobile, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
            username=username,
			email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            mobile=mobile,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email,first_name,last_name,dob,mobile, password):
		user = self.create_user(
			username=username,
			email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            mobile=mobile,
            password=password,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser):
    email=models.EmailField(max_length=254,unique=True)
    username=models.CharField(max_length=50,unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    dob=models.DateField()
    phone_regex = RegexValidator(regex=r'^[0-9]{10}$', message="Phone number must be entered in the format: '999999999'. 10 digits allowed.")
    mobile = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email','first_name','last_name','dob','mobile']

    objects=UserManager()

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
