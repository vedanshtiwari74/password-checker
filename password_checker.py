import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        print("❌ Password is too short (min 8 characters).")

    # Uppercase and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        print("❌ Use both UPPERCASE and lowercase letters.")

    # Numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        print("❌ Add at least one number (0–9).")

    # Symbols
    if re.search(r'[\W_]', password):
        score += 1
    else:
        print("❌ Add at least one symbol (!, @, #, etc.).")

    # Final result
    if score == 4:
        print("✅ Your password is STRONG.")
    elif score >= 2:
        print("⚠️ Your password is MODERATE.")
    else:
        print("❌ Your password is WEAK.")

# ---- MAIN PROGRAM ----
print("🔐 Password Strength Checker 🔐")
user_password = input("Enter your password to test: ")
check_password_strength(user_password)
