
import React, { useEffect, useState } from 'react'

import  modalStyle from './modal.module.css'
import  buttonStyle from '../../style/buttons.module.css'

import { useGlobalContext } from '../../context/GlobalContextProvider'
import { useModalContext } from '../../context/ModalContextProvider'

import {Indicators, EditRoutine, CreateRoutine} from '../index'

import axios from 'axios'

const Modal = ({onConfirm}) => {
    const {modalTitle, 
        modalText, 
        modal, 
        toggleModal, 
        onClose, 
        isConfirmationModal,
        isMoveModal} = useModalContext()

    if(modal){
        document.body.classList.add('active-modl')
    }else{
        document.body.classList.remove('active-modl')
    }

    return (
        <>  
            {   
                modal && (
                

                <div className={ modalStyle.modal }>
                    <div className={ modalStyle.overlay }>
                        <button className={modalStyle.closeModal} onClick={toggleModal}>X</button>
                    </div>
                    <div className={modalStyle.modalContent}>
                        <h2>{modalTitle}</h2>
                        <div>
                            <h3>{modalText}</h3>
                        </div>
                        <div className={modalStyle.modalFooter}>
                            <span>
                                <button className={`${ buttonStyle.buttonPrimary } ${modalStyle.acceptModal}`} onClick={toggleModal}>OK</button>
                            </span>
                        </div>
                    </div>  
                </div>)
            }      
        </>
    )
}

export default Modal