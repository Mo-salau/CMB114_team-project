"""
code written by Yoyo
"""
import os
import json
import random
import csv
import time


"""
Conversion factors to Joules:
E = h*c*wavenumber (in m⁻¹)
E = h*freq
E = h*c/wavelength (handled below)
E = kB * T
1 Hartree = 27.211 eV
"""
TO_JOULES = {
    "J":        1.0,
    "kJ":       1e3,
    "eV":       1.602176634e-19,
    "cal":      4.184,
    "kcal":     4184.0,
    "kJ/mol":   1e3 / 6.02214076e23,
    "kcal/mol": 4184.0 / 6.02214076e23,
    "cm-1":     6.62607015e-34 * 2.99792458e8 * 100,   
    "Hz":       6.62607015e-34,             
    "nm":       None,          
    "K":        1.380649e-23,           
    "Eh":       27.2113862 * 1.602176634e-19
}

"""
open and load the question for beginner and intermediate level stored in JSON file
"""
def load_question():
    with open("question_bank.json","r") as data: 
        question_bank=json.load(data)
        return question_bank
    
"""
function to check the conversion answer
"""
class check:
    """
    convert to Joules first
    """
    def to_joules(self,value, unit):
        if unit == "nm":
            return (H * C) / (value * 1e-9)
        return value * TO_JOULES[unit]

    """
    Converting Joules to the given unit
    """
    def from_joules(self,joules, unit):
        if unit == "nm":
            return (H * C) / joules / 1e-9
        return joules / TO_JOULES[unit]


"""
define class
"""
class quiz_class:
    def beginner(self):
        """
        Quiz at beginner level
        """
        print("Difficulty choosen: Beginner")
        bank = load_question()
        level_questions = bank["beginner"]

        """
        randomly pick 3 questions from the bank
        """
        selected = random.sample(level_questions, 3) 

        """
        count the time
        """
        time_start = time.time() 
        score=0      
        for i,q in enumerate(selected, start=1):
            """time passed"""
            elapsed = time.time() - time_start 
            print(f"\nTime elapsed: {elapsed:.1f} seconds")
            print(f"Question {i}: {q['question']}")
            for option in q["options"]:
                print(option)
            
            """
            error handling: control the user can only enter one character
            """
            while True:
                user_answer = input("\nAnswer (e.g. A):" ).lower().strip()
                if len(user_answer) == 1 and user_answer in "abcd": 
                    break
                else:
                    print("Please enter a valid option (A/B/C/D)")        
            if user_answer == q["answer"].lower():
                print("Correct!")
                score +=1 
                print(f"Explanation: ", q['explanation'])
            else:
                print("Incorrect!")
                """
                let user choose to retry the question the got wrong
                """
                while True:
                    retry = input("Try again? (y/n): ").lower().strip()
                    if retry == "y":
                        while True: 
                            user_answer = input("Answer (e.g. A): ").lower().strip()
                            """
                            error handling
                            """
                            if len(user_answer) != 1 or user_answer not in "abcd":
                                print("Please enter a valid option (A/B/C/D)")
                                continue
                            if user_answer == q["answer"].lower():
                                print("Correct!")
                                print(q["explanation"])
                                score += 1
                                correct = True
                                break                           
                            else:
                                print("Still incorrect.")
                        if correct:
                            break
                    elif retry == "n":
                        print(f"Correct answer: {q['answer']}")
                        print(q["explanation"])
                        break
                    else:
                        print("Please enter y / n.")
            """
            skip showing in the last question
            """                   
            if i != 3:
                input("\nPress Enter to proceed to the next question...")
                       
        print(f"\nFinal Score: {score}/3")
        """stop counting time"""
        time_end = time.time() 
        """get the time taken to complete the quiz"""
        time_taken = round(time_end - time_start, 2) 
        print(f"\nYou took {time_taken} seconds to complete.")
        print("Summary of the quiz stored. Please check in the same directory and open with notepad.\n")
        
        return score, time_taken

    """
    quiz at intermediate level
    """
    def intermediate(self):
        print("Difficulty choosen: Intermediate")
        bank = load_question()
        level_questions = bank["intermediate"]
        selected = random.sample(level_questions, 3)
        score = 0
        time_start=time.time()
        for i,q in enumerate(selected, start=1):
            elapsed = time.time() - time_start 
            print(f"\nTime elapsed: {elapsed:.1f} seconds")
            print(f"Question {i}: {q['question']}")

            """
            error handling: control the user can only enter characters
            """        
            while True:
                user_answer = input("\nAnswer:" ).lower().strip()
                if user_answer:
                    break
                else:
                    print("Please enter an answer in character.")

            if user_answer == q['answer'].lower():
                print("Correct!")
                score +=1
                print(f"Explanation: ",q['explanation'])
            else:
                print("Incorrect!")
                while True:
                    retry = input("Try again? (y/n): ").lower().strip()
                    if retry == "y":
                        while True: 
                            user_answer = input("Answer (e.g. A): ").lower().strip()
                            if user_answer == q["answer"].lower():
                                print("Correct!")
                                print(q["explanation"])
                                score += 1
                                correct = True
                                break                           
                            else:
                                print("Still incorrect.")
                        if correct:
                            break
                    elif retry == "n":
                        print(f"Correct answer: {q['answer']}")
                        print(q["explanation"])
                        break
                    else:
                        print("Please enter y / n.")
                            
            if i != 3:
                input("\nPress Enter to proceed to the next question...")

        print(f"\nFinal Score: {score}/3")
        time_end = time.time()
        time_taken = round(time_end - time_start, 2)
        print(f"\nYou took {time_taken} seconds to complete.")
        print("Summary of the quiz stored. Please check in the same directory and open with notepad.\n")
        return score, time_taken

    """
    quiz at advanced level
    """
    def advanced(self):
        score = 0
        time_start=time.time()
        """
        get units from TO_JOULES
        """
        units = list(TO_JOULES.keys()) 

        """
        generate 3 questions for unit conversion with for loop
        """
        for i in range (1,4):
            unit_from = random.choice(units)
            unit_to = random.choice([x for x in units if x != unit_from]) # avoide choosing the same unit to convert in the question
            if unit_from == "nm":
                value = round(random.uniform(200, 800), 3) # set ranges for getting random number for nm (thats the usual wavelength range)

            elif unit_from == "Hz":
                value = round(random.uniform(1e12, 1e15), 3)

            else:
                value = round(random.uniform(1, 100), 3)
            """
            convert the value in question to get the correct answer, convert it to joule first, then to the target unit
            call the function from converter_engine
            """
            ck = check()
            joules = ck.to_joules(value, unit_from)
            correct = ck.from_joules(joules, unit_to)

            elapsed = time.time() - time_start 
            print(f"\nTime elapsed: {elapsed:.1f} seconds")
            print(f"\nQuestion {i}")
            print(f"Convert {value} {unit_from} to {unit_to} (enter the power to e, e.g.1.23e-19, and correct the answer to 3 decimal places)")
            while True:
                user_input = input(f"Answer in {unit_to}: ").strip()

                """
                error handling: control the user can only enter number
                """
                try:
                    user_answer = float(user_input)
                    break
                except ValueError:
                    print("Please enter a valid number (e.g. 1.23e-19)")
            """
            allow error
            """
            if correct != 0 and abs(user_answer - correct) / correct < 0.01:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
                while True:
                    retry = input("Try again? (y/n): ").lower().strip()
                    if retry == "y":
                            try:
                                user_answer = float(user_input)
                            except ValueError:
                                print("Please enter a number.")
                                continue
                            if abs(user_answer - correct) / correct < 0.01 and correct != 0:
                                print("Correct!")
                                score += 1
                                correct = True
                                break                           
                            else:
                                print("Still incorrect.")
                    elif retry == "n":
                        print(f"Correct answer: {correct}")
                        break
                    else:
                        print("Please enter y / n.")

            if i != 3:
                input("\nPress Enter to proceed to the next question...")

        print(f"\nFinal Score: {score}/3")
        time_end = time.time()
        time_taken = round(time_end - time_start, 2)
        print(f"\nYou took {time_taken} seconds to complete.")
        print("Summary of the quiz stored. Please check in the same directory and open with notepad.\n")
        return score, time_taken

