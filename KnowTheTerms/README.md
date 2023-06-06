# KnowTheTerms

KnowTheTerms is an app that takes a terms of service URL as input and provides a summary along with a safety remark, helping users decide whether it's safe to sign up for a product or service.

## Installation

1. Clone the repository:

```
git clone https://github.com/juniorvish/KnowTheTerms.git
```

2. Change to the project directory:

```
cd KnowTheTerms
```

3. Install the required Python packages:

```
pip install -r backend/requirements.txt
```

## Usage

1. Start the backend server:

```
python backend/app.py
```

2. Open `index.html` in your web browser.

3. Enter the terms of service URL in the input field and click the "Submit" button.

4. The app will display a summary of the terms of service and a safety remark.

## Technologies

- Frontend: HTML, Tailwind CSS, JavaScript
- Backend: Python, OpenAI GPT-4 model

## License

This project is licensed under the MIT License.