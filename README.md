# A RESTful API to Mint and Validate ARKs

This API generate ARKs stateless, pseudo-random ARK identifiers- although the
identifiers generated should should fill the identifier space evenly, the tool
will produce the same "first ARK" each time it is run.  The API accepts a
formatting string that describes how ARKs should be constructed, and it can
accept an ARK as an optional parameter to return the next or previous ARK based
on what was passed to it. It can also validate ARKs produced by other sources.

This system creates and validates ARK identifiers only.

# API

## Mint

* Mint : `GET /mint`

### Required Parameters

template : a template string for this ARK, e.g. ark:61001/b2.reedeedeedk

### Optional Parameters

arkid-after : return the ARKid after this one.
arkid-before : return the ARKid before this one.
n : number of ARKs to return.

### Response

```
{
    "status": "OK",
    "arks": [
        <arkid>,
        ...
    ]
}
```


## Validate

* Validate : `GET /validate`

### Required Parameters

arkid : an ARK identifier (repeatable)
template : a template string for this ARK, e.g. ark:61001/b2.reedeedeedk

### Response

```
{
    "status": "OK",
    "valid": [
        <arkid>
    ],
    "invalid": [
        <arkid>
    ],
}
```

## Templates

UChicago ARKs follow this pattern:

ark:61001/b2.reedeedeedk

In the above string-
    "ark:" is the ARK label,
    "61001" is the Name Assigning Authority Number (NAAN)
    "b2" is a shoulder- literal characters we want each ARK to start with.
    "r" means that we generate ARKs randomly. 
    "e" is an extended digit. (see https://metacpan.org/dist/Noid/view/noid#NOID-CHECK-DIGIT-ALGORITHM)
    "d" is a digit.
    "k" is a check digit. 

Please confirm: is this the correct way to express an ARK format string? 

See the nog command line tool's help message for more info. 
