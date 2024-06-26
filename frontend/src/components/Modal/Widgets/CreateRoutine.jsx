import { React, useState, useEffect } from 'react'


import { useGlobalContext } from '../../../context/GlobalContextProvider'
import { useModalContext } from '../../../context/ModalContextProvider'

import  modalStyle from '../modal.module.css'
import  buttonStyle from '../../../style/buttons.module.css'

import { API_ENDPOINTS } from '../../../apiConfig'

const CreateRoutine = () => {
    const {actualPortfolio, 
            setPortfolios,
            setActualPortfolio,
            portfolioTypes, 
            portfolioStatus, 
            setPortfolioHasChanged, 
            portfolioHasChanged,
            csrfToken} = useGlobalContext()
    const {setModalError, toggleModal, isCreatePortfolioModal, isEditPortfolioModal} = useModalContext()

    const initialValues = {
        name: "",
        type: 0,
        status: 0
    }

    const [formValues, setFormValues] = useState(initialValues)
    
    const handleChangeInput = (value, name) => {
        if(value === ""){
            value = 0
        }
        const aux = {...formValues, [name]:value}
        setFormValues(aux)
    }

    useEffect(() => {
        if(isCreatePortfolioModal){
            setFormValues(initialValues)
        }else{ 
            setFormValues({
                portfolio: actualPortfolio.id || 1,
                name: actualPortfolio.name,
                status: actualPortfolio.status,
                type: actualPortfolio.type,
            })
        }
    },[actualPortfolio])


  return (
    <div className={modalStyle.formContainer}>
        <form>
            <div className={modalStyle.formBody}>
                <input style={{display:"none"}} type="text" name="portfolio" value={formValues.portfolio} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>
                <span>
                    <label htmlFor="name">Name</label>
                    <input type="text" name="name" value={formValues.name} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}/>    
                </span>
                <span>
                    <label htmlFor="type">Type</label>     
                    <select name="type" value={formValues.type} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}>
                        {portfolioTypes && portfolioTypes.map((t, i) => <option key={i} value={t[0]}>{t[1]}</option>)}
                    </select>
                </span>
                
                {
                    isEditPortfolioModal &&
                    <span>
                        <label htmlFor="status">Status</label>
                        <select name="status" value={formValues.status} onChange={(e) => handleChangeInput(e.target.value, e.target.name)}>
                            {portfolioStatus && portfolioStatus.map((t, i) => <option key={i} value={t[0]}>{t[1]}</option>)}
                        </select>
                    </span>
                }
                
            </div>
            <div className={modalStyle.formFooter}>
                <button type="submit" className={buttonStyle.buttonPrimary}>{isCreatePortfolioModal ? 'Create': 'Save'}</button>
                <button className={`${ buttonStyle.buttonPrimary } ${modalStyle.acceptModal}`} onClick={toggleModal}>Cancel</button>
            </div>
        </form>
    </div>
  )
}

export default CreateRoutine