# Shobdohash - Bengali Soundex Implementation

Shobdohash is a Bengali Soundex Implementation to phonetically hash and compare similar words. Implemented from the
algorithm described by Naushad UzZaman and Mumit Khan in
[A Bangla Phonetic Encoding for Better Spelling Suggestions](http://panl10n.net/english/final%20reports/pdf%20files/Bangladesh/BAN18.pdf).

## Installation

### Stable Version
```shell script
$ python -m pip install shobdohash
```

### Development Version
```shell script
$ python -m pip install -e 'git+https://github.com:banglakit/shobdohash.git#egg=shobdohash'
```


## Usage
```python
from shobdohash import ShobdoHash

s = ShobdoHash()
s('আমি')

s('বাংলা') == s('বাঙলা')
```

## Running Tests
```shell script
$ pip install -r requirements-test.txt
$ pytest
```

## Citing
```
Adhikary, A. (2020, March 14). Shobdohash (Version 1.0.3) [Computer software]. Retrieved [Date], from https://github.com/banglakit/shobdohash
```
