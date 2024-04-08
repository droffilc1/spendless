import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Chart from 'chart.js/auto';

const Analytics = () => {
  const [analyticsData, setAnalyticsData] = useState(null);

  useEffect(() => {
    fetchAnalyticsData();
  }, []);

  const fetchAnalyticsData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/v1/analytics', {
        // Add any headers or authorization if needed
      });
      if (!response.ok) {
        throw new Error('Failed to fetch analytics data');
      }
      const data = await response.json();
      setAnalyticsData(data);
    } catch (error) {
      console.error('Error fetching analytics data:', error.message);
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchAnalyticsData();
      setAnalyticsData(data);
    };
    fetchData();
  }, []);

  useEffect(() => {
    const renderCharts = () => {
      const ctx = document.getElementById('expenseChart');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: Object.keys(analyticsData.expense_category),
          datasets: [{
            label: 'Total Expenses by Category',
            data: Object.values(analyticsData.expense_category),
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    };

    if (analyticsData) {
      renderCharts();
    }
  }, [analyticsData]);

  return (
    <div className="p-8">
      <Link to="/dashboard" className="text-blue-400 hover:text-blue-600 mb-4">Back to Dashboard</Link>
      <h2 className="text-2xl font-bold mb-4 text-white">Analytics</h2>
      <div className="bg-white rounded-lg shadow-md p-4">
        <canvas id="expenseChart" width="400" height="400"></canvas>
      </div>
    </div>
  );
};

export default Analytics;
