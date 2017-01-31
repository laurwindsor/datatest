FROM python:3.5

RUN \
	apt-get update -y \
	&& apt-get install -y postgresql-client-9.4 vim

ENV LUCID_APP {{cookiecutter.app_name}}
ENV GIT_REPO lucidhq/{{cookiecutter.app_name}}

RUN mkdir -p /opt/{{cookiecutter.app_name}}
WORKDIR /opt/{{cookiecutter.app_name}}

COPY src/requirements.txt /tmp/requirements.txt

RUN \
	pip install --no-cache-dir -r /tmp/requirements.txt \
	&& rm /tmp/requirements.txt

COPY src /opt/{{cookiecutter.app_name}}

RUN \
	cd /opt/{{cookiecutter.app_name}} \
	&& pip install -e .

COPY .bashrc /root

EXPOSE 80

CMD ["{{cookiecutter.app_name}}-serve"]
