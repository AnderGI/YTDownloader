run:
	uvicorn src.apps.backoffice.backend.main:app --reload &
unit:
	PYTHONPATH=. pytest
e2e:
	PYTHONPATH=. behave
