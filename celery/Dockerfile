#
# Builder (multi stage build)
#
FROM python:3.8-buster as builder

WORKDIR /opt/app

ENV ACCEPT_EULA=Y
ENV PATH="${PATH}:/opt/mssql-tools/bin"

RUN apt -y update
RUN apt install -y gnupg gnupg1 gnupg2
RUN curl https://packages.microsoft.com/keys/microsoft.asc > microsoft.asc
RUN apt-key add microsoft.asc
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt -y update && apt -y install msodbcsql17 mssql-tools postgresql-client-common postgresql-client unixodbc-dev

COPY requirements.txt /opt/app/
RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r /opt/app/requirements.txt

#
# Runner
#
FROM python:3.8-slim-buster as runner

WORKDIR /opt/app

ENV ACCEPT_EULA=Y
ENV PATH="${PATH}:/opt/mssql-tools/bin"

RUN apt update
RUN apt install -y gnupg gnupg1 gnupg2

COPY --from=builder /opt/app/microsoft.asc /opt/app/microsoft.asc
COPY --from=builder /etc/apt/sources.list.d/mssql-release.list /etc/apt/sources.list.d/mssql-release.list
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

RUN apt-key add /opt/app/microsoft.asc
RUN apt -y update \
	&& apt -y install tzdata msodbcsql17 mssql-tools postgresql-client-common postgresql-client unixodbc-dev \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

