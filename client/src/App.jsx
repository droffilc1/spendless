import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import About from "./components/About";
import Footer from "./components/Footer";


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
