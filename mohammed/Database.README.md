Database README\
\
This file explains how the database is structured and how to edit it.\
The database is the single place where all unit data lives. The Python\
engine reads it and does the maths and nothing is hardcoded in the
Python.\
To add a unit, add an entry here. To remove one, delete it here.\
No Python changes needed.\
\
symbol\
The short abbreviation used in the UI and code.\
Examples: J, eV, kJ/mol, cm⁻¹\
\
name\
The readable name.\
Examples: Joule, Electronvolt, Kilojoule per mole\
\
category\
Which group this unit belongs to.\
Options: SI, atomic, thermochemical, molar, thermal, spectroscopic\
\
type\
Tells the engine which conversion formula to use.\
See the CONVERSION TYPES section below.\
\
factor_to_J\
For linear units only.\
Multiply any value in this unit by this number to get Joules.\
Example: 1 eV × 1.602e-19 = 1.602e-19 J\
\
scale_to_metres\
For wavelength units only (nm, μm, Å).\
Multiply by this to convert to metres before applying E = hc/λ.\
\
scale_to_Hz\
For frequency units only (Hz, GHz, THz).\
Multiply by this to convert to Hz before applying E = hν.\
\
scale_to_per_metre\
For wavenumber (cm⁻¹) only.\
Multiply by this to convert to m⁻¹ before applying E = hcṽ.\
\
si_prefixes\
true or false.\
If true, the engine auto-generates all prefixed variants at startup.\
Example: J with si_prefixes=true becomes kJ, MJ, GJ, mJ, μJ, nJ\...\
\
dimensions\
The physical dimension of this unit as base quantity exponents.\
Used to check two units are compatible before converting.\
See the DIMENSIONS section below.\
\
CONVERSION TYPES\
\
linear\
Simple multiplication.\
E (in Joules) = value × factor_to_J\
Used for: J, eV, cal, kcal, kJ/mol, Eh, K and all their variants.\
\
photon_wavelength\
For units that describe a photon by its wavelength.\
E (in Joules) = h × c / (value × scale_to_metres)\
Shorter wavelength = higher energy.\
Used for: nm, μm, Å\
\
photon_frequency\
For units that describe a photon by its frequency.\
E (in Joules) = h × (value × scale_to_Hz)\
Higher frequency = higher energy.\
Used for: Hz, GHz, THz\
\
wavenumber\
For cm⁻¹, the standard unit in IR and Raman spectroscopy.\
E (in Joules) = h × c × (value × scale_to_per_metre)\
Proportional to energy. 1 cm⁻¹ = 100 m⁻¹, hence scale_to_per_metre =
100.\
Used for: cm⁻¹\
\
DIMENSIONS\
\
The letters used and what they stand for:\
\
M Mass kilograms (kg)\
L Length metres (m)\
T Time seconds (s)\
N Amount moles (mol) --- only in per-mole units\
\
Energy has dimensions M=1, L=2, T=-2\
This means kg × m² / s², which is exactly how a Joule is defined.\
Every energy unit in the database shares this signature.\
\
Molar energy (kJ/mol, kcal/mol, J/mol) adds N=-1\
Full dimensions: M=1, L=2, T=-2, N=-1\
Meaning: kg × m² / s² / mol\
\
Spectroscopic units have different dimensions because they describe\
photon properties, not energy directly:\
nm, μm, Å → L=1 (they are lengths / wavelengths)\
Hz → T=-1 (it is a frequency, cycles per second)\
cm⁻¹ → L=-1 (wavenumber, cycles per metre)\
\
The engine catches any attempt to directly convert these to energy\
and tells the user to use the Planck-law mode instead.\
\
\
HOW TO ADD A NEW UNIT\
1. Open Database in VS Code\
2. Find the \"units\" array\
3. Copy an existing entry that uses the same type as your new unit\
4. Paste it before the closing \] of the units array\
5. Make sure the entry before yours has a comma after its closing }\
6. Fill in the correct values\
7. Save the file
