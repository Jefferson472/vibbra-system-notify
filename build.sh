#!/usr/bin/env bash
# exit on error
set -o errexit


echo "-----> Poetry install"
poetry install --without dev --no-root --no-interaction
echo "-----> Poetry done"

echo "-----> Running collectstatic"
poetry run python src/manage.py collectstatic --no-input

echo "-----> Running manage.py migrate"
poetry run python src/manage.py migrate --noinput


echo "-----> Post-compile done 🎈✨🎉"