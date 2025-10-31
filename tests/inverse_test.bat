@echo off

echo.
echo -- Junit 3.8.1 inverse dependencies --
py ../grapher.py -c files/spring-local-full.yaml < files/input1.txt

echo.
echo -- Log4j 1.2.15 inverse dependencies --
py ../grapher.py -c files/spring-local-full.yaml < files/input2.txt

echo.
pause