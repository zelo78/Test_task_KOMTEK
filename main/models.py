from django.db import models
from django.utils import timezone


class Resource(models.Model):
    identifier = models.CharField(
        max_length=64, unique=True,
        verbose_name="Идентификатор справочника"
    )
    name = models.CharField(
        max_length=1024,
        verbose_name="Наименование справочника"
    )
    short_name = models.CharField(
        max_length=128,
        verbose_name="Краткое наименование справочника"
    )
    description = models.TextField(verbose_name="Описание справочника")

    class Meta:
        verbose_name = "Справочник"
        verbose_name_plural = "Справочники"
        ordering = ['short_name']

    def __str__(self):
        return f'{self.short_name}, ID: {self.identifier}'


class ResourceVersion(models.Model):
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE, related_name='versions',
        verbose_name="Справочник"
    )
    version = models.CharField(
        max_length=32,
        verbose_name="Версия справочника"
    )
    valid_from = models.DateTimeField(default=timezone.now, verbose_name="Дата начала действия")

    class Meta:
        verbose_name = "Версия справочника"
        verbose_name_plural = "Версии справочника"
        ordering = ['-valid_from']
        constraints = [
            models.UniqueConstraint(
                fields=['resource', 'version'],
                name='unique_version_for_resource'
            ),
        ]

    def __str__(self):
        return f'Версия `{self.version}` для `{self.resource.short_name}` от {self.valid_from}'


class Record(models.Model):
    resource_version = models.ForeignKey(
        ResourceVersion, on_delete=models.CASCADE, related_name='records',
        verbose_name="Версия справочника"
    )
    code = models.CharField(
        max_length=64,
        verbose_name="Код элемента",
    )
    value = models.CharField(
        max_length=256,
        verbose_name="Значение элемента"
    )

    class Meta:
        verbose_name = "Элемент справочника"
        verbose_name_plural = "Элементы справочника"
        ordering = ['code']

    def __str__(self):
        return f'{self.code}: {self.value} из справочника {self.resource_version.resource.short_name}'
