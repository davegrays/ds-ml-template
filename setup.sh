env_name=template

conda env create -f environment.yml
conda activate ${env_name}
pip install -e .
python -m ipykernel install --name ${env_name}
pre-commit install
conda deactivate