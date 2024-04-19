import React from "react";

import './slider.css'
import {HIGHLIGHT_COLOR} from '../../apiConfig'

const Step = ({ onChange, currentIndex, steps }) => {
  return (
    <div className="steps-container">
      {steps.map((step, index) => {
        let color = currentIndex === index ? HIGHLIGHT_COLOR : "#FFF";
        return (
          <div className="steps-item" key={index}>
            <h3
              style={{
                margin: 0,
                color: color
              }}
              onClick={(e) => onChange(index)}
            >
            {step.name} 
            </h3>
          </div>
        );
      })}
    </div>
  );
};

export default Step;