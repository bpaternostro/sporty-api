import React, { useContext, createContext, useState } from 'react'

const ModalGlobalContext = createContext()
const ModalContextProvider = ({children}) => {
    const [modal, setModal] = useState(false)
    const [modalOk, setModalOk] = useState(false)
    const [modalTitle, setModalTitle] = useState(false)
    const [modalText, setModalText] = useState(false)
    const [modalError, setModalError] = useState(false)
    const [entityId, setEntityId] = useState("")
    const [errorMsg, setErrorMsg] = useState("")
    const [toStatus, setToStatus] = useState()
    const [onClose, setOnClose] = useState()
    const [isConfirmationModal, setIsConfirmationModal] = useState(false)

    const toggleModal = () => {
        setModal(!modal)
    }

    return (
        <ModalGlobalContext.Provider value={{
            modal,
            toggleModal,
            modalOk, setModalOk,
            modalTitle, setModalTitle,
            modalText, setModalText,
            modalError, setModalError,
            entityId, setEntityId,
            toStatus, setToStatus,
            onClose, setOnClose,
            isConfirmationModal, setIsConfirmationModal,
            setErrorMsg
            }}>
            {children}
        </ModalGlobalContext.Provider>
    )
}

/*cremos un custom Hook para utilizar el contexto */
export const useModalContext = () => useContext(ModalGlobalContext)

export default ModalContextProvider