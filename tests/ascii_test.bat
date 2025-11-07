@echo off

echo.
echo -- Ascii tree test --
py ../grapher.py -c files/ascii-tree-test.yaml

echo.
echo -- Ascii list test --
py ../grapher.py -c files/ascii-list-test.yaml

echo.
pause