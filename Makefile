GIT_COMMIT=$$(git rev-parse --short HEAD)
IMAGE_REPO?="arnobroekhof"

.PHONY: image/build
image/build:
	DOCKER_BUILDKIT=1 docker build -t $(IMAGE_REPO)/flask-docker-example:$(GIT_COMMIT) .

.PHONY: image/push
image/push: image/build
	docker push $(IMAGE_REPO)/flask-docker-example:$(GIT_COMMIT)

.PHONY: image/test
image/test:	image/build
	docker run -e API_PORT=8080 -p 8080:8080 $(IMAGE_REPO)/flask-docker-example:$(GIT_COMMIT)

.PHONY: image/deps
dev/deps:
	python -m venv .venv
