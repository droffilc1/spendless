import { Link } from 'react-router-dom';
import DashboardOverview from './DashboardOverview';

const Dashboard = () => {
  return (
    <div className='min-h-screen flex relative'>
      {/* Sidebar */}
      <div className='bg-gray-800 w-64 flex-shrink-0'>
        <div className='p-4'>
          <h1 className='text-3xl font-bold text-yellow-400'>Spendless</h1>
          <ul className='mt-8'>
            <li className='mb-4'>
              <Link to="/categories" className='text-gray-300 hover:text-white'>Categories</Link>
            </li>
            <li className='mb-4'>
              <Link to="/expenses" className='text-gray-300 hover:text-white'>Expenses</Link>
            </li>
            <li className='mb-4'>
              <Link to="/analytics" className='text-gray-300 hover:text-white'>Analytics</Link>
            </li>
            <li className='absolute bottom-0 p-8'>
              <Link to="/logout" className='text-gray-300 hover:text-white'>Logout</Link>
            </li>
          </ul>
        </div>
      </div>
      {/* Main content */}
      <div className="flex-1">
        <div className="container mx-auto py-8 px-4">
          <DashboardOverview />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
