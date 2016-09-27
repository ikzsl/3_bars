import json

data = json.loads(open("bars.json", 'r', encoding='utf-8').read())
print(data[1:2])

def load_data(filepath):
    pass


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    pass

