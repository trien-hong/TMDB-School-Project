import React, { useState, useEffect } from 'react';
import './App.css';

var deletedMovies = [];
var deletedRatings = [];
var deletedComments = [];

function App() {
  const [movie, setMovie] = useState(['']);
  const [rating, setRating] = useState(['']);
  const [comment, setComment] = useState(['']);
  const [inputRating, setInputRating] = useState('');
  const [inputComment, setInputComment] = useState('');
  // if only javascript had an equivalent of python's zip() function without import
  const combinedArray = movie.map((x, i) => [x, rating[i], comment[i]]);

  //when the save button is clicked it'll call this function
  function save(){
    // this will get all the current elements in each input and push it to an array
    var edited_rating = []
    var edited_comment = []
    var rating_elements = document.getElementsByClassName('edit_rating');
    var comment_elements = document.getElementsByClassName('edit_comment');

    for(var i = 0; i < rating_elements.length; i++) {
      edited_rating.push(rating_elements[i].value);
    }

    for(var i = 0; i < comment_elements.length; i++) {
      edited_comment.push(comment_elements[i].value);
    }
    
    // finally go to the route /save_changes with the json data
    fetch('/save_changes',{
      method: 'POST',
      body: JSON.stringify({
        deletedMovies: deletedMovies,
        deletedRatings: deletedRatings,
        deletedComments: deletedComments,
        edited_rating: edited_rating,
        edited_comment: edited_comment,
      })
    })
    .then(response => response.json())
    .catch(() => {
      alert('Data has been saved! Page will refresh when you click okay.');
      window.location.reload();
    })
  }

  useEffect(() => {
   fetch('/profile', {
     method: 'POST',
   })
   .then(response => response.json())
   .then(jsonData => {
     setMovie(jsonData[0])
     setRating(jsonData[1])
     setComment(jsonData[2])
   })
  }, []);

  // evey time the delete button is clicked it'll call this function
  // and delete the review at index
  function handleDelete(name){
    var m = movie.indexOf(name[0][0]);
    var r = rating.indexOf(name[0][1]);
    var c = comment.indexOf(name[0][2]);
    // these were needed to make sure it get's the correct index
    if(name[0][0] === movie[m] && name[0][1] === rating[m] && name[0][2] === comment[m]) {
      var index = m;
      deletedMovies.push(movie[index]);
      deletedRatings.push(rating[index]);
      deletedComments.push(comment[index]);
      setMovie([...movie.slice(0, index), ...movie.slice(index + 1)]);
      setRating([...rating.slice(0, index), ...rating.slice(index + 1)]);
      setComment([...comment.slice(0, index), ...comment.slice(index + 1)]);
    } else if(name[0][0] === movie[r] && name[0][1] === rating[r] && name[0][2] === comment[r]) {
      var index = r;
      deletedMovies.push(movie[index]);
      deletedRatings.push(rating[index]);
      deletedComments.push(comment[index]);
      setMovie([...movie.slice(0, index), ...movie.slice(index + 1)]);
      setRating([...rating.slice(0, index), ...rating.slice(index + 1)]);
      setComment([...comment.slice(0, index), ...comment.slice(index + 1)]);
    } else {
      var index = c;
      deletedMovies.push(movie[index]);
      deletedRatings.push(rating[index]);
      deletedComments.push(comment[index]);
      setMovie([...movie.slice(0, index), ...movie.slice(index + 1)]);
      setRating([...rating.slice(0, index), ...rating.slice(index + 1)]);
      setComment([...comment.slice(0, index), ...comment.slice(index + 1)]);
    }
  }

  function Value(props, i) {
    return (
      <div>
        <p>{props.name[0][0]}{" | "}<input type="number" class="edit_rating" min="1" max="10" value={inputRating} onChange={(e) => setInputRating(e.target.value[i])} placeholder={props.name[0][1]}/>{" | "}<input type="text" class="edit_comment" value={inputComment} onChange={(e) => setInputComment(e.target.value[i])} placeholder={props.name[0][2]}/>{" | "}<button onClick={() => handleDelete(props.name)}>DELETE REVIEW</button></p>
        <hr/>
      </div>
    );
  }

  return (
    <div>
      <center> 
        <h2>Here is all your reviews!</h2>
        <h3>Feel free to edit your rating or delete the review.</h3>
        <h4>Format: Movie Title | Current Rating (1-10) | Current Comment</h4>
        <h5>NOTE: If something is blank means that no data was entered in.</h5>
        <hr/>
        {combinedArray.map((dataValue, i) => <Value name={[dataValue, i]}/>)}
        <button onClick={save}>SAVE CHANGES</button>
        <br/>
        <br/>
      </center>
    </div>
  );
}

export default App;
