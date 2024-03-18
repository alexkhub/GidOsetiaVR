import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Header from './components/header/header';
import Main from './components/main/main';
import Landmark from './components/landmark/landmark';
import Footer from './components/footer/footer';
import Registration from './components/registration/registration';
import Login from './components/login/login';
import Events from './components/events/events';
import Panorama from './components/panorama/panorama';

function App() {
  return (
    <>
      <BrowserRouter>
        <Header />
        <Routes>
            <Route path='/registration' element={<Registration/>}/>
            <Route path='/login' element={<Login/>}/>
            <Route path='/main' element={<Main/>}/>
            <Route path='/events' element={<Events/>}/>
            <Route path='/panorama' element={<Panorama/>}/>
            <Route path='/landmark' element={<Landmark/>}/>
            <Route path='/' element={<Main/>}/>
        </Routes>
      </BrowserRouter>
      <Footer/>
    </>
  );
}

export default App;
