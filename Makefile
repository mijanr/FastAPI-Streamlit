# define variables

STREAMLIT_APP = app/Home.py
FASTAPI_APP = main

.PHONY: frontend backend run_app

frontend:
	streamlit run $(STREAMLIT_APP)

backend:
	uvicorn $(FASTAPI_APP):app --reload &

run_app: backend frontend 