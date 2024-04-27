import React, {useEffect} from 'react'

import { useGlobalContext } from '../../context/GlobalContextProvider'

import spinnerStyle from './spinner.module.css'
import indexStyle from '../../style/index.module.css'

const Spinner = () => {
  
  return (
    <>
        <div>
            <div className={ spinnerStyle.spinnerContainer }>
                <div className={ spinnerStyle.overlay }>
                    <div className={spinnerStyle.spinner}></div>
                </div>
            </div>
        </div>
    </>
    
  )
}

export default Spinner