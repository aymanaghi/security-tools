import re
from getpass import getpass

def check_password():
    print("\n🔒 SECURITY PASSWORD CHECKER 🔒")
    print("This tool analyzes your password strength and gives personalized suggestions")
    print("Your password is never stored or sent anywhere - analysis happens locally!\n")
    
    while True:
        password = getpass("Enter your password to analyze (or type 'exit' to quit): ")
        
        if password.lower() == 'exit':
            print("\n✅ Thank you for caring about your security!")
            break
        
        if len(password.strip()) == 0:
            print("❌ Please enter a password or type 'exit'")
            continue
        
        analyze_password(password)
        
        print("\n" + "-"*50)
        again = input("Analyze another password? (y/n): ").lower()
        if again != 'y':
            print("\n🔐 Stay secure! Remember: A strong password is your first line of defense.")
            break

def analyze_password(password):
    print("\n" + "="*50)
    print("PASSWORD SECURITY ANALYSIS")
    print("="*50)
    
    suggestions = []
    strength_score = 0
    
    # Check length
    if len(password) < 8:
        suggestions.append("⚠️  Your password is too short! Make it at least 8 characters long.")
    elif len(password) >= 12:
        strength_score += 2
        print("✓ Excellent length (12+ characters)")
    else:
        strength_score += 1
        print("✓ Good length (8-11 characters)")
    
    # Check uppercase
    if re.search("[A-Z]", password):
        strength_score += 1
        print("✓ Contains uppercase letters")
    else:
        suggestions.append("💡 Add uppercase letters (A-Z) - this makes your password much harder to crack!")
    
    # Check lowercase
    if re.search("[a-z]", password):
        strength_score += 1
        print("✓ Contains lowercase letters")
    else:
        suggestions.append("💡 Add lowercase letters (a-z) - mix it up for better security!")
    
    # Check numbers
    if re.search("[0-9]", password):
        strength_score += 1
        print("✓ Contains numbers")
    else:
        suggestions.append("💡 Add numbers (0-9) - this adds another layer of complexity!")
    
    # Check special characters
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 2
        print("✓ Contains special characters")
    else:
        suggestions.append("💡 Add special characters (!@#$%^&* etc.) - this dramatically increases security!")
    
    # Check for common patterns
    common_patterns = ["123", "abc", "password", "qwerty", "admin", "letmein"]
    for pattern in common_patterns:
        if pattern in password.lower():
            suggestions.append(f"🚨 Avoid common patterns like '{pattern}' - hackers try these first!")
            strength_score -= 1
    
    # Check for repeated characters
    if re.search(r"(.)\1{2,}", password):
        suggestions.append("⚠️  Avoid repeating characters (like 'aaa' or '111') - this makes passwords predictable!")
        strength_score -= 1
    
    # Display results
    print(f"\nOverall Strength Score: {strength_score}/7")
    
    if strength_score <= 2:
        print("\n🔴 CRITICAL: Your password is very weak!")
        print("This could be cracked in seconds by automated tools.")
    elif strength_score <= 4:
        print("\n🟡 MODERATE: Your password needs improvement")
        print("This might be cracked within hours or days.")
    else:
        print("\n🟢 STRONG: Excellent password!")
        print("This would take years to crack with current technology.")
    
    # Show personalized suggestions
    if suggestions:
        print("\n" + "="*50)
        print("PERSONALIZED SUGGESTIONS FOR YOUR PASSWORD:")
        print("="*50)
        for i, suggestion in enumerate(suggestions, 1):
            print(f"{i}. {suggestion}")
        
        print("\n" + "="*50)
        print("QUICK TIPS TO IMPROVE YOUR PASSWORD:")
        print("="*50)
        print("✅ Use a mix of uppercase, lowercase, numbers and symbols")
        print("✅ Make it at least 12 characters long")
        print("✅ Avoid personal information (names, birthdays, etc.)")
        print("✅ Consider using a passphrase: 'CorrectHorseBatteryStaple'")
        print("✅ Use a password manager to generate and store strong passwords")
    else:
        print("\n" + "="*50)
        print("🎉 PERFECT SCORE! No improvements needed!")
        print("="*50)
        print("Your password is secure and follows best practices.")
        print("Keep this level of security for all your important accounts!")
