@echo off

echo.
echo -- config path test --
py ../grapher.py -c files/wrong-config.yaml

echo.
echo -- yaml format test --
py ../grapher.py -c files/yaml-test.yaml

echo.
echo -- version test --
py ../grapher.py -c files/version-test.yaml

echo.
echo -- package test --
py ../grapher.py -c files/package-test.yaml

echo.
echo -- repo mode test --
py ../grapher.py -c files/repo-mode-test.yaml

echo.
echo -- ascii format test --
py ../grapher.py -c files/ascii-format-test.yaml

echo.
echo -- depth test --
py ../grapher.py -c files/depth-test.yaml

echo.
pause