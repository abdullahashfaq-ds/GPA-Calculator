# GPA Calculator

This project is a Django based web application designed to calculate Grade Point Average (GPA) based on predefined policies, with the ability to generate PDF reports of the results. The application features a modern frontend and supports Dockerized deployment for easy integration across different environments.

## Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, TailwindCSS, JavaScript
- **PDF Generation:** ReportLab
- **Containerization:** Docker, Docker Compose

## Installation

### Prerequisites
Ensure that the following are installed on your local machine:
- Python 3.8+
- Docker and Docker Compose

### Clone the Repository

```bash
git clone git@github.com:abdullahashfaq-ds/GPA-Calculator.git
cd GPA-Calculator
```

### Create Virtual Environment

```bash
python -m venv venv
# On Windows, use:
venv\Scripts\activate
# On Linux/MacOS, use:
source venv/bin/activate
```

### Install Dependencies

```bash
# To set up the production environment:
pip install -r requirements.txt
# To set up the development environment:
pip install -r requirements.dev.txt
```

### Docker Setup

For containerized deployment, ensure Docker is running and use the following commands:

1. Build and start the containers:

```bash
docker-compose up --build
```

2. Access the application at `http://localhost:8000`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For inquiries or support, please open an issue on GitHub or contact the project maintainer at [abdullahashfaq.ds@gmail.com](mailto:abdullahashfaq.ds@gmail.com).
