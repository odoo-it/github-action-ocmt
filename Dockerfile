FROM python:3
RUN pip install oca-maintainers-tools@git+https://github.com/OCA/maintainer-tools.git
COPY . /app/
WORKDIR /app
CMD ["/app/main.py"]
