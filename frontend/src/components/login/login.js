import {Link} from 'react-router-dom';
import './login.css';

function Login() {
    const body = document.querySelector('body');
    function loginClose() {
        body.style.overflowY = '';
    }
    return (
        <div className='login-bg'>
            <div className='login-content'>
            <h2 className='login-title'>Вход</h2>
            <form>
                <input type='email' placeholder='Логин' />
                <input type='password' placeholder='Пароль' />
            </form>
                <div className='login-buttons'>
                    <Link to='/registration'><button>Регистрация</button></Link>
                    <Link to='/main' onClick={loginClose}><button><i class="fas fa-times"></i></button></Link>
                    <button><i class="fas fa-check"></i></button>
                </div>
        </div>
        </div>
    )
}

export default Login;