import React from 'react'

import './tab.css'
import { useGlobalContext } from '../../context/GlobalContextProvider'

const TabButton = ({ d, activeTab, setActiveTab }) => {
  const {setCurrentIndex} = useGlobalContext()

  const handleClick = (e, index) =>{
    setActiveTab(index)
    setCurrentIndex(0)
  }
    return (
        <div className="tabHeader">
          {d.map((item, index) => (
            <li
              className={activeTab === index ?  "tabButton activeButton": "tabButton"}
              key={index}
              onClick={(e) => handleClick(e, index)}>
              {item.day.name}
            </li>
          ))}
        </div>
      );
}

export default TabButton