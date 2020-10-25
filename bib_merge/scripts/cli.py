import os
import argparse
import shutil

from bib_merge.utils import io_utils
from bib_merge.scripts.merge import merge


def get_new_bib_path(path, prefix='copy'):
    assert ".bib" in path, (
        "path must be a bib file: %s" % path
    )
    if '/' not in path:
        splits = path.split(".")
        assert len(splits) == 2 and splits[-1] == "bib", (
            "prefix should be *.bib: %s" % path
        )
        new_path = '%s_%s.bib' % (prefix, splits[0])
    else:
        old_path, last_item = path.split('/')[:-1], path.split('/')[-1]
        splits = last_item.split(".")
        assert len(splits) == 2 and splits[-1] == "bib", (
            "prefix should be *.bib: %s" % path
        )
        new_path = path.replace(last_item, '%s_%s.bib' % (prefix, splits[0]))
    return new_path


def update_library(args):
    source = io_utils.read_bib_file(args.file, verbose=args.verbose)
    library = io_utils.read_bib_file(args.library_file, verbose=args.verbose)

    new_file = merge(
        source=source,
        target=library,
        replace=args.replace,
        verbose=args.verbose,
    )
    io_utils.write_bib_file(new_file, get_new_bib_path(args.file, 'new'))
    print('Add %d item into %s.' % (len(new_file.entries) - len(source.entries), args.file))

    if args.update_library:
        shutil.copyfile(args.library_file, get_new_bib_path(args.library_file, 'copy'))
        io_utils.write_bib_file(new_file, args.library_file, verbose=False)
        print('Update library file.')


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file', type=str, default='reference.bib',
                        help='path to reference bib file')
    parser.add_argument('-u', '--update-library', type=int, default=1,
                        help='whether to update library file')
    parser.add_argument('-l', '--library-file', type=str, default=os.path.join(
        os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "library", "reference.bib"),
                        help='path to library file')
    parser.add_argument('-r', '--replace', type=int, default=1,
                        help='Whether to replace old item in library with the new one if applicable.')
    parser.add_argument('-v', '--verbose', type=int, default=1)

    args = parser.parse_args()
    if not os.path.exists(args.file):
        raise FileNotFoundError("%s does not exist." % args.file)
    if not os.path.exists(args.library_file):
        basedir = os.path.dirname(args.library_file)
        if not os.path.exists(basedir):
            os.makedirs(basedir)
        shutil.copyfile(args.file, args.library_file)

        print('Copy %s to %s as a library file.' % (args.file, args.library_file))
        print('There is no need for library update.')
        return
    update_library(args)


if __name__ == "__main__":
    main()
