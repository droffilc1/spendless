import { FaGithub, FaLinkedin  } from "react-icons/fa";
import { FaSquareXTwitter } from "react-icons/fa6";


const Footer = () => {
  return (
    <footer className="h-1/4 flex flex-col space-y-10 justify-center mt-10" id="contact">

      <nav className="flex justify-center flex-wrap gap-6 text-gray-500 font-medium">
        <a className="hover:text-white" href="#">Home</a>
        <a className="hover:text-white" href="#how-it-works">How It Works</a>
        <a className="hover:text-white" href="#contact">Contact</a>
      </nav>

      <div className="flex justify-center space-x-5 text-2xl">
        <a href="https://www.linkedin.com/in/clifford-mapesa-a98601216/" target="_blank" rel="noopener noreferrer">
          <FaLinkedin />
        </a>
        <a href="https://twitter.com/droffilcasepam1" target="_blank" rel="noopener noreferrer">
          <FaSquareXTwitter />
        </a>
        <a href="https://github.com/droffilc1/spendless" target="_blank" rel="noopener noreferrer">
          <FaGithub />
        </a>
      </div>
      <p className="text-center text-gray-700 font-medium">&copy; {new Date().getFullYear()} Company Ltd. All rights reserved.</p>
    </footer>
  )
}

export default Footer
