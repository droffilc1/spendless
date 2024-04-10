import { useState, useEffect } from "react";
import PropTypes from 'prop-types'

const CategoryForm = ({ fetchCategories }) => {
    const [name, setName] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:5000/api/v1/categories', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name }),
            });
            if (response.ok) {
                setName('')
                fetchCategories()
            } else {
                console.error("Failed to add category")
            }
        } catch (error) {
            console.error("Error adding category:", error)
        }
    }

    return (
        <form onSubmit={handleSubmit} className="mb-8">
            <div className="flex items-center">
                <input
                    type="text"
                    placeholder="Enter category name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="mr-2 px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                    required
                />
                <button
                    type="submit"
                    className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none focus:bg-blue-600"
                >
                    Add Category
                </button>
            </div>
        </form>
    )
}

CategoryForm.propTypes = {
    fetchCategories: PropTypes.func.isRequired,
}

export default CategoryForm
