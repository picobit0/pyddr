@echo off

echo.
echo -- Remote Junit dependencies test --
py ../grapher.py -c files/junit-test.yaml

echo.
echo -- Local Junit dependencies test --
py ../grapher.py -c files/junit-test-local.yaml

echo.
echo -- Local Spring dependencies test --
py ../grapher.py -c files/spring-test-local.yaml

echo.
pause