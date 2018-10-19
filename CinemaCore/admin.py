from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from CinemaCore.forms import ClientChangeForm, ClientCreationForm, EmployeeChangeForm, EmployeeCreationForm
from CinemaCore.models import Client, Employee, Actor, Movie, MovieCrew, Token, User, CinemaRoom, MovieFunction


class ClientAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = ClientChangeForm
    add_form = ClientCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'username', 'email',)
    # readonly_fields = ('activation_token',)
    # list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Account Info', {'fields': ('avatar', 'username', 'is_special_client', 'deleted', 'is_active')}),
        # ('tokens', {'fields': ('token',)}),
        # ('Permissions', {'fields': ('',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Account Info', {'fields': ('avatar', 'username', 'is_special_client', 'deleted', 'is_active')}),
        # ('Tokens', {'fields': ('token',)}),
        # ('Permissions', {'fields': ('',)}),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ()


class EmployeeAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = EmployeeChangeForm
    add_form = EmployeeCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'username', 'email',)
    # readonly_fields = ('activation_token',)
    # list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Account Info', {'fields': ('avatar', 'username', 'administrator', 'deleted', 'is_active')}),
        # ('tokens', {'fields': ('token',)}),
        # ('Permissions', {'fields': ('',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Account Info', {'fields': ('avatar', 'username', 'administrator', 'deleted', 'is_active')}),
        # ('tokens', {'fields': ('token',)}),
        # ('Permissions', {'fields': ('',)}),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ()


class TokenAdmin(admin.ModelAdmin):
    readonly_fields = ('value', 'expiry_date', 'user')
    # readonly_fields = ('activation_token',)

    def has_add_permission(self, request):
        return False


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'release_date',)
    readonly_fields = ('slug', 'moviedb_id')


class UserAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

# Now register the new UserAdmin...
admin.site.register(Client, ClientAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieCrew)
admin.site.register(Actor)
admin.site.register(Token, TokenAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(CinemaRoom)
admin.site.register(MovieFunction)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
