import React, { useState, useEffect } from 'react'

import { useNavigate } from 'react-router-dom'

import { Dashboard, Modal} from '../components'

import { API_ENDPOINTS, ROOT } from '../apiConfig'
import { useGlobalContext } from '../context/GlobalContextProvider';
import { useModalContext } from '../context/ModalContextProvider';

import { verifyUser } from '../helpers/verifyToken';

const Home = () => {
  const {routines, getCustomerData, customer, getLists} = useGlobalContext()
  const navigate = useNavigate()

  useEffect(() => {
    verifyUser(navigate)
    if(!customer){
      getCustomerData()
    }
    
  },[])
  
  return (
    <main>
      <div>
        { routines ? <Dashboard></Dashboard> : <span>El usuario no tiene ninguna rutina asignada</span>}
      </div>
      <Modal></Modal>
    </main>
  )
}

export default Home