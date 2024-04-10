import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import ExpenseForm from './ExpenseForm'
import ExpenseItem from './ExpenseItem'


const Expenses = () => {
    const [expenses, setExpenses] = useState([]);

    const fetchExpenses = async () => {
        try {
            const response = await fetch('http:127.0.0.1:5000/api/v1/expenses', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                    // Auth header
                }
            })
            if (!response.ok) {
                throw new Error('Failed to fetch expenses')
            }
            const data = await response.json()
            console.log('Fetched expenses:', data);
            setExpenses(data)
        } catch (error) {
            console.error('Error fetching expenses:', error.message)
        }
    }

    useEffect(() => {
        fetchExpenses()
    }, [])

    return (
        <div className="container mx-auto py-8 px-4">
            <Link to="/dashboard" className="text-blue-400 hover:text-blue-600">Back to Dashboard</Link>
            <div className="flex items-center mb-4 mt-4">
                <h2 className="text-2xl font-bold mr-4">Expenses</h2>
            </div>
            <ExpenseForm fetchExpenses={fetchExpenses} />
            <div className="mt-12 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                {expenses.map((expense) => (
                    <ExpenseItem
                    key={expense.id}
                    expense={expense}
                    fetchExpenses={fetchExpenses} />
                ))}
            </div>
        </div>
    )
}

export default Expenses
