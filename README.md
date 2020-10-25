
# Bib-merge

Bib-merge is a python-based command line tool to automatically merge bib files. 

It maintains a (global) library bib file under the package folder. Calling the following cmd will update ``reference.bib`` into the library file and generate the merged version ``new_reference.bib`` (the library file will be also updated).

```
bib-merge -f reference.bib
```

see ``bib_merge/scripts/cli.py`` for detailed args explanation.

## Install


```
git clone git@github.com:liziniu/bib-merge.git
python setup.py install
```









