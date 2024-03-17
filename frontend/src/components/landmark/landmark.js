import './landmark.css';
import Footer from '../footer/footer';
import LandmarkMenuItem from './landmarkMenuItem/landmarkMenuItem';
import RecomendationsItem from './recomendationsItem/recomendationsItem';

import landmarkImg from './landmark-img.jpg';
import backgroundRoutes from './background-routes.png';

import restaurantExample from './restaurant-example-img.png';
import hotelExample from './hotel-example-img.png';

import campingIcon from './landmarkMenuItem/icons/camping-icon.png';
import eventsIcon from './landmarkMenuItem/icons/events-icon.png';
import excursionsIcon from './landmarkMenuItem/icons/excursions-icon.png';
import feedbackIcon from './landmarkMenuItem/icons/feedback-icon.png';
import hotelsIcon from './landmarkMenuItem/icons/hotels-icon.png';
import placesIcon from './landmarkMenuItem/icons/places-icon.png';
import restaurantsIcon from './landmarkMenuItem/icons/restaurants-icon.png';
import routesIcon from './landmarkMenuItem/icons/routes-icon.png';


function Landmark() {
    return (
        <div className='landmark-content'>
            <div className='landmark-img-container'>
                <img src={landmarkImg} alt='landmark img' />
                <button className='add-favorite-button'>
                    <p>Добавить в избранное</p>
                </button>
            </div>
            <div className='landmark-info'>
                <h3 className='landmark-title'>Проспект Мира</h3>
                <p className='landmark-text'>Исторически Владикавказу повезло оказаться на торговом пути в направлении Закавказья. Это означало, что в городе стали заселяться богатые люди, которые помогали городу быстро расти и развиваться.
                    Проспект начал формироваться в первой половине XIX века усилиями начальника военного округа Петра Нестерова.</p>
            </div>
            <div className='landmark-menu'>
                <LandmarkMenuItem icon={routesIcon} itemName='Маршруты' alt='routes icon' />
                <LandmarkMenuItem icon={campingIcon} itemName='Кемпинг' alt='camping icon' />
                <LandmarkMenuItem icon={feedbackIcon} itemName='Отзывы' alt='feedback icon' />
                <LandmarkMenuItem icon={restaurantsIcon} itemName='Рестораны' alt='restaurants icon' />
                <LandmarkMenuItem icon={hotelsIcon} itemName='Отели' alt='hotels icon' />
                <LandmarkMenuItem icon={excursionsIcon} itemName='Экскурсии' alt='excursions icon' />
                <LandmarkMenuItem icon={eventsIcon} itemName='События' alt='events icon' />
                <LandmarkMenuItem icon={placesIcon} itemName='Места' alt='places icon' />
            </div>
            <img src={backgroundRoutes} alt='background img' className='background-img-routes' />
            <div className='recomendations'>
                <p className='recomendations-title'>Лучшие рестораны Владикавказа</p>
                <div className='recomendations-content'>
                    <RecomendationsItem recomendationImg={restaurantExample} alt='restaurant img' recomendationItemName='Ресторан "Дендрариум"' adress='Ул. Еврея Холокостова 1933' />
                    <RecomendationsItem recomendationImg={hotelExample} alt='hotel img' recomendationItemName='Ресторан "Владикавказ"' adress='Ул. Еврея Холокостова 1933' />
                    <RecomendationsItem recomendationImg={restaurantExample} alt='restaurant img' recomendationItemName='Ресторан "Дендрариум"' adress='Ул. Еврея Холокостова 1933' />
                    <RecomendationsItem recomendationImg={hotelExample} alt='hotel img' recomendationItemName='Ресторан "Владикавказ"' adress='Ул. Еврея Холокостова 1933' />
                </div>
            </div>
            <Footer />
        </div>
    )
}

export default Landmark;