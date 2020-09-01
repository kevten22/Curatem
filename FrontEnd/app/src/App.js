import React from 'react';
import { Route } from 'react-router-dom';
import NavBar from './components/navbar';
import Home from './pages/Home';
import Category from './pages/Category'
import Categories from './pages/Categories';
import Path from './pages/Path';
import MyPaths from './pages/MyPaths';

function App() {
  return (
    <div className="App">
      <NavBar/>
      <Route exact path="/" component={Home} />
      <Route path="/category" component={Category} />
      <Route path="/categories" component={Categories} />
      <Route path="/path" component={Path} />
      <Route path="/mypaths" component={MyPaths} />
    </div>
  );
}

export default App;
