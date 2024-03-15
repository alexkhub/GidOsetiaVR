import React, { useState } from 'react';
import {Link} from 'react-router-dom';
import './header.css';

function Header() {

    return (
        <header className='header'>
            <div className='header-top-menu'>
                <div className='header-logo'>
                    <Link to='/main'>GidOsetia</Link>
                </div>
                <div className='header-menu'>
                    <Link to='/registration'>Регистрация</Link>
                    <Link to='/login'>Вход</Link>
                </div>
            </div>
            <div className='header-main-menu'>
                <Link to='/tours' className='header-main-menu-item'>Туры</Link>
                <Link to='/events' className='header-main-menu-item'>Мероприятия</Link>
                <Link to='/booking' className='header-main-menu-item'>Букинг</Link>
            </div>
        </header>
    )
}

export default Header;