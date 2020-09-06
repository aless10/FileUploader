FROM python:3.8 as base
COPY requirements.txt /
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt
FROM python:3.8
COPY --from=base /wheels /wheels
COPY --from=base requirements.txt .

ENV PYTHONBUFFERED=1

RUN pip install --no-cache /wheels/*
WORKDIR /app
COPY ./file_uploader /app/file_uploader
COPY ./scripts /app/scripts
COPY .env /app

RUN mv ../requirements.txt .
RUN useradd uploader_dev
RUN chown -R uploader_dev:uploader_dev /app
RUN chmod +x /app/scripts/start_file_uploader.sh
RUN chown -R uploader_dev:uploader_dev /app

USER uploader_dev

CMD ["/app/scripts/start_file_uploader.sh"]
