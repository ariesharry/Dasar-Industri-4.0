#!/bin/bash
set -e
pip uninstall -y opencv-python opencv-contrib-python || true
pip install opencv-python-headless
echo "OpenCV headless setup complete."