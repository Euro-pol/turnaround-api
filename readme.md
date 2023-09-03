# turnaround-api

Cloudflare turnstile solver API, based on [turnaround](https://github.com/Body-Alhoha/turnaround). Developed using Python and Flask.

## Installation

To get started with the turnaround-api, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Euro-pol/turnaround-api
    cd turnaround-api
    ```

2. Initialize and update the submodules to fetch external dependencies:

    ```bash
    git submodule init
    git submodule update
    ```

3. Create a symbolic link (symlink) to the required `page.html` file. Choose the appropriate command based on your operating system:

    **Linux / macOS**:

    ```bash
    ln utils/utils/page.html utils/page.html
    ```

    **Windows (using `mklink`)**:

    ```bash
    mklink /H "utils\page.html" "utils\utils\page.html"
    ```

4. Create a Python virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate.bat
    ```

5. Install the required Python packages from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

6. Install Playwright for automated browser actions:

    ```bash
    python -m playwright install
    ```

7. Start the Flask application:

    ```bash
    python main.py
    ```

## Example

You can find a Python code example [here](https://github.com/Euro-pol/turnaround-api/blob/main/example.py) to help you get started with using the turnaround-api in your own projects.

## Contributing

Contributions to the turnaround-api are welcome! If you encounter issues or have ideas for improvements, please open a pull request or create an issue.

## Images

![image1](./images/image1.png)
![image2](./images/image2.png)
![image3](./images/image3.png)

## Credits

This project is based on [turnaround](https://github.com/Body-Alhoha/turnaround/), and we appreciate their work on the original project owner.
