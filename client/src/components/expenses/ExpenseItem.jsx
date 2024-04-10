import PropTypes from 'prop-types'

const ExpenseItem = ({ expense }) => {
  return (
    <li>
      <div>Description: {expense.description}</div>
      <div>Amount: {expense.amount}</div>
    </li>
  );
};

ExpenseItem.propTypes = {
    expense: PropTypes.object.isRequired
}

export default ExpenseItem;
