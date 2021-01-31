FROM python:3.7
COPY . /app
WORKDIR /app
ENV STRINGS ab,xyz,ab,abc,def
ENTRYPOINT ["python", "-m", "main"]
CMD []