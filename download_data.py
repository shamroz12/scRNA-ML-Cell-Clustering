
import os
import requests
import zipfile
import io

# 10X Genomics PBMC 3k dataset URL
url = "http://cf.10xgenomics.com/samples/cell-exp/3.0.0/pbmc_3k/pbmc_3k_filtered_feature_bc_matrix.h5"
data_dir = os.path.join(os.path.dirname(__file__), "../data")
os.makedirs(data_dir, exist_ok=True)
out_path = os.path.join(data_dir, "pbmc_3k_filtered_feature_bc_matrix.h5")

print("Downloading PBMC 3k dataset...")
r = requests.get(url, stream=True)
with open(out_path, "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)
print("Download complete:", out_path)
