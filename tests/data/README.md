# Test data

Fixtures copied from the VocaLink modulus checking publication. Line endings are
normalised from CRLF to LF; the field spacing is left exactly as published.

The parsers reject anything that is not a well-formed record, so the provenance
cannot live in the data files themselves — keep this table current instead.

| File | Upstream | Valid from | Records | sha256 |
|---|---|---|---|---|
| `weights.txt` | [valacdos.txt](https://www.vocalink.com/media/zttpmnlp/valacdos.txt) | 17 October 2026 | 1170 | `8ffaf939…47951c` |
| `subs.txt` | [scsubtab.txt](https://www.vocalink.com/media/tedlwtxz/scsubtab.txt) | 13 June 2005 | 21 | `2d264407…0b3749` |

Specification: [Validating account numbers, v9.10](https://www.vocalink.com/media/e0mo2xxa/validating-account-numbers-uk-modulus-checking-v910.pdf), 7 September 2026.

Both files were last checked against upstream on 2026-09-22. `subs.txt` was
already current and is unchanged.

VocaLink publishes the tables from <https://www.vocalink.com/tools/modulus-checking/>,
changing the URL slug with each revision, so resolve the current link from that
page rather than reusing the one above.
