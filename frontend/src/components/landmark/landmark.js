import './landmark.css';
import landmarkImg from './landmarkImg1.png'
function Landmark() {
    return (
        <div className="landmark-content">
            <div className="landmark-img-container">
                <h2 className='landmark-title'>Проспект</h2>
                <img src={landmarkImg} alt='landmark img'></img>
                <div className="landmark-text">
                    <div className='landmark-text-container'>
                    <p>
                        Исторически Владикавказу повезло оказаться на торговом пути в направлении Закавказья. Это означало, что в городе стали заселяться богатые люди, которые помогали городу быстро расти и развиваться.
                        Проспект начал формироваться в первой половине XIX века усилиями начальника военного округа Петра Нестерова.
                        Исторически Владикавказу повезло оказаться на торговом пути в направлении Закавказья. Это означало, что в городе стали заселяться богатые люди, которые помогали городу быстро расти и развиваться.
                        Проспект начал формироваться в первой половине XIX века усилиями начальника военного округа Петра Нестерова.
                    </p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Landmark;