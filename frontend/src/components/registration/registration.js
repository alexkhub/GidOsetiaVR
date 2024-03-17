import { Link } from 'react-router-dom';
import './registration.css';
import axios from 'axios';

function Registration() {
    const body = document.querySelector('body');
    function registrationClose() {
        body.style.overflowY = '';
    }

    const login = document.querySelector('#registration-input-login');
    const firstName = document.querySelector('#registration-input-firstname');
    const lastName = document.querySelector('#registration-input-lastname');
    const email = document.querySelector('#registration-input-email');
    const tel = document.querySelector('#registration-input-tel');
    const password = document.querySelector('#registration-input-password');
    const repeatPassword = document.querySelector('#registration-input-repeat-password');
    const newsletter =document.querySelector('#subscribe-checkbox')
    const fileInput = document.querySelector('#registration-file-input-label');
    const csrf_token = document.cookie;

    function registration() {
        axios.post("http://127.0.0.1:8000/api-expeditions/registration/",
            {
                username: login.value,
                first_name: firstName.value,
                last_name: lastName.value,
                email: email.value,
                phone: tel.value,
                password: password.value,
                repeat_password: repeatPassword.value,
                subscribe_to_the_newsletter: newsletter.checked,
                csrfmiddlewaretoken: csrf_token
            },
        );
        console.log(csrf_token)
    }
    return (
        <div className='registration-bg'>
            <div className='registration-content'>
                <h2 className='registration-title'>Регистрация</h2>
                <form>
                    <input type='text' placeholder='Логин' id='registration-input-login' />
                    <input type='text' placeholder='Имя' id='registration-input-firstname' />
                    <input type='text' placeholder='Фамилия' id='registration-input-lastname' />
                    <input type='email' placeholder='Почта' id='registration-input-email' />
                    <input type='tel' placeholder='Телефон' id='registration-input-tel' />
                    <input type='password' placeholder='Пароль' id='registration-input-password' />
                    <input type='password' placeholder='Повторите пароль' id='registration-input-repeat-password' />
                    <div className='registration-form-buttons'>
                        <div className='subscribe-container'>
                            <input type='checkbox' id='subscribe-checkbox' />
                            <label for='subscribe-checkbox'>Подписаться на рассылку</label>
                        </div>
                    </div>
                </form>
                <div className='registration-buttons'>
                    <Link to='/login'><button>Вход</button></Link>
                    <Link to='/main' onClick={registrationClose}><button><i class="fas fa-times"></i></button></Link>
                    <button><i class="fas fa-check" onClick={registration}></i></button>
                </div>
            </div>
        </div>
    )
}

export default Registration;