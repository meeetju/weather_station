coverage run --source=./ -m unittest discover -s _tests/
coverage report -m
coverage html -d coverage_html
start coverage_html/index.html
cmd /k