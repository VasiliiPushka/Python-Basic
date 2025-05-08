movies = {
    'The Hateful Eight': 2015,
    'Inglourious Basterds': 2009,
    'Death Proof': 2007
}
class MyDict(dict):
    def get(self, key: str, default=0):
        return dict.get(self, key, default)


m = MyDict(movies)
print(m.get('Inglourious Basterds'))
print(m.get('Kill Bill'))
print(m.pop('Death Proof'))
print(m)
