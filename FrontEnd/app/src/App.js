import React from 'react';
import { Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <NavBar/>
      <Route exact path="/" component={Home} />
    </div>
  );
}

export default App;
