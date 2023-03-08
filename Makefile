SHELL := /usr/bin/env bash

.PHONY: run
run:
	git secret reveal -f
	docker-compose up --build
