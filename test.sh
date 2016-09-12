cd $(dirname "$0")
pwd
rm *.pyc

python -m pytest -s *test.py
