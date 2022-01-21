from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, first_name, last_name, country, phone_number, home_address):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not password:
            raise ValueError(-('Password is required'))
        if not first_name:
            raise ValueError(-('Enter your first name'))
        if not last_name:
            raise ValueError(-('Enter your last name'))
        if not country:
            raise ValueError(-('country is required'))
        if not phone_number:
            raise ValueError(-('Enter an active number'))
        if not home_address:
            raise ValueError(-('Home address is required'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, 
        password=password,
        first_name = first_name,
        last_name = last_name,
        country = country,
        phone_number = phone_number,
        home_address = home_address
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self.db)
        return user