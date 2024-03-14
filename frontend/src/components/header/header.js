import { Link } from 'react-router-dom';
import HeaderImg from '../assets/img/header/header-background.png'
import './header.css';

function Header() {
    return (
        <header className='header'>
            <div className='header-top-menu'>
                <div className='header-logo'>
                    <p>GidOsetia</p>
                </div>
                <div className='header-menu'>
                    <a href=''>Регистрация</a>
                    <a href=''>Вход</a>
                </div>
            </div>
            <div className='header-main-menu'>
                <a href='' className='header-main-menu-item'>Туры</a>
                <a href='' className='header-main-menu-item'>Мероприятия</a>
                <a href='' className='header-main-menu-item'>Букинг</a>
            </div>
        </header>
    )
}

export default Header;