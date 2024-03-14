import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Header from './components/header/header';
import Main from './components/main/main';
import Footer from './components/footer/footer';

function App() {
  return (
    <BrowserRouter>
      <Header/>
      <Main/>
      <Footer/>
      <Routes>
          {/* <Route path='/tours' element={} /> */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
