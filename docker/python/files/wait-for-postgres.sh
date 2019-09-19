#!/usr/bin/env bash
# wait-for-postgres.sh

# exit if any command in the script returns non-zero code
set -e

host=$1
shift
cmd="$@"

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -U django -c '\q'
do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

>&2 echo "Postgres is up - executing command"
python manage.py makemigrations core &>> migration.log
python manage.py migrate core &>> migration.log
PGPASSWORD=$POSTGRES_PASSWORD pg_restore -c -h "$host" -U django -d django /postgres_bk.tar
exec $cmd
