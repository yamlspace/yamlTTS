import os
from TTS.utils.manage import ModelManager

def download_and_prepare_model():
    # Initialize model manager
    manager = ModelManager()
    
    # Download XTTS v2 model
    model_path = manager.download_model("tts_models/multilingual/multi-dataset/xtts_v2")
    
    # Create output directory
    os.makedirs("huggingface_model", exist_ok=True)
    
    # Copy files to prepare for HuggingFace upload
    import shutil
    for file in os.listdir(model_path):
        shutil.copy2(
            os.path.join(model_path, file),
            os.path.join("huggingface_model", file)
        )

if __name__ == "__main__":
    download_and_prepare_model() 