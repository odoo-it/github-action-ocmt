FROM python:3 AS builder
RUN mkdir /app
RUN pip install --target=/app oca-maintainers-tools@git+https://github.com/OCA/maintainer-tools.git

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app
COPY . /app/
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]
