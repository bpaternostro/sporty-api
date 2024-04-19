import React, {useState} from 'react'

import './nps.css'

const Nps = ({handleClick, scale}) => {
    const [isActivated, setIsActivated] = useState(false)

    const handleActivate = (item) => {
        setIsActivated(item)
        handleClick(item)
    }

    return (
        <div className="npsContainer">
            {scale.map((item, index) => (
            <li
                className={item === isActivated ? "npsButton activated":"npsButton"} 
                key={index}
                onClick={() => handleActivate(item)}>
                {item}
            </li>
            ))}
        </div>
    )
}

export default Nps