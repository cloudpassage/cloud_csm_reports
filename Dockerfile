FROM docker.io/halotools/python-sdk:ubuntu-18.04_sdk-latest_py-3.6

LABEL com.fidelissecurity.CLOUD_CSM_REPORTS.authors="Thomas.Miller@fidelissecurity.com"

ENV HALO_API_HOSTNAME='https://api.cloudpassage.com'
ENV HALO_API_PORT='443'
ENV HALO_API_VERSION='v1'
ENV OUTPUT_DIRECTORY=/var/log

ARG HALO_API_KEY
ARG HALO_API_SECRET_KEY
ARG OUTPUT_DIRECTORY

WORKDIR /app/

COPY app/ /app/

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

CMD /usr/bin/python /app/runner.py