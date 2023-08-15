APP := flask-docker

network:
	@docker network create github-dev || true

image:
	@docker build -t ${APP}:latest .

shell:
	@docker compose exec -it api /bin/bash
