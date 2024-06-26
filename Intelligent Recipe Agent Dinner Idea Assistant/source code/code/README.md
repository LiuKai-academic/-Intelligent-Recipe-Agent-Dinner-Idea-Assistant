# Eta recipe

This project is designed to generate high-quality images of recipes using the Stability  Stable Diffusion AI API and ChatGPT API to display them using a PyQt5 GUI.

## Prerequisites

- Python 3.9
- Anaconda (recommended for managing the Python environment)

## Installation

1. **Create and activate the virtual environment** (recommended):
    ```bash
    conda create --name eta_recipe python=3.9
    conda activate eta_recipe
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the main application**:
    ```bash
    python main.py
    ```

## Project Structure

│  main.py
│  README.md
│  requirements.txt
│  respond.py
│  sd.py
│  software.py
│  software2.py
│  software3.py
│
├─out/

- `main.py`: The main script to run the PyQt5 application.
- `requirements.txt`: A file listing all Python packages required to run the project.
- `out/`: Directory where generated images will be saved.
- `README.md`: This file.

## Configuration

- Ensure you have a valid API key for the Stability AI API and update the `Authorization` header in `generate_image` function within `sd.py`.
- Ensure you have a valid API key for the OpenAI  API and update the `Authorization` header in `respond` function within `respond.py`.

## Example

Here is an example of what you can expect:

1. Input  `I have tomatoes and eggs what can I do to eat?` Then the system will offer some choice for users. In this situation it may offer `Tomato and egg Seramble`  and `Shakshuka` for user to select.
2. Input `show me the recipe of  Tomato and egg Seramble` then the system will offer a detail recipe and the preview of the dishes.

## License

This project is licensed under the MIT License.
