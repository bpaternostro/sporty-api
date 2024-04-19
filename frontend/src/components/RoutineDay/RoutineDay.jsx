import React, {useState} from 'react'

import { useNavigate } from 'react-router-dom'

import { Step, Slider, SliderContent } from '../../components'


import { useGlobalContext } from '../../context/GlobalContextProvider'

import {ROOT} from '../../apiConfig'

import style from './routine-day.module.css'


const RoutineDay = ({ d }) => {
  const {currentIndex, setCurrentIndex} = useGlobalContext()
  const { day, blocks } = d || {}
  const navigate = useNavigate()

  const _handleIndexChange = (index) => {
    setCurrentIndex(index);
  };

  const _handleNext = (currentIndex) => {
    setCurrentIndex(currentIndex + 1);
  };

  const _handleComplete = () => {
    navigate(`${ROOT}/survey`)
    return
  };
  
  return (
    <div className={style.routineDayContainer}>
        <div>
          <div className="first-step-container">
            <Step onChange={setCurrentIndex} currentIndex={currentIndex} steps={blocks} />
          </div>
          <Slider onChange={_handleIndexChange} currentIndex={currentIndex} steps={blocks}/>
          <div className="second-step-container">
            <Step onChange={setCurrentIndex} currentIndex={currentIndex} steps={blocks} />
          </div>
          <SliderContent
            currentIndex={currentIndex}
            handleNext={_handleNext}
            handleComplete={_handleComplete}
            steps={blocks}
          />
        </div>
    </div>
  )
}

export default RoutineDay