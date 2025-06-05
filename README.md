# Classical Chinese Letter Generator

This project is a web application built with Flask that generates classical Chinese letters using the DeepSeek/KIMI API. Users can input a prompt, and the application will generate a letter in classical Chinese style. The application also allows users to choose from a variety of fonts and seals to customize the letter.

## Features

- **Classical Chinese Letter Generation**: Uses the DeepSeek API to generate letters based on user prompts.
- **Custom Fonts**: Supports multiple fonts for rendering the letter.
- **Seal Images**: Allows users to add custom seal images to the letter.
- **Dynamic Backgound**: Generates Backgound dynamically to apply selected fonts.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/classical-chinese-letter-generator.git
   cd classical-chinese-letter-generator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   ./run.sh
   ```

4. **Access the application**:
   Open your browser and navigate to `http://localhost:5002`.

## Usage

1. **Home Page**:
   - Enter a prompt in the input field and click "Generate" to create a classical Chinese letter.
   - Select a font and seal image to customize the letter.

2. **Edit Content**:
   - After generating the letter, you can edit the content directly in the text area and save the changes.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/`: Contains HTML templates for the web pages.
- `static/`: Contains static files like fonts, seal images, and CSS.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 