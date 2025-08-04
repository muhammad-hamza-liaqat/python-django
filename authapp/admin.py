from django.contrib import admin
from authapp.models import User, UserWallet

class UserWalletInline(admin.StackedInline):
    model = UserWallet
    can_delete = False
    verbose_name_plural = 'Wallet'
    readonly_fields = ('id', 'created_at')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'name', 'is_active', 'is_staff']
    search_fields = ['email', 'name', 'phone']
    list_filter = ['is_active', 'is_staff', 'gender']
    inlines = [UserWalletInline]

@admin.register(UserWallet)
class UserWalletAdmin(admin.ModelAdmin):
    list_display = ['id', 'balance', 'created_at', 'user']
    readonly_fields = ['id', 'created_at']
    search_fields = ['id', 'user__email']
