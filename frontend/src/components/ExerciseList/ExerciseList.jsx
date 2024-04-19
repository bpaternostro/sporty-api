import React, {useState} from 'react'

import {YOUTUBE_VIDEO_PARAMETERS_AUTOPLAY, YOUTUBE_VIDEO_PARAMETERS} from '../../apiConfig'

import { LiaRecycleSolid } from "react-icons/lia";
import { IoBody } from "react-icons/io5";
import { FaHashtag } from "react-icons/fa";
import { FaWeightHanging } from "react-icons/fa6";
import { MdMotionPhotosPaused } from "react-icons/md";
import { BiSolidDetail } from "react-icons/bi";

import './exercise-list.css'
const ExerciseList = ({block}) => {
  const {exercises, status, creator, id, type} = block || {}
  const [active, setActive] = useState(0);

  const handleToggle = (index) => setActive(index);
  const iconSize = 14
  const iconSizeDescription = 18
  return (
    <section className="imageAccordion">
      {block &&  exercises.map((e, index) => {
        const isActive = active === index ? "active" : "";
        return (
          <div
            key={index}
            className={`imageAccordionItem ${isActive}`}
            onClick={() => handleToggle(index)}
          > 
            <iframe className="video-content" src={`${e.exercise.video_link}${isActive ? YOUTUBE_VIDEO_PARAMETERS_AUTOPLAY: YOUTUBE_VIDEO_PARAMETERS}${e.exercise.video_link.split("/")[4]}`}></iframe>
            <div className="content">
              <div className="video-content-container">
                <span className="video-content-label-container">
                    <span>
                      <span className="video-label"><IoBody size={iconSize} color={"#FFF"} title="Ejercicio"/></span>
                      <span className="video-label-value">{e.exercise.name}</span>    
                    </span>
                </span>
                <span className="video-content-label-container">
                  <span>
                      <span className="video-label"><FaHashtag size={iconSize} color={"#FFF"} title="Series"/></span>
                      <span className="video-label-value">{e.serie}</span>    
                  </span>
                  <span>
                      <span className="video-label"><LiaRecycleSolid size={iconSize} color={"#FFF"} title="Repeticiones"/></span>
                      <span className="video-label-value">{e.reps}</span>    
                  </span>
                  <span>
                      <span className="video-label"><FaWeightHanging size={iconSize} color={"#FFF"} title="Peso"/></span>
                      <span className="video-label-value">{e.weight}</span>    
                  </span>
                  <span>
                      <span className="video-label"><MdMotionPhotosPaused size={iconSize} color={"#FFF"} title="Pausa"/></span>
                      <span className="video-label-value">{e.pause}</span>    
                  </span>
                </span>
                {
                  isActive &&
                  <span className="video-content-label-container">
                    <span>
                      <span className="video-label"><BiSolidDetail size={iconSize} color={"#FFF"} title="Observaciones"/></span>
                      <span className="video-label-value">{e.observation}</span>   
                    </span>  
                  </span>  
                }
                
              </div>
            </div>
          </div>
        );
      })}
    </section>
  )
}

export default ExerciseList