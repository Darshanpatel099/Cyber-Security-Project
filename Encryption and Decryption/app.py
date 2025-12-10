from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

# ---------------- MORSE CODE TABLE ----------------
MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

# Reverse Morse Table
REVERSE_MORSE = {v: k for k, v in MORSE.items()}


# -------------- STEP 1: NORMAL → MORSE --------------
def normal_to_morse(text):
    output = []
    for char in text.upper():
        if char in MORSE:
            output.append(MORSE[char])
    return ' '.join(output)


# -------------- STEP 2: MORSE → SHA1 + KEY --------------
def morse_to_sha1(morse, key):
    combined = morse + key
    return hashlib.sha1(combined.encode()).hexdigest()


# -------------- FAKE DECRYPTION STORAGE --------------
DB = {}   # SHA1_HASH : (morse, normal_text)


# -------------- STEP 3: ENCRYPT FUNCTION --------------
def encrypt_process(text, key):
    morse = normal_to_morse(text)
    final_sha1 = morse_to_sha1(morse, key)

    # store for reverse decryption
    DB[final_sha1] = (morse, text)

    return morse, final_sha1


# -------------- STEP 4: DECRYPT FUNCTION --------------
def decrypt_process(sha1_hash, key):
    if sha1_hash not in DB:
        return "Invalid hash or key!", ""

    morse, normal = DB[sha1_hash]
    return morse, normal


# ---------------- FLASK ROUTES ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    result_morse = ""
    result_sha1 = ""
    result_normal = ""

    if request.method == "POST":
        user_input = request.form.get("user_input")
        key = request.form.get("key")
        mode = request.form.get("mode")

        # ENCRYPTION
        if mode == "encrypt":
            morse, sha1_hash = encrypt_process(user_input, key)
            result_morse = morse
            result_sha1 = sha1_hash

        # DECRYPTION
        elif mode == "decrypt":
            morse, normal = decrypt_process(user_input, key)
            result_morse = morse
            result_normal = normal

    return render_template("index.html",
                           morse=result_morse,
                           sha1=result_sha1,
                           normal=result_normal)


if __name__ == "__main__":
    app.run(debug=True)
