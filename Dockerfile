FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    espeak-ng \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install packages one by one
RUN pip3 install --no-cache-dir numpy==1.24.3
RUN pip3 install --no-cache-dir torch>=2.1.0
RUN pip3 install --no-cache-dir torchaudio>=2.1.0
RUN pip3 install --no-cache-dir TTS==0.21.1

EXPOSE 5000

CMD ["python3", "-m", "TTS.server.server"]

# Add a health check to verify model exists
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD [ -f "/root/.local/share/tts/tts_models--multilingual--multi-dataset--xtts_v2/model_file.pth" ] || exit 1