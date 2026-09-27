# Indian Pincode Lookup API

A lightweight, fast, and developer-friendly **Indian PIN Code Lookup REST API** built with **Python and FastAPI**.

The API allows applications to look up location information using Indian six-digit PIN codes. It supports both **single PIN-code lookup** and **bulk PIN-code lookup**, with custom validation and structured error handling.

The project uses a **local PIN-code dataset**, making lookups fast and independent of external APIs.

---

## 📌 Overview

The **Pincode Lookup API** is designed to provide location information associated with Indian postal PIN codes.

Given a valid Indian PIN code such as:

```text
520001
```

the API can return information such as:

```json
{
    "pincode": "520001",
    "city": "Vijayawada",
    "state": "Andhra Pradesh",
    "district": "NTR"
}
```

The underlying dataset can contain additional information such as:

* City
* State
* District
* Latitude
* Longitude
* About the city

The API controls which fields are exposed through its Pydantic response models.

---

## ✨ Features

* 🚀 Fast REST API powered by **FastAPI**
* 🇮🇳 Indian six-digit PIN-code validation
* 🔎 Single PIN-code lookup
* 📦 Bulk PIN-code lookup
* ⚡ Local in-memory dataset for fast lookups
* 🛡️ Custom exception handling
* ✅ Request validation using **Pydantic**
* 📋 Automatic OpenAPI documentation
* 🔧 Swagger UI
* 📖 ReDoc documentation
* 🧩 Type hints throughout the application
* 🏗️ Simple and modular project structure
* 🔌 Easy to integrate with frontend and backend applications
* 🌐 No external API dependency for PIN-code lookups

---

# 🛠️ Tech Stack

| Technology | Purpose                           |
| ---------- | --------------------------------- |
| Python     | Core programming language         |
| FastAPI    | REST API framework                |
| Pydantic   | Data validation and serialization |
| Uvicorn    | ASGI server                       |
| OpenAPI    | API specification                 |
| Swagger UI | Interactive API documentation     |
| ReDoc      | Alternative API documentation     |

---

# 📂 Project Structure

A recommended project structure is:

```text
pincode-api/
│
├── main.py
├── models.py
├── exceptions.py
├── data.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `main.py`

Contains:

* FastAPI application configuration
* Route definitions
* Request handling
* Custom exception-handler registration
* Uvicorn startup configuration

### `models.py`

Contains Pydantic models used for:

* Request validation
* Response validation
* Bulk request validation
* Bulk response serialization

### `exceptions.py`

Contains custom application exceptions and their FastAPI handlers.

Examples:

```text
PinCodeNotFoundError
InvalidPinCodeError
```

### `data.py`

Contains the local PIN-code dataset.

Example:

```python
pincode_data: dict[str, dict[str, str | float]] = {
    "520001": {
        "pincode": "520001",
        "city": "Vijayawada",
        "state": "Andhra Pradesh",
        "district": "NTR",
        "latitude": 16.5062,
        "longitude": 80.648,
        "about_city": (
            "Vijayawada is known for the Kanaka Durga Temple "
            "on Indrakeeladri Hill."
        ),
    }
}
```

### `requirements.txt`

Contains the Python dependencies required to run the application.

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/Zain-Ahma12/Indian_Pincode_lookup.git
```

Move into the project directory:

```bash
cd Indian_Pincode_lookup
```

---

## 2. Create a virtual environment

It is recommended to use a virtual environment so that project dependencies remain isolated.

### Windows

