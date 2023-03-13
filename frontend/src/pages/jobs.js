
import React from 'react';
import '../styles.css';

function JobList(props) {
  const { jobs } = props;

  return (
    <ul className="job-list">
      {jobs.map((job) => (
        <li key={job.id}>
          <h2>{job.title}</h2>
          <p>{job.description}</p>
          <button className='joblist-button' type="submit"><a href={job.url}>Check out</a></button>
        </li>
      ))}
    </ul>
  );
}

export default JobList;
