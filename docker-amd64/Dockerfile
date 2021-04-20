FROM python:3.9.4-slim-buster

# Build dependencies - Pandas requires GCC on arm64
# https://github.com/docker-library/python/blob/18ef1b6500a622da8b138d1b413c963c279e7ea4/3.9/buster/slim/Dockerfile
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		build-essential \
	; \
	rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install numpy pandas scipy

COPY script.py .

ENTRYPOINT [ "python", "script.py" ]
