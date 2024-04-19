import React, {useEffect, useState} from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { API_ENDPOINTS, ROOT, PASSWORD_LENGTH } from '../apiConfig'
import { COMPONENTS } from '../colors'
import { MESSAGES } from '../messages'
import { isAdmin } from '../helpers/verifyToken'

import { jwtDecode } from 'jwt-decode';
import { RiErrorWarningLine } from "react-icons/ri";

import buttonsStyle from '../style/buttons.module.css'
import contactStyle from '../style/contact.module.css'
import indexStyle from '../style/index.module.css'

import { useGlobalContext } from '../context/GlobalContextProvider';

const Login = () => {
  const {setUserData, getCustomerData, getLists, csrfToken} = useGlobalContext()
  const navigate = useNavigate()
  const [errorLogin, setErrorLogin] = useState(false)
  const initialValues = {
    email:'',
    password: ''
  }
  
  const [formValues, setFormValues] = useState(initialValues)

  const handleChangeInput = (value, name) => {
    const aux = {...formValues, [name]:value}
    setFormValues(aux)
  }

  const handleSubmit = async (e) => {
    e.preventDefault() /** Es para prevenir que el formulario se recargue y la pagina*/
    fetch(API_ENDPOINTS.login, {
          mode: 'cors',
          method: 'post',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
          },
          body: JSON.stringify(formValues)
    })
    .then( response => {
      if (!response.ok) {
        throw new Error('Problems with authentication')
      }
      return response;
    })
    .then(response => {
      return response.json()
    })
    .then( data => {
      /* 
        guardamos el token en el local storage, persiste en la memoria del navegador 
      */
      const accessToken = data.jwt
      const decoded = jwtDecode(accessToken)
      setUserData(decoded)
      localStorage.setItem('auth-token-app', accessToken)
      localStorage.setItem('name', decoded.name)
      localStorage.setItem('customer_id', decoded.customer_id)
      getCustomerData()
      getLists()
      if(isAdmin()){
        navigate(`${ROOT}/admin`)
        return
      }else{
        navigate(`${ROOT}/panel`)
        return
      }
    })
    .catch(error => {
      console.log(error)
      setErrorLogin(true)
   })
  }
  return (
      <main className={contactStyle.contactContainer}>
        <div className={contactStyle.contactFormContainer}>
              <h1>Login</h1>
              <form action="Post" onSubmit={(e) => handleSubmit(e)}>
                  <div>
                      <label className={contactStyle.label}>Email</label>
                      <span className={indexStyle.warningContainer}>
                        <input name="email" type="email" required onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                        <span className={indexStyle.warningButton}><RiErrorWarningLine color={COMPONENTS.REQUIRED} /></span>
                      </span>
                      <label className={contactStyle.label}>Password</label>
                      <span className={indexStyle.warningContainer}>
                        <input name="password" minLength={PASSWORD_LENGTH} type="password" required onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                        <span className={indexStyle.warningButton}><RiErrorWarningLine color={COMPONENTS.REQUIRED}/></span>
                      </span>
                      {
                        errorLogin && <span className={indexStyle.errorMessage}>{MESSAGES.LOGIN_ERROR}</span>
                      }
                      <div className={contactStyle.forwardLinkContainer}>
                        <span className={contactStyle.forwardMessage}>Si todavia no estas registrado, podes hacerlo aqui:</span>
                        <span><Link to={`${ROOT}/register`}>Click aqui!</Link></span>
                      </div>
                  </div>
                  <div className={contactStyle.toolBar}>
                      <button type="submit" className={buttonsStyle.buttonPrimary}>Ingresar</button>
                  </div>
              </form>
        </div>
      </main>    
  )
}

export default Login