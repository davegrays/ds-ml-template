from DSMLtemplate import utils


class Proc:
    """PROC step."""

    def __init__(self, config: dict):
        """Initialize PROC step.

        Args:
            config (dict): Configuration dictionary.
        """
        self.proc_key = config["PROC_KEY"]

    def run(self, prev_output):
        """Run PROC step.

        Args:
            prev_output (any): Output from previous step.

        Returns:
            any: Output from PROC step.
        """
        return utils.get_something(prev_output + self.proc_key)
