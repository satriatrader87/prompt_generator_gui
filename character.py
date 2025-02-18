import gradio as gr
import json

def generate_prompt(
    name, gender, custom_gender, age, custom_age, eye_color, custom_eye_color, hair_style, custom_hair_style,
    hair_color, custom_hair_color, outfit, custom_outfit, outfit_color, custom_outfit_color, footwear,
    custom_footwear, footwear_color, custom_footwear_color, skin_color, custom_skin_color, accessories,
    custom_accessories, expression, custom_expression, pose, custom_pose, background, custom_background,
    art_style, custom_art_style, color_palette, height, custom_height, weight, custom_weight, personality,
    custom_personality, weapon, custom_weapon, tool, custom_tool, pet, custom_pet, theme, custom_theme
):
    """Generate a clean and consistent prompt based on selected details."""
    if not name:
        return "Please enter a name."

    def get_feature(feature, custom):
        return custom if feature == "Custom input" and custom else feature

    # Start building the prompt
    prompt = f"{name} is a character"

    # Gender and age
    if (desc := get_feature(gender, custom_gender)) and desc != "Not specified":
        prompt += f" who is {desc.lower()}"
    if (desc := get_feature(age, custom_age)) and desc != "Not specified":
        prompt += f" and is {desc.lower()} years old"

    # Height and weight
    if (desc := get_feature(height, custom_height)) and desc != "Not specified":
        prompt += f", {desc.lower()} in height"
    if (desc := get_feature(weight, custom_weight)) and desc != "Not specified":
        prompt += f" and {desc.lower()} in weight"

    # Personality
    if (desc := get_feature(personality, custom_personality)) and desc != "Not specified":
        prompt += f". {name} has a {desc.lower()} personality"

    # Physical features
    physical_features = []
    if (desc := get_feature(eye_color, custom_eye_color)) and desc != "Not specified":
        physical_features.append(f"{desc.lower()} eyes")
    if (desc := get_feature(hair_style, custom_hair_style)) and desc != "Not specified":
        physical_features.append(f"{desc.lower()} hair")
    if (desc := get_feature(hair_color, custom_hair_color)) and desc != "Not specified":
        physical_features.append(f"{desc.lower()} hair color")
    if (desc := get_feature(skin_color, custom_skin_color)) and desc != "Not specified":
        physical_features.append(f"{desc.lower()} skin tone")
    if physical_features:
        prompt += " with " + ", ".join(physical_features)

    # Clothing and accessories
    clothing_features = []
    if (desc := get_feature(outfit, custom_outfit)) and desc != "Not specified":
        clothing_features.append(f"a {desc.lower()}")
    if (desc := get_feature(outfit_color, custom_outfit_color)) and desc != "Not specified":
        clothing_features.append(f"{desc.lower()} color")
    if clothing_features:
        prompt += ", wearing " + " ".join(clothing_features)

    footwear_features = []
    if (desc := get_feature(footwear, custom_footwear)) and desc != "Not specified":
        footwear_features.append(f"{desc.lower()} as footwear")
    if (desc := get_feature(footwear_color, custom_footwear_color)) and desc != "Not specified":
        footwear_features.append(f"{desc.lower()} color")
    if footwear_features:
        prompt += ", with " + " ".join(footwear_features)

    if (desc := get_feature(accessories, custom_accessories)) and desc != "Not specified":
        prompt += f", accessorized with {desc.lower()}"

    # Weapon and tool
    if (desc := get_feature(weapon, custom_weapon)) and desc != "Not specified":
        prompt += f", carrying a {desc.lower()}"
    if (desc := get_feature(tool, custom_tool)) and desc != "Not specified":
        prompt += f", equipped with a {desc.lower()}"

    # Pet
    if (desc := get_feature(pet, custom_pet)) and desc != "Not specified":
        prompt += f", accompanied by a {desc.lower()}"

    # Expression and pose
    if (desc := get_feature(expression, custom_expression)) and desc != "Not specified":
        prompt += f", with a {desc.lower()} expression"
    if (desc := get_feature(pose, custom_pose)) and desc != "Not specified":
        prompt += f", in a {desc.lower()} pose"

    # Background and style
    if (desc := get_feature(background, custom_background)) and desc != "Not specified":
        prompt += f", set against a {desc.lower()} background"
    if (desc := get_feature(art_style, custom_art_style)) and desc != "Not specified":
        prompt += f". The art style is {desc.lower()}"
    if color_palette and color_palette != "Not specified":
        prompt += f", using a {color_palette.lower()} color palette"

    # Theme
    if (desc := get_feature(theme, custom_theme)) and desc != "Not specified":
        prompt += f". The character is themed around {desc.lower()}"

    prompt += ". Maintain the same color scheme and artistic style for consistency."
    return prompt

