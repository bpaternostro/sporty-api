import React from 'react'

import style from "./widget.module.css"

const Widget = ({name, value}) => {
  return (
    <div className={style.widget}>
        <h3 className={style.widgetTitle}>{name}</h3>
        <div>
          {
            Array.isArray(value) ? value.map( (v,i)  => <span key={i} className={style.widgetValue}>{v.name}</span>) :
            <span className={style.widgetValue}>{value}</span>
          }
        </div>
    </div>
  )
}

export default Widget