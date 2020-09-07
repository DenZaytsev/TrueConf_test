Создаем образ.
---
$ docker build .

Собираем образ командой:
---


$ sudo docker-compose build


Как только образ будет собран, запускаем контейнер:
---


$ docker-compose up -d


В браузере http://localhost:8000/api/v1/



Проверьте наличие ошибок в журналах, если это не работает, через команду:
---


docker-compose logs -f
