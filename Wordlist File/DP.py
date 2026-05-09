#!/usr/bin/env python3
# ============================================================
# CUSTOMIZABLE MEGA WORDLIST GENERATOR
# Created by: HackerDP
# For Educational Purposes Only
# ============================================================

import time
import os
import sys

def print_banner():
    print("\n" + "="*70)
    print("    CUSTOMIZABLE MEGA WORDLIST GENERATOR".center(70))
    print("        Created by: HackerDP".center(70))
    print("    [For Educational Purposes Only]".center(70))
    print("="*70 + "\n")

def get_user_config():
    """Get all configuration from user"""
    
    print("[*] CONFIGURATION SETUP")
    print("-" * 50)
    
    # Output file name
    print("\n[1] OUTPUT FILE NAME")
    print("    Default: hackerdp_wordlist.txt")
    custom_name = input("    Enter custom name (or press Enter for default): ").strip()
    if custom_name:
        if not custom_name.endswith('.txt'):
            custom_name += '.txt'
        output_file = custom_name
    else:
        output_file = "hackerdp_wordlist.txt"
    
    # Minimum length
    print("\n[2] MINIMUM LENGTH")
    print("    Default: 8 characters")
    try:
        min_len = int(input("    Enter minimum length (press Enter for 8): ").strip() or "8")
        if min_len < 4:
            print("    [!] Minimum length too small! Setting to 4")
            min_len = 4
    except ValueError:
        min_len = 8
    print(f"    ✓ Minimum length: {min_len} characters")
    
    # Maximum length
    print("\n[3] MAXIMUM LENGTH")
    print("    Default: 20 characters")
    print("    Options: 8, 12, 16, 20, 24, 30, 50")
    try:
        max_len = int(input("    Enter maximum length (press Enter for 20): ").strip() or "20")
        if max_len < min_len:
            print(f"    [!] Max length can't be less than min length! Setting to {min_len + 5}")
            max_len = min_len + 5
    except ValueError:
        max_len = 20
    print(f"    ✓ Maximum length: {max_len} characters")
    
    # Target combinations
    print("\n[4] TARGET COMBINATIONS")
    print("    Options:")
    print("       1 → 1 Crore (10,000,000)")
    print("       5 → 5 Crore (50,000,000)")
    print("       10 → 10 Crore (100,000,000)")
    print("       20 → 20 Crore (200,000,000)")
    print("       50 → 50 Crore (500,000,000)")
    
    target_choice = input("\n    Enter choice (1/5/10/20/50) or custom number: ").strip()
    
    if target_choice == '1':
        target = 10_000_000
        target_name = "1 Crore"
    elif target_choice == '5':
        target = 50_000_000
        target_name = "5 Crore"
    elif target_choice == '10':
        target = 100_000_000
        target_name = "10 Crore"
    elif target_choice == '20':
        target = 200_000_000
        target_name = "20 Crore"
    elif target_choice == '50':
        target = 500_000_000
        target_name = "50 Crore"
    else:
        try:
            target = int(float(target_choice) * 10000000)
            target_name = f"{target_choice} Crore"
        except:
            target = 100_000_000
            target_name = "10 Crore (Default)"
    
    print(f"    ✓ Target: {target_name} ({target:,} combinations)")
    
    print("\n" + "="*70)
    print("[*] CONFIGURATION SUMMARY")
    print("="*70)
    print(f"    Output File      : {output_file}")
    print(f"    Length Range     : {min_len} - {max_len} characters")
    print(f"    Target           : {target_name} ({target:,})")
    print("="*70)
    
    confirm = input("\n[?] Proceed with this configuration? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("[!] Exiting...")
        sys.exit()
    
    return output_file, min_len, max_len, target

print_banner()
output_file, min_len, max_len, target = get_user_config()

start_time = time.time()

# ============ EXTENSIVE COMMON PASSWORDS (Most used passwords globally) ============
common_words = [
    # Top 50 most common passwords
    '12345678', '123456789', 'qwerty123', 'password123', '1234567890',
    'admin123', 'qwertyuiop', 'iloveyou123', 'sunshine123', 'password1',
    'welcome123', 'dragon123', 'master123', 'football123', 'baseball123',
    'superman123', 'princess1', 'trustno1', 'letmein123', 'monkey123',
    'shadow123', 'secret123', 'ninja123', 'matrix123', 'hello123',
    'world123', 'hacker123', 'kali123', 'linux123', 'windows123',
    'adminadmin', 'passwordpass', 'qwertyqwerty', '123123123', 'abc123456',
    'test1234', 'demo1234', 'user1234', 'root1234', 'pass123456',
    'mypassword', 'mypass123', 'mypassword1', 'password2024', 'admin2024',
    'user2024', 'root2024', 'test2024', 'demo2024', 'welcome2024'
]

# More common base words
base_words = [
    'admin', 'password', 'user', 'root', 'test', 'demo', 'hacker', 'kali',
    'linux', 'windows', 'apple', 'google', 'facebook', 'amazon', 'microsoft',
    'netflix', 'spotify', 'instagram', 'twitter', 'whatsapp', 'youtube',
    'gmail', 'outlook', 'yahoo', 'hotmail', 'github', 'stackoverflow'
]

# Common names (most popular)
names = [
    'john', 'james', 'robert', 'michael', 'william', 'david', 'joseph',
    'charles', 'thomas', 'christopher', 'daniel', 'matthew', 'anthony',
    'donald', 'mark', 'paul', 'steven', 'andrew', 'kenneth', 'joshua',
    'mary', 'patricia', 'jennifer', 'linda', 'elizabeth', 'barbara',
    'susan', 'jessica', 'sarah', 'karen', 'lisa', 'nancy', 'betty',
    'helen', 'sandra', 'donna', 'carol', 'ruth', 'sharon', 'michelle'
]

# Common sports teams
sports = [
    'cricket', 'football', 'hockey', 'tennis', 'baseball', 'basketball',
    'soccer', 'rugby', 'golf', 'volleyball', 'badminton', 'swimming'
]

# Common animals
animals = [
    'dragon', 'tiger', 'lion', 'elephant', 'monkey', 'dolphin', 'eagle',
    'shark', 'wolf', 'panda', 'koala', 'kangaroo', 'cheetah', 'leopard'
]

# Common years
years = [str(y) for y in range(1970, 2030)]

# Numbers
numbers_2digit = [f"{i:02d}" for i in range(100)]       # 00-99
numbers_3digit = [f"{i:03d}" for i in range(1000)]      # 000-999
numbers_4digit = [f"{i:04d}" for i in range(10000)]     # 0000-9999

# Special characters
specials = ['!', '@', '#', '$', '%', '&', '*', '?']

# Common suffixes
suffixes = ['123', '1234', '12345', '2024', '2025', '123456', '!', '@', '#']

# Common prefixes
prefixes = ['admin', 'user', 'pass', 'my', 'your', 'super', 'mega']

print("\n[*] EXTENSIVE WORDLIST STATISTICS:")
print("="*50)
print(f"    Common passwords    : {len(common_words)}")
print(f"    Base words          : {len(base_words)}")
print(f"    Names               : {len(names)}")
print(f"    Sports              : {len(sports)}")
print(f"    Animals             : {len(animals)}")
print(f"    Years               : {len(years)}")
print(f"    Special chars       : {len(specials)}")
print(f"    4-digit numbers     : {len(numbers_4digit)}")
print(f"    3-digit numbers     : {len(numbers_3digit)}")
print(f"    2-digit numbers     : {len(numbers_2digit)}")
print(f"    Suffixes            : {len(suffixes)}")
print(f"    Prefixes            : {len(prefixes)}")
print("="*50)

total_combinations = len(common_words) * len(numbers_4digit) + \
                     len(base_words) * len(suffixes) * len(specials) + \
                     len(names) * len(numbers_4digit)
print(f"\n[*] Approximate combinations possible: {total_combinations:,}")
print(f"[*] Target: {target:,}\n")

total = 0

def write_password(f, password):
    """Write password if length within range"""
    global total
    if min_len <= len(password) <= max_len:
        f.write(password + '\n')
        total += 1
        return True
    return False

try:
    with open(output_file, 'w', encoding='utf-8', errors='ignore') as f:
        
        # Header with By HackerDP
        f.write("#" + "="*70 + "\n")
        f.write("# EXTENSIVE MEGA WORDLIST GENERATOR\n")
        f.write(f"# Length Range: {min_len} - {max_len} characters\n")
        f.write(f"# Target: {target:,} combinations\n")
        f.write("# Created By: HackerDP\n")
        f.write("# For Educational Purposes Only\n")
        f.write("#" + "="*70 + "\n\n")
        
        # ============================================================
        # PATTERN 1: Common passwords + number variations
        # ============================================================
        print("[1/8] Generating: Common passwords + numbers...")
        for word in common_words:
            for num in numbers_4digit:
                password = word + num
                write_password(f, password)
                if total % 5_000_000 == 0 and total > 0:
                    print(f"     → {total:,} / {target:,} ({(total/target)*100:.1f}%)")
            if total >= target:
                break
        
        # ============================================================
        # PATTERN 2: Base word + suffix + special
        # ============================================================
        if total < target:
            print("[2/8] Generating: Base word + suffix + special...")
            for word in base_words:
                for suffix in suffixes:
                    for sp in specials:
                        password = word + suffix + sp
                        write_password(f, password)
                        if total >= target:
                            break
                    if total >= target:
                        break
                if total >= target:
                    break
                if total % 2_000_000 == 0 and total > 0:
                    print(f"     → {total:,} / {target:,} ({(total/target)*100:.1f}%)")
        
        # ============================================================
        # PATTERN 3: Name + birth year (1980-1999)
        # ============================================================
        if total < target:
            print("[3/8] Generating: Name + birth year...")
            birth_years = [str(y) for y in range(1980, 2000)]
            for name in names:
                for year in birth_years:
                    password = name + year
                    write_password(f, password)
                    if total >= target:
                        break
                if total >= target:
                    break
                if total % 2_000_000 == 0 and total > 0:
                    print(f"     → {total:,} / {target:,} ({(total/target)*100:.1f}%)")
        
        # ============================================================
        # PATTERN 4: Word + 4digit (Basic)
        # ============================================================
        if total < target:
            print("[4/8] Generating: Base word + 4digit number...")
            all_words = base_words + names + sports + animals
            for word in all_words:
                for num in numbers_4digit:
                    password = word + num
                    write_password(f, password)
                    if total >= target:
                        break
                if total >= target:
                    break
                if total % 2_000_000 == 0 and total > 0:
                    print(f"     → {total:,} / {target:,} ({(total/target)*100:.1f}%)")
        
        # ============================================================
        # PATTERN 5: Word + year + special
        # ============================================================
        if total < target:
            print("[5/8] Generating: Base word + year + special...")
            all_words = base_words[:20] + names[:20]
            for word in all_words:
                for year in years:
                    for sp in specials:
                        password = word + year + sp
                        write_password(f, password)
                        if total >= target:
                            break
                    if total >= target:
                        break
                if total >= target:
                    break
                if total % 2_000_000 == 0 and total > 0:
                    print(f"     → {total:,} / {target:,} ({(total/target)*100:.1f}%)")
        
        # ============================================================
        # PATTERN 6: Word1 + Word2 (Common combos)
        # ============================================================
        if total < target:
            print("[6/8] Generating: Word1 + Word2 combinations...")
            word_pairs = [
                ('admin', 'user'), ('password', '123'), ('hello', 'world'),
                ('john', 'doe'), ('james', 'bond'), ('super', 'man'),
                ('bat', 'man'), ('spider', 'man'), ('iron', 'man'),
                ('captain', 'america'), ('black', 'widow'), ('thor', 'hammer')
            ]
            for w1, w2 in word_pairs:
                password = w1 + w2
                write_password(f, password)
                for num in numbers_2digit:
                    password = w1 + w2 + num
                    write_password(f, password)
                if total % 2_000_000 == 0 and total > 0:
                    print(f"     → {total:,} / {target:,} ({(total/target)*100:.1f}%)")
        
        # ============================================================
        # PATTERN 7: Prefix + word (mypassword, yourpassword)
        # ============================================================
        if total < target:
            print("[7/8] Generating: Prefix + word...")
            for prefix in prefixes:
                for word in base_words[:15]:
                    password = prefix + word
                    write_password(f, password)
                    for num in numbers_2digit:
                        password = prefix + word + num
                        write_password(f, password)
                    if total >= target:
                        break
                if total >= target:
                    break
        
        # ============================================================
        # PATTERN 8: Word + special + word
        # ============================================================
        if total < target:
            print("[8/8] Generating: Word + special + word...")
            for w1 in base_words[:15]:
                for sp in specials:
                    for w2 in base_words[:15]:
                        password = w1 + sp + w2
                        write_password(f, password)
                        if total >= target:
                            break
                    if total >= target:
                        break
                if total >= target:
                    break
        
        # Footer
        f.write("\n" + "#" + "="*70 + "\n")
        f.write(f"# Total Combinations Generated: {total:,}\n")
        f.write(f"# Length Range: {min_len} - {max_len}\n")
        f.write("# Created By: HackerDP\n")
        f.write("# End of Wordlist\n")
        f.write("#" + "="*70 + "\n")

except KeyboardInterrupt:
    print("\n\n[!] Stopped by user! Saving partial wordlist...")

end_time = time.time()
time_taken = (end_time - start_time) / 60

# Final Report
print("\n" + "="*70)
print("                    FINAL REPORT".center(70))
print("="*70)
print(f"  Output File        : {output_file}")
print(f"  Total Generated    : {total:,}")
print(f"  Target             : {target:,}")
print(f"  Achievement        : {'✅ ACHIEVED' if total >= target else '⚠️ PARTIAL'}")
print(f"  Time taken         : {time_taken:.2f} minutes")
print("="*70)
print("              Created By: HackerDP".center(70))
print("         For Educational Purposes Only".center(70))
print("="*70 + "\n")

if os.path.exists(output_file):
    size_bytes = os.path.getsize(output_file)
    size_mb = size_bytes / (1024 * 1024)
    size_gb = size_mb / 1024
    
    print("[INFO] File Information:")
    print(f"  - File name: {output_file}")
    if size_gb >= 1:
        print(f"  - File size: {size_gb:.2f} GB")
    else:
        print(f"  - File size: {size_mb:.2f} MB")
    
    # Show sample passwords
    print("\n[INFO] Sample Passwords Generated:")
    count = 0
    with open(output_file, 'r') as f:
        for line in f:
            if not line.startswith('#') and min_len <= len(line.strip()) <= max_len:
                print(f"  {line.strip()}")
                count += 1
                if count >= 10:
                    break
