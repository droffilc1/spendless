const Navbar = () => {
  return (
    <header className="sticky top-0 right-0 left-0 bg-black z-10">
      <nav className="flex justify-between items-center py-2 px-6">
        {/* Logo text */}
        <div className="flex items-center">
          <div className="ml-2 text-3xl font-bold text-yellow-400"><a href="/"> SpendLess</a></div>
        </div>
        {/* Menu items */}
        <div className='text-gray-400 max-md:hidden'>
          <a href="/" rel="noopener noreferrer" className="mx-3 hover:text-gray-200 hover:underline decoration-pink-600 underline-offset-8">Home</a>
          <a href="#how-it-works" rel="noopener noreferrer" className="mx-3 hover:text-gray-200 hover:underline decoration-pink-600 underline-offset-8">How It Works</a>
          <a href="#contact" rel="noopener noreferrer" className="mx-3 hover:text-gray-200 hover:underline decoration-pink-600 underline-offset-8">Contact</a>
        </div>
        {/* Buttons */}
        <div className='max-md:hidden'>
          <a href="/login" rel="noopener noreferrer" className="mr-4 py-2 p-3 rounded-lg shadow-sm shadow-yellow-400 bg-yellow-400 text-gray-900 hover:text-gray-800 hover:bg-yellow-300">Login</a>
          <a href="/signup" rel="noopener noreferrer" className="mr-4 py-2 p-3 rounded-lg shadow-sm shadow-yellow-400 bg-yellow-400 text-gray-900 hover:text-gray-800 hover:bg-yellow-300">Sign up</a>
        </div>
        {/* Menu hamburger responsive */}
        <div className="hidden max-md:block">
            <span className="w-4 h-1 bg-pink-600 block mb-2"></span>
            <span className="w-8 h-1 bg-pink-600 block mb-2"></span>
            <span className="w-5 h-1 bg-pink-600 block"></span>
        </div>
      </nav>
    </header>
  )
}

export default Navbar
