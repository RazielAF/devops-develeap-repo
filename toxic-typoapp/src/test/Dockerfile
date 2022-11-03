FROM python:2.7
WORKDIR /test
COPY . .
RUN pip install -r requirments.txt
ENTRYPOINT ["python", "e2e_test.py", "35.176.222.34:2137"]