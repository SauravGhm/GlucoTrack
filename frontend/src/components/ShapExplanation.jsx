import React from 'react';

const ShapExplanation = ({ shapValues }) => {
  return (
    <div className="bg-white mt-4 p-4 shadow-md rounded">
      <h2 className="text-xl font-semibold mb-2">SHAP Explanation</h2>
      <ul className="list-disc pl-6">
        {Object.entries(shapValues).map(([key, val]) => (
          <li key={key}>
            <span className="font-medium">{key}</span>: {val}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ShapExplanation;