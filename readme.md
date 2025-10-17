# Конфигурационное управление/Практика 2
## Низамутдинов Степан, ИКБО-20-24
### Вариант 16

## Запуск
Запуск приложения с настройками по умолчанию (файл config.yaml):
```
py grapher.py
```

Запуск приложения с заданным файлом настроек:
```
py grapher.py --config <config-file.yaml>
```

```
py grapher.py -c <config-file.yaml>
```

# Этап 1
## Список изменений:
* ### Добавлено считывание настроек из файла
    
    Доступные настройки:
    * `verision` - версия файла настроек
    * `package-name` - название пакета
    * `repository-path` - путь к репозиторию
    * `repository-mode` - режим работы с репозиторием (`local` | `url`)
    * `output-path` - путь к файлу вывода
    * `ascii-format` - формат вывода в ascii-дереве (`default`)
    * `max-depth` - максимальная глубина анализа зависимостей
    
    Пример файла настроек:
    ```yaml
    %YAML 1.2
    ---
    version: '0.1'
    package-name: package
    repository-path: repo.txt
    repository-mode: local
    output-path: output.png
    ascii-format: default
    max-depth: 15
    ```

## Демонстрация работы:
### Пример обычного запуска:
```console
$ py grapher.py
```
```
Version: 0.1
Package name: package
Repository path: repo.txt
Repository mode: local
Output path: output.png
Ascii format: default
Max depth: 15
```

### Примеры обработки ошибок:
* Ошибка в синтаксисе файла
    ```console
    $ py grapher.py -c wrong-config.yaml
    ```
    ```
    Error! Config file is not a valid yaml file
    ```

* Ошибка в параметре максимальной глубины

    ```console
    $ py grapher.py -c depth-test.yaml
    ```
    ```
    Error! Invalid max depth: -1
    ```

* Несоответствующая версия файла

    ```console
    $ py grapher.py -c version-test.yaml
    ```
    ```
    Error! Config version mismach (999.0 != 0.1)
    ```