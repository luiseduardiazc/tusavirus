#!/usr/bin/env bash
echo "run test for utilities .."
./manage.py test utilities/

echo "run test front-end .."

./manage.py test tests/test_front_end.py

#kill -9 "$(lsof -t -i:8000)"