def toggle_custom_input(selected_feature):
    """Show custom input textbox if 'Custom input' is selected."""
    return gr.update(visible=(selected_feature == "Custom input"))

def save_template(name, gender, custom_gender, age, custom_age, eye_color, custom_eye_color, hair_style, custom_hair_style,
                  hair_color, custom_hair_color, outfit, custom_outfit, outfit_color, custom_outfit_color, footwear,
                  custom_footwear, footwear_color, custom_footwear_color, skin_color, custom_skin_color, accessories,
                  custom_accessories, expression, custom_expression, pose, custom_pose, background, custom_background,
                  art_style, custom_art_style, color_palette, height, custom_height, weight, custom_weight, personality,
                  custom_personality, weapon, custom_weapon, tool, custom_tool, pet, custom_pet, theme, custom_theme):
    """Save the character template to a JSON file."""
    template = {
        "name": name,
        "gender": gender if gender != "Custom input" else custom_gender,
        "age": age if age != "Custom input" else custom_age,
        "eye_color": eye_color if eye_color != "Custom input" else custom_eye_color,
        "hair_style": hair_style if hair_style != "Custom input" else custom_hair_style,
        "hair_color": hair_color if hair_color != "Custom input" else custom_hair_color,
        "outfit": outfit if outfit != "Custom input" else custom_outfit,
        "outfit_color": outfit_color if outfit_color != "Custom input" else custom_outfit_color,
        "footwear": footwear if footwear != "Custom input" else custom_footwear,
        "footwear_color": footwear_color if footwear_color != "Custom input" else custom_footwear_color,
        "skin_color": skin_color if skin_color != "Custom input" else custom_skin_color,
        "accessories": accessories if accessories != "Custom input" else custom_accessories,
        "expression": expression if expression != "Custom input" else custom_expression,
        "pose": pose if pose != "Custom input" else custom_pose,
        "background": background if background != "Custom input" else custom_background,
        "art_style": art_style if art_style != "Custom input" else custom_art_style,
        "color_palette": color_palette,
        "height": height if height != "Custom input" else custom_height,
        "weight": weight if weight != "Custom input" else custom_weight,
        "personality": personality if personality != "Custom input" else custom_personality,
        "weapon": weapon if weapon != "Custom input" else custom_weapon,
        "tool": tool if tool != "Custom input" else custom_tool,
        "pet": pet if pet != "Custom input" else custom_pet,
        "theme": theme if theme != "Custom input" else custom_theme
    }
    with open(f"{name}_template.json", "w") as f:
        json.dump(template, f, indent=4)
    return f"Template saved as {name}_template.json"

def load_template(file):
    """Load the character template from a JSON file."""
    with open(file.name, "r") as f:
        template = json.load(f)
    return template

