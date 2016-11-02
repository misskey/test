import toml

with open("config.ini") as conffile:
    config = toml.loads(conffile.read())
    print config