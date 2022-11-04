FROM python:3.10-slim-buster
COPY . .
RUN pip install -r requirements.txt
CMD [ "python3", "-m" , "flask", "--app", "weight_api/weight.py", "run", "--host=0.0.0.0"]
# CMD ["python3", "-m" , "flask", "--app", "weight_api/weight.py", "run"]
