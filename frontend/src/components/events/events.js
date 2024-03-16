import './events.css'
import Event from './event/event';
import eventImg1 from '../assets/img/events/event-img1.png';
import eventImg2 from '../assets/img/events/event-img2.png';

function Events() {
    return (
        <div className='events-content'>
            <div className='events-container'>
                <Event
                    eventImg={eventImg1}
                    descr='Старый Новый год'
                />
                <Event
                    eventImg={eventImg2}
                    descr='Молодой Старый год'
                />
            </div>
            <div className='events-container'>
                <Event
                    eventImg={eventImg1}
                    descr='Старый Новый год'
                />
                <Event
                    eventImg={eventImg2}
                    descr='Молодой Старый год'
                />
            </div>
            <div className='events-container'>
                <Event
                    eventImg={eventImg1}
                    descr='Старый Новый год'
                />
                <Event
                    eventImg={eventImg2}
                    descr='Молодой Старый год'
                />
            </div>
        </div>
    )
}

export default Events;