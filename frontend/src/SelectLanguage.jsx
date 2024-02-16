import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function SelectLanguage () {

    
    const navigate = useNavigate()
    
    function handleLanguageClick(e) {

        const user_id = 4

        fetch('http://localhost:5555/select-languages', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: user_id, language_id: e.target.value }),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.message); // "User progress initialized" or "User already has progress in this language"
        })
        navigate('/home',{state:{language_id:e.target.value, user_id:user_id}})
    }


    return(
        <div>
            <h1>Welcome to FilmFluency!</h1>
            <h4>Pick a language to start learning right away:</h4>
            <div id='start-buttons-container'>
                <button className="start-button" onClick={handleLanguageClick} value="2">Spanish</button>
                <button className="start-button" onClick={handleLanguageClick} value="1">Portuguese</button>
                <button className="start-button" onClick={handleLanguageClick} value='4'>Japanese</button>
                <button className="start-button" onClick={handleLanguageClick} value='3'>French</button>
            </div>
        </div>
    )
}

export default SelectLanguage