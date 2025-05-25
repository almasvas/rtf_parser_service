# RTF Parser Service

A lightweight FastAPI-based microservice that parses RTF files (e.g., Russian Labor Code) and extracts structured articles with metadata. Designed to be used as a backend service in a legal AI assistant or any system requiring article-level access to legal documents.

## Features

- Parses `.rtf` files with legacy encodings (e.g., CP1251)
- Splits content into individual articles with titles and text
- Provides a REST API to trigger parsing and return results as JSON
- Handles typical formatting and legal document quirks

## Use Case

Originally built to preprocess the Russian Labor Code into a structured format for semantic search and vector databases (e.g., Qdrant), enabling AI-powered legal question answering.

## API Endpoints

| Method | Endpoint       | Description                         |
|--------|----------------|-------------------------------------|
| POST   | `/parse`       | Upload and parse an RTF file        |

### Example Request

```bash
curl -X POST http://localhost:8000/parse   -F "file=@/path/to/labor_code.rtf"
```

### Example Response

```json
[
  {
    "number": "1",
    "title": "General Provisions",
    "text": "This Code defines the labor relations..."
  },
  ...
]
```

## Getting Started

### Prerequisites

- Python 3.10+
- `pip`

### Installation

```bash
git clone https://github.com/yourname/rtf_parser_service.git
cd rtf_parser_service
pip install -r requirements.txt
```

### Run the Service

```bash
python -m app.main
```

Then open [http://localhost:8000/docs](http://localhost:8000/docs) to view the interactive Swagger UI.

## Project Structure

```
rtf_parser_service/
├── app/
│   ├── main.py        # FastAPI app entry point
│   ├── parser.py      # Core RTF parsing logic
│   ├── api.py         # API route definitions
│   ├── models.py      # Data models (Pydantic)
│   └── config.py      # Settings and constants
├── requirements.txt
└── README.md
```

## License

MIT License.
