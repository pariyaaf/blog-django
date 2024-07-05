from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from posts.models import PostModel

class Command(BaseCommand):  # تغییر این خط از Commad به Command
    help = 'Create default groups and assign permissions'

    def handle(self, *args, **kwargs):
        # create admin group
        admins_group, created = Group.objects.get_or_create(name='Admins')
        
        # add permissions to admin group
        admins_permissions = Permission.objects.all()
        admins_group.permissions.set(admins_permissions)
        admins_group.save()

        # create user group
        users_group, created = Group.objects.get_or_create(name='Users')

        # get content types for post models
        post_content_type = ContentType.objects.get_for_model(PostModel)

        # add specific permissions to user group
        user_permissions = Permission.objects.filter(
            content_type__in=[ post_content_type])
        
        users_group.permissions.set(user_permissions)
        users_group.save()

        self.stdout.write(self.style.SUCCESS('Successfully created groups and assigned permissions'))
