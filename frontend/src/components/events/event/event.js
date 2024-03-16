import './event.css';

function Event (props) {
    return (
        <div className = 'event-item'>
            <img src={props.eventImg}></img>
            <p className='event-description'>{props.descr}</p>
        </div>
    )
}

export default Event;