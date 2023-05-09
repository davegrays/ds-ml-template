# ds-ml-template
![CI](https://github.com/davegrays/ds-ml-template/actions/workflows/ci.yml/badge.svg)

An opinionated template repo for data science / ML pipelines in python

Read more about it [in this blog post](https://davegrays.github.io/posts/05-08-2023-ds-ml-template/ds-ml-template.html)

## Philosophy && Practice
- Modularity
  - Separate directories for data, notebooks, base package, and tests.
  - Different *workflow components* are separated from each other and from *workflow management* (i.e. `Pipeline`), to allow flexible recomposition.
  - Configurations are further separated via config files.
- Readability
  - Pipeline manager enables low-code notebooks designed for *data exploration* and *workflow management*.
  - Code formatting / linting / testing is enforced
  - Docstrings and type-hinting in function definitions
- Repeatability
  - Dependencies / environment managed through code (i.e. `setup.sh`), including installation of the base package.
  - Workflows instantiated through low-code scripts or notebooks, which could further be managed by a dedicated WMS.
- Robustness
  - Unit tests and code coverage requirements strictly enforced through
    - pre-commit hooks
    - CI pipeline through github actions
    - branch management.

## Summary diagram
![data](data/summary_ds_ml_lifecycle.png)
