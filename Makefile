install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python3 -m pytest -vv --cov=main --cov=calCLI --cov=mylib test_*.py

format:	
	black *.py mylib/*.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*?py *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin 637423227526.dkr.ecr.ap-southeast-2.amazonaws.com
	docker build -t logistics .
	docker tag logistics:latest 637423227526.dkr.ecr.ap-southeast-2.amazonaws.com/logistics:latest
	docker push 637423227526.dkr.ecr.ap-southeast-2.amazonaws.com/logistics:latest
	
all: install lint test format deploy