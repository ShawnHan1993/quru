run-infra: create-docker-network
	docker-compose -f infra.yaml up

create-docker-network:
	@docker network create --attachable -d overlay quru-network || true