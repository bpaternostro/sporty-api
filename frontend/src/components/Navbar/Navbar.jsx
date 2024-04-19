import React from 'react'
import { Link } from 'react-router-dom'
import { FaUserAlt } from 'react-icons/fa'
import { IoNotificationsSharp } from "react-icons/io5";
import { BsWhatsapp } from "react-icons/bs";

import { useGlobalContext } from '../../context/GlobalContextProvider'
import { useModalContext } from '../../context/ModalContextProvider'

import { DropDownProfile, DropDownNotification } from '../'

import {ROOT, COMPANY_NAME, ICON_SIZE_NORMAL, API_ENDPOINTS} from '../../apiConfig'
import navbarStyle from './navbar.module.css'
import buttonStyle from '../../style/buttons.module.css'

const Navbar = () => {
    const {openProfile, setOpenProfile, openNotifications, setOpenNotifications, userData} = useGlobalContext()  
    const {setModalTitle, setModalText, toggleModal, setIsCreatePortfolioModal, setIsConfirmationModal, setIsEditModal, setIsIndicatorsModal, setIsEditPortfolioModal} = useModalContext()
    
    const handlePopUp = () => {
        setModalTitle("Create a new portfolio")
        setModalText(`Insert all the information`)
        setIsConfirmationModal(false)
        setIsEditModal(false)
        setIsIndicatorsModal(false)
        setIsCreatePortfolioModal(true)
        setIsEditPortfolioModal(false)
        toggleModal(true)
    }

    const handlePopUpEditPortfolio = () => {
        setModalTitle("Edit portfolio")
        setModalText(`Edit all the information`)
        setIsConfirmationModal(false)
        setIsEditModal(false)
        setIsIndicatorsModal(false)
        setIsCreatePortfolioModal(false)
        setIsEditPortfolioModal(true)
        toggleModal(true)
    }

    return (
        <header>    
            <h1>{COMPANY_NAME}</h1>
            <nav>
                <span className={navbarStyle.navItem}>
                    {
                        localStorage.getItem('name') !== "" &&
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
                        localStorage.getItem('name') !== "" ?
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