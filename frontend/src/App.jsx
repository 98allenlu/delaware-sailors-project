import { useState, useEffect } from 'react';
// Import the mock data from the file you created
import { MOCK_DATA } from './mockVoyages.js';
// Import the basic styling
import './App.css';

function App() {
  // Use React's "state" to hold our list of voyages
  const [voyages, setVoyages] = useState([]);
  const [loading, setLoading] = useState(true);

  // This "useEffect" hook runs once when the component first loads
  useEffect(() => {
    // We're simulating a network request by using the mock data
    // In the future, we will replace this with a real 'fetch' call to our API
    setVoyages(MOCK_DATA);
    setLoading(false);
  }, []); // The empty array [] means "only run this once"

  return (
    <div className="app-container">
      <h1>Delaware Sailors Database</h1>
      <p>A searchable database of voyages from 1730-1775.</p>

      {/* A simple loading message */}
      {loading && <div>Loading data...</div>}

      {/* We only show the table *after* data has loaded */}
      {!loading && (
        <div className="table-container">
          <table>
            <thead>
              <tr>
                <th>Voyage ID</th>
                <th>Ship Name</th>
                <th>Captain</th>
                <th>Date</th>
                <th>Origin Port</th>
                <th>Destination Port</th>
                <th>Source</th>
              </tr>
            </thead>
            <tbody>
              {/* Loop over each voyage in our "voyages" state and create a table row */}
              {voyages.map((voyage) => (
                <tr key={voyage.voyageid}>
                  <td>{voyage.voyageid}</td>
                  <td>{voyage.shipname || 'N/A'}</td>
                  <td>{voyage.captain || 'N/A'}</td>
                  <td>{voyage.date}</td>
                  <td>{voyage.origin_port || 'N/A'}</td>
                  <td>{voyage.destination_port || 'N/A'}</td>
                  <td>{voyage.Source_Database}</td>
                </tr>
              ))}
            </tbody>
          </table>
          {voyages.length === 0 && <p>No voyages found.</p>}
        </div>
      )}
    </div>
  );
}

export default App;

