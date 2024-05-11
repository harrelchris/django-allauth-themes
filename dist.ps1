python -m pip install --upgrade build pip setuptools twine wheel
python -m build
python -m twine upload --repository pypi dist/*
Remove-Item -Recurse -Force dist
Remove-Item -Recurse -Force django_allauth_themes.egg-info
