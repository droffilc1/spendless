import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from '../layout/Navbar';

const Registration = () => {
  const [formData, setFormData] = useState({
    Name: '',
    email: '',
    password: ''
  });
  const [errorMessage, setErrorMessage] = useState(''); // State to store error message
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
    setErrorMessage(''); // Clear error message on input change
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrorMessage(''); // Clear any previous error message before submitting
    try {
      const response = await fetch('https://spendless.ink/api/v1/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });

      if (response.ok) {
        // Redirect to dashboard after successful registration
        navigate('/dashboard');
      } else {
        const errorData = await response.json(); // Get error message from server response
        setErrorMessage(errorData.message || 'Registration failed. Please try again.'); // Display error message
      }
    } catch (error) {
      setErrorMessage('An unexpected error occurred. Please try again later.'); // Display a generic error message
    }
  };

  return (
    <div className="h-screen md:bg-[url('auth.jpeg')] bg-stone-500 overflow-hidden bg-cover transition duration-300">
      <Navbar />
      <div className="max-w-md mx-auto">
        <h2 className="text-2xl font-bold mb-4">Registration</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-black text-sm font-bold mb-2" htmlFor="Name">Name</label>
            <input
              type="text"
              id="Name"
              name="Name"
              value={formData.Name}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="Enter your name"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-black text-sm font-bold mb-2" htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="Enter your email address"
              required
            />
          </div>
          <div className="mb-6">
            <label className="block text-black text-sm font-bold mb-2" htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="Enter your password"
              required
            />
          </div>
          <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          >
            Register
          </button>
        </form>

        {errorMessage && ( // Display error message if there's any
          <div className="mt-3 text-red-600">
            {errorMessage}
          </div>
        )}

        <p className="mt-3">Already have an account? <a href="/login">Login</a></p>
      </div>
    </div>
  );
};

export default Registration;
