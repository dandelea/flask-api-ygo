cnf ?= config.env
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))

build:
	docker build -t $(APP_NAME) .

run: 
	docker run -i -t --rm --env-file=./config.env -p=$(PORT):5000 --name="$(APP_NAME)" $(APP_NAME)

stop: ## Stop running containers
	docker stop $(APP_NAME)