import './landmarkMenuItem.css';
function LandmarkMenuItem(props) {
    return (
        <div className='landmark-menu-item'>
            <img src={props.icon} alt={props.alt} className='landmark-menu-item-img' />
            <p className='landmark-menu-item-text'>{props.itemName}</p>
        </div>
    )
}

export default LandmarkMenuItem;