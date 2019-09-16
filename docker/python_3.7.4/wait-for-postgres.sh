#!/usr/bin/env bash
# wait-for-postgres.sh

# exit if any command in the script returns non-zero code
set -e

host=$1
shift
cmd="$@"

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -c '\q'
do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done

>&2 echo "Postgres is up - executing command"
python3 manage.py makemigrations core
python3 manage.py migrate core
exec $cmd
