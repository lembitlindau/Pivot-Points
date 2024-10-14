const express = require('express');
const exphbs = require('express-handlebars');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

// Initialize app
const app = express();
const PORT = 3000;

// Configure Handlebars
app.engine('handlebars', exphbs.engine({ defaultLayout: 'main' }));
app.set('view engine', 'handlebars');

// Serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Initialize SQLite Database
const db = new sqlite3.Database('./db/database.sqlite');

// Middleware to parse form data
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Set up routes (see Step 5)

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

const { getAllInstruments, getInstrumentById } = require('./models/instrument');

// Home page - list of instruments
app.get('/', (req, res) => {
    getAllInstruments((err, instruments) => {
        if (err) {
            return res.status(500).send('Database error');
        }
        res.render('home', { instruments });
    });
});

// Display a specific instrument's pivot point
app.get('/instrument/:id', (req, res) => {
    const instrumentId = req.params.id;
    getInstrumentById(instrumentId, (err, instrument) => {
        if (err || !instrument) {
            return res.status(404).send('Instrument not found');
        }
        res.render('instrument', { instrument });
    });
});
