@echo off

echo.
echo -- Spring maven package --
py ../grapher.py -c files/spring-test.yaml

echo.
echo -- Junit maven package --
py ../grapher.py -c files/junit-test.yaml

echo.
echo -- Scala maven package --
py ../grapher.py -c files/scala-test.yaml

echo.
pause