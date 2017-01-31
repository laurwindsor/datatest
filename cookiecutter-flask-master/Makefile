.PHONY: test test-server test-setup

TEST_DIR=tests
DEFAULT_APP=default_lucid_app_name

test: test-setup
	cd $(TEST_DIR)/$(DEFAULT_APP) && make test

shell: test-setup
	cd $(TEST_DIR)/$(DEFAULT_APP) && make shell

test-serve: test-setup
	cd $(TEST_DIR)/$(DEFAULT_APP) && make test-serve

test-setup:
	-rm -rf $(TEST_DIR)
	mkdir -p $(TEST_DIR)
	. env/bin/activate && cookiecutter -o $(TEST_DIR) --no-input .

bootstrap:
	rm -rf env
	virtualenv env && . env/bin/activate && pip install cookiecutter
