from django.contrib import admin
from django.utils.html import mark_safe

from theses.models import Role

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class RoleForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Role
        fields = '__all__'


class MyRoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['id', 'name']
    list_filter = ['id', 'name']
    form = RoleForm


admin.site.register(Role, MyRoleAdmin)