with gr.Blocks() as demo:
    gr.Markdown("## Advanced Character Prompt Generator")

    with gr.Row():
        name = gr.Textbox(label="Enter Name", placeholder="Enter the name of your character")

    with gr.Row():
        gender = gr.Dropdown(
            choices=["Male", "Female", "Non-binary", "Custom input", "Not specified"],
            label="Gender", value="Not specified"
        )
        custom_gender = gr.Textbox(label="Custom Gender", placeholder="Enter custom gender", visible=False)
        age = gr.Dropdown(
            choices=["Child", "Teen", "Adult", "Elderly", "Custom input", "Not specified"],
            label="Age", value="Not specified"
        )
        custom_age = gr.Textbox(label="Custom Age", placeholder="Enter custom age", visible=False)

    with gr.Row():
        eye_color = gr.Dropdown(
            choices=["Black", "Blue", "Green", "Brown", "Custom input", "Not specified"],
            label="Eye Color", value="Not specified"
        )
        custom_eye_color = gr.Textbox(label="Custom Eye Color", placeholder="Enter custom eye color", visible=False)

    with gr.Row():
        hair_style = gr.Dropdown(
            choices=["Short", "Long", "Curly", "Straight", "Custom input", "Not specified"],
            label="Hair Style", value="Not specified"
        )
        custom_hair_style = gr.Textbox(label="Custom Hair Style", placeholder="Enter custom hair style", visible=False)
        hair_color = gr.Dropdown(
            choices=["Black", "Blonde", "Brown", "Red", "Custom input", "Not specified"],
            label="Hair Color", value="Not specified"
        )
        custom_hair_color = gr.Textbox(label="Custom Hair Color", placeholder="Enter custom hair color", visible=False)

    with gr.Row():
        outfit = gr.Dropdown(
            choices=["Casual", "Armor", "Dress", "Shirt", "Custom input", "Not specified"],
            label="Outfit", value="Not specified"
        )
        custom_outfit = gr.Textbox(label="Custom Outfit", placeholder="Enter custom outfit", visible=False)
        outfit_color = gr.Dropdown(
            choices=["Red", "Blue", "Green", "Yellow", "Black", "White", "Custom input", "Not specified"],
            label="Outfit Color", value="Not specified"
        )
        custom_outfit_color = gr.Textbox(label="Custom Outfit Color", placeholder="Enter custom outfit color", visible=False)

    with gr.Row():
        footwear = gr.Dropdown(
            choices=["Sneakers", "Boots", "Sandals", "Custom input", "Not specified"],
            label="Footwear", value="Not specified"
        )
        custom_footwear = gr.Textbox(label="Custom Footwear", placeholder="Enter custom footwear", visible=False)
        footwear_color = gr.Dropdown(
            choices=["Black", "White", "Brown", "Custom input", "Not specified"],
            label="Footwear Color", value="Not specified"
        )
        custom_footwear_color = gr.Textbox(label="Custom Footwear Color", placeholder="Enter custom footwear color", visible=False)

    with gr.Row():
        skin_color = gr.Dropdown(
            choices=["Fair", "Tan", "Brown", "Dark", "Olive", "Custom input", "Not specified"],
            label="Skin Color", value="Not specified"
        )
        custom_skin_color = gr.Textbox(label="Custom Skin Color", placeholder="Enter custom skin color", visible=False)
        accessories = gr.Dropdown(
            choices=["Necklace", "Glasses", "Hat", "Custom input", "Not specified"],
            label="Accessories", value="Not specified"
        )
        custom_accessories = gr.Textbox(label="Custom Accessories", placeholder="Enter custom accessories", visible=False)

    with gr.Row():
        expression = gr.Dropdown(
            choices=["Smiling", "Angry", "Neutral", "Custom input", "Not specified"],
            label="Expression", value="Not specified"
        )
        custom_expression = gr.Textbox(label="Custom Expression", placeholder="Enter custom expression", visible=False)
        pose = gr.Dropdown(
            choices=["Standing", "Sitting", "Running", "Custom input", "Not specified"],
            label="Pose", value="Not specified"
        )
        custom_pose = gr.Textbox(label="Custom Pose", placeholder="Enter custom pose", visible=False)

    with gr.Row():
        background = gr.Dropdown(
            choices=["Futuristic city", "Ancient temple", "Forest landscape", "Custom input", "Not specified"],
            label="Background", value="Not specified"
        )
        custom_background = gr.Textbox(label="Custom Background", placeholder="Enter custom background", visible=False)
        art_style = gr.Dropdown(
            choices=["3D Pixar", "Anime", "Realistic", "Cartoonish", "Minimalist", "Custom input", "Not specified"],
            label="Artistic Style", value="Not specified"
        )
        custom_art_style = gr.Textbox(label="Custom Artistic Style", placeholder="Enter custom artistic style", visible=False)

    with gr.Row():
        color_palette = gr.Dropdown(
            choices=["Warm", "Cool", "Pastel", "Vibrant", "Monochrome", "Not specified"],
            label="Color Palette", value="Not specified"
        )

    with gr.Row():
        height = gr.Dropdown(
            choices=["Short", "Average", "Tall", "Custom input", "Not specified"],
            label="Height", value="Not specified"
        )
        custom_height = gr.Textbox(label="Custom Height", placeholder="Enter custom height", visible=False)
        weight = gr.Dropdown(
            choices=["Slim", "Average", "Heavy", "Custom input", "Not specified"],
            label="Weight", value="Not specified"
        )
        custom_weight = gr.Textbox(label="Custom Weight", placeholder="Enter custom weight", visible=False)

    with gr.Row():
        personality = gr.Dropdown(
            choices=["Friendly", "Shy", "Bold", "Custom input", "Not specified"],
            label="Personality", value="Not specified"
        )
        custom_personality = gr.Textbox(label="Custom Personality", placeholder="Enter custom personality", visible=False)

    with gr.Row():
        weapon = gr.Dropdown(
            choices=["Sword", "Bow", "Gun", "Custom input", "Not specified"],
            label="Weapon", value="Not specified"
        )
        custom_weapon = gr.Textbox(label="Custom Weapon", placeholder="Enter custom weapon", visible=False)
        tool = gr.Dropdown(
            choices=["Book", "Toolbox", "Magic Staff", "Custom input", "Not specified"],
            label="Tool", value="Not specified"
        )
        custom_tool = gr.Textbox(label="Custom Tool", placeholder="Enter custom tool", visible=False)

    with gr.Row():
        pet = gr.Dropdown(
            choices=["Cat", "Dog", "Bird", "Custom input", "Not specified"],
            label="Pet", value="Not specified"
        )
        custom_pet = gr.Textbox(label="Custom Pet", placeholder="Enter custom pet", visible=False)

    with gr.Row():
        theme = gr.Dropdown(
            choices=["Fantasy", "Sci-Fi", "Modern", "Custom input", "Not specified"],
            label="Theme", value="Not specified"
        )
        custom_theme = gr.Textbox(label="Custom Theme", placeholder="Enter custom theme", visible=False)

    with gr.Row():
        save_btn = gr.Button("Save Template")
        load_btn = gr.UploadButton("Load Template", file_types=[".json"])

    generate_btn = gr.Button("Generate Prompt")
    output = gr.Textbox(label="Generated Prompt", lines=6)

    # Toggle custom inputs
    for feature, custom in zip(
        [gender, age, eye_color, hair_style, hair_color, outfit, outfit_color, footwear, footwear_color, skin_color, accessories, expression, pose, background, art_style, height, weight, personality, weapon, tool, pet, theme],
        [custom_gender, custom_age, custom_eye_color, custom_hair_style, custom_hair_color, custom_outfit, custom_outfit_color, custom_footwear, custom_footwear_color, custom_skin_color, custom_accessories, custom_expression, custom_pose, custom_background, custom_art_style, custom_height, custom_weight, custom_personality, custom_weapon, custom_tool, custom_pet, custom_theme]
    ):
        feature.change(toggle_custom_input, inputs=[feature], outputs=[custom])

    generate_btn.click(
        generate_prompt,
        inputs=[
            name, gender, custom_gender, age, custom_age, eye_color, custom_eye_color, hair_style, custom_hair_style,
            hair_color, custom_hair_color, outfit, custom_outfit, outfit_color, custom_outfit_color, footwear,
            custom_footwear, footwear_color, custom_footwear_color, skin_color, custom_skin_color, accessories,
            custom_accessories, expression, custom_expression, pose, custom_pose, background, custom_background,
            art_style, custom_art_style, color_palette, height, custom_height, weight, custom_weight, personality,
            custom_personality, weapon, custom_weapon, tool, custom_tool, pet, custom_pet, theme, custom_theme
        ],
        outputs=output
    )

    save_btn.click(
        save_template,
        inputs=[
            name, gender, custom_gender, age, custom_age, eye_color, custom_eye_color, hair_style, custom_hair_style,
            hair_color, custom_hair_color, outfit, custom_outfit, outfit_color, custom_outfit_color, footwear,
            custom_footwear, footwear_color, custom_footwear_color, skin_color, custom_skin_color, accessories,
            custom_accessories, expression, custom_expression, pose, custom_pose, background, custom_background,
            art_style, custom_art_style, color_palette, height, custom_height, weight, custom_weight, personality,
            custom_personality, weapon, custom_weapon, tool, custom_tool, pet, custom_pet, theme, custom_theme
        ],
        outputs=output
    )

    load_btn.upload(
        load_template,
        inputs=[load_btn],
        outputs=[name, gender, custom_gender, age, custom_age, eye_color, custom_eye_color, hair_style, custom_hair_style,
                 hair_color, custom_hair_color, outfit, custom_outfit, outfit_color, custom_outfit_color, footwear,
                 custom_footwear, footwear_color, custom_footwear_color, skin_color, custom_skin_color, accessories,
                 custom_accessories, expression, custom_expression, pose, custom_pose, background, custom_background,
                 art_style, custom_art_style, color_palette, height, custom_height, weight, custom_weight, personality,
                 custom_personality, weapon, custom_weapon, tool, custom_tool, pet, custom_pet, theme, custom_theme]
    )

demo.launch(debug=True)
