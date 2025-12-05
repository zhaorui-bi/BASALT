#!/bin/bash
# BASALT 1.2 Installation Script
 
# 1. Ensure the Conda environment is activated
if [ -z "$CONDA_PREFIX" ]; then 
    echo "Error: Please activate your Conda environment first."
    exit 1
fi

# 2. Copy all source files directly into the bin directory
# Assumes the source code is located in the 'BASALT' folder in the current directory
echo "Copying files to $CONDA_PREFIX/bin/ ..."
cp -r BASALT/* "$CONDA_PREFIX/bin/"

# 3. Grant execution permissions to all scripts
chmod +x "$CONDA_PREFIX/bin/"*.py
chmod +x "$CONDA_PREFIX/bin/"*.pl

# 4. Create the 'BASALT' launcher command
# This allows you to type 'BASALT' in the terminal to execute BASALT.py located in bin
echo '#!/bin/bash' > "$CONDA_PREFIX/bin/BASALT"
echo 'python "$CONDA_PREFIX/bin/BASALT.py" "$@"' >> "$CONDA_PREFIX/bin/BASALT"
chmod +x "$CONDA_PREFIX/bin/BASALT"

echo "Installation complete. Files have been placed directly in $CONDA_PREFIX/bin/"