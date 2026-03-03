from pyscript import display, document

def intrams_checker(e):
    document.getElementById('output').innerHTML = ''
    document.getElementById('image').innerHTML = ''

    reg_el = document.querySelector('input[name="registration"]:checked')
    clear_el = document.querySelector('input[name="clearance"]:checked')

    if reg_el is None or clear_el is None:
        display("Please answer all Yes / No questions.", target="output")
        return

    # safely get values
    registration = getattr(reg_el, "value", None)
    clearance = getattr(clear_el, "value", None)

    pe_grade_el = document.getElementById("pe_grade")
    level_el = document.getElementById("level")
    section_el = document.getElementById("section")
    sport_el = document.getElementById("sport")

    # check if inputs exist before reading .value
    if None in [pe_grade_el, level_el, section_el, sport_el]:
        display("Some inputs are missing from the page.", target="output")
        return

    pe_grade = pe_grade_el.value
    try:
        grade_level = int(level_el.value)
    except ValueError:
        display("Invalid grade level.", target="output")
        return

    section = section_el.value
    sport = sport_el.value

    if registration == "undecided" or clearance == "undecided":
        display("Please pick yes or no.", target="output")
        return

    if registration != "registered":
        display(
            "Not eligible: student is not registered for Intrams.",
            target="output"
        )
        return

    if clearance != "cleared":
        display(
            "Not eligible: medical clearance required.",
            target="output"
        )
        return

    # Main selection logic
    if grade_level in [7, 10] and section == "emerald":
        display(
            f"Congrats! You are part of the Green Hornets {sport.title()} Tryout!",
            target="output"
        )
        document.getElementById("image").innerHTML = "<img src='GREEN.jpg'>"

    elif grade_level in [7, 10] and section == "ruby":
        display(
            f"Congrats! You are part of the Yellow Tigers {sport.title()} Tryout!",
            target="output"
        )
        document.getElementById("image").innerHTML = "<img src='YELLOW.jpg'>"

    elif grade_level in [8, 9] and section == "emerald":
        display(
            f"Congrats! You are part of the Red Bulldogs {sport.title()} Tryout!",
            target="output"
        )
        document.getElementById("image").innerHTML = "<img src='RED.jpg'>"

    elif grade_level in [8, 9] and section == "ruby":
        display(
            f"Congrats! You are part of the Blue Bears {sport.title()} Tryout!",
            target="output"
        )
        document.getElementById("image").innerHTML = "<img src='BLUE.jpg'>"

    else:
        display(
            "Congrats! You are registered for Intrams. Please wait for further instructions.",
            target="output"
        )