import {Link} from 'react-router-dom';
import './attraction.css'

function Attraction(props) {
    return (
        <Link to='/landmark' className='main-content-item'>
            <img src={props.img} alt = {props.img} />
            <div className='item-info'>
                <p className='item-title'>{props.name}</p>
                <p className='item-description'>{props.description}</p>
            </div>
        </Link>
    )
}

export default Attraction;