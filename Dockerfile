FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
# Add environment variable to auto-accept TOS
ENV COQUI_TOS_AGREED=1

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    espeak-ng \
    curl \
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

# Pre-download the model during build
RUN mkdir -p /root/.local/share/tts && \
    python3 -c "from TTS.utils.manage import ModelManager; ModelManager().download_model('tts_models/multilingual/multi-dataset/xtts_v2')"

EXPOSE 5002

# Use python from virtual environment with explicit model name
CMD ["/app/.venv/bin/python", "-m", "TTS.server.server", "--model_name", "tts_models/multilingual/multi-dataset/xtts_v2"]

# Add a health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5002/health || exit 1