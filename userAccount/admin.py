from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userAccount.models import User


class AccountAdmin(UserAdmin):
	list_display = ('username','email','first_name','last_name','dob','mobile','date_joined', 'last_login', 'is_admin','is_staff','profilepic')
	search_fields = ('username','email',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(User, AccountAdmin)