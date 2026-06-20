import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

_root = Path(__file__).parent
load_dotenv(_root / ".env")


def _load() -> dict:
    with open(_root / "config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


_yaml = _load()

# -------------------------------------------------------------------
# Portal settings (config.yaml)
# -------------------------------------------------------------------
BASE_URL: str = _yaml.get("base_url", "")
HEADLESS: bool = bool(_yaml.get("headless", False))
TIMEOUT: int = int(_yaml.get("timeout", 30))

# -------------------------------------------------------------------
# Credentials (.env)
# -------------------------------------------------------------------
USERNAME: str = os.getenv("TEST_USERNAME", "")
PASSWORD: str = os.getenv("TEST_PASSWORD", "")
