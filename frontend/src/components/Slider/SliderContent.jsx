import React, {useState} from 'react'

import { ExerciseList, FormElement } from '../../components'
import { LuChevronsDown, LuChevronsUp } from "react-icons/lu";
import { LiaRecycleSolid } from "react-icons/lia";
import { IoBody } from "react-icons/io5";
import { FaHashtag } from "react-icons/fa";
import { FaWeightHanging } from "react-icons/fa6";
import { MdMotionPhotosPaused } from "react-icons/md";
import { BiSolidDetail } from "react-icons/bi";


import buttonStyle from '../../style/buttons.module.css'
import widgetStyle from '../Widget/widget.module.css'

import './slider.css'

const SliderContent = ({ currentIndex, handleNext, handleComplete, steps }) => {
    const currentStep = steps[currentIndex]
    const [showDetail, setShowDetail] = useState(false)
    const [showDetailGlosario, setShowDetailGlosario] = useState(false)
    const {name, description} = currentStep || {}
    const iconSize = 18

    const handleShowDetail = () => {
      setShowDetail(!showDetail)
      setShowDetailGlosario(false)
    }

    const handleShowDetailGlosario = () => {
      setShowDetail(false)
      setShowDetailGlosario(!showDetailGlosario)
    }

    return (
      <div className="formContainer">
        <span className="blockDetailContainer">
          <span className="blockDetailToolbarContainer">
            <span className="blockDetailToolbarButton" onClick={() => handleShowDetail()}>  
              <span>
                {
                  showDetail ? 
                    <LuChevronsUp size={iconSize} color={"#FFF"} title="Mostrar comentarios"/>
                  :
                    <LuChevronsDown  size={iconSize} color={"#FFF"} title="Ocultar comentarios"/>
                } 
                Comentarios
              </span>
            </span>
            <span className="blockDetailToolbarButton" onClick={() => handleShowDetailGlosario()}>
              <span>
                {
                  showDetailGlosario ? 
                    <LuChevronsUp size={iconSize} color={"#FFF"} title="Mostrar glosario"/>
                  :
                    <LuChevronsDown  size={iconSize} color={"#FFF"} title="Ocultar glosario"/>
                } 
                Glosario
              </span>
            </span>
          </span>
          {
          showDetail && <span className="block-detail">
              <span>
                {description}
              </span>
          </span> 
          }
          {
          showDetailGlosario && <span className="block-detail">
              <span>
                  <span className="video-label"><IoBody size={iconSize} color={"#FFF"} title="Ejercicio"/></span>
                  <span className="video-label-value">Nombre del Ejercicio</span>    
              </span>
              <span>
                  <span className="video-label"><FaHashtag size={iconSize} color={"#FFF"} title="Series"/></span>
                  <span className="video-label-value">Cantidad de series</span>    
              </span>
              <span>
                  <span className="video-label"><LiaRecycleSolid size={iconSize} color={"#FFF"} title="Repeticiones"/></span>
                  <span className="video-label-value">Cantidad de repeticiones</span>    
              </span>
              <span>
                  <span className="video-label"><FaWeightHanging size={iconSize} color={"#FFF"} title="Peso"/></span>
                  <span className="video-label-value">Peso sugerido</span>    
              </span>
              <span>
                  <span className="video-label"><MdMotionPhotosPaused size={iconSize} color={"#FFF"} title="Pausa"/></span>
                  <span className="video-label-value">Pausa sugerida</span>    
              </span>
              <span>
                  <span className="video-label"><BiSolidDetail size={iconSize} color={"#FFF"} title="Observaciones"/></span>
                  <span className="video-label-value">Observaciones del entrenador</span>    
              </span>
          </span> 
          }
        </span>
        <ExerciseList block={currentStep} />
        {currentIndex === steps.length - 1 ? (
          <FormElement
            value={"Fin de la rutina"}
            onClick={() => handleComplete(currentIndex)}
          />
        ) : (
          <FormElement value={">>>"} onClick={() => handleNext(currentIndex)} />
        )}
      </div>
);
}

export default SliderContent