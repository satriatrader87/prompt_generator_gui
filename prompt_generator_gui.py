
import PySimpleGUI as sg
import json
import os

PROMPT_HISTORY_FILE = "previous_prompt.json"

def save_prompt_to_file(prompt, filename="generated_prompt.txt"):
    with open(filename, "w") as file:
        file.write(prompt)

def load_previous_prompt():
    if os.path.exists(PROMPT_HISTORY_FILE):
        with open(PROMPT_HISTORY_FILE, "r") as file:
            return json.load(file)
    return {}

def save_prompt_history(prompt_data):
    with open(PROMPT_HISTORY_FILE, "w") as file:
        json.dump(prompt_data, file, indent=4)

def generate_prompt(prompt_type, details):
    if prompt_type == "Character":
        prompt = (f"{details['name']} is described as having {details['physical']} appearance, wearing {details['outfit']}. "
                  f"They are currently {details['situation']}, in a {details['background']} setting. Keep the design consistent.")
    elif prompt_type == "Object":
        prompt = (f"The object is a {details['name']} with {details['material']} material, in {details['color']} color. "
                  f"It is used for {details['purpose']} and currently located in a {details['background']} environment.")
    elif prompt_type == "Animal":
        prompt = (f"The animal is a {details['species']} with {details['fur_color']} fur and {details['size']} size. "
                  f"It is {details['behavior']} and found in a {details['habitat']} habitat.")
    return prompt

def main():
    sg.theme("DarkBlue")

    layout = [
        [sg.Text("Select Prompt Type:"), sg.Combo(["Character", "Object", "Animal"], key="-PROMPT_TYPE-")],
        [sg.Button("Next"), sg.Button("Exit")]
    ]

    window = sg.Window("Prompt Generator GUI", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        elif event == "Next":
            prompt_type = values["-PROMPT_TYPE-"]
            if prompt_type:
                window.close()
                run_details_window(prompt_type)
            else:
                sg.popup("Please select a prompt type.")

    window.close()

def run_details_window(prompt_type):
    detail_layouts = {
        "Character": [
            [sg.Text("Name:"), sg.Input(key="-NAME-")],
            [sg.Text("Physical Description (e.g., eye color, height):"), sg.Input(key="-PHYSICAL-")],
            [sg.Text("Outfit Description:"), sg.Input(key="-OUTFIT-")],
            [sg.Text("Current Situation:"), sg.Input(key="-SITUATION-")],
            [sg.Text("Background Setting:"), sg.Input(key="-BACKGROUND-")]
        ],
        "Object": [
            [sg.Text("Object Name:"), sg.Input(key="-NAME-")],
            [sg.Text("Material:"), sg.Input(key="-MATERIAL-")],
            [sg.Text("Color:"), sg.Input(key="-COLOR-")],
            [sg.Text("Purpose:"), sg.Input(key="-PURPOSE-")],
            [sg.Text("Background Setting:"), sg.Input(key="-BACKGROUND-")]
        ],
        "Animal": [
            [sg.Text("Species:"), sg.Input(key="-SPECIES-")],
            [sg.Text("Fur Color:"), sg.Input(key="-FUR_COLOR-")],
            [sg.Text("Size:"), sg.Input(key="-SIZE-")],
            [sg.Text("Behavior:"), sg.Input(key="-BEHAVIOR-")],
            [sg.Text("Habitat:"), sg.Input(key="-HABITAT-")]
        ]
    }

    layout = detail_layouts.get(prompt_type, []) + [[sg.Button("Generate"), sg.Button("Back")]]
    window = sg.Window(f"{prompt_type} Details", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Back"):
            break
        elif event == "Generate":
            prompt = generate_prompt(prompt_type, values)
            sg.popup_scrolled("Generated Prompt:", prompt)
            save_prompt_to_file(prompt)
            save_prompt_history({"generated_prompt": prompt})
            break

    window.close()

if __name__ == "__main__":
    main()