```bash
uv venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the API

Start the development server with:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

You can also start the application using:

```bash
python main.py
```

if your `main.py` contains the Uvicorn startup block.

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

Open:

```text
http://127.0.0.1:8000/swagger
```

Swagger allows you to:

* Explore available endpoints
* View request parameters
* View request bodies
* Execute API requests
* Inspect responses
* Test validation errors

---

## ReDoc

Open:

```text
http://127.0.0.1:8000/redoc
```

ReDoc provides a more documentation-oriented view of the API.

---

## OpenAPI Specification

The OpenAPI specification is available at:

```text
http://127.0.0.1:8000/openAPI
```

This specification can be consumed by tools that support OpenAPI.

---

# 🔌 API Endpoints

The API currently provides three main endpoints.

| Method | Endpoint          | Description                   |
| ------ | ----------------- | ----------------------------- |
| `GET`  | `/`               | Returns basic API information |
| `GET`  | `/pincode/{code}` | Looks up a single PIN code    |
| `POST` | `/pincode/bulk`   | Looks up multiple PIN codes   |

---

# 🏠 1. Root Endpoint

### Request

```http
GET /
```

### Example

```bash
curl http://127.0.0.1:8000/
```

### Response

```json
{
    "message": "Pincode Lookup API"
}
```

This endpoint can be used as a simple health/information endpoint.

---

# 🔎 2. Single PIN-Code Lookup

### Endpoint

```http
GET /pincode/{code}
```

The `{code}` parameter represents an Indian six-digit PIN code.

### Example

```http
GET /pincode/520001
```

### cURL

```bash
curl http://127.0.0.1:8000/pincode/520001
```

### Successful Response

```json
{
    "pincode": "520001",
    "city": "Vijayawada",
    "state": "Andhra Pradesh",
    "district": "NTR"
}
```

---

# ❌ Invalid PIN Code

The API validates that a PIN code:

1. Contains exactly six characters
2. Contains only numeric digits

For example:

```text
12345
```

is invalid because it contains only five digits.

Similarly:

```text
ABC123
```

is invalid because it contains non-numeric characters.

### Example

```http
GET /pincode/12345
```

### Response

```json
{
    "error": "invalid_pincode",
    "message": "pincode '12345' is invalid because Must be exactly 6 digits (Indian PIN code format)",
    "pincode": "12345"
}
```

### HTTP Status

```text
400 Bad Request
```

---

# ❓ PIN Code Not Found

A PIN code can be syntactically valid but still not exist in the local dataset.

For example:

```text
999999
```

If the PIN code is not present in the dataset, the API raises:

```text
PinCodeNotFoundError
```

### Response

```json
{
    "error": "pincode_not_found",
    "message": "No location for pincode: 999999",
    "pincode": "999999"
}
```

### HTTP Status

```text
404 Not Found
```

---

# 📦 3. Bulk PIN-Code Lookup

The bulk endpoint allows multiple PIN codes to be checked in a single request.

### Endpoint

```http
POST /pincode/bulk
```

### Request Body

```json
{
    "pincodes": [
        "520001",
        "272001",
        "110001"
    ]
}
```

### cURL

```bash
curl -X POST http://127.0.0.1:8000/pincode/bulk \
     -H "Content-Type: application/json" \
     -d "{\"pincodes\":[\"520001\",\"272001\",\"110001\"]}"
```

---

## Successful Bulk Response

```json
{
    "status": "success",
    "found": 2,
    "not_found": 1,
    "results": [
        {
            "pincode": "520001",
            "city": "Vijayawada",
            "state": "Andhra Pradesh",
            "district": "NTR"
        },
        {
            "pincode": "272001",
            "city": "Basti",
            "state": "Uttar Pradesh",
            "district": "Basti"
        }
    ],
    "missing": [
        "999999"
    ]
}
```

The response separates successful and unsuccessful lookups:

```text
results
    ↓
PIN codes found in the dataset

missing
    ↓
PIN codes not found in the dataset
```

---

# ✅ Request Validation

The API uses **Pydantic** models for request validation.

## Single PIN Code

A valid PIN code must:

```text
✓ contain exactly 6 characters
✓ contain only digits
```

Examples:

```text
520001  ✓
272001  ✓
110001  ✓

12345   ✗
1234567 ✗
ABC123  ✗
```

---

## Bulk PIN Codes

The bulk endpoint accepts between **1 and 10 PIN codes** per request.

Valid:

```json
{
    "pincodes": [
        "520001",
        "272001"
    ]
}
```

Invalid:

```json
{
    "pincodes": []
}
```

because at least one PIN code is required.

Also invalid:

```json
{
    "pincodes": [
        "520001",
        "272001",
        "110001",
        "400001",
        "500001",
        "600001",
        "700001",
        "800001",
        "900001",
        "123456",
        "999999"
    ]
}
```

because the API limits each request to 10 PIN codes.

---

# 🧱 Data Model

The application uses Pydantic models to define its API contract.

## `LocationResponse`

```python
class LocationResponse(BaseModel):
    """Response model containing location information for a PIN code."""

    pincode: str
    city: str
    state: str
    district: str
```

This model defines the public fields returned by the single PIN-code endpoint.

---

## `BulkPinCodesRequest`

```python
class BulkPinCodesRequest(BaseModel):
    """Request model for looking up multiple Indian PIN codes."""

    pincodes: list[str]
```

---

## `BulkPinCodesResponse`

```python
class BulkPinCodesResponse(BaseModel):
    """Response model containing the results of a bulk PIN-code lookup."""

    status: str = "success"
    found: int
    not_found: int
    results: list[LocationResponse]
    missing: list[str]
