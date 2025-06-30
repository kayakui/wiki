import { BrowserRouter as Router, Route} from "react-router-dom";
import { Routes } from "react-router";
import Header from "./comp/Header";
import MainPage from "./comp/MainPage";
import Footer from "./comp/Footer";


function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<MainPage />} />
      </Routes>
      <Footer />
    </Router>
  )
}

export default App;
