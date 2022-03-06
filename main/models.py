from datetime import date

from django.db import models


class ResourceIdentifier(models.Model):
    value = models.CharField(
        max_length=64, unique=True,
        verbose_name="идентификатор справочника"
    )

    class Meta:
        verbose_name = "идентификатор справочника"
        verbose_name_plural = "идентификаторы справочников"
        ordering = ['value']

    def __str__(self):
        return f'Идентификатор {self.value}, ID: {self.id}'


class Resource(models.Model):
    name = models.CharField(
        max_length=1024,
        verbose_name="наименование справочника"
    )
    short_name = models.CharField(
        max_length=128,
        verbose_name="краткое наименование справочника"
    )
    description = models.TextField(verbose_name="описание справочника")
    version = models.CharField(
        max_length=32,
        verbose_name="версия справочника"
    )
    valid_from = models.DateField(default=date.today, verbose_name="дата начала действия")
    identifier = models.ForeignKey(
        ResourceIdentifier, on_delete=models.CASCADE, related_name='versions',
        verbose_name="идентификатор"
    )

    class Meta:
        verbose_name = "Справочник"
        verbose_name_plural = "Справочники"
        ordering = ['identifier', '-valid_from']
        constraints = [
            models.UniqueConstraint(
                fields=['identifier', 'version'],
                name='unique_version_for_identifier'
            ),
        ]

    def __str__(self):
        return f'Справочник #{self.identifier.value} `{self.short_name}`, версия `{self.version}` от {self.valid_from}'


class Record(models.Model):
    code = models.CharField(
        max_length=64,
        verbose_name="код элемента",
    )
    value = models.CharField(
        max_length=256,
        verbose_name="значение элемента"
    )
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE, related_name='records',
        verbose_name="справочник"
    )

    class Meta:
        verbose_name = "Элемент справочника"
        verbose_name_plural = "Элементы справочника"
        ordering = ['code']

    def __str__(self):
        return f'{self.code}: {self.value} из справочника {self.resource.short_name}'
