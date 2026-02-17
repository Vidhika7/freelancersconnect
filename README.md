
# FreelancersConnect

A platform connecting freelancers with clients.

## How to Run Locally

### Prerequisites
- Python 3.8+
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vidhika7/freelancersconnect.git
   cd freelancersconnect
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the server:**
   - Double-click `run_project.bat` (Windows only)
   - OR run:
     ```bash
     python manage.py runserver
     ```

7. **Visit the site:**
   Open your browser to `http://127.0.0.1:8000/`.
