#!/usr/bin/env python3
"""
Download RMBG-2.0 ONNX model from ModelScope to models/rmbg/model.onnx.
Requires: pip install modelscope
"""
import os
import shutil
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(PROJECT_ROOT, "models", "rmbg")
TARGET_PATH = os.path.join(MODEL_DIR, "model.onnx")
RMBG_MODEL_ID = "AI-ModelScope/RMBG-2.0"


def main():
    try:
        from modelscope import snapshot_download
    except ImportError:
        print("Install modelscope first: pip install modelscope")
        sys.exit(1)

    print(f"Downloading {RMBG_MODEL_ID} from ModelScope...")
    cache_dir = snapshot_download(RMBG_MODEL_ID)
    # Model may be at repo root or under onnx/
    candidates = [
        os.path.join(cache_dir, "model.onnx"),
        os.path.join(cache_dir, "onnx", "model.onnx"),
    ]
    src = None
    for p in candidates:
        if os.path.isfile(p):
            src = p
            break
    if not src:
        # Search for any .onnx file
        for root, _, files in os.walk(cache_dir):
            for f in files:
                if f.endswith(".onnx"):
                    src = os.path.join(root, f)
                    break
            if src:
                break
    if not src or not os.path.isfile(src):
        print(f"model.onnx not found under {cache_dir}; download from ModelScope and place at {TARGET_PATH}")
        sys.exit(1)

    os.makedirs(MODEL_DIR, exist_ok=True)
    shutil.copy2(src, TARGET_PATH)
    print(f"Saved: {TARGET_PATH}")
    print("For RMBG inference also install: pip install onnxruntime  # or onnxruntime-gpu")


if __name__ == "__main__":
    main()
