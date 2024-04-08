import { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import CategoryItem from './CategoryItem';
import CategoryForm from './CategoryForm';

const Categories = () => {
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        fetchCategories();
    }, []);

    const fetchCategories = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/api/v1/categories');
            const data = await response.json()
            setCategories(data);
        } catch (error) {
            console.error('Error fetching categories:', error);
        }
    }

    return (
        <div className="container mx-auto py-8 px-4">
            <Link to="/dashboard" className="text-blue-400 hover:text-blue-600">Back to Dashboard</Link>
            <div className="flex items-center mb-4 mt-4">
                <h2 className="text-2xl font-bold mr-4">Categories</h2>
            </div>
            <CategoryForm fetchCategories={fetchCategories} />
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                {categories.map(category => (
                    <CategoryItem
                        key={category.id}
                        category={category}
                        fetchCategories={fetchCategories}
                    />
                ))}
            </div>
        </div>
    )
}

export default Categories;
