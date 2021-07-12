# Shobdohash - Bengali Soundex Implementation

Shobdohash is a Bengali Soundex Implementation to phonetically hash and compare similar words. Implemented from the
algorithm described by Naushad UzZaman and Mumit Khan in
[A Bangla Phonetic Encoding for Better Spelling Suggestions](http://dspace.bracu.ac.bd/bitstream/handle/10361/310/Problems%20in%20teaching%20speaking%20in%20traditional%20ESL%20classrooms.PDF?sequence=1).

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
@software{aniruddha_adhikary_ani_2021_5091303,
  author       = {Aniruddha Adhikary (Ani) and
                  Mohammad Shiekh Ghazanfar},
  title        = {banglakit/shobdohash: v1.0.4},
  month        = jul,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {v1.0.4},
  doi          = {10.5281/zenodo.5091303},
  url          = {https://doi.org/10.5281/zenodo.5091303}
}
```
