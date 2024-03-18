import './recomendationsItem.css';

function RecomendationsItem(props) {
    return (
        <div className='recomendations-item'>
            <img src={props.recomendationImg} alt={props.alt} />
            <div className='recomendations-item-info'>
                <p className='recomendations-item-name'>{props.recomendationItemName}</p>
                <p className='recomendations-item-adress'>{props.adress}</p>
                <button>Добавить в избранное</button>
            </div>
        </div>
    )
}

export default RecomendationsItem;