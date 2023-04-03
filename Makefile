SHELL := /usr/bin/env bash

.PHONY: run
run: config/secrets.yml
	docker-compose up --build

config/secrets.yml:
	git secret reveal -f