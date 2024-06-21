import React from 'react';
import './App.css';
import Home from './components/Home'; 
import '@fortawesome/fontawesome-free/css/all.min.css';
import { BrowserRouter as Router, Route, Routes, BrowserRouter } from 'react-router-dom';

function App() {
  return (
    <>
    <BrowserRouter>
    <Home/>
    </BrowserRouter>
      
    </> 
  );
}

export default App;
