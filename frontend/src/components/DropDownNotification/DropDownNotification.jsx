import React, { useEffect, useState, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import { useGlobalContext } from '../../context/GlobalContextProvider'

import {ROOT, API_ENDPOINTS} from '../../apiConfig'
import { getCookie } from '../../helpers/CoreMethods'

import  navbarStyle from '../Navbar/navbar.module.css'
import buttonStyles from '../../style/buttons.module.css'


const DropDownNotification = () => {
    const {openProfile, setOpenProfile, openNotifications, setOpenNotifications, setUserData} = useGlobalContext()
    const [isAdmin, setIsAdmin] = useState(false)
    const navigate = useNavigate()
    const menuRef = useRef()
    const csrfToken = getCookie('csrftoken');


    const handleGoTo = (e, to) => {
        setOpenNotifications(!openNotifications)
        setOpenProfile(false)
        navigate(`${ROOT}/${to}`)
        return
    }

    useEffect(() => {
        let handler = (e) => {
            if(!menuRef.current.contains(e.target)){
                setOpenNotifications(false)
            }
            
        }
        document.addEventListener('mousedown', handler);

        return() =>{
            document.removeEventListener('mousedown', handler)
        }
    }, []);

    return (
        <div ref={menuRef}>
            <ul className={`flex flex-col gap-4 ${ navbarStyle.dropDownNotification}`}>
                
            </ul>
        </div>
    )
}


export default DropDownNotification