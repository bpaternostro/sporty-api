import React, { useState, useEffect } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { useParams } from 'react-router-dom'

import { Modal, Player} from '../components'

import { ROOT, ICON_SIZE_BIG } from '../apiConfig'
import { useGlobalContext } from '../context/GlobalContextProvider';
import { useModalContext } from '../context/ModalContextProvider';
import { IoChevronBackCircle } from "react-icons/io5";

import style from '../style/routine-player.module.css'
import axios from 'axios'

const RoutinePlayer = () => {
  const routineId = useParams()
  const {actualRoutine} = useGlobalContext()
  const {toggleModal, toStatus} = useModalContext()
  
  return (
    <main>
      <div className={style.routinePlayerBack}>
        <Link to={`${ROOT}/panel`} title="Volver al panel"><IoChevronBackCircle size={ICON_SIZE_BIG} /></Link>
      </div>
      <div className={style.routinePlayerContainer}>
        {actualRoutine && 
            <div>
              <Player routine={actualRoutine}></Player>
            </div>
        }
      </div>
      <Modal></Modal>
       
    </main>
    
  )
}

export default RoutinePlayer