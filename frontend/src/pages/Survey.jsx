import React, {useState, useEffect} from 'react'
import Switch from "react-switch";
import axios from 'axios'
import moment from 'moment';

import { useNavigate } from 'react-router-dom'
import { API_ENDPOINTS, ROOT } from '../apiConfig'
import { COMPONENTS } from '../colors'

import { useGlobalContext } from '../context/GlobalContextProvider'
import { useModalContext } from '../context/ModalContextProvider';

import { RiErrorWarningLine } from "react-icons/ri";

import { Modal, Nps } from '../components'

import buttonsStyle from '../style/buttons.module.css'
import surveyStyle from '../style/survey.module.css'
import indexStyle from '../style/index.module.css'


const Survey = () => {
  const {lists, customer, getCustomerData, getLists, setCustomer, actualRoutine} = useGlobalContext()
  const {toggleModal, toStatus, setModalTitle, setModalText} = useModalContext()
  const [effortScale, setEffortScale] = useState(0)
  const [welfareScale, setWelfareScale] = useState(0)
  const [enjoymentScale, setEnjoymentScale] = useState(0)
  const [wasCompleted, setWasCompleted] = useState(false)
  const [incompleteForm, setIncompleteForm] = useState(false)
  const navigate = useNavigate()

  const initialValues = {
    customer: +localStorage.getItem("customer_id"),
    routine: actualRoutine.id,
    started_on: localStorage.getItem("routine_start_time"),
    effort_scale:'',
    welfare_scale:'',
    enjoyment_scale:'',
    was_completed:''
  }

  const [formValues, setFormValues] = useState(initialValues)
  
  const _handleOmit = () => {
    navigate(`${ROOT}/panel`)
    return
  };

  const handleSubmit = async (e) => {
    e.preventDefault() /** Es para prevenir que el formulario se recargue y la pagina*/
    if(!enjoymentScale || !welfareScale || !effortScale){
      setIncompleteForm(true)
      return
    }
    formValues.was_completed = + wasCompleted
    formValues.enjoyment_scale = enjoymentScale
    formValues.welfare_scale = welfareScale
    formValues.effort_scale = effortScale
    axios.post(`${API_ENDPOINTS.routineCustomersIndicator}/`, formValues, {headers: {'Authorization': localStorage.getItem('auth-token-app')}})
    .then(resp  => {
      return resp.data
    })
    .then((data) => {
      setCustomer(data)
      return
    })
    .catch(error => {
      return
    })
    .finally(() => {
      navigate(`${ROOT}/panel`)
      return
    })
    
  }

  const handleConfirmation = (value) =>{
    console.log("vino")
  }

  return (
      <main className={surveyStyle.surveyContainer}>
        <Modal onConfirm={handleConfirmation}></Modal>
        {
          customer &&
          <div className={surveyStyle.surveyFormContainer}>
            <form action="Post" onSubmit={(e) => handleSubmit(e)}>
                <div className={surveyStyle.surveySectionFormContainer}>
                    <h2>Indicadores de rendimiento deportivo</h2>
                    <label>
                      <span>Escala de bienestar <RiErrorWarningLine color={COMPONENTS.INFO} title="Del 1 al 5, que tan bien te sentiste en el día hoy"/></span>
                      <Nps handleClick={setWelfareScale} scale={[1,2,3,4,5]} />
                    </label>
                    <label>
                      <span>Escala de efuerzo realizado <RiErrorWarningLine color={COMPONENTS.INFO} title="Del 1 al 5, que tanto te esforzaste"/></span>
                      <Nps handleClick={setEffortScale} scale={[1,2,3,4,5]} />
                    </label>
                    <label>
                      <span>Disfrutaste el entrenamiento? <RiErrorWarningLine color={COMPONENTS.INFO} title="Que tanto disfrutaste el entrenamiento"/></span>
                      <Nps handleClick={setEnjoymentScale} scale={[1,2,3,4,5]} />
                    </label>
                    <label htmlFor="complete_training">
                      <span>Completaste el entrenamiento? <RiErrorWarningLine color={COMPONENTS.INFO} title="Completaste el entrenamiento?"/></span>
                      <Switch name="complete_training" onChange={setWasCompleted} checked={wasCompleted} />
                    </label>
                </div>
                <div className={surveyStyle.errorFormContainer}>
                  { incompleteForm && <span className={indexStyle.errorMessage}>Para guardar, por favor completar todas las escalas</span>}
                </div>
                <div className={surveyStyle.toolBar}>
                    <button onClick={_handleOmit} className={buttonsStyle.buttonPrimary}>Omitir</button>
                    <button type='submit' className={buttonsStyle.buttonPrimary}>Guardar</button>
                </div>
            </form>
        </div>
        }
          
      </main>    
  )
}

export default Survey