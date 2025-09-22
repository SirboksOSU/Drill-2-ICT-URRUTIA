from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value

    # Clear the output div first
    document.querySelector("#output").innerText = ""

    # Multiline message using input values
    message = f"""👤 Student Profile
    Name   : {Lucas Urrutia}
    Age    : {15}
    School : {OBMC}

    ✏️ Notes:
    {Lucas} is currently {15} years old and studies at {OBMC}.
    This information was gathered through input fields and displayed using
    a multiline string in Python via PyScript.
    """

    display(message, target="output")
