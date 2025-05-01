import { useState } from 'react';

function App() {
  const [result, setResult] = useState(null);

  const testPrediction = async () => {
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          input: [5, 166, 72, 19, 175, 25.8, 0.587, 51] // Sample input features
        })
        .then(res => res.json())
        .then(data => console.log(data))
        .catch(err => console.error(err))
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error:', error);
      setResult({ error: 'Failed to fetch prediction' });
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Diabetes Predictor</h1>
      <button onClick={testPrediction}>Test Prediction</button>
      {result && (
        <div style={{ marginTop: '1rem' }}>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;