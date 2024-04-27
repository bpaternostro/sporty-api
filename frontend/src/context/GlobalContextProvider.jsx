import React, { useContext, createContext, useState, useEffect } from 'react'

import { useNavigate } from 'react-router-dom'

import { getCookie } from '../helpers/CoreMethods';
import { API_ENDPOINTS } from '../apiConfig';
import { routinesMock } from '../mockRoutine'

const GlobalContext = createContext()
const GlobalContextProvider = ({children}) => {
  const [loading, setLoading] = useState(false)
  const [routines, setRoutines] = useState([])
  const [customer, setCustomer] = useState(null)
  const [actualRoutine, setActualRoutine] = useState(false)
  const [openProfile, setOpenProfile] = useState(false)
  const [openNotifications, setOpenNotifications] = useState(false)
  const [showSidebar, setShowSidebar] = useState(false)
  const [routineHasChanged, setRoutineHasChanged] = useState(false)
  const [routineTypes, setRoutineTypes] = useState([])
  const [routineStatus, setRoutinestatus] = useState([])
  const [userData, setUserData] = useState(false)
  const [lists, setLists] = useState(null)
  const [currentIndex, setCurrentIndex] = useState(0);
  const csrfToken = getCookie('csrftoken');
  
  const getLists = () =>{
    fetch(API_ENDPOINTS.list, {
      mode: 'cors',
      method: 'get',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
        'Authorization': localStorage.getItem('auth-token-app')
      }
    })
    .then( res => {
      if(!res.ok){
        throw new Error('It was impossible get list values');
      }
      return res.json()
    })
    .then( data => {
      setLists(data)
    })
  }

  const getCustomerData = () =>{
    fetch(API_ENDPOINTS.customers + `/${localStorage.getItem('customer_id')}`, {
      mode: 'cors',
      method: 'get',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
        'Authorization': localStorage.getItem('auth-token-app')
      }
    })
    .then( res => {
      if(!res.ok){
        throw new Error('User has not assigned routine');
      }
      return res.json()
    })
    .then( data => {
      setCustomer(data)
      setRoutines(data.routines)
    })  
  }

  return (
        <GlobalContext.Provider value={{
            actualRoutine, setActualRoutine,
            customer, setCustomer,
            openProfile, setOpenProfile,
            openNotifications, setOpenNotifications,
            csrfToken,
            showSidebar, setShowSidebar,
            routineTypes, routineStatus,
            routines, setRoutines,
            routineHasChanged, setRoutineHasChanged,
            loading, setLoading,
            userData, setUserData,
            currentIndex, setCurrentIndex,
            lists, setLists,
            getCustomerData,
            getLists
            }}>
            {children}
        </GlobalContext.Provider>
    )
}

/*cremos un custom Hook para utilizar el contexto */
export const useGlobalContext = () => useContext(GlobalContext)

export default GlobalContextProvider