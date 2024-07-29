# 2022-MAI-Backend-M_Ruzhickiy
## Описание ##
### data - статические файлы
### nginx.conf - настройки nginx ###
### myapp.py - WSGI-приложение ###
### requirements.txt - зависимости ###
### ###


## Статика ##
### wrk -t12 -c400 -d30s http://localhost/public/index.html ###

### Running 30s test @ http://localhost/public/index.html 12 threads and 400 connections Thread Stats Avg Stdev Max +/- Stdev Latency 48.82ms 86.21ms 2.00s 98.75% Req/Sec 474.33 369.18 3.00k 72.48% 124281 requests in 30.09s, 29.51MB read Socket errors: connect 0, read 0, write 0, timeout 891 Requests/sec: 4130.93 Transfer/sec: 0.98MB ###

## Gunicorn через nginx ##
### wrk -t12 -c400 -d30s http://localhost/backend/ ###

### Running 30s test @ http://localhost/backend/ 12 threads and 400 connections Thread Stats Avg Stdev Max +/- Stdev Latency 396.10ms 59.78ms 611.88ms 82.70% Req/Sec 84.97 68.00 323.00 73.39% 28432 requests in 30.10s, 4.91MB read Socket errors: connect 0, read 205683, write 0, timeout 0 Requests/sec: 944.63 Transfer/sec: 166.97KB ###

## Gunicorn напрямую ##
 ### wrk -t12 -c400 -d30s http://localhost:8000 ###

### Running 30s test @ http://localhost:8000 12 threads and 400 connections Thread Stats Avg Stdev Max +/- Stdev Latency 186.86ms 52.11ms 350.73ms 84.04% Req/Sec 189.00 102.35 333.00 54.89% 63284 requests in 30.10s, 9.84MB read Requests/sec: 2102.55 Transfer/sec: 334.72KB ###
 
# Лабораторные работы Программная инженерия #


[Первая лабораторная работа](https://github.com/fe3nder/2022-MAI-Backend-M_Ruzhickiy--first-/tree/master/Lab1)
[Вторая лабораторная работа](https://github.com/fe3nder/2022-MAI-Backend-M_Ruzhickiy--first-/tree/master/Lab2)
