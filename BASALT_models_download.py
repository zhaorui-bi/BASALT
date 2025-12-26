#!/usr/bin/env python
import os
import requests
import argparse
from tqdm import tqdm

def download_model(target_dir):
    # Ensure target directory exists, create if not
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
        print(f"Created directory: {target_dir}")
    else:
        print(f"Target directory exists: {target_dir}")

    url = "https://figshare.com/ndownloader/files/41093033"
    # The file will be saved inside target_dir
    local_path = os.path.join(target_dir, "BASALT.zip")

    if os.path.exists(local_path):
        print(f"Zip file already exists: {local_path}")
    else:
        print(f"Downloading to: {local_path}")
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status() # Check for HTTP errors
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024
            progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

            with open(local_path, 'wb') as f:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data)) 
                    f.write(data)

            progress_bar.close()
            print("Download successful.")
        except Exception as e:
            print(f"Download failed: {e}")
            return None

    return local_path

if __name__ == '__main__':
    # 1. Setup argument parsing
    parser = argparse.ArgumentParser(description="Download and unzip BASALT model.")
    parser.add_argument('--path', type=str, default=None, help="Target directory for download and unzip")
    args = parser.parse_args()

    # 2. Determine download path
    if args.path:
        # If user provided a path, use it
        save_dir = args.path
    else:
        # If not provided, default to ./BASALT_WEIGHT in current working directory
        current_path = os.getcwd()
        save_dir = os.path.join(current_path, "BASALT_WEIGHT")
    
    print(f"Model will be saved to: {save_dir}")

    # 3. Execute download
    # The download_model function will automatically create the save_dir folder
    zip_file_path = download_model(save_dir)

    # 4. Execute unzip
    if zip_file_path and os.path.exists(zip_file_path):
        print(f"Unzipping {zip_file_path} ...")
        
        # -o: overwrite without prompting
        # -d: specify destination directory
        # Wrap paths in quotes to prevent errors with spaces
        exit_code = os.system(f'unzip -o "{zip_file_path}" -d "{save_dir}"')

        if exit_code == 0:
            print(f"Successfully unzipped to {save_dir}")
        else:
            print(f"Unzip failed. Please ensure 'unzip' command is installed.")
    else:
        print("Skipping unzip because file was not found.")
