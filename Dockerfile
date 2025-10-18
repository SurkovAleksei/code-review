FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade setuptools
RUN chmod 775 . .

COPY main.py database.py parser.py /app/
COPY templates /app/templates/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]

