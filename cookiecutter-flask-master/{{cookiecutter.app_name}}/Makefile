APP={{cookiecutter.app_name}}
IMAGE=lucidhq/{{cookiecutter.app_name}}
VERSION=1.0
INSTALL_DIR=/opt/$(APP)
POSTGRES_USER?=postgres
PGPASSWORD?={{cookiecutter.app_name}}pass
POSTGRES_HOST?=localhost
POSTGRES_ENV?= \
			   -e POSTGRES_USER=$(POSTGRES_USER) \
			   -e PGPASSWORD=$(PGPASSWORD) \
			   -e POSTGRES_HOST=$(POSTGRES_HOST)

.PHONY: image shell test test-$(APP) run-$(APP)

image: Dockerfile
	docker build -t $(IMAGE):$(VERSION) .
	docker tag $(IMAGE):$(VERSION) $(IMAGE):latest
		
vbox-manage:
	-docker-machine stop
	-VBoxManage modifyvm "default" --natpf1 "tcp-port8080,tcp,,8080,,8080"

shell: image
	docker run \
		--rm \
		--name $(APP)-shell \
		-P \
		-e APP_CONFIG=$(INSTALL_DIR)/config/production.yaml \
		-e DEBUG=1 \
		$(POSTGRES_ENV) \
		-e PORT=5000 \
		-p 5000:5000 \
		-v `pwd`/tests:/tests \
		-it $(IMAGE):$(VERSION) \
		bash

db-shell: image
	docker run \
		--rm \
		--name $(APP)-shell \
		-P \
		-e APP_CONFIG=$(INSTALL_DIR)/config/production.yaml \
		$(POSTGRES_ENV) \
		-it $(IMAGE):$(VERSION) \
		psql -h $(POSTGRES_HOST) -U $(POSTGRES_USER) {{cookiecutter.app_name}}

test: image
	docker run \
		--rm \
		--name $(APP)-test \
		-e APP_CONFIG=$(INSTALL_DIR)/config/test.yaml \
		-e DEBUG=1 \
		$(POSTGRES_ENV) \
		-v `pwd`/tests:/tests \
		-it $(IMAGE):$(VERSION) \
		bash -c 'echo "Running tests..." && cd $(INSTALL_DIR) && flake8 . && cd /tests && flake8 . && py.test'

bootstrap-db: image
	docker run \
		--name db-create \
		--rm \
		$(POSTGRES_ENV) \
		-v `pwd`/bootstrap_db:/bootstrap_db \
		-it $(IMAGE):$(VERSION) \
		bash -c 'echo "Running migrations..." && /bootstrap_db/init.sh'
	docker run \
		--name db-migrate \
		--rm \
		$(POSTGRES_ENV) \
		-it $(IMAGE):$(VERSION) \
		bash -c 'echo "Running migrations..." && cd $(INSTALL_DIR) && alembic upgrade head'

serve: image
	-docker kill $(APP)-server
	-docker rm $(APP)-server
	docker run \
		--name $(APP)-server \
		--rm \
		-e APP_CONFIG=$(INSTALL_DIR)/config/production.yaml \
		-e DEBUG=1 \
		$(POSTGRES_ENV) \
		-e PORT=5000 \
		-p 5000:5000 \
		-it $(IMAGE):$(VERSION) \
		$(APP)-serve

run-db:
	docker run \
		--name {{cookiecutter.app_name}}-db \
		-e POSTGRES_PASSWORD=$(PGPASSWORD) \
		-d \
		postgres
