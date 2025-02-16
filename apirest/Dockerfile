FROM python:latest


WORKDIR /app


COPY . /app


RUN python3 -m venv /app/venv


RUN /app/venv/bin/pip install --no-cache-dir -r /app/requirements.txt


EXPOSE 8000


CMD ["/app/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
