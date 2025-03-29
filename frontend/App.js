
import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';

const Graphique = () => {
  const [graphData, setGraphData] = useState([]);
  const [selectedPair, setSelectedPair] = useState('BTC-USD');
  
  useEffect(() => {
    fetch(`http://127.0.0.1:8000/graph/${selectedPair}`)
      .then(response => response.json())
      .then(data => {
        setGraphData(data);
      });
  }, [selectedPair]);

  return (
    <div>
      <select onChange={(e) => setSelectedPair(e.target.value)}>
        <option value="BTC-USD">Bitcoin (Crypto)</option>
        <option value="ETH-USD">Ethereum (Crypto)</option>
        <option value="EURUSD=X">EUR/USD (Forex)</option>
        <option value="TSLA">Tesla (Action)</option>
      </select>
      <Plot
        data={graphData.data}
        layout={graphData.layout}
        config={{ responsive: true }}
      />
    </div>
  );
};

export default Graphique;
