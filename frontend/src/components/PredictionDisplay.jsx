import React from 'react';

const PredictionDisplay = ({ prediction }) => {
  return (
    <div className="bg-white p-4 shadow-md rounded text-center">
      <h2 className="text-xl font-semibold">Prediction Result</h2>
      <p className="text-lg mt-2">Risk: <strong>{prediction.prediction ? 'High' : 'Low'}</strong></p>
      <p className="text-sm text-gray-600">Probability: {prediction.probability}</p>
    </div>
  );
};

export default PredictionDisplay;