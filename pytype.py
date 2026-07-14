import argparse 
import time
import random
import json
import os
from datetime import datetime



def make_sentence_from_file(file_path='words.txt', length=35):
    try:

        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().split()

            if not words:
                return "The file is empty."

            chosen_words = random.choices(words, k=length)

            return " ".join(chosen_words).capitalize() + "."

    except FileNotFoundError:
        return f"Error: Could not find the file '{file_path}'. Make sure it is in the same folder as this script."

        print(make_sentence_from_file())



def calculate_accuracy(target_text, typed_text):

    clean_target = target_text.lower().replace(".", "")
    clean_typed = typed_text.lower().replace(".", "")
    
    target_words = clean_target.split()
    typed_words = clean_typed.split()
    
    correct_words = 0
    correct_chars = 0
    shortest_length = min(len(target_words), len(typed_words))
    
    for i in range(shortest_length):
        if target_words[i] == typed_words[i]:
            correct_words += 1
            correct_chars += len(target_words[i]) + 1
            
    if len(target_words) == 0:
        return 0, 0, 0
        
    accuracy = (correct_words / len(target_words)) * 100
    
    return accuracy, correct_words, correct_chars


def calculate_wpm(start_time, end_time, correct_chars):
    seconds_passed = end_time - start_time
    minutes_passed = seconds_passed / 60

    wpm = (correct_chars / 5) / minutes_passed
    
    print(f"Your speed is {round(wpm, 2)} WPM")
    return wpm

def save_result(wpm, accuracy):
    filepath = "history.json"
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    new_record = {
        "date": current_time,
        "wpm": round(wpm, 2),
        "accuracy": round(accuracy, 2)
    }
    
    if os.path.exists(filepath):

        with open(filepath, 'r') as file:
            history_list = json.load(file)
    else:

        history_list = []
        

    history_list.append(new_record)
    
    with open(filepath, 'w') as file:
        json.dump(history_list, file, indent=4)
        
    print("\nResult saved to history!")



def run_test(time_limit=None):
    target_text = make_sentence_from_file()

    BOLD = '\033[1m'
    CYAN = '\033[96m' 
    RESET = '\033[0m'
    
    print("\n" + "="*40)
    print(" TYPECTL - TYPING TEST")
    print("="*40)
    
    input("\nPress [ENTER] when you are ready to start typing...")
    
    start_time = time.time()
    
    print(f"\n  {BOLD}{CYAN}{target_text}{RESET}\n")    
    typed_text = input("-> ")
    
    end_time = time.time()
    
    accuracy, correct_words, correct_chars = calculate_accuracy(target_text, typed_text)
    
    print("\n--- RESULTS ---")
    wpm = calculate_wpm(start_time, end_time, correct_chars)
    print(f"Your accuracy is {round(accuracy, 2)}%")
    
    save_result(wpm, accuracy)


def show_stats():
    filepath = "history.json"
    
    if not os.path.exists(filepath):
        print("\nNo history found! Take a typing test first to generate some stats.")
        return
        
    with open(filepath, 'r') as file:
        history_list = json.load(file)
        
    if len(history_list) == 0:
        print("\nYour history is empty! Take a test first.")
        return

    total_tests = len(history_list)

    wpms = [record["wpm"] for record in history_list]
    accuracies = [record["accuracy"] for record in history_list]
    
    best_wpm = max(wpms)
    avg_wpm = sum(wpms) / total_tests
    avg_accuracy = sum(accuracies) / total_tests
    
    print("\n" + "="*40)
    print(" TYPECTL - LIFETIME STATS")
    print("="*40)
    print(f"Tests Taken:      {total_tests}")
    print(f"Highest Speed:    {best_wpm:.2f} WPM")
    print(f"Average Speed:    {avg_wpm:.2f} WPM")
    print(f"Average Accuracy: {avg_accuracy:.2f}%")
    print("="*40 + "\n")

def show_history():
    filepath = "history.json"
    
    if not os.path.exists(filepath):
        print("\nNo history found! Take a typing test first.")
        return
        
    with open(filepath, 'r') as file:
        history_list = json.load(file)
        
    if len(history_list) == 0:
        print("\nYour history is empty! Take a test first.")
        return
        
    recent_history = history_list[-10:]
    
    print("\n" + "="*55)
    print(" TYPECTL - RECENT HISTORY (Last 10 Tests)")
    print("="*55)
    
    for i, record in enumerate(recent_history, 1):
        date = record["date"]
        wpm = record["wpm"]
        accuracy = record["accuracy"]
        
        print(f"{i:2}. Date: {date}  |  Speed: {wpm:5.2f} WPM  |  Accuracy: {accuracy:6.2f}%")
        
    print("="*55 + "\n")


def main():
    parser = argparse.ArgumentParser(description="typectl - A Terminal Typing Trainer")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    test_parser = subparsers.add_parser("test", help="Start a typing test")
    test_parser.add_argument("--seconds", type=int, help="Time limit in seconds")
    
    stats_parser = subparsers.add_parser("stats", help="Show your lifetime typing stats")
    
    history_parser = subparsers.add_parser("history", help="Show your recent test history")
    
    args = parser.parse_args()
    
    if args.command == "test":
        run_test(time_limit=args.seconds)
    elif args.command == "stats":
        show_stats()
    elif args.command == "history":
        show_history()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()