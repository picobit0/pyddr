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

# Этап 3
## Список изменений:
* ### Добавлен режим работы с локальным репозиторием
    Пример настроек режима работы:
    ```yaml
    repository-path: tests/repo/
    repository-mode: local
    ```

* ### Реализовано построение графа зависимостей
    Для указания глубины анализа используется настройка `max-depth` (0 - поиск только прямых зависимостей). При построении графа используется алгоритм обхода в ширину.

## Демонстрация работы:
* ### Построение графа зависимостей пакета Junit (режим удаленного репозитория):
```console
$ py grapher.py -c tests/junit-test.yaml
```
```
Fetched 1 package (depth 0)
Fetched 4 packages (depth 1)

MavenPackage(org.junit.jupiter/junit-jupiter-api - 6.0.0):
- MavenPackage(org.opentest4j/opentest4j - 1.3.0)
- MavenPackage(org.junit.platform/junit-platform-commons - 6.0.0)
- MavenPackage(org.apiguardian/apiguardian-api - 1.1.2)
- MavenPackage(org.jspecify/jspecify - 1.0.0)

MavenPackage(org.opentest4j/opentest4j - 1.3.0):
-

MavenPackage(org.junit.platform/junit-platform-commons - 6.0.0):
- MavenPackage(org.apiguardian/apiguardian-api - 1.1.2)
- MavenPackage(org.jspecify/jspecify - 1.0.0)

MavenPackage(org.apiguardian/apiguardian-api - 1.1.2):
-

MavenPackage(org.jspecify/jspecify - 1.0.0):
-
```

* ### Построение графа зависимостей пакета Junit (режим локального репозитория):
```console
$ py grapher.py -c tests/junit-test-local.yaml
```
```
Fetched 1 package (depth 0)
Fetched 4 packages (depth 1)

MavenPackage(org.junit.jupiter/junit-jupiter-api - 6.0.0):
- MavenPackage(org.opentest4j/opentest4j - 1.3.0)
- MavenPackage(org.junit.platform/junit-platform-commons - 6.0.0)
- MavenPackage(org.apiguardian/apiguardian-api - 1.1.2)
- MavenPackage(org.jspecify/jspecify - 1.0.0)

MavenPackage(org.opentest4j/opentest4j - 1.3.0):
-

MavenPackage(org.junit.platform/junit-platform-commons - 6.0.0):
- MavenPackage(org.apiguardian/apiguardian-api - 1.1.2)
- MavenPackage(org.jspecify/jspecify - 1.0.0)

MavenPackage(org.apiguardian/apiguardian-api - 1.1.2):
-

MavenPackage(org.jspecify/jspecify - 1.0.0):
-
```

# Этап 2
## Список изменений:
* ### Версия файла настроек обновлена до 0.2
    
    Новые настройки:
    * `package-group` - группа пакета
    * `package-version` - версия пакета

    Пример нового файла настроек:
    ```yaml
    %YAML 1.2
    ---
    version: '0.2'

    package-group: org.junit.jupiter
    package-name: junit-jupiter-api
    package-version: 6.0.0

    repository-path: https://repo.maven.apache.org/maven2/
    repository-mode: url
    output-path: output.png
    ascii-format: default
    max-depth: 15
    ```
* ### Добавлена поддержка формата пакетов Maven
    Пример получения прямых зависимостей из [Центрального Репозитория Maven](https://repo.maven.apache.org/maven2/):
    ```console
    $ py grapher.py -c config.yaml
    ```

    ```
    MavenPackage(org.junit.jupiter/junit-jupiter-api - 6.0.0):
    - MavenPackage(org.opentest4j/opentest4j - 1.3.0)
    - MavenPackage(org.junit.platform/junit-platform-commons - 6.0.0)
    - MavenPackage(org.apiguardian/apiguardian-api - 1.1.2)
    - MavenPackage(org.jspecify/jspecify - 1.0.0)
    ```
## Демонстрация работы:
### Получение зависимостей пакета Spring:
```console
$ py grapher.py -c tests/files/spring-test.yaml
```

```
MavenPackage(org.springframework.boot/spring-boot-starter-web - 3.5.4):
- MavenPackage(org.springframework.boot/spring-boot-starter - 3.5.4)
- MavenPackage(org.springframework.boot/spring-boot-starter-json - 3.5.4)
- MavenPackage(org.springframework.boot/spring-boot-starter-tomcat - 3.5.4)
- MavenPackage(org.springframework/spring-web - 6.2.9)
- MavenPackage(org.springframework/spring-webmvc - 6.2.9)
```

### Получение зависимостей пакета Junit:
```console
$ py grapher.py -c tests/files/junit-test.yaml
```

```
MavenPackage(org.junit.jupiter/junit-jupiter-api - 5.13.4):
- MavenPackage(org.opentest4j/opentest4j - 1.3.0)
- MavenPackage(org.junit.platform/junit-platform-commons - 1.13.4)
- MavenPackage(org.apiguardian/apiguardian-api - 1.1.2)
```

### Получение зависимостей пакета Scala:
```console
$ py grapher.py -c tests/files/scala-test.yaml
```

```
MavenPackage(org.scala-lang/scala3-library_3 - 3.7.3):
- MavenPackage(com.github.sbt/junit-interface - 0.13.3)
- MavenPackage(org.scala-lang/scala-library - 2.13.16)
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