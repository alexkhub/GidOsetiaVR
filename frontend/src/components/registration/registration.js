import {Link} from 'react-router-dom';
import './registration.css';

function Registration() {
    const body = document.querySelector('body');
    function registrationClose() {
        body.style.overflowY = '';
    }
    return (
        <div className='registration-bg'>
            <div className='registration-content'>
            <h2 className='registration-title'>Регистрация</h2>
            <form>
                <input type='email' placeholder='Логин' />
                <input type='tel' placeholder='Телефон' />
                <input type='password' placeholder='Пароль' />
                <input type='password' placeholder='Повторите пароль' />
            </form>
                <div className='registration-buttons'>
                    <Link to='/login'><button>Вход</button></Link>
                    <Link to='/main' onClick={registrationClose}><button><i class="fas fa-times"></i></button></Link>
                    <button><i class="fas fa-check"></i></button>
                </div>
        </div>
        </div>
    )
}

export default Registration;