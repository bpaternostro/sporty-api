import React from "react";
import ReactSlider from "react-slider";

import "./slider.css";

const Slider = ({ onChange, currentIndex, steps }) => {
    return (
      <ReactSlider
        className="horizontalSlider"
        markClassName="block-mark"
        onChange={onChange}
        trackClassName="block-track"
        defaultValue={0}
        value={currentIndex}
        min={0}
        max={steps.length - 1}
        marks
        renderMark={(props) => {
          if (props.key < currentIndex) {
            props.className = "block-mark block-mark-completed";
          } else if (props.key === currentIndex) {
            props.className = "block-mark block-mark-active";
          }
          return <span {...props} />;
        }}
        orientation="horizontal"
      />
    );
  };
  
  export default Slider;