```

---

# 🗃️ Dataset

The project currently uses a local Python dictionary as its data source.

Example:

```python
pincode_data = {
    "520001": {
        "pincode": "520001",
        "city": "Vijayawada",
        "state": "Andhra Pradesh",
        "district": "NTR",
        "latitude": 16.5062,
        "longitude": 80.648,
        "about_city": "Vijayawada is known for..."
    }
}
```

The PIN code itself is used as the dictionary key:

```python
pincode_data["520001"]
```

This provides constant-time average dictionary lookup:

```text
O(1)
```

which makes the local lookup very fast.

---

# 🧩 Custom Exception Handling

The API uses custom exceptions rather than returning error responses directly from every route.

Two custom exceptions are currently implemented.

### `InvalidPinCodeError`

Used when a PIN code does not satisfy the required format.

```python
raise InvalidPinCodeError(
    code,
    "Must be exactly 6 digits (Indian PIN code format)"
)
```

---

### `PinCodeNotFoundError`

Used when a syntactically valid PIN code does not exist in the dataset.

```python
raise PinCodeNotFoundError(code)
```

---

## Exception Handler Flow

The application registers custom handlers:

```python
app.add_exception_handler(
    PinCodeNotFoundError,
    pincode_not_found_handler,
)

app.add_exception_handler(
    InvalidPinCodeError,
    invalid_pincode_handler,
)
```

The overall flow is:

```text
Client
  │
  ▼
FastAPI Route
  │
  ├── Invalid format
  │       │
  │       ▼
  │  InvalidPinCodeError
  │       │
  │       ▼
  │  400 Bad Request
  │
  └── Valid format
          │
          ▼
      Search dataset
          │
          ├── Found
          │     │
          │     ▼
          │  LocationResponse
          │
          └── Not Found
                │
                ▼
        PinCodeNotFoundError
                │
                ▼
          404 Not Found
```

---

# 🌐 Example Frontend Use Case

The API can be used to automatically populate an address form.

For example:

```text
User enters:

PIN Code
┌──────────────┐
│ 520001       │
└──────────────┘

        │
        ▼

Pincode Lookup API

        │
        ▼

┌─────────────────────────┐
│ City     : Vijayawada   │
│ State    : Andhra Pradesh│
│ District : NTR           │
└─────────────────────────┘
```

This can be useful for:

* E-commerce checkout forms
* Address forms
* Delivery applications
* Logistics systems
* Shipping applications
* Customer registration
* Location-based services

---

# 🔄 Future Improvements

The current implementation is intentionally simple, but the project can be extended in several directions.

### 📍 More Location Information

Add fields such as:

```text
latitude
longitude
post_office
taluk
division
region
circle
delivery_status
```

---

### 🗄️ Database Support

Replace the Python dictionary with a database such as:

* SQLite
* PostgreSQL
* MySQL

This would make it easier to handle a large dataset and update records without modifying Python source code.

---

### 🔍 Search by City

Add an endpoint such as:

```http
GET /city/{city}
```

---

### 🗺️ Geographic Search

With latitude and longitude available, the API could eventually support:

```text
Nearby PIN codes
Distance-based searches
Location radius searches
```

For example:

```http
GET /pincode/nearby?latitude=16.5062&longitude=80.6480&radius=10
```

---

### 📊 Dataset Statistics

A statistics endpoint could provide information such as:

```http
GET /stats
```

Example:

```json
{
    "total_pincodes": 150000,
    "states": 36,
    "districts": 700
}
```

---

### 🔐 Authentication

Authentication could be added for applications requiring controlled API access.

Possible approaches include:

```text
API Keys
JWT
OAuth2
```

---


# 🤝 Contributing

Contributions are welcome.

A typical contribution workflow is:

```bash
fork the repo

git clone forked_repo

cd Indian_Pincode_lookup

git checkout -b feature/your-feature

# Make your changes

git add .

git commit -m "Add your feature"

git push origin feature/your-feature
```

Then open a Pull Request.

---

# 📜 License

This project can be distributed under the terms of the license included in this repository.

If no license has been added yet, consider adding an appropriate open-source license before publishing the project for public use.

---

# 👨‍💻 Author

**Zain Ahmad**

---

# ⭐ Project Status

```text
Status: Active Development 🚧
Version: 1.0.0
```

The current version provides local PIN-code lookup functionality with request validation, bulk lookup, structured responses, and custom exception handling.

---

## 📌 Quick Reference

| Feature               | Status |
| --------------------- | ------ |
| Single PIN lookup     | ✅      |
| Bulk PIN lookup       | ✅      |
| PIN validation        | ✅      |
| Custom exceptions     | ✅      |
| Custom error handlers | ✅      |
| Pydantic models       | ✅      |
| Swagger documentation | ✅      |
| ReDoc documentation   | ✅      |
| Local dataset         | ✅      |
| Database              | 🔜     |
| Automated tests       | 🔜     |
| Authentication        | 🔜     |
| Rate limiting         | 🔜     |
| Geographic search     | 🔜     |
