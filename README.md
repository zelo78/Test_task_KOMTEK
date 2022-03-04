# Комтек ТЗ Python

Разработать сервис терминологии и REST API к нему.



## Описание

Сервис терминологии оперирует ниже перечисленными сущностями.



Сущность "Справочник" содержит следующие атрибуты:

- идентификатор справочника (глобальный и не зависит от версии)
- наименование
- короткое наименование
- описание
- версия (тип: строка,  не может быть пустойуникальная в пределах одного справочника)
- дата начала действия справочника этой версии



Сущность "Элемент справочника"

- идентификатор
- родительский идентификатор
- код элемента (тип: строка, не может быть пустой)
- значение элемента (тип: строка, не может быть пустой)



API должно предоставлять следующие методы:

- получение списка справочников.
- получение списка справочников, актуальных на указанную дату.
- получение элементов заданного справочника текущей версии
- валидация элементов заданного справочника текущей версии
- получение элементов заданного справочника указанной версии
- валидация элемента заданного справочника по указанной версии

В API должен быть предусмотрен постраничный вывод результата (данные должны возвращаться частями по 10 элементов).

К сервису должна иметься GUI административной части, с помощью которой можно добавлять новые справочники, новые версии справочников, указывать дату начала действия и наполнять справочники элементами.

Некоторые подробности намеренно не указаны. Оставляем их на ваше усмотрение.

## Технологии

* Python >= 3.8

## Критерии оценки

* Выполнение требований ТЗ.
* Читаемость программного кода (отступы, разделители и т.д.).
* Адекватность выбора подхода: технологий, конструкций языка.
* Наличие в коде программы комментариев и их содержание.
* Невозможность внесения некорректных данных пользователем.
* Наличие ошибок в программе (не ожиданное поведение, не корректные выходные данные), в том числе возникающих при непредусмотренных действиях пользователей.
* Удобство использования (логичность элементов API и GUI-интерфейса).
* Наличие описания разработанного API с примерами.

## Размещение

* Проект должен быть размещён на GitHub или аналогичном сервисе.

## Контакты

Telegram: @KonstantinShpilko — Константин Шпилько.



