rm -rf dist/discosub*
if [ -z "$1" ]
then
	echo "deploying on pypi production server"
	python setup.py sdist bdist_wheel
 	twine register dist/*.whl
 	twine upload dist/discosub-*
else
	echo "deploying on pypi testing server"
	python setup.py sdist bdist_wheel
 	twine register -r test dist/*.whl
 	twine upload -r test dist/discosub-*
fi
