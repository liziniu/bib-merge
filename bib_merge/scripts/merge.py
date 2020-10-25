import bibtexparser as bp
from copy import deepcopy

from bib_merge.utils.io_utils import read_bib_file


def merge(
        source: bp.bibdatabase.BibDatabase or str,
        target: bp.bibdatabase.BibDatabase or str,
        replace: bool = False,
        verbose: bool = True
):
    if isinstance(source, str):
        source = read_bib_file(source)
    if isinstance(target, str):
        target = read_bib_file(target)
    else:
        target = deepcopy(target)
    assert isinstance(source, bp.bibdatabase.BibDatabase), (
        "source must be a BibDataBase: %s" % (type(source))
    )
    assert isinstance(target, bp.bibdatabase.BibDatabase), (
        "target must be a BibDataBase: %s" % (type(target))
    )
    if verbose:
        print('There are %d items in source file.' % len(source.entries))
        print('There are %d items in target file.' % len(target.entries))

    target_titles = [e['title'] for e in target.entries]
    for entry in source.entries:
        if entry['title'] in target_titles:
            if not replace:
                continue
            # replace with new one
            index = target_titles.index(entry['title'])
            target.entries[index] = entry
        else:
            # append new one
            target.entries.append(entry)

    return target
