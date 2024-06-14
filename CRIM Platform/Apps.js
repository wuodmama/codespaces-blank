import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [incidents, setIncidents] = useState([]);
  const [newIncident, setNewIncident] = useState('');

  useEffect(() => {
    axios.get('/status')
      .then(response => {
        setIncidents(response.data);
      })
      .catch(error => {
        console.error('Error fetching incidents:', error);
      });
  }, []);

  const createIncident = () => {
    axios.post('/monitor', { description: newIncident })
      .then(response => {
        setIncidents([...incidents, response.data.incident]);
      })
      .catch(error => {
        console.error('Error creating incident:', error);
      });
  };

  return (
    <div className="App">
      <h1>Incident Management</h1>
      <input
        type="text"
        value={newIncident}
        onChange={(e) => setNewIncident(e.target.value)}
        placeholder="Describe the incident"
      />
      <button onClick={createIncident}>Create Incident</button>
      <ul>
        {incidents.map(incident => (
          <li key={incident.id}>
            {incident.description} - {incident.status}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
