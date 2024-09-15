# AI-Driven Website Benchmarking System

This project implements an AI-driven website benchmarking system using FastAPI. It analyzes websites across multiple dimensions including performance, user experience, content quality, visual appeal, and security.

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the Application](#running-the-application)
6. [API Usage](#api-usage)
7. [Running Tests](#running-tests)
8. [Project Structure](#project-structure)
9. [Contributing](#contributing)
10. [License](#license)

## Features

- Performance analysis using Google PageSpeed Insights
- User experience analysis
- Content quality assessment
- Visual design analysis
- Security assessment
- Extensible architecture for adding new analysis modules

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-website-benchmarking.git
   cd ai-website-benchmarking
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the root directory of the project.
2. Add your API keys to the `.env` file:
   ```
   GOOGLE_PAGESPEED_API_KEY=your_google_api_key
   HOTJAR_API_KEY=your_hotjar_api_key
   MARKETMUSE_API_KEY=your_marketmuse_api_key
   EYEQUANT_API_KEY=your_eyequant_api_key
   DARKTRACE_API_KEY=your_darktrace_api_key
   ```

## Running the Application

To run the application, use the following command:

```
python -m app.main
```

The API will be available at `http://localhost:8000`.

## API Usage

The API provides two main endpoints:

### 1. Analyze All Modules

**Endpoint:** `POST /api/v1/analyze`

**Request Body:**
```json
{
  "url": "https://example.com",
  "modules": ["performance", "ux", "content", "visual", "security"]
}
```

**Response:**
```json
{
  "url": "https://example.com",
  "results": {
    "performance": {
      "score": 85,
      "metrics": {
        "first_contentful_paint": 1000,
        "largest_contentful_paint": 2500,
        "cumulative_layout_shift": 0.1,
        "time_to_interactive": 3000
      }
    },
    "ux": {
      "score": 90,
      "metrics": {
        "click_engagement": 85,
        "scroll_depth": 70
      }
    },
    ...
  }
}
```

### 2. Analyze Specific Module

**Endpoint:** `POST /api/v1/analyze/{module}`

**Path Parameter:**
- `module`: One of "performance", "ux", "content", "visual", or "security"

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "url": "https://example.com",
  "results": {
    "performance": {
      "score": 85,
      "metrics": {
        "first_contentful_paint": 1000,
        "largest_contentful_paint": 2500,
        "cumulative_layout_shift": 0.1,
        "time_to_interactive": 3000
      }
    }
  }
}
```

## Running Tests

To run the tests, use the following command:

```
pytest
```

This will run all tests in the `tests/` directory.

## Project Structure

```
benchmark_system/
│
├── .env
├── requirements.txt
├── README.md
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── config/
│   ├── models/
│   ├── interfaces/
│   ├── api_clients/
│   ├── analyzers/
│   └── services/
│
└── tests/
    ├── test_analyzers/
    ├── test_api_clients/
    └── test_services/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.