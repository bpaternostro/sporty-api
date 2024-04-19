import React from 'react'

import buttonStyle from '../../style/buttons.module.css'
import './slider.css'

const FormElement = ({ name, onClick, value }) => {
  return (
    <div>
      <input
        className={buttonStyle.buttonSeconday}
        type={"button"}
        value={value}
        onClick={onClick}
      />
    </div>
  )
}

export default FormElement