@echo off

echo.
echo -- config path test --
py ../grapher.py -c wrong-config.yaml

echo.
echo -- yaml format test --
py ../grapher.py -c yaml-test.yaml

echo.
echo -- version test --
py ../grapher.py -c version-test.yaml

echo.
echo -- package test --
py ../grapher.py -c package-test.yaml

echo.
echo -- repo path test --
py ../grapher.py -c repo-path-test.yaml

echo.
echo -- repo mode test --
py ../grapher.py -c repo-mode-test.yaml

echo.
echo -- output path test --
py ../grapher.py -c out-path-test.yaml

echo.
echo -- ascii format test --
py ../grapher.py -c ascii-format-test.yaml

echo.
echo -- depth test --
py ../grapher.py -c depth-test.yaml

echo.
echo -- normal test --
py ../grapher.py -c ../config.yaml

echo.
pause