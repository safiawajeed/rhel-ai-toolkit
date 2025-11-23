FROM python:3.9-slim
WORKDIR /app
COPY dist/*.whl /tmp/
RUN pip install /tmp/*.whl
ENTRYPOINT ["rhel-ai"]
