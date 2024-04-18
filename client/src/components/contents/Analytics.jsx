import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Chart from 'chart.js/auto';

const Analytics = () => {
  const [analyticsData, setAnalyticsData] = useState(null);
  const [chartInstance, setChartInstance] = useState(null);

  useEffect(() => {
    fetchAnalyticsData();
  }, []);

  const fetchAnalyticsData = async () => {
    try {
      const response = await fetch('https://cliffordmapesa.tech/api/v1/analytics');
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
    const renderChart = () => {
      if (chartInstance) {
        chartInstance.destroy(); // Destroy the existing chart instance
      }
      const ctx = document.getElementById('expenseChart');
      const newChartInstance = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: Object.keys(analyticsData.expense_category),
          datasets: [{
            label: 'Total Expenses by Category',
            data: Object.values(analyticsData.expense_category),
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
          }]
        },
        options: {
          plugins: {
            tooltip: {
              callbacks: {
                label: (context) => {
                  const label = context.label || '';
                  const value = context.parsed || 0;
                  return `${label}: $${value.toFixed(2)}`;
                }
              }
            }
          },
          layout: {
            padding: {
              top: 10,
              bottom: 10,
              left: 10,
              right: 10
            }
          },
          elements: {
            arc: {
              borderWidth: 0
            }
          },
          radius: '70%'
        }
      });
      setChartInstance(newChartInstance);
    };

    if (analyticsData) {
      renderChart();
    }
  }, [analyticsData]);


  return (
    <div className="h-screen p-8">
      <Link to="/dashboard" className="text-blue-400 hover:text-blue-600 mb-4">Back to Dashboard</Link>
      <h2 className="text-2xl font-bold mb-4 text-white">Analytics</h2>
      <div className="max-w-2xl mx-auto bg-white rounded-lg shadow-md p-4"> {/* Set maximum width and center */}
        <canvas id="expenseChart" width="200" height="200"></canvas>
        {analyticsData && (
          <div>
            <p>Total Expenses: ${analyticsData.total_expenses}</p>
            <ul>
              {Object.entries(analyticsData.expense_category).map(([category, amount]) => (
                <li key={category}>{category}: ${amount}</li>
              ))}
            </ul>
          </div>
        )}
      </div>

    </div>
  );
};

export default Analytics;
