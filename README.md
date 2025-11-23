# Flask Todo App

A simple and modern task management web application built with Flask. It allows users to create, update, and delete tasks, organize them by status, and keep track of daily todos. The app demonstrates CRUD operations, Flask basics, and a clean, responsive UI.

## Features

- User-friendly interface for managing tasks
- Add, edit, and delete todos
- Mark tasks as complete/incomplete
- Persistent storage (SQLite)
- Responsive design using Bootstrap

## Requirements

- Python 3.x
- Flask
- SQLite (bundled)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jay789-code-pixel/flasktodoapp.git
   cd flasktodoapp
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Project Structure

```
flasktodoapp/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── ...
├── static/
│   ├── styles.css
│   └── ...
└── README.md
```

## License

This project is licensed under the MIT License.
