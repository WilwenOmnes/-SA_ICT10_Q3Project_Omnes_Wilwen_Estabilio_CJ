from pyscript import document
import re

# Checks username and password once the button is pressed.
def validate_user(event=None):
    username = document.getElementById("username").value.strip()
    password = document.getElementById("password").value.strip()
    message = document.getElementById("message")

    # Username rules with if and else statements.
    username_valid = (
        username != ""
        and 3 <= len(username) <= 20
        and re.fullmatch(r"[A-Za-z]+", username)
    )

    # Rules with if and else statements.
    password_valid = (
        password != ""
        and len(password) >= 10
        and re.search(r"[A-Za-z]", password) #Compressed so there aren't that many elif statements, or any at all.
        and re.search(r"[0-9]", password) #Also compressed so that making mistakes give out a generalized message of "Please follow rules".
    )

    # Results
    if not username_valid or not password_valid:
        message.innerText = "⚠ Please follow the rules"
        message.style.color = "red"
    else:
        message.innerText = "✅ Sign up successful!"
        message.style.color = "green"
