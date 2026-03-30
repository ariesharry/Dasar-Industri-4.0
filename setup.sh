#!/bin/bash
set -e

# Uninstall any full opencv-python
pip uninstall -y opencv-python opencv-contrib-python || true

# Ensure headless is installed
pip install opencv-python-headless

echo "OpenCV headless setup complete."