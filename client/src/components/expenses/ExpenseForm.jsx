import { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

const ExpenseForm = ({ fetchExpenses, userId }) => {
  const [description, setDescription] = useState('');
  const [amount, setAmount] = useState('');
  const [category, setCategory] = useState('');
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    fetchCategories();
  }, []);

  const fetchCategories = async () => {
    try {
      const response = await fetch('https://spendless.ink/api/v1/categories');
      if (!response.ok) {
        throw new Error('Failed to fetch categories');
      }
      const data = await response.json();
      setCategories(data);
    } catch (error) {
      console.error('Error fetching categories:', error.message);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('https://spendless.ink/api/v1/expenses', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          // Add authorization header if needed
        },
        body: JSON.stringify({
          amount: parseFloat(amount),
          description,
          category_id: category,
          user_id: userId
        }),
      });
      if (!response.ok) {
        throw new Error('Failed to add expense');
      }
      setDescription('');
      setAmount('');
      setCategory('');
      fetchExpenses(); // Fetch expenses again to update the list
    } catch (error) {
      console.error('Error adding expense:', error.message);
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-4">
      <h3 className="text-lg font-semibold mb-2">Add Expense</h3>
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label htmlFor="description" className="block font-medium">Description:</label>
          <input
            type="text"
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="mt-1 p-2 border rounded-lg w-full"
            required
          />
        </div>
        <div className="mb-4">
          <label htmlFor="amount" className="block font-medium">Amount:</label>
          <input
            type="number"
            id="amount"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            className="mt-1 p-2 border rounded-lg w-full"
            required
          />
        </div>
        <div className="mb-4">
          <label htmlFor="category" className="block font-medium">Category:</label>
          <select
            id="category"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            className="mt-1 p-2 border rounded-lg w-full"
            required
          >
            <option value="">Select category</option>
            {categories.map(cat => (
              <option key={cat.id} value={cat.id}>{cat.name}</option> // Display category name
            ))}
          </select>
        </div>
        <button type="submit" className="bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition duration-300">Add Expense</button>
      </form>
    </div>
  );
};

ExpenseForm.propTypes = {
  fetchExpenses: PropTypes.func.isRequired,
  userId: PropTypes.string.isRequired
};

export default ExpenseForm;
