import bibtexparser as bp


def read_bib_file(file_path: str, verbose=True):
    assert file_path.endswith('.bib'), (
        "Provided path does not reach to a bib file: %s" % file_path
    )

    with open(file_path) as bib_file:
        bib_database = bp.load(bib_file)
    if verbose:
        print('Load bib database from %s.' % file_path)
    return bib_database


def write_bib_file(bib_database: bp.bibdatabase.BibDatabase, file_path='new_reference.bib', verbose=True):
    with open(file_path, 'w') as bib_file:
        bp.dump(bib_database, bib_file)
    if verbose:
        print('Write bib database into %s.' % file_path)
