const Hero = () => {
    return (
        <section className="h-screen flex items-center max-md:flex-col max-md:mt-10">
            {/* Hero text */}
            <div className="w-full px-8 py-4 mb-6">
                <h1 className="capitalize text-6xl max-md:text-5xl font-semibold mb-10 text-gray-300">we <span className="text-yellow-300">guarantee</span> <br /> the worthiness of <br /> every <span className="text-yellow-300">money</span> transaction</h1>
                <p className="text-xl max-md:text-base mb-4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae dolor modi quisquam excepturi quia. Hic autem a neque commodi. Sint!</p>
                <p className="text-yellow-400 max-md:text-sm mb-6">Take charge of your expenses</p>
                <button className="px-6 py-2 rounded-xl shadow shadow-pink-600 bg-pink-600 hover:bg-pink-500"><a href="/signup">Get Started</a></button>
            </div>
            {/* Hero image */}
            <div className="w-full overflow-hidden h-3/4 flex items-center">
                <img src="https://images.unsplash.com/photo-1700836607024-598bbff80b55?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDd8fHxlbnwwfHx8fHw%3D" alt="" className="contrast-150 object-center w-full" />
            </div>
        </section>
    )
}

export default Hero
