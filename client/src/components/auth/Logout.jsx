import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const Logout = () => {
  const navigate = useNavigate();

  useEffect(() => {
    navigate('/login')
  }, [navigate])

  return (
    <div className="flex items-center justify-center h-screen">
      <div className="bg-white p-8 rounded-lg shadow-md">
        <p className="text-center text-gray-700">Logging out...</p>
        <p className="text-center text-green-700">Logout process completed. Redirecting...</p>
      </div>
    </div>
  );
};

export default Logout;
