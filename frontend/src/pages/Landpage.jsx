import { Link, useNavigate } from 'react-router-dom'
import { ROOT, COMPANY_NAME } from '../apiConfig'

import buttonsStyle from '../style/buttons.module.css'
import indexStyle from '../style/index.module.css'
import identifyStyle from '../style/identify.module.css'

const Landpage = () => {

  return (
      <main className={identifyStyle.identifyContainer}>
        <div className={identifyStyle.identifyButtonContainer}>
              <h1>Bienvenido a {COMPANY_NAME} BETA</h1>
        </div>
      </main>    
  )
}

export default Landpage