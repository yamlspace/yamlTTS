FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    espeak-ng \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create and activate virtual environment using uv
RUN pip3 install uv
RUN uv venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Install packages using uv in the virtual environment
RUN uv pip install numpy==1.24.3
RUN uv pip install "torch>=2.1.0"
RUN uv pip install "torchaudio>=2.1.0"
RUN uv pip install "TTS==0.21.1"

EXPOSE 5002

# Use python from virtual environment
CMD ["/app/.venv/bin/python", "-m", "TTS.server.server"]

# Add a health check to verify model exists
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD [ -f "/root/.local/share/tts/tts_models--multilingual--multi-dataset--xtts_v2/model.pth" ] || exit 1