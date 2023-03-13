// SearchForm.js

import React, { useState } from 'react';
import './styles.css';

function SearchForm(props) {
  const [query, setQuery] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    props.onSearch(query);
  };

  const handleQueryChange = (event) => {
    setQuery(event.target.value);
  };

  return (
    <form className="search-form" onSubmit={handleSubmit}>
      <label htmlFor="query">Search Jobs:</label>
      <input type="text" id="query" value={query} onChange={handleQueryChange} />
      <button type="submit">Search</button>
    </form>
  );
}

export default SearchForm;
