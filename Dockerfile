# AI-assisted implementation based on the Lecture 4 activity description.
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends bash git perl grep sed gawk coreutils \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN chmod +x /app/.github/scripts/entrypoint.sh \
    /app/.github/scripts/update_index.sh

ENTRYPOINT ["/bin/bash", "/app/.github/scripts/entrypoint.sh"]
