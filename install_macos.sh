#!/bin/bash
echo "Installing Python 3.13.0 and dependencies..."

# Install Homebrew if not present
if ! command -v brew &> /dev/null; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install Python 3.13
brew install python@3.13

# Install Pillow
pip3 install Pillow

echo "Installation complete!"