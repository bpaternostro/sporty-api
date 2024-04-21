import React, {useState, useEffect} from 'react'

import { Link, useNavigate } from 'react-router-dom'
import { API_ENDPOINTS, ROOT, PASSWORD_LENGTH } from '../apiConfig'
import { MESSAGES } from '../messages'

import axios from 'axios'
import { getUserId } from '../helpers/verifyToken'
import { RiErrorWarningLine } from "react-icons/ri";

import buttonsStyle from '../style/buttons.module.css'
import contactStyle from '../style/contact.module.css'
import indexStyle from '../style/index.module.css'


import { useGlobalContext } from '../context/GlobalContextProvider';

const Register = () => {
  const navigate = useNavigate()
  const {csrfToken} = useGlobalContext()
  const [repeatedUser, setRepeatedUser] = useState(false)
  const [problemsUpdating, setProblemsUpdating] = useState(false)
  const [userId, setUserId] = useState(getUserId())
  const [label, setLabel] = useState(userId ? "Perfil de usuario": "Registro de usuario")
  const [buttonLabel, setButtonLabel] = useState(userId ? "Guardar": "Registrar")
  const [canSubmit, setCanSubmit] = useState(false)
  
  const initialValues = {
    first_name:'',
    last_name:'',
    email:'',
    password: '',
    username:''
  }
  const [formValues, setFormValues] = useState(initialValues)
  const handleChangeInput = (value, name) => {
    setCanSubmit(true)
    const aux = {...formValues, [name]:value}
    setFormValues(aux)
  }
  
  const handleSubmit = async (e) => {
    e.preventDefault() /** Es para prevenir que el formulario se recargue y la pagina*/
    if(!userId){
      formValues.username = formValues.email
      axios.post(API_ENDPOINTS.register, formValues, { headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken}})
      .then( resp => {
        navigate(`${ROOT}/login`)
        return
      })
      .catch(error => {
        setRepeatedUser(true)
        return
      })
    }else{
      axios.put(`${API_ENDPOINTS.auth}/${userId}`, formValues, {headers: {'Authorization': localStorage.getItem('auth-token-app')}})
      .then(resp  => {
        setCanSubmit(false)
        return
      })
      .catch(error => {
        setProblemsUpdating(true)
        return
      })
    }
  }

  useEffect(() => {
    if(!userId){
      return
    }
    axios.get(`${API_ENDPOINTS.auth}/${userId}`, {headers: {'Authorization': localStorage.getItem('auth-token-app')}})
    .then(resp  => {
        setFormValues(resp.data.user)
    })
    
  }, [])

  return (
      <main className={contactStyle.contactContainer}>
        <div className={contactStyle.contactFormContainer}>

           <h1>{label}</h1>
              <form action="Post" onSubmit={(e) => handleSubmit(e)}>
                  <div>
                      <label className={contactStyle.label}>Email</label>
                      <span className={indexStyle.warningContainer}>
                        <input name="email" type="email" required value={formValues.email} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                        <span className={indexStyle.warningButton}><RiErrorWarningLine color={"#15202b"}/></span>
                      </span>
                      <label className={contactStyle.label}>Password</label>
                      <span className={indexStyle.warningContainer}>
                        <input name="password" minLength={PASSWORD_LENGTH} type="password" required value={formValues.password} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                        <span className={indexStyle.warningButton}><RiErrorWarningLine color={"#15202b"}/></span>
                      </span>
                      <label className={contactStyle.label}>Nombre</label>
                      <input name="first_name" type="text" required value={formValues.first_name} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                      <label className={contactStyle.label}>Apellido</label>
                      <input name="last_name" type="text" required value={formValues.last_name} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                      {
                        repeatedUser && <span className={indexStyle.errorMessage}>{MESSAGES.REGISTER_REPEATED_USER_ERROR}</span>
                      }
                      {
                        problemsUpdating && <span className={indexStyle.errorMessage}>{MESSAGES.REGISTER_PROBLEMS_ERROR}</span>
                      }
                      {!userId ? 
                        <div className={contactStyle.forwardLinkContainer}>
                          <span className={contactStyle.forwardMessage}>Ya tenes una cuenta?</span>
                          <span><Link to={`${ROOT}/login`}>Click aqui!</Link></span>
                        </div>
                        :
                        <div></div>
                      }
                  </div>
                  <div>
                      <button type='submit' className={buttonsStyle.buttonPrimary} disabled={!canSubmit ? true:false}>{buttonLabel}</button>
                  </div>
              </form>
        </div>
      </main>    
  )
}

export default Register