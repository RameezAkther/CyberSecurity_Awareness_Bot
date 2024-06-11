import json

# List of JSON objects
questions = [
    {
        "question": "Which of the following is NOT a type of malware?",
        "choices": [
            "Virus",
            "Trojan horse",
            "Worms",
            "Ransomware",
            "Dental software"
        ],
        "correct_answer": "Dental software",
        "explanation": "Dental software is a type of software used in dentistry, not a type of malware."
    },
    {
        "question": "What is the primary purpose of a firewall in network security?",
        "choices": [
            "To block all incoming network traffic",
            "To prevent unauthorized access to or from a private network",
            "To encrypt all network traffic",
            "To detect and remove viruses from the network",
            "To manage dental software installations"
        ],
        "correct_answer": "To prevent unauthorized access to or from a private network",
        "explanation": "A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. Its primary purpose is to prevent unauthorized access to or from a private network."
    },
    {
        "question": "What is the main purpose of ransomware?",
        "choices": [
            "To steal personal information",
            "To encrypt files and demand payment for decryption",
            "To monitor network traffic",
            "To provide remote access to a computer",
            "To manage dental records"
        ],
        "correct_answer": "To encrypt files and demand payment for decryption",
        "explanation": "Ransomware is a type of malware that encrypts files on a victim's computer and demands payment for the decryption key."
    },
    {
        "question": "What is the role of an Intrusion Detection System (IDS) in network security?",
        "choices": [
            "To encrypt network traffic",
            "To monitor network traffic and detect suspicious activity",
            "To prevent all incoming network traffic",
            "To manage dental software installations",
            "To provide remote access to a computer"
        ],
        "correct_answer": "To monitor network traffic and detect suspicious activity",
        "explanation": "An Intrusion Detection System (IDS) is a device or software application that monitors a network or systems for malicious activity or policy violations."
    },
    {
        "question": "What is a common best practice for creating strong passwords?",
        "choices": [
            "Use simple and easy-to-guess passwords",
            "Use the same password for multiple accounts",
            "Use a combination of uppercase and lowercase letters, numbers, and symbols",
            "Use the name of your pet as a password",
            "Manage dental records"
        ],
        "correct_answer": "Use a combination of uppercase and lowercase letters, numbers, and symbols",
        "explanation": "Using a combination of uppercase and lowercase letters, numbers, and symbols can help create strong and secure passwords."
    }
]

# Save to a JSON file
with open('questions.json', 'w') as f:
    json.dump(questions, f, indent=2)
