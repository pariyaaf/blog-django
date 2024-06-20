from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='updated_%(class)s_set', on_delete=models.SET_NULL, null=True, blank=True)
    deleted_by = models.ForeignKey(User, related_name='deleted_%(class)s_set', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

    def soft_delete(self, deleter_id):
        self.deleted_at = timezone.now()
        self.deleted_by_id = deleter_id
        self.save()

    def restore(self, updater_id):
        self.deleted_at = None
        self.updated_at = timezone.now()
        self.updated_by_id = updater_id
        self.save()

    def update_record(self, updater_id):
        self.updated_at = timezone.now()
        self.updated_by_id = updater_id
        self.save()

    @classmethod
    def get(cls, ident, with_deleted=False):
        if with_deleted:
            return cls.objects.filter(id=ident).first()
        return cls.objects.filter(id=ident, deleted_at__isnull=True).first()

    @classmethod
    def get_or_404(cls, ident, with_deleted=False):
        if with_deleted:
            return cls.objects.get(id=ident)
        return cls.objects.get(id=ident, deleted_at__isnull=True)

    @classmethod
    def filter(cls, *args, with_deleted=False, **kwargs):
        if with_deleted:
            return cls.objects.filter(*args, **kwargs)
        return cls.objects.filter(*args, **kwargs).filter(deleted_at__isnull=True)

    @classmethod
    def filter_by(cls, with_deleted=False, **kwargs):
        query = cls.objects.filter(**kwargs)
        if not with_deleted:
            query = query.filter(deleted_at__isnull=True)
        return query

    @classmethod
    def all(cls, with_deleted=False):
        if with_deleted:
            return cls.objects.all()
        return cls.objects.filter(deleted_at__isnull=True)
