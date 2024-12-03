# eBay Price Tracker Api

eBayPriceTracker is a Python-based web api designed to track prices of products on eBay and provide insights into the best deals available. This project aims to help users make informed purchasing decisions by analyzing product prices and identifying below-average offers.

## Features

- Scrapes product titles, prices, and links from eBay search results.
- Calculates the average price of listed products.
- Identifies products priced below the average, helping users find better deals.
- RESTful API built with Flask for easy integration and access to data.

## Installation

To get started with eBayPriceTracker, follow these steps:

1. **Clone the repository:**
    ```bash
   git clone https://github.com/ImaCod3r/ebay-price-tracker-api.git
   ```
2. **Enter the directory**
    ```bash
   cd ebay-price-tracker-api
   ```
3. **Set up a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
5. **Create a .env file in the root directory to store environment variables (if needed).**

## Usage

To run the application, use the following command:

```bash
python app.py
```

The application will start a local server, and you can access the API at http://localhost:5000.

## API Endpoints

- GET /search?q=YOUR_SEARCH_TERM
    - Query the eBay database for products matching the search term.
    - Returns a JSON response with the total number of items, average price, and a list of cheaper items.

**Example Request**

```http
GET http://localhost:5000/search?q=laptop
```

**Example Response**

```json
{
    "total": 100,
    "average price": 750.00,
    "cheaper": [
        {
            "title": "Used Laptop Model A",
            "price": "$600.00",
            "link": "https://www.ebay.com/..."
        },
        {
            "title": "Refurbished Laptop Model B",
            "price": "$700.00",
            "link": "https://www.ebay.com/..."
        }
    ]
}
```

## Logging

Logs are stored in the `logs/` directory. Check `app.log` for any errors or important information while running the application.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, please open an issue or submit a pull request.

## License

This project is licensed under the **MIT License**.

By: **ImaCod3r**