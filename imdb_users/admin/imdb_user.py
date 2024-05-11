from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

imdb_user_fieldsets = (
    (_('Personal info'), {'fields': ('first_name', 'last_name')}),
    (
        _('Permissions'),
        {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        },
    ),
    (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
)

class ImdbUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        *imdb_user_fieldsets,
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
        *imdb_user_fieldsets,
    )
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
