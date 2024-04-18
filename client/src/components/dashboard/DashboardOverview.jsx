import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const DashboardOverview = () => {
  const [summaryData, setSummaryData] = useState(null);
  const [username, setUsername] = useState(null);


  // Fetch summary data from the server
  useEffect(() => {
    const fetchSummaryData = async () => {
      try {
        // Fetch summary data from the backend API
        const response = await fetch('https://cliffordmapesa.tech/api/v1/analytics');
        if (!response.ok) {
          throw new Error('Failed to fetch dashboard overview data');
        }
        const data = await response.json();
        setSummaryData(data);
      } catch (error) {
        console.error('Error fetching dashboard overview data:', error.message);
      }
    };

    fetchSummaryData();
  }, []);

  useEffect(() => {
    async function fetchUsername() {
      try {
        if (username) {
          const response = await fetch(`https://cliffordmapesa.tech/api/users/${username}`);
          if (response.ok) {
            const data = await response.json();
            setUsername(data.username);
          } else {
            console.error("Failed to fetch username:", response.statusText);
          }
        }
      } catch (error) {
        console.error("Error fetching username:", error.message);
      }
    }

    fetchUsername();
  }, [username]);

  return (
    <div className="container mx-auto py-8 px-4">
      <h2 className="text-2xl font-bold mb-4">Dashboard Overview</h2>
      {username && <h3 className='text-white'>Hello, {username}</h3>}
      {/* Display summary information */}
      {summaryData && (
        <div className="grid grid-cols-3 gap-4">
          {/* Categories summary */}
          <div className="p-4 rounded-lg text-center">
            <h3 className="text-lg font-bold mb-2">Categories</h3>
            <p className="text-3xl font-bold">{summaryData.categoriesCount}</p>
            <Link to="/categories" className="text-blue-400 hover:text-blue-600 mt-2 block">View Categories</Link>
          </div>
          {/* Expenses summary */}
          <div className="p-4 rounded-lg text-center">
            <h3 className="text-lg font-bold mb-2">Expenses</h3>
            <p className="text-3xl font-bold">{summaryData.expensesTotal}</p>
            <Link to="/expenses" className="text-blue-400 hover:text-blue-600 mt-2 block">View Expenses</Link>
          </div>
          {/* Analytics summary */}
          <div className="p-4 rounded-lg text-center">
            <h3 className="text-lg font-bold mb-2">Analytics</h3>
            {/* Display any relevant analytics summary */}
            {/* Example: Total expenses */}
            <p className="text-3xl font-bold">{summaryData.totalExpenses}</p>
            <Link to="/analytics" className="text-blue-400 hover:text-blue-600 mt-2 block">View Analytics</Link>
          </div>
        </div>
      )}
    </div>
  );
};

export default DashboardOverview;
