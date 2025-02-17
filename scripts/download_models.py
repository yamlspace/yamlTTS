import os
import requests
from tqdm import tqdm
import hashlib

MODELS = {
    "xtts_v2": {
        "url": "https://huggingface.co/coqui/xtts-v2/resolve/main/model.pth",  # Example
        # Or use other stable hosting:
        # - Hugging Face
        # - AWS S3
        # - Google Cloud Storage
        "sha256": "HASH_OF_MODEL_FILE",
        "path": "models/tts_models--multilingual--multi-dataset--xtts_v2"
    }
}

def download_file(url, dest_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(dest_path, 'wb') as f, tqdm(
        desc=os.path.basename(dest_path),
        total=total_size,
        unit='iB',
        unit_scale=True
    ) as pbar:
        for data in response.iter_content(chunk_size=1024):
            size = f.write(data)
            pbar.update(size)

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
            download_file(info["url"], dest_path)
            
            if info["sha256"]:
                print("Verifying download...")
                if not verify_hash(dest_path, info["sha256"]):
                    print("Warning: Hash verification failed!")
        else:
            print(f"Model {model_name} already exists")

if __name__ == "__main__":
    main() 