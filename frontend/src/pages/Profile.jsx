import React, {useState, useEffect} from 'react'
import { Link } from 'react-router-dom'
import Select from 'react-select';
import Switch from "react-switch";
import axios from 'axios'

import { useNavigate } from 'react-router-dom'
import { ROOT, API_ENDPOINTS, ICON_SIZE_BIG } from '../apiConfig'
import { COMPONENTS } from '../colors'

import { verifyUser } from '../helpers/verifyToken';

import { useGlobalContext } from '../context/GlobalContextProvider'
import { useModalContext } from '../context/ModalContextProvider';

import { RiErrorWarningLine } from "react-icons/ri";
import { IoChevronBackCircle } from "react-icons/io5";

import { Modal } from '../components'

import buttonsStyle from '../style/buttons.module.css'
import profileStyle from '../style/profile.module.css'
import indexStyle from '../style/index.module.css'


const Profile = () => {
  const {lists, customer, getCustomerData, getLists, setCustomer} = useGlobalContext()
  const {toggleModal, toStatus, setModalTitle, setModalText} = useModalContext()
  const navigate = useNavigate()
  const [repeatedUser, setRepeatedUser] = useState(false)
  const [problemsUpdating, setProblemsUpdating] = useState(false)
  const [successMsg, setSuccessMsg] = useState(false)
  const [coreFieldsHasChanged, setCoreFieldsHasChanged] = useState(false)
  const [hasEquiment, setHasEquiment] = useState(false)
  const [hasSpace, setHasSpace] = useState(false)
  const [trainAtHome, setTrainAtHome] = useState(false)
  const [lackOfTime, setLackOfTime] = useState(false)
  
  const initialValues = {
    first_name:'',
    last_name:'',
    date_of_birth:'',
    country:'',
    weight:'',
    height:'',
    imc:'',
    goals:'',
    restrictions:'',
    level:'',
    customer_with_equipement:'',
    customer_train_at_home:'',
    customer_with_lack_space:'',    
    customer_with_lack_time:''
  }

  const [formValues, setFormValues] = useState(initialValues)
  
  const handleToogleHasEquipmentChange = nextChecked => {
    setHasEquiment(nextChecked);
    handleChangeInput(+ nextChecked, "customer_with_equipement")
  };

  const handleToogleHasSpaceChange = nextChecked => {
    setHasSpace(nextChecked);
    handleChangeInput(+ nextChecked, "customer_with_lack_space")
  };

  const handleToogleTrainAtHomeChange = nextChecked => {
    setTrainAtHome(nextChecked);
    handleChangeInput(+ nextChecked, "customer_train_at_home")
  };

  const handleToogleLackOfTimeChange = nextChecked => {
    setLackOfTime(nextChecked);
    handleChangeInput(+ nextChecked, "customer_with_lack_time")
  };

  const handleChangeInput = (value, name) => {
    if(name === "first_name" || name === "last_name"){
      setCoreFieldsHasChanged(true)
    }
    const aux = {...formValues, [name]:value}
    setFormValues(aux)
  }

  const handleChangeSelectInput = (value, name) => {
    const aux = {...formValues, [name]:parseInt(value)}
    setFormValues(aux)
  }

  const handleSubmit = async (e) => {
    e.preventDefault() /** Es para prevenir que el formulario se recargue y la pagina*/
    if(coreFieldsHasChanged){
      console.log("hoa")
    }
    const auxForm = {...formValues} 
    auxForm.goals = formValues.goals.map( g => g.value)
    auxForm.restrictions = formValues.restrictions.map( r => r.value)
    auxForm.trainings_preferences = formValues.trainings_preferences.map( t => t.value)
    axios.put(`${API_ENDPOINTS.customersUpdate}/${localStorage.getItem('customer_id')}/`, auxForm, {headers: {'Authorization': localStorage.getItem('auth-token-app')}})
    .then(resp  => {
      return resp.data
    })
    .then((data) => {
      setCustomer(data)
      return
    })
    .catch(error => {
      setProblemsUpdating(true)
      return
    })
    .finally(() => {
      setModalTitle("Perfil de usuario")
      setModalText("Sus cambios fueron ingresados correctamente.")
      toggleModal()
    })
    
  }

  useEffect(() => {
    if(customer){
      verifyUser(navigate)
      setFormValues(
        {
          first_name:customer.customer.first_name,
          last_name:customer.customer.last_name,
          date_of_birth:customer.date_of_birth,
          country:customer.country,
          weight:customer.weight,
          height:customer.height,
          imc:customer.imc,
          goals:customer.goals.map(g => ({label:g.name, value: g.id})),
          restrictions:customer.restrictions.map(r => ({label:r.name, value: r.id})),
          trainings_preferences:customer.trainings_preferences.map(t => ({label:t.name, value: t.id})),
          level:customer.level.id,
          customer_with_equipement:customer.customer_with_equipement,
          customer_train_at_home:customer.customer_train_at_home,
          customer_with_lack_space:customer.customer_with_lack_space,    
          customer_with_lack_time:customer.customer_with_lack_time
        }
      )
      setHasEquiment(Boolean(customer.customer_with_equipement))
      setHasSpace(Boolean(customer.customer_with_lack_space))
      setLackOfTime(Boolean(customer.customer_with_lack_time))
      setTrainAtHome(Boolean(customer.customer_train_at_home))
      return
    }
  },[customer])

  useEffect(() => {
    if(!customer){
      getCustomerData()
      getLists()
      return
    }
  },[])

  const handleConfirmation = () =>{
    console.log("vino")
  }
  
  const _handleOmit = () => {
    navigate(`${ROOT}/panel`)
    return
  };

  return (
      <main className={profileStyle.profileContainer}>
        <Modal onConfirm={handleConfirmation}></Modal>
        <div className={profileStyle.profileFormContainerBack}>
          <Link to={`${ROOT}/panel`} title="Volver al panel"><IoChevronBackCircle size={ICON_SIZE_BIG} /></Link>
        </div>
        {
          customer &&
          <div className={profileStyle.profileFormContainer}>
            <form action="Post" onSubmit={(e) => handleSubmit(e)}>
                <div className={profileStyle.profileSectionFormContainer}>
                    <h2>Perfil del usuario</h2>
                    <label>
                      <span>Nombre</span>
                      <input className={profileStyle.disabledInput} name="first_name" type="text" required value={formValues.first_name} onChange={(e) => handleChangeInput(e.target.value, e.target.name)} disabled/>  
                    </label>
                    <label>
                      <span>Apellido</span>
                      <input className={profileStyle.disabledInput} name="last_name" type="text" required value={formValues.last_name} onChange={(e) => handleChangeInput(e.target.value, e.target.name)} disabled/>
                    </label>
                    <label>
                      <span>Fecha de nacimiento</span>
                      <input name="date_of_birth" type="date" required value={formValues.date_of_birth ? formValues.date_of_birth: ""} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                    </label>
                    <label>
                      <span>Pais de origen</span>
                      <select name="country" value={formValues.country} onChange={(e) => handleChangeSelectInput(e.target.value, e.target.name)}>
                      {
                          lists && lists.countries.map((item, index) => {
                            return <option key={index} value={item[0]}>{item[1]}</option>
                          })
                        }
                      </select>
                    </label>
                </div>
                <div className={profileStyle.profileSectionFormContainer}>
                    <h2>Datos corporales</h2>
                    <span>
                      <label>
                        <span>Peso</span>
                        <input name="weight" type="number" min="0" step=".01" value={formValues.weight} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                      </label>
                      <label>
                        <span>Altura</span>
                        <input name="height" type="number" min="0" step=".01" value={formValues.height} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                      </label>
                      <label>
                        <span>Imc <RiErrorWarningLine color={COMPONENTS.INFO} title="Indice de masa muscular"/></span>
                        <input name="imc" type="number" min="0" step=".01" value={formValues.imc} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                      </label>
                    </span>
                </div>
                <div className={profileStyle.profileSectionFormContainer}>
                  <h2>Preferencias de entrenamiento</h2>
                  <label htmlFor="goals">
                    <span>Objetivos</span>
                    <Select
                      isMulti
                      name="goals"
                      options={lists.goals || []}
                      className="basic-multi-select"
                      classNamePrefix="select"
                      value={formValues.goals}
                      onChange={(e) => handleChangeInput(e,"goals")}
                    />
                  </label>
                  <label htmlFor="restrictions">
                    <span>Restricciones</span>
                    <Select
                      isMulti
                      name="restrictions"
                      options={lists.restrictions}
                      className="basic-multi-select"
                      classNamePrefix="select"
                      value={formValues.restrictions}
                      onChange={(e) => handleChangeInput(e,"restrictions")}
                    />
                  </label>
                  <label htmlFor="trainings_preferences">
                    <span>Entrenamientos preferidos</span>
                    <Select
                      isMulti
                      name="trainings_preferences"
                      options={lists.trainings}
                      className="basic-multi-select"
                      classNamePrefix="select"
                      value={formValues.trainings_preferences}
                      onChange={(e) => handleChangeInput(e, "trainings_preferences")}
                    />
                  </label>
                  <label htmlFor="level">
                    <span>Nivel</span>
                    <select name="level" value={formValues.level} onChange={(e) => handleChangeSelectInput(e.target.value, e.target.name)}>
                        {
                          lists && lists.levels.map((item, index) => {
                            return <option key={index} value={item[0]}>{item[1]}</option>
                          })
                        }
                    </select>
                  </label>
                  <label htmlFor="customer_with_equipement">
                    <span>Cuenta con equipamiento</span>
                    <Switch 
                      trackColor={{false: '#767577', true: '#7315fe'}}
                      name="customer_with_equipement" 
                      onChange={handleToogleHasEquipmentChange} checked={hasEquiment} 
                    />
                  </label>
                  <label htmlFor="customer_train_at_home">
                    <span>Entrena en casa</span>
                    <Switch name="customer_train_at_home" onChange={handleToogleTrainAtHomeChange} checked={trainAtHome} />
                  </label>
                  <label htmlFor="customer_with_lack_space">
                    <span>Cuenta con poco espacio</span>
                    <Switch name="customer_with_lack_space" onChange={handleToogleHasSpaceChange} checked={hasSpace} />
                  </label>
                  <label htmlFor="customer_with_lack_time">
                    <span>Cuenta con poco tiempo</span>
                    <Switch name="customer_with_lack_time" onChange={handleToogleLackOfTimeChange} checked={lackOfTime} />
                  </label>
                </div>
                <div className={profileStyle.toolBar}>
                    <button onClick={_handleOmit} className={buttonsStyle.buttonPrimary}>Volver</button>
                    <button type='submit' className={buttonsStyle.buttonPrimary}>Guardar</button>
                </div>
            </form>
        </div>
        }
          
      </main>    
  )
}

export default Profile