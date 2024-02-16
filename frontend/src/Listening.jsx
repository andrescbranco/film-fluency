import React, { useEffect, useState } from "react";
import VideoPlayer from "./VideoPlayer";
import { useOutletContext } from "react-router-dom";

function Listening() {
    const {transcript} = useOutletContext()
    const {randomVideo} = useOutletContext()
    const [userInput, setUserInput] = useState('');
    const [showPanels, setShowPanels] = useState(false);
    const [data, setData] = useState({})

    console.log(transcript,randomVideo)



    const {languageId} = useOutletContext()


    function handleChange(e) {
        setUserInput(e.target.value);
    }

    function handleSubmit(e) {
        e.preventDefault();
        fetch(`http://localhost:5555/text_comparison/4/${languageId}`,{
            method : 'POST',
            headers : {
                'Content-Type' : 'application/json'
            },
            body : JSON.stringify({
                user_input : userInput,
                transcript: transcript
            })
        })
        .then((res)=>res.json())
        .then((data)=>{
            setData(data)
        })
        setShowPanels(true); // Show panels on submit
    }

    function handleClose() {
        setShowPanels(false); // Hide panels
        setUserInput('')
    }

    return (
        <div id='listening-container'>
            <h2>Test your listening skills!</h2>
            <h4>Type along the following clips:</h4>
            <div id="content" className={showPanels ? 'blur' : ''}>
                <VideoPlayer key={randomVideo} src={randomVideo} />
                <form onSubmit={handleSubmit}>
                    <div className="typewriter">
                        <textarea type='text' className="typewriter-input" value={userInput} onChange={handleChange} placeholder="Type what you hear..." />
                    </div>
                    <button className='start-button' type="submit">Check your answer!</button>
                </form>
            </div>
            {showPanels && (
                <div>
                    <div id="panels">
                        <h2>See what you missed!</h2>
                        <button onClick={handleClose} className="start-button" id="closeBtn-panel">Close</button>
                        <div id='panels-container'>
                            <div>
                                <h4>User Input:</h4>
                                <div className="panel">
                                    {data.differences?.map((diff, index) => {
                                        let style = {};
                                        if (diff.type === 'replace' || diff.type === 'delete' || diff.type === 'insert') {
                                        style = { backgroundColor: "red", color: "white" };
                                        }
                                        return <span key={index} style={style}>{diff.text}</span>;
                                    })}
                                </div>
                            </div>
                            <div>
                                <h4>Video Transcript:</h4>
                                <div className="panel">{transcript}</div>
                            </div>
                        </div>
                        <h4>Similarity: {Math.floor(data.similarity)}%</h4>
                    </div>
                </div>

            )}
        </div>
    );
}

export default Listening;