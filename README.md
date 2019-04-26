# Raman-Database

Converter of Raman spectroscopy data files in the format for submission to the [Raman Open Database](http://solsa.crystallography.net/rod/).

*! This is alpha stage and is not ready yet for production work !*

The rod_converter.py code contains the main function. rod_tools.py and chemistry.py contain some necessary tools.

# Usage

See example of CIF file in the ./raw folder (in csv).

Call as:
```
python3 rod_converter.py arg1 arg2 arg3
```
with:
- arg1: name of CIF information file without extension;
- arg2: path of spectra and CIF information file (don't forget the / at the end);
- arg3: output folder (don't forget the / at the end).

An example of usage with the folders indicated above and a ROD converter file name 'c064.csv' will be:

```
python3 rod_converter.py c064 ./raw/ ./converted/
```

# Roadmap

## Short term (2 month)
- [ ] The code waits for CIF files in .csv, but some spectra may also be in .csv, so we need to add some sort of safeguard there. Suggestions?
- [ ] Adding optional argument for spectra file extension
- [ ] Adding optional argument for CIF file extension

## Medium term (6 month)
- [ ] PyPI packaging

# Contributors
- Bernard Hehlen, University of Montpellier, France
- Charles Le Losq, Australian National University, Australia
- Oscar Branson, Australian National University, Australia

# Licence
See Licence.MD