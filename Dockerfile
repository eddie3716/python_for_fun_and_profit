FROM python:3.9.9-alpine3.14

RUN addgroup --gid 1000 app
RUN adduser -D --uid 1000 --ingroup app --home /app --shell /bin/sh app

ENV FLASK_APP=gitprofiles
ENV FLASK_ENV=development

COPY /app /app

WORKDIR /app

RUN pip install --upgrade pip && pip install --editable .

RUN apk add --update --no-cache openssl

RUN openssl req -x509 -newkey rsa:4096 -nodes -subj "/C=US/ST=Colorado/L=Broomfield/O=SomeDude/ON=somewebsite.net" -out /app/cert.pem -keyout /app/key.pem -days 365

RUN apk del openssl

RUN chown -R app:app /app && \
    rm -rf /var/cache/apk/*

USER app:app

EXPOSE 443

CMD [ "flask", "run", "--host=0.0.0.0", "--port=443", "--cert=/app/cert.pem", "--key=/app/key.pem" ]