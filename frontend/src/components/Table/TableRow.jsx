import React, {useEffect, useState} from 'react'
import { Link } from 'react-router-dom'
import moment from 'moment';

import styles from './table.module.css'
import indexStyles from '../../style/index.module.css'
import buttonStyle from '../../style/buttons.module.css'

import { GiFinishLine } from "react-icons/gi";
import { GrStatusCriticalSmall } from "react-icons/gr";
import { AiFillStop } from "react-icons/ai";
import { FaCalendarAlt, FaPauseCircle } from "react-icons/fa";
import { VscSymbolMethod, VscDebugStart} from "react-icons/vsc";
import { TfiTarget } from "react-icons/tfi";
import { MdDownloading, MdMonitorHeart, MdOutlineTireRepair, MdOutlineSettingsSystemDaydream, MdOutlineStart } from "react-icons/md";
import { RiRhythmLine } from "react-icons/ri";
import { GiStopwatch } from "react-icons/gi";
import { FaRegPlayCircle } from "react-icons/fa";
import { SiLevelsdotfyi } from "react-icons/si";
import { BiExpandVertical, BiCollapseVertical } from "react-icons/bi";

import {API_ENDPOINTS, ROOT, ICON_SIZE_BIG, ICON_SIZE_NORMAL, ROUTINE_STATUS_OK} from '../../apiConfig'
import { useGlobalContext } from '../../context/GlobalContextProvider';
import { useModalContext } from '../../context/ModalContextProvider'

import axios from 'axios'

