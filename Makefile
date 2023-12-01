setup:
	pip install -r requirements.txt
	cp .env.template .env

report:
	python3 generate-report.py