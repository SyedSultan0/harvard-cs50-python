# 🔐 Password Manager

#### Video Demo: 111111111

#### Description:

This project is a Python-based command-line Password Manager that allows users to securely store and manage account credentials. It focuses on basic cybersecurity principles such as hashing, encryption, password strength analysis, and breach checking using real-world tools and APIs.

The program starts with a simple signup/login system where the master password is hashed using SHA-256 and stored securely. Once logged in, users can add accounts (like Google or Apple), search saved credentials, and delete them when needed.

Each account password is encrypted using Fernet symmetric encryption, ensuring that stored data cannot be read without the encryption key. Email inputs are validated using the `email-validator` library to avoid invalid entries.

The project also includes a password strength checker powered by the `zxcvbn` library, which gives a score, crack-time estimate, and improvement suggestions. Additionally, it integrates the "Have I Been Pwned" API to check whether a password has appeared in known data breaches using a privacy-safe method.

All data is stored locally using JSON files (`accounts.json` and `restricted.json`), keeping the project simple and easy to run without external databases.

Overall, this project demonstrates how core security concepts like hashing, encryption, validation, and API integration can be combined into a functional and practical application.

In the end this was CS50...
