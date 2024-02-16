import React, { useState } from "react";
import VideoPlayer from "./VideoPlayer";
import { useLocation, useOutletContext } from "react-router-dom";
import ReactCountryFlag from "react-country-flag"

function Home () {
    const path = "../assets/Braveheart_ William Wallace Freedom Speech [Full HD].mp4"

    const location = useLocation()
    const {setLanguageId} = useOutletContext()
    const language_id = location.state?.language_id
    const user_id = location.state?.user_id
    console.log(language_id,user_id)
    setLanguageId(language_id)


    return(
        <div id='home-container'>
            Stats:
            <div className="loading-container">
                <ReactCountryFlag countryCode="ES" className="flag" svg />Lvl.{4}
                <div className="range" style={{"--p":"98"}}></div>
                
            </div>
            <div className="loading-container">
                <ReactCountryFlag countryCode="BR" className="flag" svg /> Lvl.{5}
                <div className="range" style={{"--p":"40"}}></div>
            </div>
            <div className="loading-container">
                <ReactCountryFlag countryCode="FR" className="flag" svg /> Lvl.{2}
                <div className="range" style={{"--p":"30"}}></div>
            </div>
            <div className="loading-container">
                <ReactCountryFlag countryCode="JP" className="flag" svg /> Lvl.{1}
                <div className="range" style={{"--p":"70"}}></div>
            </div>
        </div>
    )
}

export default Home