import os
import requests
from tqdm import tqdm
from pathlib import Path

MODELS = {
    "xtts_v2": {
        "model_name": "tts_models--multilingual--multi-dataset--xtts_v2",
        "files": {
            "model.pth": "https://huggingface.co/deepbrainspace/TTS/resolve/main/model.pth",
            "config.json": "https://huggingface.co/deepbrainspace/TTS/resolve/main/config.json",
            "vocab.json": "https://huggingface.co/deepbrainspace/TTS/resolve/main/vocab.json",
            "speakers_xtts.pth": "https://huggingface.co/deepbrainspace/TTS/resolve/main/speakers_xtts.pth",
            "dvae.pth": "https://huggingface.co/deepbrainspace/TTS/resolve/main/dvae.pth",
            "mel_stats.pth": "https://huggingface.co/deepbrainspace/TTS/resolve/main/mel_stats.pth"
        },
        "path": "models/tts_models--multilingual--multi-dataset--xtts_v2"
    }
}

def download_file(url, dest_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    Path(dest_path).parent.mkdir(parents=True, exist_ok=True)
    
    with open(dest_path, 'wb') as file, tqdm(
        desc=os.path.basename(dest_path),
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            pbar.update(size)

def main():
    for model_name, info in MODELS.items():
        print(f"\nDownloading {model_name} files...")
        
        for file_name, url in info["files"].items():
            dest_path = os.path.join(info["path"], file_name)
            
            if not os.path.exists(dest_path):
                print(f"Downloading {file_name}...")
                download_file(url, dest_path)
            else:
                print(f"{file_name} already exists, skipping...")

if __name__ == "__main__":
    main() 