# CMB114 CW2 Unit converter and energy quiz tool by Yoyo and Muhammed

The code is divided between folders `mohammed` and `yoyo` for the group project. The code division is indicated with the file name and also typed in each file.

## General info
This tool aims to let users convert an energy value to a supported unit and test the understanding of energy.

You can run the code by calling
~~~~
python driver.py
~~~~
Constants are stored in a PhysicalConstants class inside converter_engine.py. Values are from NIST CODATA 2018
## Running from GitHub
We came across various problems when trying to run the code through git due to our folder structures and python not knowing where some files were, so empty `__init__.py` files
were added to both folders. This tells Python that the folders have python in them and should treat them as packages.

## 1. Unit Conversion
Converts any energy value to all supported units at once.
Units are grouped by category (SI, atomic, thermochemical, molar, thermal, spectroscopic).
Spectroscopic units (K, Hz, nm, cm-1) show a note explaining how they are converted.

## 2. Physics Mode
For when you have a physical quantity rather than a direct energy value.
Supports: Planck (frequency), Planck (wavelength), Einstein (E=mc^2),
Boltzmann (thermal energy), Voltage, and molar scaling in both directions.

## 3. Compatibility Check
Checks whether two units measure the same physical quantity using
the dimension data stored in the database. E.g: J and kJ are
compatible, but J and nm are not.

## 4. Conversion History
Stores the last 10 conversions performed and displays them in a table.
The user can also clear the history from this menu.

## 5. Supported Units
Lists all units the converter supports, grouped by category,
pulled directly from the database.

## 6. How To Use
A built-in help guide explaining what each mode does.

## 7. Energy quiz
The quiz covers the frequency, wavelengths and energy in physical chemistry. It is divided into three difficulties: Beginner, Intermediate and Advanced.
It has different question types, such as multiple choice, definition, and unit conversion.
For multiple-choice and definition questions, the questions are stored in a JSON file (question_bank.json).
For unit conversion questions, the code randomly generates numbers and units for the questions. The units are from the dictionary in the code.
At the end of the quiz, a summary report will be exported. Leaderboard is also available if there is more than one attempt at the quiz.
Explaination and correct answer are shown after getting the question correctly or choose not to retry after getting the question wrong.

### How to use the quiz function 
1. When entering the menu, choose "2. Energy quiz".
2. Enter a username (at least 3 characters) and choose a difficulty.
3. Complete the quiz. The quiz contains 3 questions in each difficulty. If you get any questions wrong, you can retry the question.
4. You will get the score and time taken after completing the quiz.
5. A summary report exported as a CSV file. Open it from the same directory with Notepad, and you can see all the records.

### How to access the leaderboard
Leaderboard is available when more than one attempts recorded. Higher ranking when you get a higher score.
To access the leaderboard, you will need to go back to the page where you chose the difficulty. Then, enter "4" to choose "4. Leaderboard".

### References for Energy quiz
1. Time library for the quiz: https://docs.python.org/3/library/time.html
2. Values for the five constants: https://physics.nist.gov/cuu/Constants/
