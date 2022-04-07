import yaml


def load_config(config_path):
    with open(config_path) as stream:
        config = yaml.safe_load(stream=stream)
    return config

print(load_config('/home/lyova/work/market_app/logs/market_log_config.yaml'))
