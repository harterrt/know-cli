# `know` CLI

`know` is a small command line tool for maintaining a personal knowledge repo.
Everything here is experimental and will change quickly
(if it changes at all, who knows).

## Concepts

The knowledge repo is made up of a 
[stream and a garden](https://hapgood.us/2015/10/17/the-garden-and-the-stream-a-technopastoral/)
stored in `know/raw` and `know/wiki` respectively.

Adding content to `raw` should be effortless.
A lot of the content collection should be automatic.
The non-automatic should be as simple as possible.
E.g. you shouldn't need to decide on a name before writing.

The `wiki` is manually curated and will often link to documents in `raw`.
 
Everything is text files.
Interoperability, own your data, future proofing... all that stuff.


## Existing Commands

* `know zett` - Opens vim to a timestamped text file in `raw/zett`.
  Meant to collect quick temporal notes, like index cards in a shoebox.
  See [zettelkasten](https://zettelkasten.de/) for more info.

## Future Commands

* `know wiki` - Open an index of all wiki articles
  and allow the user to select one to edit
