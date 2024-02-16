import React from "react"
import { NavLink } from "react-router-dom"
import { BiSolidCameraMovie } from "react-icons/bi";
import { FaLanguage } from "react-icons/fa";
import { MdLocalMovies } from "react-icons/md";
import { IoIosArrowBack } from "react-icons/io";
import { MdOutlineLocalMovies } from "react-icons/md";
import { TbLanguage } from "react-icons/tb";
import { MdLanguage } from "react-icons/md";

function Header(){
    return (
       <div>
            <div id='header'>
                <div id='select-language-container'>
                <NavLink to='/select-language'>
                    <p><IoIosArrowBack style={{color:'white'}}/><TbLanguage style={{fontSize:'48', color:"white"}}/></p>
                </NavLink>
                </div>
                <div id='logo-container'>
                    <NavLink to ='/home'>
                        <div id='logo'>     
                            <p id='logo-font'>Film(Fluency)</p>
                        </div>
                    </NavLink>
                </div>
                <div id='user-bubble-container'>
                <NavLink to = '/user'>
                    <img id='user-bubble' src='https://is.zobj.net/image-server/v1/images?r=9LGcNX6GsvQA9cJgREwSu7vzuH-w7a4Bwqq7yLXBF_bj0FIyH-9w-CIMaA5OuJs_68Vgf2oBXPfoSj0SaY-SfzdjMgItAT1Bl7h40H_C5ZWVkEfSEu54T2BcWf4tK1mDjM_lobad9YHDI4EFpjGb3tuu6e3qWu2KF9GzfVOnkT_TsRd5tywnAxrNRgpStA3uxNhPsIgNTUNvXNe_QbW4_I--InaTJW393ESV4NDdRW_RWfz8r8uCMB6aijg'></img>
                </NavLink>
                </div>
            </div>
       </div> 
    )
}

export default Header

