import React from 'react'

import { RoutineDay } from '..';

import './tab.css'

const Tab = ({ d, activeTab }) => {
  return (
    <div className="tabContainer">
      <div className="tabContent">
        <RoutineDay d={d[activeTab]}/>
      </div>
    </div>
  );
}

export default Tab