import About from "./components/contents/About";
import Footer from "./components/layout/Footer";
import Hero from "./components/contents/Hero";
import Navbar from "./components/layout/Navbar";


const App = () => {
  return (
    <div>
      <main className="bg-black text-white">
        <Navbar />
        <Hero />
        <About />
        <Footer />
      </main>
    </div>
  );
};

export default App;
