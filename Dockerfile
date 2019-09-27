FROM python:3.7-alpine

WORKDIR "/code"
COPY ./db.sqlite ./
COPY ./requirements.txt ./
RUN pip install -Ur requirements.txt
COPY . .

ENTRYPOINT ["python"]
CMD ["manage.py", "runserver"]