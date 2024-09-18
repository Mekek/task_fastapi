Запуск через Docker
1. Сборка Docker-образа
Соберите Docker-образ с вашим приложением:

bash
Copy code
docker build -t my_fastapi_app .
2. Запуск контейнера
Запустите контейнер с вашим приложением:

bash
Copy code
docker run -d -p 8000:8000 my_fastapi_app
Теперь приложение будет доступно по адресу http://127.0.0.1:8000.

Тестирование
Запустите тесты с помощью pytest:

bash
Copy code
pytest
Использование
Чтобы отправить POST-запрос для расчета депозита, используйте следующий формат:

bash
Copy code
POST /calculate
Пример тела запроса:
json
Copy code
{
  "date": "31.01.2021",
  "periods": 3,
  "amount": 10000,
  "rate": 6
}
Пример успешного ответа:
json
Copy code
{
  "31.01.2021": 10050.0,
  "28.02.2021": 10100.25,
  "31.03.2021": 10150.75
}