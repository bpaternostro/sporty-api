import React, {useState} from 'react'

import { TabButton, Tab } from '../../components'

import style from './player.module.css'

const Player = ({routine}) => {
  const [activeTab, setActiveTab] = useState(0)
  const {
    id,
    days,
    info
  } = routine || {}
  
  return (
    <div className={style.playerContainer}>
        <div>
          <TabButton
            activeTab={activeTab}
            setActiveTab={setActiveTab}
            d={days}/>
          <Tab d={days} activeTab={activeTab}/>
        </div>
    </div>
  )
}

export default Player