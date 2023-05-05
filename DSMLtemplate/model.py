from DSMLtemplate import utils


class Model:
    """Model step."""

    def __init__(self, config: dict):
        """Initialize model step.

        Args:
            config (dict): Configuration dictionary.
        """
        self.model_key = config["MODEL_KEY"]

    def run(self, prev_output):
        """Run model step.

        Args:
            prev_output (any): Output from previous step.

        Returns:
            any: Output from model step.
        """
        return utils.get_something(prev_output + self.model_key)
