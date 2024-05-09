import React from 'react'
import '../css/Header.css'
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import LanguageIcon from '@mui/icons-material/Language';

const Header = () => {
  return (
    <>
    <div className="header-box">
      <div className="header-logo">
        <img src="" alt="logo" />
      </div>
      <div className="header-main-menu">
        <ul className="main-menu">
          <li className="menu-item">Home</li>
          <li className="menu-item">About</li>
          <li className="menu-item">Contact</li>
          <li className="menu-item">Faq</li>
        </ul>
      </div>
      <div className="header-icons">
        <div><AccountCircleIcon /></div>
        <div><LanguageIcon /></div>
      </div>
    </div>
    </>
  )
}

export default Header