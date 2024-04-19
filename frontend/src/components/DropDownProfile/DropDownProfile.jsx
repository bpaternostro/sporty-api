import React, { useEffect, useState, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import { useGlobalContext } from '../../context/GlobalContextProvider'

import {ROOT, API_ENDPOINTS} from '../../apiConfig'
import { getCookie } from '../../helpers/CoreMethods'

import  navbarStyle from '../Navbar/navbar.module.css'
import buttonStyles from '../../style/buttons.module.css'


const DropDownProfile = () => {
    const {openProfile, setOpenProfile, setOpenNotifications, setUserData} = useGlobalContext()
    const [isAdmin, setIsAdmin] = useState(false)
    const navigate = useNavigate()
    const menuRef = useRef()
    const csrfToken = getCookie('csrftoken');

    const handleLogout = (e) => {
        fetch(API_ENDPOINTS.logout, {
            mode: 'cors',
            method: 'post',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrfToken,
              'Authorization': localStorage.getItem('auth-token-app')
            }
        })
        .then((res) => {
            localStorage.setItem('auth-token-app','')
            localStorage.setItem('name','')
            localStorage.setItem('customer_id','')
            localStorage.setItem('customer','')
            setUserData(false)
            setOpenProfile(!openProfile)
            navigate(`${ROOT}/login`)
            return
        })
        .catch( (err) => {
            console.log(err)
            return
        })
    }

    const handleGoTo = (e, to) => {
        setOpenProfile(!openProfile)
        setOpenNotifications(false)
        navigate(`${ROOT}/${to}`)
        return
    }

    useEffect(() => {
        let handler = (e) => {
            if(!menuRef.current.contains(e.target)){
                setOpenProfile(false)
            }
            
        }
        document.addEventListener('mousedown', handler);

        return() =>{
            document.removeEventListener('mousedown', handler)
        }
    }, []);

    return (
        <div ref={menuRef}>
            <ul className={`flex flex-col gap-4 ${ navbarStyle.dropDownProfile}`}>
                <li onClick={(e) => handleGoTo(e, "panel")}>Panel</li>
                <li onClick={(e) => handleGoTo(e, "profile")}>Perfil</li>
                <li onClick={(e) => handleGoTo(e, "admin")} style={{display: isAdmin ? "block": "none"}}>Admin</li>
                <li onClick={(e) => handleLogout(e)}>Logout</li>
            </ul>
        </div>
    )
}


export default DropDownProfile