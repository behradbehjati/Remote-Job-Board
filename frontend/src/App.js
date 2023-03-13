import React, { useState, useEffect } from 'react';
import SearchForm from './search';
import JobList from './pages/jobs';

function App() {
  const [jobs, setJobs] = useState([]);
  const [nextPage, setNextPage] = useState([]);
  const [previousPage, setPreviousPage] = useState([]);
  const [query, setQuery] = useState('react');

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`http://127.0.0.1:8000/jobs/?field=${query}`);
      const data = await response.json();
      setJobs(data.results);
      setNextPage(data.next)
      setPreviousPage(data.previous)
    };
    fetchData();
  }, [query]);

  const handleSearch = (newQuery) => {
    setQuery(newQuery);
  };
   const loadNextPage = async () => {
    if (nextPage) {
      const response = await fetch(nextPage);
      const data = await response.json();
      setJobs(data.results);
      setNextPage(data.next);
      setPreviousPage(data.previous);
    }
  };

  const loadPreviousPage = async () => {
    if (previousPage) {
      const response = await fetch(previousPage);
      const data = await response.json();
      setJobs(data.results);
      setNextPage(data.next);
      setPreviousPage(data.previous);
    }
  };

  return (
    <div>
      <h1>Job List</h1>
      <SearchForm onSearch={handleSearch} />
      <JobList jobs={jobs} />

      <button onClick={loadPreviousPage} disabled={!previousPage}>Previous Page</button>
      <button onClick={loadNextPage} disabled={!nextPage}>Next Page</button>




    </div>
  );
}

export default App;
