import { Link } from 'react-router-dom';
import './header.css';
import React, { useEffect, useState } from 'react';

function Header() {

    const body = document.querySelector('body');
    function registrationOpen() {
        body.style.overflowY = 'hidden';
    }

    function loginOpen() {
        body.style.overflowY = 'hidden';
    }

    const [scroll, setScroll] = useState(0);

    const handleScroll = () => {
      setScroll(window.scrollY);
    };
  
    useEffect(() => {
      window.addEventListener("scroll", handleScroll);
      return () => window.removeEventListener("scroll", handleScroll);
    }, []);

    return (
        <header className='header'>
            <div className='header-top-menu'>
                <div className='header-logo'>
                    <Link to='/main' className='header-logo-link'>GidOsetia</Link>
                </div>
                <div className='header-menu'>
                    <Link to='/registration' onClick={registrationOpen}>Регистрация</Link>
                    <Link to='/login' onClick={loginOpen}>Вход</Link>
                </div>
            </div>
            <div className={scroll > 276 ? 'header-main-menu__sticky header-main-menu' : 'header-main-menu'}>
                <Link to='/tours' className={scroll > 276 ? 'header-main-menu-item__sticky header-main-menu-item' : 'header-main-menu-item'}><p>Туры</p></Link>
                <Link to='/events' className={scroll > 276 ? 'header-main-menu-item__sticky header-main-menu-item' : 'header-main-menu-item'}><p>Мероприятия</p></Link>
                <Link to='/booking' className={scroll > 276 ? 'header-main-menu-item__sticky header-main-menu-item' : 'header-main-menu-item'}><p>Букинг</p></Link>
            </div>
        </header>
    )
}

export default Header;