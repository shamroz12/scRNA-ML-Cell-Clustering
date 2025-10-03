
# scRNA-ML-CellClustering

## Description
A machine learning pipeline for clustering real single-cell RNA-seq (scRNA-seq) data. Implements data download, preprocessing, dimensionality reduction, clustering, and visualization of cell types using the PBMC 3k dataset from 10X Genomics.

## Project Structure
```
scRNA-ML-CellClustering/
├─ data/                  # downloaded dataset
├─ notebooks/
│   └─ scRNA_ML_pipeline.ipynb  # full analysis pipeline
├─ scripts/
│   └─ download_data.py    # download PBMC dataset
├─ results/               # UMAP plots, heatmaps, CSV results
├─ README.md
├─ .gitignore
├─ environment.yml        # dependencies
```

## Instructions
1. Run `scripts/download_data.py` to download the PBMC 3k dataset.
2. Open `notebooks/scRNA_ML_pipeline.ipynb` in Jupyter or Google Colab.
3. Run all cells to preprocess, cluster, and visualize the data.
4. Results will be saved in the `results/` folder (UMAP plots, heatmaps, CSVs).
