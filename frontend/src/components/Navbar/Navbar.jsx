import React, { useEffect } from 'react'

import { useNavigate, Link } from 'react-router-dom'
import { FaUserAlt } from 'react-icons/fa'
import { IoNotificationsSharp } from "react-icons/io5";
import { BsWhatsapp } from "react-icons/bs";

import { useGlobalContext } from '../../context/GlobalContextProvider'

import { DropDownProfile, DropDownNotification } from '../'
import { verifyUser } from '../../helpers/verifyToken';

import {ROOT, COMPANY_NAME, ICON_SIZE_NORMAL, API_ENDPOINTS} from '../../apiConfig'
import navbarStyle from './navbar.module.css'
import buttonStyle from '../../style/buttons.module.css'

const Navbar = () => {
    const {openProfile, setOpenProfile, openNotifications, setOpenNotifications, userData} = useGlobalContext()  
    const navigate = useNavigate()
 
    useEffect(() => {
        verifyUser(navigate)
    },[])

    return (
        <header>    
            <h1>{COMPANY_NAME}</h1>
            <nav>
                <span className={navbarStyle.navItem}>
                    {
                        localStorage.getItem("name") !== "" &&
                        <div className={navbarStyle.profileMenu}>
                            <button onClick={() => setOpenNotifications(!openNotifications)} className={buttonStyle.iconNavButton}>
                                <IoNotificationsSharp size={ICON_SIZE_NORMAL}/>
                            </button>
                        </div>
                        
                    }
                    {openNotifications && <DropDownNotification/>}
                </span>
                <span className={navbarStyle.navItem}>
                    <Link to={API_ENDPOINTS.whatsapp} id={navbarStyle.login} title="Enviar mensaje" className={buttonStyle.iconNavButton}>
                            <BsWhatsapp size={ICON_SIZE_NORMAL} />
                    </Link>
                </span>
                <span className={navbarStyle.navItem}>
                    {
                        localStorage.getItem("name") !== "" ?
                            <div className={navbarStyle.profileMenu}>
                                <span className={navbarStyle.nickName} onClick={() => setOpenProfile(!openProfile)}>
                                    <img className={navbarStyle.avatar} src="./profile.jpg" alt={`${localStorage.getItem('name')} avatar`} />
                                </span>  
                                
                            </div>
                            :
                            <Link to={`${ROOT}/identify`} id={navbarStyle.login} title="Login / Registrarse">
                                <FaUserAlt size={ICON_SIZE_NORMAL} />
                            </Link>
                    } 
                    {openProfile && <DropDownProfile/>} 
                    </span>
            </nav>
        </header>
    )
    }

export default Navbar