from botocore.config import Config

my_config = Config(
    region_name = 'us-west-2',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)