import PropTypes from 'prop-types'


const CategoryItem = ({ category, fetchCategories}) => {
    const handleDelete = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/api/v1/categories/${category.id}', {
                method: 'DELETE',
            });
            if (response.ok) {
                fetchCategories();
            } else {
                console.error('Failed to delete category')
            }
        } catch (error) {
            console.error('Error deleting category:', error)
        }
    }

    return (
        <li>
            <span>{category.name}</span>
            <button onClick={handleDelete}>Delete</button>
        </li>
    )
}

CategoryItem.propTypes = {
  category: PropTypes.object.isRequired,
  fetchCategories: PropTypes.func.isRequired,
}

export default CategoryItem
