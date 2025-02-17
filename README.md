# yamlTTS
TTS based on coquiXTTS for voice services
# CoquiTTS Docker Build

## Requirements
- 30GB+ free disk space
- NVIDIA GPU with CUDA support
- Docker with NVIDIA runtime
- Python 3.10+


# yamlTTS Docker Build

## Model Files
The XTTS model files are not included in this repository due to size constraints. You can:

1. Download automatically:
```bash
python scripts/download_models.py
```

2. Download manually:
- Download from: [Terabox Link]
- Place in: `models/tts_models--multilingual--multi-dataset--xtts_v2/`
- Verify SHA256: `[hash]`

## Directory Structure
```
.
├── Dockerfile
├── models/                    # Pre-downloaded models (gitignored)
│   └── .gitkeep
├── scripts/
│   └── download_models.py    # Script to download models
└── README.md
```
