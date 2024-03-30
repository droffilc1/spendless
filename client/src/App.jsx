

const App = () => {

  return (
    <div>
      <main className="bg-black text-white">
        {/* Navbar */}
        <header className="sticky top-0 right-0 left-0 bg-black z-10">
          <nav className="flex justify-between items-center py-2 px-6">
            {/* Logo text */}
            <div className="flex items-center">
              <div className="ml-2 text-3xl font-bold text-yellow-400"><a href="/"> SpendLess</a></div>
            </div>
            {/* Menu items */}
            <div className="text-gray-400 max-md:hidden">
              <a href="/" rel="noopener noreferrer" className="mx-3 hover:text-gray-200 hover:underline decoration-pink-600 underline-offset-8">Home</a>
              <a href="/" rel="noopener noreferrer" className="mx-3 hover:text-gray-200 hover:underline decoration-pink-600 underline-offset-8">How It Works</a>
              <a href="/" rel="noopener noreferrer" className="mx-3 hover:text-gray-200 hover:underline decoration-pink-600 underline-offset-8">Contact</a>
            </div>
            {/* Buttons */}
            <div className="max-md:hidden">
              <a href="http://" target="_blank" rel="noopener noreferrer" className="mr-4 py-2 p-3 rounded-lg shadow-sm shadow-yellow-400 bg-yellow-400 text-gray-900 hover:text-gray-800 hover:bg-yellow-300">Login</a>
              <a href="http://" target="_blank" rel="noopener noreferrer" className="mr-4 py-2 p-3 rounded-lg shadow-sm shadow-yellow-400 bg-yellow-400 text-gray-900 hover:text-gray-800 hover:bg-yellow-300">Sign up</a>
            </div>
            {/* Menu hamburger responsive */}
            <div className="hidden max-md:block">
              <span className="w-4 h-1 bg-pink-600 block mb-2"></span>
              <span className="w-8 h-1 bg-pink-600 block mb-2"></span>
              <span className="w-5 h-1 bg-pink-600 block"></span>
            </div>
          </nav>
        </header>

        {/* Hero section */}
        <section className="h-screen flex items-center max-md:flex-col max-md:mt-10">
        {/* Hero text */}
          <div className="w-full px-4 py-4 mb-6">
            <h1 className="capitalize text-6xl max-md:text-5xl font-semibold mb-10 text-gray-300">we <span className="text-yellow-300">guarantee</span> <br /> the worthiness of <br /> every <span className="text-yellow-300">money</span> transaction</h1>
            <p className="text-xl max-md:text-base mb-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae dolor modi quisquam excepturi quia. Hic autem a neque commodi. Sint!</p>
            <p className="text-yellow-400 max-md:text-sm mb-6">Take charge of your expenses</p>
            <button className="px-6 py-2 rounded-xl shadow shadow-pink-600 bg-pink-600 hover:bg-pink-500">Get Started</button>
          </div>
          {/* Hero image */}
          <div className="w-full overflow-hidden h-3/4 flex items-center">
            <img src="https://images.unsplash.com/photo-1700836607024-598bbff80b55?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDd8fHxlbnwwfHx8fHw%3D" alt="" className="contrast-150 object-center w-full" />
          </div>
        </section>
        {/* How it works */}
        <section className="h-screen flex items-center max-md:flex-col max-md:mt-10">
          <h3>How It Works</h3>
          <h1>Add All Your Daily Expenses</h1>
          <div>
            <div>
              <p>Create an account</p>
            </div>
            <div>
              <p>Add daily expenses</p>
            </div>
            <div>
              <p>Create a budget</p>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
};

export default App;
