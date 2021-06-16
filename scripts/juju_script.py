from credentials import keys

script = f'''
cat << EOF1 > credentials.yaml
credentials:
  aws:
    AC:
      auth-type: access-key
      access-key: {keys.ACCESS_KEY}
      secret-key: {keys.SECRET_KEY}
EOF1

juju add-credential aws -f credentials.yaml --client
juju bootstrap --bootstrap-constraints instance-type=t2.micro aws aws-controller
'''