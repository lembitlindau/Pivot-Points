const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./db/database.sqlite');

// Fetch all instruments
function getAllInstruments(callback) {
    const query = 'SELECT * FROM instruments';
    db.all(query, [], (err, rows) => {
        callback(err, rows);
    });
}

// Fetch a specific instrument by ID
function getInstrumentById(id, callback) {
    const query = 'SELECT * FROM instruments WHERE id = ?';
    db.get(query, [id], (err, row) => {
        callback(err, row);
    });
}

module.exports = { getAllInstruments, getInstrumentById };
