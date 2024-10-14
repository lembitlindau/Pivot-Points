
---

# Trading App with Pivot Points

A Node.js application for traders to view and filter a list of financial instruments and see their pivot points. This app is built with Node, Express, Express Handlebars, and SQLite.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [License](#license)

## Project Overview

This project aims to help traders quickly access pivot points for financial instruments, enabling them to make more informed trading decisions. It uses a lightweight, server-rendered interface with Handlebars and is backed by an SQLite database.

## Technologies Used

- **Node.js**: Server-side JavaScript runtime
- **Express**: Web framework for Node.js
- **Express Handlebars**: Template engine for rendering views
- **SQLite**: Lightweight SQL database for data storage

## Features

- Display a list of instruments with pivot points.
- Filter the list of instruments for quick access.
- Dynamically load pivot points for selected instruments.

## Project Structure

```plaintext
trading-app/
├── db/
│   └── database.sqlite        # SQLite database file
├── models/
│   └── instrument.js          # Database interactions for instruments
├── public/
│   └── styles.css             # CSS styles for the app
├── views/
│   ├── layouts/
│   │   └── main.handlebars    # Main layout template
│   ├── home.handlebars        # Homepage view
│   └── instrument.handlebars  # Instrument detail view
├── app.js                     # Main server file
├── init-db.js                 # Script to initialize database
└── README.md                  # Project README
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/trading-app.git
   cd trading-app
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Initialize the database:
    - Run the setup script to create the database and tables:
      ```bash
      node init-db.js
      ```

## Usage

1. Start the server:
   ```bash
   node app.js
   ```

2. Open a browser and go to `http://localhost:3000` to access the app.

## API Endpoints

- `GET /`: Displays a list of all instruments and their pivot points.
- `GET /instrument/:id`: Shows pivot point details for a selected instrument.
- `POST /filter`: Filters the instrument list based on user input.

## Database Schema

The `instruments` table is structured as follows:

| Column       | Type     | Description                    |
|--------------|----------|--------------------------------|
| `id`         | INTEGER  | Primary key, auto-incremented  |
| `name`       | TEXT     | Name of the instrument         |
| `symbol`     | TEXT     | Stock symbol or ticker         |
| `pivot_level`| REAL     | Calculated pivot point         |

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---