import os
import requests
from tqdm import tqdm
import hashlib
import subprocess

MODELS = {
    "xtts_v2": {
        "url": "https://huggingface.co/coqui/xtts-v2/resolve/main/model.pth",
        "sha256": "HASH_OF_MODEL_FILE",
        "path": "models/tts_models--multilingual--multi-dataset--xtts_v2"
    }
}

def download_with_wget(url, dest_path, options=""):
    cmd = f"wget {options} -O {dest_path} '{url}'"
    print(f"Downloading with command: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def verify_hash(file_path, expected_hash):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest() == expected_hash

def main():
    os.makedirs("models", exist_ok=True)
    
    for model_name, info in MODELS.items():
        dest_path = os.path.join(info["path"], "model_file.pth")
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        if not os.path.exists(dest_path):
            print(f"Downloading {model_name}...")
            download_with_wget(info["url"], dest_path)
            
            if info["sha256"]:
                print("Verifying download...")
                if not verify_hash(dest_path, info["sha256"]):
                    print("Warning: Hash verification failed!")
        else:
            print(f"Model {model_name} already exists")

if __name__ == "__main__":
    main() 