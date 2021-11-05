#!/usr/bin/env bash
set -e

source venv/bin/activate

pylint_flag=false
mypy_flag=false
flake8_flag=false
test_flag=false
coverage_flag=false

while test $# -gt 0; do
    if [ "$1" == linting ]; then
        pylint_flag=true
        mypy_flag=true
        flake8_flag=true
    elif [ "$1" == "pylint" ]; then
        pylint_flag=true
    elif [ "$1" == flake8 ]; then
        flake8_flag=true
    elif [ "$1" == mypy ]; then
        mypy_flag=true
    elif [ "$1" == coverage ]; then
        coverage_flag=true
    elif [ "$1" == each ]; then
        pylint_flag=true
        mypy_flag=true
        flake8_flag=true
        test_flag=true
    fi
    shift
done

if [[ $pylint_flag == true ]]; then
    python3 -m pylint --max-line-length=120 --disable=all --enable=simplifiable-if-statement,redefined-variable-type,invalid-name,global-statement hse-SE-course tests
fi

if [[ $mypy_flag == true ]]; then
    python3 -m mypy --ignore-missing-imports tests
fi

if [[ $flake8_flag == true ]]; then
    python3 -m flake8 --max-line-length=120 tests
fi

if [[ $test_flag == true ]]; then
    python3 -m pytest tests/unit_tests.py
fi

if [[ $coverage_flag == true ]]; then
    coverage run -m pytest tests/unit_tests.py
    coverage report --fail-under 90
fi
