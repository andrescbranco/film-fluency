import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Header from './Header'
import { Outlet } from 'react-router-dom'
import NavBar from './NavBar'

function App() {

  const [languageId, setLanguageId] = useState()
  const [randomVideo, setRandomVideo] = useState('')
  const [transcript, setTranscript] = useState('')
  

  useEffect(()=>{
    fetch('http://localhost:5555/user/2')
    .then((res)=>res.json())
    .then(data=>{
      console.log(data)
    })
  },[])

  function handleGetContent(){
    console.log('vocab')
    fetch(`http://localhost:5555/get_content/4/${languageId}`)
    .then((res)=>res.json())
    .then((data)=>{
    console.log(data)
}) 
}

  function handleGetRandomVideo(){
    console.log('listening')
    fetch(`http://localhost:5555/listening_randomizer/${languageId}`)
    .then((res)=>res.json())
    .then((data)=>{
        setTranscript(data.transcript)
        setRandomVideo(data.video_url)
    })
 }

  return (
    <div>
      <Header/>
      <div className="video-background">
        <img url='./assets/background test 2.jpg'/>

      </div>
      <nav id='movie-reel'></nav>
      <nav id='division'></nav>
      <NavBar id='nav-bar'handleGetContent={handleGetContent} handleGetRandomVideo={handleGetRandomVideo}/>
      <div id='outlet-container'>
      <Outlet context={{languageId, setLanguageId, transcript, randomVideo}}/>
      </div>
    </div>
  );

  }
export default App
