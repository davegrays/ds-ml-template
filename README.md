# ds-ml-template
![CI](https://github.com/davegrays/ds-ml-template/actions/workflows/ci.yml/badge.svg)

An opinionated template repo for data science / ML pipelines in python

## Philosophy && Practice
- Modularity
  - Separate directories for data, notebooks, source code, and tests.
  - Different *workflow components* are separated from each other and from *workflow management* (i.e. `Pipeline`), to allow flexible recomposition.
  - Configurations are further separated via config files.
- Readability
  - Pipeline manager enables low-code notebooks designed for *data exploration* and *workflow management*.
  - Code formatting / linting / testing is enforced
- Repeatability
  - Dependencies / environment managed through code, including installation of the base package
  - Workflows insantiated through low-code scripts or notebooks, which could further be managed by a dedicated WMS.
- Robustness
  - Unit tests and code coverage requirements strictly enforced through
    - pre-commit hooks
    - CI pipeline through github actions
    - branch management.
