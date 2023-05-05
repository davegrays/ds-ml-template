import pytest
from DSMLtemplate.Pipeline import Pipeline


@pytest.fixture
def pipeline():
    return Pipeline("tests/test_config.yml")


def test_pipeline_init(pipeline):
    assert pipeline.params["ETL_KEY"] == "etl"
    assert pipeline.params["PROC_KEY"] == "proc"
    assert pipeline.params["MODEL_KEY"] == "model"


def test_pipeline(pipeline):
    assert pipeline.run(steps=["etl"]) == "etl"
    assert pipeline.run(steps=["etl", "proc"]) == "etlproc"
    assert pipeline.run(steps=["etl", "proc", "model"]) == "etlprocmodel"
    assert pipeline.run() == "etlprocmodel"
