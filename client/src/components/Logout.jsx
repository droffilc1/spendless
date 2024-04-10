import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Logout = () => {
  const navigate = useNavigate();
  const [loggingOut, setLoggingOut] = useState(false);

  useEffect(() => {
    const logoutUser = async () => {
      try {
        // Set loggingOut state to true to show loading message
        setLoggingOut(true);

        // Send a request to the server to log out the user
        const response = await fetch('http://127.0.0.1:5000/api/v1/logout', {
          method: 'POST',
          credentials: 'include', // Include cookies in the request
          headers: {
            'Content-Type': 'application/json',
          },
        });

        if (response.ok) {
          // User is logged out successfully
          navigate('/login');
        } else {
          // Handle logout failure
          console.error('Logout failed:', response.statusText);
        }
      } catch (error) {
        console.error('Error logging out:', error.message);
        // Handle errors if needed
      } finally {
        // Reset loggingOut state to false after logout process completes
        setLoggingOut(false);
      }
    };

    logoutUser();
  }, [navigate]);

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="bg-white p-8 rounded-lg shadow-md">
        {loggingOut ? (
          <p className="text-center text-gray-700">Logging out...</p>
        ) : (
          <p className="text-center text-green-700">Logout process completed. Redirecting...</p>
        )}
      </div>
    </div>
  );
};

export default Logout;
