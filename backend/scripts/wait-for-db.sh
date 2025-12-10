#!/bin/sh

#Ajuste para 
set -e

echo "Aguardando banco de dados ($DB_HOST:5432)..."

while ! nc -z $DB_HOST 5432; do
  sleep 0.5
done

echo "Banco de dados disponível! Iniciando aplicação..."

exec "$@"