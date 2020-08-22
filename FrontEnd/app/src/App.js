import React from 'react';
import { Route } from 'react-router-dom';
import NavBar from './components/navbar';
import Home from './pages/Home';

function App() {
  return (
    <div className="App">
      <NavBar/>
      <Route exact path="/" component={Home} />
    </div>
  );
}

export default App;
