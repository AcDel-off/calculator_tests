\# Calculator CI/CD Tests



Проект автоматических тестов для класса `Calculator` с интеграцией в GitHub Actions.



\## Структура проекта



\- `calculator.py` — класс калькулятора

\- `test\_calculator.py` — модульные тесты (pytest)

\- `.github/workflows/run-tests.yml` — конфигурация CI/CD



\## Запуск тестов локально



```bash

pip install -r requirements.txt

pytest -v

