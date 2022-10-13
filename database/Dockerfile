FROM postgres:12.12-alpine
ENV POSTGRES_PASSWORD=ITBA
ENV POSTGRES_USER=aalonso
ENV POSTGRES_DB=database_pizza
COPY ddl.sql /docker-entrypoint-initdb.d/ddl.sql