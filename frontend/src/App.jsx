import { useState } from 'react'
import PageRouter from './router/PageRouter'
import { Footer, Navbar } from './components';

import { useGlobalContext } from './context/GlobalContextProvider';

function App() {

  const {customer} = useGlobalContext()
  return (
    <>
      <Navbar></Navbar>
        <PageRouter/>
      <Footer></Footer>
    </>
  )
}

export default App