const TableRow = ({routineData}) => {
    const {info, days, status_routine, observation, start_date, due_date} = routineData
    const {
        id,  
        table,
        status,
        name,
        description,
        cardio,
        duration,
        pre_exhaustion,
        activation,
        rest_between_exercises,
        routine_type,
        system,
        cadence,
        training_method,
        restrictions,
        days_of_week,
        routine_metadata,
        creator
       } = info || {}
    
    const [showWidgetContainer, setWidgetContainer] = useState(false)
    const {customer, routines, setActualRoutine, setCurrentIndex} = useGlobalContext();
    const {setModalTitle, 
          setModalText, 
          toggleModal} = useModalContext()
    const [selected, setSelected] = useState(false)

    const handlePopUpIndicators = (e) => {
      e.preventDefault()
      setModalTitle("table indicators")
      setModalText(`Show table indicators`)
      setActualtable(tableData)
      toggleModal()
    }

    const handleRoutineRowClick = () => {
      const currentTime = new Date();
      localStorage.setItem("routine_start_time", moment(currentTime).format('YYYY-MM-DD HH:MM:ss'))
      setCurrentIndex(0)
      setActualRoutine(routines.find((r) => r.id == id))
    }

    const handleShowHide = ((e) => {
      e.preventDefault()
      setWidgetContainer(!showWidgetContainer)
    })

    const globalStatus = 1
    const metadatas = routine_metadata[0]
    const DISABLED_COLOR = "#101820"
    const ENABLED_COLOR = "#FFF"
    const STATUS_OK_COLOR = "#3ED17A"
    const STATUS_NOT_OK_COLOR = "#C70039"
    return (
        <div className={styles.tableRow}>
              <div className={styles.toolbarContainer}>
                <span>
                  {
                    status_routine === ROUTINE_STATUS_OK 
                    &&
                    <Link to={`${ROOT}/panel/routine/${id}`} className={styles.tableRowLink} onClick={(e) => handleRoutineRowClick(e)}>
                      <FaRegPlayCircle size={ICON_SIZE_BIG} color={"#FFF"} title="Play routine"/>
                    </Link>
                  }
                </span>
                <span className={styles.toolbar}>
                    <span className={styles.routineBullet} style={{background: status_routine === ROUTINE_STATUS_OK ? ENABLED_COLOR: DISABLED_COLOR}}></span>
                    <span>
                      {globalStatus ? <GrStatusCriticalSmall size={ICON_SIZE_NORMAL} color={status_routine === ROUTINE_STATUS_OK ? STATUS_OK_COLOR: STATUS_NOT_OK_COLOR}/>:<GrStatusCriticalSmall size={20} color={DISABLED_COLOR}/>} 
                    </span>
                    <span>
                      <button disabled={status_routine !== ROUTINE_STATUS_OK} className={buttonStyle.iconButton} onClick={(e) =>   handlePopUpIndicators(e)}><MdDownloading size={ICON_SIZE_NORMAL} color={status_routine === ROUTINE_STATUS_OK ? ENABLED_COLOR: DISABLED_COLOR} title="Descargar routine"/></button>
                    </span>
                    <span>
                      <button disabled={status_routine !== ROUTINE_STATUS_OK} className={buttonStyle.iconButton} onClick={(e) => handleShowHide(e)}>{showWidgetContainer ? <BiCollapseVertical size={ICON_SIZE_NORMAL} color={status_routine === ROUTINE_STATUS_OK ? ENABLED_COLOR: DISABLED_COLOR} title="Expandir"/>: <BiExpandVertical size={ICON_SIZE_NORMAL} color={status_routine === ROUTINE_STATUS_OK ? ENABLED_COLOR: DISABLED_COLOR} title="Colapsar"/>}</button>
                    </span>
                  </span>
              </div>
              <div className={styles.rowContainer}>
                <div>
                  <span className={styles.routineTitle}>{`${routine_type} Routine ${name} by ${creator.name}`}</span>
                </div>                  
              </div>
              <div className={styles.rowContainer}>
                <div>
                    <span>
                      <span className={styles.mobileLabel}><FaCalendarAlt size={ICON_SIZE_NORMAL} color={"#FFF"} title="días de entrenamiento"/></span>
                      <div>
                        {days_of_week.map( (d, i) => <span key={i} className={styles.mobileLabelValue}>{d.name}</span>)}
                      </div>
                    </span>
                    <span>
                      <span className={styles.mobileLabel}><GiStopwatch size={ICON_SIZE_NORMAL} color={"#FFF"} title="duración"/></span>
                      <span className={styles.mobileLabelValue}>{duration}</span>
                    </span>
                    <span>
                      <span className={styles.mobileLabel}><SiLevelsdotfyi size={ICON_SIZE_NORMAL} color={"#FFF"} title="nivel"/></span>
                      <div>
                        {metadatas ? 
                          metadatas.level.map( (l, i) => <span key={i} className={styles.mobileLabelValue}>{l.name}</span>)
                          : <span></span>
                        }
                      </div>
                    </span>
                    <span>
                          <span className={styles.mobileLabel}><TfiTarget size={ICON_SIZE_NORMAL} color={"#FFF"} title="objetivos"/></span>
                          <div>
                            {metadatas ?  
                              metadatas.goals.map( (g, i) => <span key={i} className={styles.mobileLabelValue}>{g.name}</span>)
                            :
                              <span></span>
                            }
                          </div>
                    </span>
                    <span>
                      <span className={styles.mobileLabel}><MdOutlineStart size={ICON_SIZE_NORMAL} color={"#FFF"} title="fecha inicio"/></span>
                      <div>
                        <span className={styles.mobileLabelValue}>{start_date}</span>
                      </div>
                    </span>
                    <span>
                      <span className={styles.mobileLabel}><GiFinishLine size={ICON_SIZE_NORMAL} color={"#FFF"} title="fecha fin"/></span>
                      <div>
                        <span className={styles.mobileLabelValue}>{due_date}</span>
                      </div>
                    </span>
                </div>
              </div>
              <div className={styles.rowContainer}>
                {
                  showWidgetContainer &&
                  <div className={styles.routineDetailContainer}>
                    <div className={styles.routineDetailContainerDescription}>
                      <span>{description}{observation}</span>
                    </div>
                    <div>
                        <span>
                          <span className={styles.mobileLabel}><VscSymbolMethod size={ICON_SIZE_NORMAL} color={"#FFF"} title="método"/></span>
                          <span className={styles.mobileLabelValue}>{training_method}</span>    
                        </span>
                        <span>
                          <span className={styles.mobileLabel}><MdMonitorHeart size={ICON_SIZE_NORMAL} color={"#FFF"} title="cardio"/></span>
                          <span className={styles.mobileLabelValue}>{cardio}</span>
                        </span>
                        <span className={styles.tableDate}>
                          <span className={styles.mobileLabel}><MdOutlineTireRepair size={ICON_SIZE_NORMAL} color={"#FFF"} title="pre exhaustion"/></span>
                          <span className={styles.mobileLabelValue}>{pre_exhaustion}</span>
                        </span>
                        <span>
                          <span className={styles.mobileLabel}><VscDebugStart size={ICON_SIZE_NORMAL} color={"#FFF"} title="activation"/></span>
                          <span className={styles.mobileLabelValue}>{activation}</span>
                        </span>
                        <span>
                          <span className={styles.mobileLabel}><FaPauseCircle size={ICON_SIZE_NORMAL} color={"#FFF"} title="pausa"/></span>
                          <span className={styles.mobileLabelValue}>{rest_between_exercises}</span>
                        </span>
                        <span>
                          <span className={styles.mobileLabel}><MdOutlineSettingsSystemDaydream size={ICON_SIZE_NORMAL} color={"#FFF"} title="sistema"/></span>
                          <span className={styles.mobileLabelValue}>{system}</span>
                        </span>
                        <span>
                          <span className={styles.mobileLabel}><RiRhythmLine size={ICON_SIZE_NORMAL} color={"#FFF"} title="cadencia"/></span>
                          <span className={styles.mobileLabelValue}>{cadence}</span>
                        </span>
                        <span>
                          <span className={styles.mobileLabel}><AiFillStop size={ICON_SIZE_NORMAL} color={"#FFF"} title="restricciones"/></span>
                          <div>
                            {restrictions ?
                              restrictions.map( (r, i) => <span key={i} className={styles.mobileLabelValue}>{r.name}</span>)
                              :
                              <span></span>
                            }
                          </div>
                        </span>
                    </div>
                  </div>
                  
                }
                
              </div>
        </div>
    )
}

export default TableRow