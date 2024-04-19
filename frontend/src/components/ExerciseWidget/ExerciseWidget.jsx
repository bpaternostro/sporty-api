import React from 'react'

const ExerciseWidget = ({ blockExercise}) => {
  const {exercise, serie, reps, weight, pause} = blockExercise || {}
  return (
    <div className="content">
      <span className="material-symbols-outlined">photo_camera</span>
      <div>
        <h2>{exercise.name}</h2>
        <span>{serie}</span>
        <span>{reps}</span>
        <span>{weight}</span>
        <span>{pause}</span>
      </div>
    </div>
  )
}

export default ExerciseWidget