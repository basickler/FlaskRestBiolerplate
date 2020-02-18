FROM ubuntu:18.04
MAINTAINER CGLS Bioinformatics "ILMN-Org-CGLSBioinformatics@illumina.com"

# set a few environment variables
ENV TZ=%env.TZ_PCT%
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN ln -snf /usr/share/zoneinfo/%env.TZ_PCT% /etc/localtime && echo %env.TZ_PCT% > /etc/timezone

# install base packs
RUN apt-get update && apt-get install -y python3 python3-pip \
  && rm -rf /var/lib/apt/lists/*

#
# Add the Forest Users Group
#
RUN groupadd -g 32840 Forest_Users

#
# Add the service account
#

RUN export PYTHONPATH="$PYTHONPATH:/app"

RUN useradd svc_hpc_ussd_auto -u 20795 -g 32840
RUN useradd svc_cgls_sd_val_RO -u 24169 -g 32840
RUN useradd svc_cgls_sd_dev_RO -u 24149 -g 32840
RUN useradd svc_cgls_sd_prd_RO -u 24130 -g 32840
RUN useradd svc_cgls_fc_prd_RO -u 24131 -g 32840
RUN useradd svc_cgls_fc_val_RO -u 24168 -g 32840

COPY . /app
WORKDIR /app
RUN /usr/bin/pip3 install -r requirements.txt

CMD ["/usr/bin/python3", "venv/bin/gunicorn", "--config", "gunicorn_config_docker.py", "--bind", "0.0.0.0:10086", "app"]