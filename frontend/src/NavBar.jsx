import { NavLink, useOutletContext } from "react-router-dom"
import { GrAssistListening } from "react-icons/gr";
import { TbVocabulary } from "react-icons/tb";
import { TbBrandGrammarly } from "react-icons/tb";

function NavBar ({handleGetContent, handleGetRandomVideo}) {

    return(
        <div id='nav-features'>
            <NavLink to ='/vocabulary' onClick={handleGetContent}>
            <TbVocabulary className='nav-icon'/>
            </NavLink>
            <NavLink to ='/grammar' >
            <TbBrandGrammarly className='nav-icon'/>
            </NavLink>
            <NavLink to ='/listening'  onClick={handleGetRandomVideo}>
            <GrAssistListening className='nav-icon' />
            </NavLink>
        </div>
    )
}

export default NavBar