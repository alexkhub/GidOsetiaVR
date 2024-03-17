import { Link } from 'react-router-dom';
import axios from 'axios'
import './login.css';

function Login() {
    const body = document.querySelector('body');
    function loginClose() {
        body.style.overflowY = '';
    }

    function login() {
        const loginValue = document.querySelector('#login-input').value;
        const passwordValue = document.querySelector('#login-password').value;

        if (localStorage.getItem('jwt') === null) {
            axios.post("http://127.0.0.1:8000/auth/jwt/create",
                {
                    username: loginValue,
                    password: passwordValue
                },
                { headers: { 'Content-Type': 'application/json' } }).then(
                    data => {
                        console.log('fdsfsdfsd');
                    }
                );
        }

        axios.defaults.headers.common['Authorization'] = localStorage.getItem('jwt');
    }
    return (
        <div className='login-bg'>
            <div className='login-content'>
                <h2 className='login-title'>Вход</h2>
                <form>
                    <input type='email' placeholder='Логин' id='login-input' />
                    <input type='password' placeholder='Пароль' id='login-password' />
                </form>
                <div className='login-buttons'>
                    <Link to='/registration'><button className='registration-hyperlink'>Регистрация</button></Link>
                    <Link to='/main' onClick={loginClose}><button><i class="fas fa-times"></i></button></Link>
                    <button onClick={login}><i class="fas fa-check"></i></button>
                </div>
            </div>
        </div>
    )
}

export default Login;