import { Link, useNavigate } from 'react-router-dom'
import { ROOT } from '../apiConfig'

import buttonsStyle from '../style/buttons.module.css'
import indexStyle from '../style/index.module.css'
import identifyStyle from '../style/identify.module.css'

const Identify = () => {

  return (
      <main className={identifyStyle.identifyContainer}>
        <div className={identifyStyle.identifyButtonContainer}>
              <h1>Bienvenido a Fitbox!</h1>
              <div>
                <div className={indexStyle.boxContainer}>
                  <span><h3>Si todavia no estas registrado</h3></span>
                  <span><Link className={buttonsStyle.buttonPrimary} to={`${ROOT}/register`}>Registrate</Link></span>
                </div>
                <div className={indexStyle.boxContainer}>
                  <span><h3>Si ya tenes un usuario</h3></span>
                  <span><Link className={buttonsStyle.buttonPrimary} to={`${ROOT}/login`}>Ingresar</Link></span>
                </div>
              </div>
        </div>
      </main>    
  )
}

export default Identify