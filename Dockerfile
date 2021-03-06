FROM python:3.9
WORKDIR /app
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip && pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
COPY . ./
CMD ["python", "app.py"]
