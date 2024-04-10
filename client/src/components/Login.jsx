import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from './Navbar';

const LogIn = () => {
  const [credentials, setCredentials] = useState({ email: '', password: '' });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setCredentials({ ...credentials, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:5000/api/v1/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials)
      });
      const data = await response.json();

      if (response.ok) {
        // Redirect to dashboard after successful login
        navigate('/dashboard');
      } else {
        console.error('Login error', data.message);
      }
    } catch (error) {
      console.error('Login error', error);
    }
  };

  return (
    <div className="h-screen md:bg-[url('assets/auth.jpeg')] bg-stone-500 overflow-hidden bg-cover transition duration-300">
      <Navbar />
      <div className="max-w-md mx-auto">
        <h2 className="text-2xl font-bold mb-4">LogIn</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-black text-sm font-bold mb-2" htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              value={credentials.email}
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
              value={credentials.password}
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
            Log in
          </button>
        </form>
        <p className='mt-3'>Don't have an account? <a href="/signup">Register</a></p>
      </div>
    </div>
  );
}

export default LogIn;