"""
print a summary of the quiz
"""
def summary(username, difficulty, score, time_taken):
    file_exists = os.path.isfile("score.csv")
    with open("score.csv", "a",newline = "") as csv_file:
        writer=csv.writer(csv_file)

        """only write the row's titles if they are not exist in the file"""
        if not file_exists: 
            writer.writerow(["Username", "Difficulty", "Score /3", "Percentage", "Time taken"])
        writer.writerow([username, difficulty, score, f"{(score/3)*100}%", f"{time_taken} s"])

"""
class for leaderboard
"""
class ranking:
    def leaderboard(self):
        results=[]
        with open("score.csv", "r") as f:
            reader = csv.reader(f)
            """
            skip header row
            """
            next(reader) 
            for row in reader:
                if len(row) < 4:
                    continue
                name = row[0]
                difficulty = row[1]
                score = int(row[2])
                """
                compare using float for percentage and time
                """
                percent = float(row[3].replace("%", "")) 
                time_taken = float(row[4].replace("s", ""))
                results.append((name, difficulty, score, percent, time_taken))
        results.sort(key=lambda x: x[2], reverse=True)
        print("\nLEADERBOARD ")
        print("-" * 10)
        print("Ranking | Username | Difficulty | Score /3 | Percentage (%) | Time taken (s)")

        for i, r in enumerate(results[:10], start=1):
            name, diff, score, percent, time_taken = r
            print(f"{i} | {name} | {diff} | {score}/3 | {percent}% | {time_taken}")

"""
class to run the quiz
"""
def run_quiz():
    print("\n--- UNIT CONVERSION QUIZ ---")
    """enter name before choosing the difficulty"""
    while True:
        username = input("Enter your username: ").strip()
        if len(username) >= 3:
            username = username.capitalize()
            break
        else:
            print("Username should be at least 3 characters.")

    while True:
        print("Choose a difficulty for the quiz")
        print("\n 1. Beginner")
        print(" 2. Intermediate")
        print(" 3. Advanced")
        print(" 4. Leaderboard")
        print(" q. Quit")

        """
        user can choose the difficulty or to quit the quiz
        """
        choice = input("\n  Select: ").strip().lower()

        qc = quiz_class()
        rk = ranking()

        if choice == "1":
            score, time_taken = qc.beginner()
            summary(username, "Beginner", score, time_taken)

        elif choice == "2":
            score, time_taken = qc.intermediate()
            summary(username, "Intermediate", score, time_taken)

        elif choice == "3":
            score, time_taken = qc.advanced()
            summary(username, "Advanced", score, time_taken)

        elif choice == "4":
            rk.leaderboard()

        elif choice == "q":
            print("\n  Goodbye!\n")
            print("\n========================================")
            print("      ENERGY UNIT CONVERTER v1.0")
            print("========================================")
            return
        else:
            print("  Invalid option.")
    
    run_quiz()