import React from 'react'
import { Route, Routes } from 'react-router-dom'
import { Home, RoutinePlayer, Identify, Landpage, Login, Register, Profile, Survey } from '../pages'
import { ROOT } from '../apiConfig'

const PageRouter = () => {
  return (
    <>
      <Routes>
          <Route path={`${ROOT}`} element={<Landpage/>} />
          <Route path={`${ROOT}/panel`} element={<Home/>} />
          <Route path={`${ROOT}/panel/routine/:id`} element={<RoutinePlayer/>} />
          <Route path={`${ROOT}/identify`} element={<Identify/>} />
          <Route path={`${ROOT}/register`} element={<Register/>} />
          <Route path={`${ROOT}/login`} element={<Login/>} />
          <Route path={`${ROOT}/profile`} element={<Profile/>} />
          <Route path={`${ROOT}/survey`} element={<Survey/>} />
      </Routes>
    </>
  )
}

export default PageRouter