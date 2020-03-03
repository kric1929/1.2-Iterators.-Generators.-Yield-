import json


class GetUrl:

    def __init__(self, path):
        self.path = path
        self.file_read = open(self.path, encoding='utf-8')
        self.data = json.load(self.file_read)
        self.number = -1
        self.file_write = open('countries-url.txt', 'w', encoding='utf-8')

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.number += 1
            countries = self.data[self.number]['name']['common']
            replace_countries = countries.replace(' ', '_')
            url = 'https://wikipedia.org/wiki/' + replace_countries
            self.file_write.write(f'{countries} - https://wikipedia.org/wiki/{replace_countries}\n')
        except IndexError:
            raise StopIteration
        return url


if __name__ == '__main__':
    for url in GetUrl('countries.json'):
        print(url)
