# A command line tool to mint and validate ARKs

This program generate pseudo-random ARK identifiers.

# Installation

To install this software locally, set
up a virtual environment and use pip to install dependencies:

```console
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Mint

To mint a new identifier:

```console
python ark_minter.py
```

Please note that this program does not check for collisions.
You should confirm that there were no collisions before 
publishing these ARKs. This program also does not store ARKs in
any database, so please be sure to do that separately. 

## Validation

To validate an existing ARK:

```console
python ark_minter.py ark:61001/b2db20724g7b
```

The validator will report True or False for the given ARK. 

## Testing this code

```console
python test.py
```

A unit test for this program includes a set of ARKs that John Kunze 
verified independently on February 9, 2022. 

## About UChicago Library ARKs

UChicago Library ARKs follow this pattern:

ark:61001/b2.reedeedeedk

In the above string-
- "ark:" is the ARK label,
- "61001" is the Name Assigning Authority Number (NAAN)
- "b2" is a shoulder- literal characters we want each ARK to start with.
- "r" means that we generate ARKs randomly. 
- "e" is an extended digit. (see https://metacpan.org/dist/Noid/view/noid#NOID-CHECK-DIGIT-ALGORITHM)
- "d" is a digit.
- "k" is a check digit.

For more information on NOIDs, see https://metacpan.org/dist/Noid. 
