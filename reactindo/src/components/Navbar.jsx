import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Navbar = () => {
  const [navbarData, setNavbarData] = useState(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/navbar/')
      .then(response => {
        setNavbarData(response.data[0]); // Assuming the API returns a list and you want the first navbar item
      })
      .catch(error => {
        console.error('There was an error fetching the navbar data!', error);
      });
  }, []);

  if (!navbarData) {
    return <div>Loading...</div>;
  }

  return (
    <nav>
      <div className="wrapper">
        <div className="logo">
          <a href="#">{navbarData.logo}</a>
        </div>
        <input type="radio" name="slider" id="menu-btn" />
        <input type="radio" name="slider" id="close-btn" />
        <ul className="nav-links">
          <label htmlFor="close-btn" className="btn close-btn">
            <i className="fas fa-times" />
          </label>
          {navbarData.menu_items.map(menuItem => (
            <li key={menuItem.id}>
              <a href={menuItem.url}>{menuItem.name}</a>
              {menuItem.is_dropdown && (
                <>
                  <input type="checkbox" id={`showDrop${menuItem.id}`} />
                  <label htmlFor={`showDrop${menuItem.id}`} className="mobile-item">
                    {menuItem.name}
                  </label>
                  <ul className="drop-menu">
                    {menuItem.dropdown_items.map(dropdownItem => (
                      <li key={dropdownItem.id}>
                        <a href={dropdownItem.url}>{dropdownItem.name}</a>
                      </li>
                    ))}
                  </ul>
                </>
              )}
              {menuItem.is_mega_menu && (
                <>
                  <input type="checkbox" id={`showMega${menuItem.id}`} />
                  <label htmlFor={`showMega${menuItem.id}`} className="mobile-item">
                    {menuItem.name}
                  </label>
                  <div className="mega-box">
                    <div className="content">
                      {menuItem.mega_items.map(megaItem => (
                        <div key={megaItem.id} className="row">
                          <header>{megaItem.name}</header>
                          <ul className="mega-links">
                            <li><a href={megaItem.url}>{megaItem.name}</a></li>
                          </ul>
                        </div>
                      ))}
                    </div>
                  </div>
                </>
              )}
            </li>
          ))}
        </ul>
        <label htmlFor="menu-btn" className="btn menu-btn">
          <i className="fas fa-bars" />
        </label>
      </div>
    </nav>
  );
};

export default Navbar;
