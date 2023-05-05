from DSMLtemplate import utils


class ETL:
    """ETL step."""

    def __init__(self, config: dict):
        """Initialize ETL step.

        Args:
            config (dict): Configuration dictionary.
        """
        self.etl_key = config["ETL_KEY"]

    def run(self):
        """Run ETL step.

        Returns:
            any: Output from ETL step.
        """
        return utils.get_something(self.etl_key)
