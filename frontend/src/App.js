import React, { useState } from 'react';
import Register from './components/Register';

function App() {
  const [balance, setBalance] = useState(null);
  const [transactions, setTransactions] = useState([]);
  
  const fetchBalance = async (userId) => {
    const res = await fetch(`/balance/${userId}`);
    const data = await res.json();
    setBalance(data.balance);
  };

  const fetchTransactions = async (userId) => {
    const res = await fetch(`/transactions/${userId}`);
    const data = await res.json();
    setTransactions(data);
  };

  return (
    <div>
      <Register />
      <h3>Balance: {balance}</h3>
      <h3>Transactions:</h3>
      <ul>
        {transactions.map(t => (
          <li key={t.id}>{t.type} - {t.amount} - {t.date}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
