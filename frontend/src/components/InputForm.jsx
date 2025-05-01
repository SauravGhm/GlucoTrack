import React, { useState } from 'react';
import axios from 'axios';

const InputForm = ({ setPrediction, setShapValues }) => {
  const [formData, setFormData] = useState({
    Pregnancies: 0,
    Glucose: 0,
    BloodPressure: 0,
    SkinThickness: 0,
    Insulin: 0,
    BMI: 0,
    DiabetesPedigreeFunction: 0,
    Age: 0
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: parseFloat(e.target.value) });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const features = Object.values(formData);
    const response = await axios.post('http://localhost:5000/api/predict', { features });
    const shap = await axios.post('http://localhost:5000/api/shap', { features });
    setPrediction(response.data);
    setShapValues(shap.data);
  };

  return (
    <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-4 mb-6">
      {Object.keys(formData).map((key) => (
        <input
          key={key}
          name={key}
          type="number"
          value={formData[key]}
          onChange={handleChange}
          placeholder={key}
          className="border p-2 rounded"
        />
      ))}
      <button type="submit" className="col-span-2 bg-blue-600 text-white px-4 py-2 rounded">
        Predict
      </button>
    </form>
  );
};

export default InputForm;