import React, { useState } from 'react';
import Plot from 'react-plotly.js';
import './App.css';

const App = () => {
  const [symbol, setSymbol] = useState('BTC-USD');
  const [data, setData] = useState(null);

  const handleAnalyse = async () => {
    const response = await fetch(`https://f4.onrender.com/graph/${symbol}`);
    const json = await response.json();
    setData(json);
  };

  return (
    <div className="app dark-mode">
      <h1>Analyse Technique 🧠</h1>
      <select onChange={(e) => setSymbol(e.target.value)} value={symbol}>
        <option value="BTC-USD">Bitcoin</option>
        <option value="ETH-USD">Ethereum</option>
        <option value="EURUSD=X">EUR/USD</option>
        <option value="TSLA">Tesla</option>
      </select>
      <button onClick={handleAnalyse}>Analyser</button>
      {data && (
        <Plot
          data={data.data}
          layout={{
            ...data.layout,
            paper_bgcolor: '#111',
            plot_bgcolor: '#111',
            font: { color: '#fff' },
          }}
          useResizeHandler
          style={{ width: "100%", height: "600px" }}
        />
      )}
      <div className="lee-sin">👁 Mode Lee Sin Activé</div>
    </div>
  );
};

export default App;