import yaml

with open("credentials/credentials.yaml", "r") as credentials:
    cred = yaml.safe_load(credentials)

ACCESS_KEY = cred['credentials']['aws']['AC']['access-key']
SECRET_KEY = cred['credentials']['aws']['AC']['secret-key']