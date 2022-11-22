import yaml


def read_config(file):
    with open(file, "r") as fin:
        return yaml.load(fin, Loader=yaml.FullLoader)


def extend_tags(tags):
    for tag in tags:
        if '-' in tag:
            tags += [tag.replace('-', ' ')]
    return tags
