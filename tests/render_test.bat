@echo off

echo.
echo -- Spring graph render test --
py ../grapher.py -c files/spring-test.yaml

echo.
echo -- Junit graph render test --
py ../grapher.py -c files/junit-test.yaml

echo.
echo -- Scala graph render test --
py ../grapher.py -c files/scala-test.yaml

echo.
pause