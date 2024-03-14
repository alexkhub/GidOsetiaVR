import './attraction.css'

function Attraction(props) {
    return (
        <div className='main-content-item'>
            <img src={props.img} />
            <div className='item-info'>
                <p className='item-title'>{props.name}</p>
                <p className='item-description'>{props.description}</p>
            </div>
        </div>
    )
}

export default Attraction;