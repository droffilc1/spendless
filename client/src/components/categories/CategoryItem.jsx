import PropTypes from 'prop-types'


const CategoryItem = ({ category, fetchCategories }) => {
    const handleDelete = async (categoryId) => {
        try {
            const url = `https://cliffordmapesa.tech/api/v1/categories/${categoryId}`;
            const response = await fetch(url, {
                method: 'DELETE',
            });
            if (response.ok) {
                fetchCategories();
            } else {
                console.error('Failed to delete category');
            }
        } catch (error) {
            console.error('Error deleting category:', error);
        }
    }


    return (
        <li>
            <span className='mr-4'>{category.name}</span>
            <button className='px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600 focus:outline-none focus:bg-red-600' onClick={() => {handleDelete(category.id)}}>Delete</button>
        </li>
    )
}

CategoryItem.propTypes = {
    category: PropTypes.object.isRequired,
    fetchCategories: PropTypes.func.isRequired,
}

export default CategoryItem
