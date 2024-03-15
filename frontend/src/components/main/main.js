import './main.css';
import ItemImg1 from '../assets/img/main/item-img1.png';
import ItemImg2 from '../assets/img/main/item-img2.png';
import Attraction from './attraction/attraction';
function Main() {
    return (
        <div className='main-content'>
            <Attraction
                img={ItemImg1}
                name='Памятник Уастырджи'
                description='На въезде в достопримечательность расположена огромная конная статуя местного святого Уастырджи (в Осетии это самый почитаемый святой), которая словно воедино соединяется со скалой. Визуально создается ощущение, будто старец на лошади выскакивает из отвесной скалы и парит в воздухе.'
            />
            <Attraction
                img={ItemImg2}
                name='Родовые башни'
                description='Осетинские родовые башни — уникальные памятники истории и культуры осетинского народа.  В Осетии насчитывается более трехсот башен различного назначения, многие из них разрушены.  Но даже руины башен на фоне величественных гор выглядят очень красиво.'
            />
        </div>
    )
}

export default Main;