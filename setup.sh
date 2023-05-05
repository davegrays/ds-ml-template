env_name=template

conda env create -f environment.yml
# `conda env update -f environment.yml --prune` to update

CONDA_BASE=$(conda info --base)
source $CONDA_BASE/etc/profile.d/conda.sh
conda activate ${env_name}
pip install -e .
python -m ipykernel install --name ${env_name}
pre-commit install