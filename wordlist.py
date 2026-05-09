#!/usr/bin/env python3
# Wordlist Generator for Educational Purposes
# Made by Hacker DP

import itertools

def generate_wordlist():
    print("\n" + "="*50)
    print("    WORDLIST GENERATOR TOOL".center(50))
    print("      Made by Hacker DP".center(50))
    print("    [For Educational Use Only]".center(50))
    print("="*50 + "\n")
    
    print("[!] Disclaimer: Use this tool only on systems you own")
    print("    or have explicit permission to test.\n")
    
    # Collect user inputs
    print("[+] Enter base words (comma-separated):")
    base_input = input("> ").strip()
    base_words = [w.strip() for w in base_input.split(",") if w.strip()]
    
    print("\n[+] Enter numbers to append/prepend (comma-separated, e.g., 123,2024):")
    num_input = input("> ").strip()
    numbers = [n.strip() for n in num_input.split(",") if n.strip()]
    
    print("\n[+] Enter special characters (comma-separated, e.g., !,@,#):")
    special_input = input("> ").strip()
    special_chars = [s.strip() for s in special_input.split(",") if s.strip()]
    
    print("\n[+] Enter common years or other items (optional):")
    extra_input = input("> ").strip()
    extra_items = [e.strip() for e in extra_input.split(",") if e.strip()] if extra_input else []
    
    print("\n[+] Do you want to combine words? (y/n):")
    combine = input("> ").strip().lower() == 'y'
    
    print("\n[+] Max length for each entry (0 = no limit):")
    try:
        max_len = int(input("> ").strip())
    except ValueError:
        max_len = 0
    
    print("\n[+] Generating wordlist... (this may take a moment)\n")
    
    wordlist = set()
    
    # Add base words as is
    for word in base_words:
        if max_len == 0 or len(word) <= max_len:
            wordlist.add(word)
    
    # Add combinations with numbers (appended and prepended)
    for word in base_words:
        for num in numbers:
            combo1 = word + num
            combo2 = num + word
            if max_len == 0 or len(combo1) <= max_len:
                wordlist.add(combo1)
            if max_len == 0 or len(combo2) <= max_len:
                wordlist.add(combo2)
    
    # Add combinations with special characters
    for word in base_words:
        for sp in special_chars:
            combo = word + sp
            combo2 = sp + word
            if max_len == 0 or len(combo) <= max_len:
                wordlist.add(combo)
            if max_len == 0 or len(combo2) <= max_len:
                wordlist.add(combo2)
    
    # Add numbers and specials themselves if they are short enough
    for num in numbers:
        if max_len == 0 or len(num) <= max_len:
            wordlist.add(num)
    for sp in special_chars:
        if max_len == 0 or len(sp) <= max_len:
            wordlist.add(sp)
    
    # Add extra items
    for extra in extra_items:
        if max_len == 0 or len(extra) <= max_len:
            wordlist.add(extra)
    
    # Combine words if requested
    if combine and len(base_words) >= 2:
        for r in range(2, min(3, len(base_words)) + 1):
            for combo in itertools.permutations(base_words, r):
                combined = ''.join(combo)
                if max_len == 0 or len(combined) <= max_len:
                    wordlist.add(combined)
    
    # Also combine word+number+special
    for word in base_words:
        for num in numbers:
            for sp in special_chars:
                wns = word + num + sp
                if max_len == 0 or len(wns) <= max_len:
                    wordlist.add(wns)
                
                nws = num + word + sp
                if max_len == 0 or len(nws) <= max_len:
                    wordlist.add(nws)
    
    # Save to file
    output_file = "word.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in sorted(wordlist):
            f.write(word + '\n')
    
    print(f"[+] Success! Wordlist saved to '{output_file}'")
    print(f"[+] Total unique words generated: {len(wordlist)}")
    print("\n[!] Remember: Use this only for ethical, educational purposes!\n")
    print("="*50)
    print("       Tool Created by Hacker DP".center(50))
    print("="*50 + "\n")

if __name__ == "__main__":
    try:
        generate_wordlist()
    except KeyboardInterrupt:
        print("\n\n[!] Operation cancelled by user.")
    except Exception as e:
        print(f"\n[!] An error occurred: {e}")
