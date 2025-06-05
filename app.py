from flask import Flask, render_template, request
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key="sk-PUcrvcutjmwACPxL4zUD3IJxgLM5VoZ6tQzx53qM40jzWcRZ", base_url="https://api.moonshot.cn/v1")

#sk-f7f85f122702495291e0eb374de42e12
# Get list of fonts from the fonts folder
def get_fonts():
    fonts_dir = os.path.join(app.static_folder, 'fonts')  # Path to the fonts folder
    fonts = [f for f in os.listdir(fonts_dir) if f.endswith(('.TTF', '.otf'))]  # Filter font files
    return [os.path.splitext(f)[0] for f in fonts]  # Remove file extensions

# Function to generate a letter using DeepSeek API
def generate_letter_with_deepseek(prompt):
    fake = False
    if fake:
        return "大风吹\n落魄谷中寒风吹，春秋蝉鸣少年归。荡魂山处石人泪，定仙游走魔向北。\n逆流河上万仙退，爱情不敌坚持泪。宿命天成命中败。仙尊悔而我不悔。\n乙巳年芒种"
    else:
        response = client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=[
                {"role": "system", "content": "You are a helpful writing assistant, you are good at writing classical chinese."},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        return response.choices[0].message.content

# Function to get the list of seal images from the static/seals folder
def get_seals():
    seals_dir = os.path.join(app.static_folder, 'seals')
    return [f for f in os.listdir(seals_dir) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    fonts = get_fonts()  # Get list of fonts
    seals = get_seals()  # Get the list of seal images
    if request.method == "POST":
        # Get user input for the letter content
        prompt = request.form.get("prompt")
        
        # Generate letter using DeepSeek if prompt is provided, otherwise use fake letter
        if prompt:
            letter_content = generate_letter_with_deepseek(prompt)
        
        lines = [line for line in letter_content.splitlines() if line.strip()]  # Remove empty lines
        for i in range(1, len(lines) - 1):  # Skip first and last lines
            lines[i] = " " + lines[i]  # Add space to the beginning of the paragraph
        letter_content = "\n".join(lines)  # Join lines back into a single string
        
        # Render the template with the generated letter and fonts
        return render_template("index.html", letter_content=letter_content, prompt=prompt, fonts=fonts, seals=seals)
    
    return render_template("index.html", fonts=fonts, seals=seals)

# Route to serve dynamic CSS
@app.route("/styles.css")
def styles():
    fonts = get_fonts()  # Get list of fonts
    return render_template("styles.css", fonts=fonts)

# Route to handle edited content
@app.route("/edit", methods=["POST"])
def edit_content():
    edited_content = request.form.get("content_edit")
    # You can save the edited content to a database or process it further
    # For now, we'll just render the template with the edited content
    fonts = get_fonts()
    seals = get_seals()
    return render_template("index.html", letter_content=edited_content, fonts=fonts, seals=seals)

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5002, host='0.0.0.0')
