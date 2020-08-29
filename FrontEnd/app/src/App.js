import React from 'react';
import { Route } from 'react-router-dom';
import NavBar from './components/navbar';
import Home from './pages/Home';
import Categories from './pages/Categories';
import MyPaths from './pages/MyPaths'

function App() {
  return (
    <div className="App">
      <NavBar/>
      <Route exact path="/" component={Home} />
      <Route path="/categories" component={Categories} />
      <Route path="/mypaths" component={MyPaths} />
    </div>
  );
}

export default App;
