import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with (config_dir / "config.yml").open() as f:
    config_yaml = yaml.safe_load(f)

with (config_dir / "secrets.yml").open() as f:
    secrets_yaml = yaml.safe_load(f)
config_yaml.update(secrets_yaml)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
telegram_token = config_yaml["telegram_token"]
openai_api_key = config_yaml["openai_api_key"]
use_chatgpt_api = config_yaml.get("use_chatgpt_api", True)
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
new_dialog_timeout = config_yaml["new_dialog_timeout"]
mongodb_uri = config_yaml["MONGODB_URL"]

# prices
chatgpt_price_per_1000_tokens = config_yaml.get("chatgpt_price_per_1000_tokens", 0.002)
gpt_price_per_1000_tokens = config_yaml.get("gpt_price_per_1000_tokens", 0.02)
whisper_price_per_1_min = config_yaml.get("whisper_price_per_1_min", 0.006)
