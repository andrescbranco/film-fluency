import React, { useState } from "react";
import { useOutletContext } from "react-router-dom";
import VideoPlayer from "./VideoPlayer";


function Vocabulary () {
    const [featuredWords, setFeaturedWords] = useState([])
    const [backside, showBackside] = useState(false)
    const [startVocab, setStartVocab] = useState(false)
    const [featuredWord, setFeaturedWord] = useState('')

    const {languageId} = useOutletContext()

function handleClick(){
    showBackside(!backside)
}

function handleStart(e){
    // Make sure to whenever click in vocab bring state of language id with nav
    fetch(`http://localhost:5555/user/4/language/${languageId}/get_learn_review/${e.target.value}`)
    .then((res)=>res.json())
    .then((data)=>{
        setFeaturedWords(data)
        setFeaturedWord(data[Math.floor(Math.random() * Math.floor(data.length))])
    }) 
    setStartVocab(!startVocab)
}

function handleRandomizer(e) {
    showBackside(false);
    
    fetch(`http://localhost:5555/patch_user_word/${featuredWord.id}/4/${languageId}/${e.target.value}`,{
        method : 'PATCH',
        headers : {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({message: 'patch'})
        })
        .then((res)=>res.json())
        .then((data)=>{
            console.log(data)
        })

    setFeaturedWord(featuredWords[Math.floor(Math.random() * Math.floor(featuredWords.length))]);

}



function handleGoBack(){
    setStartVocab(!startVocab)
    showBackside(false)
}


return (
    <div>
        {!startVocab ?
        (
        <div id='select-vocab'>
            <button className='vocab-button' value='0' name= 'learn' onClick={handleStart}>Learn</button>
            <button className='vocab-button' value='1' name = 'review' onClick={handleStart}>Review</button>
        </div>
        )
        : (
            <div id='learn-vocab'>
            <h2>Test your vocabulary!</h2>
            <button id='go-back-button'className='start-button' onClick={handleGoBack}>Go Back</button>
            <div id='vocab'>
                <div onClick={handleClick} className='card' id='speech-bubble'>
                    <div className="card-content">
                    {!backside ? (
                        <div className="word">
                            <p>{featuredWord?.word}</p>
                            <p>{featuredWord?.context}</p>
                        </div>
                    )
                    :
                    (
                        <>
                            <div className="word">
                                <p>{featuredWord?.word}</p>
                                <span className="part-of-speech">{featuredWord?.part_of_speech}</span>
                            </div> 
                            <div className="definition">
                                {featuredWord?.definition}
                            </div>
                            <div className="english">
                                {featuredWord?.english_context}
                            </div>
                        </>
                    )}
                    </div>
                </div>
                <div>
                    <VideoPlayer id='vocab-player' src={''}/>
                </div>
            </div>
            <div className="button-container">
                <h4 id='feedback'>Feedback:</h4>
                <button onClick={handleRandomizer} value='0'className="start-button">Very Easy</button>
                <button onClick={handleRandomizer} value='1' className="start-button">Easy</button>
                <button onClick={handleRandomizer} value='2' className="start-button">Good</button>
                <button onClick={handleRandomizer} value='3' className="start-button">Hard</button>
                <button onClick={handleRandomizer} value='4' className="start-button">Very Hard</button>
                <button onClick={handleRandomizer} value='5' className="start-button">Don't Know</button>
            </div>
            </div>
    )}
    </div>

);
}

export default Vocabulary