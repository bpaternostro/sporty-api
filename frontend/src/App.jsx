import { useState } from 'react'
import PageRouter from './router/PageRouter'
import { Footer, Navbar, Spinner } from './components';

import { useGlobalContext } from './context/GlobalContextProvider';

function App() {

  const {loading} = useGlobalContext()
  return (
    <>
      <Navbar></Navbar>
         {loading && <Spinner/>}
        <PageRouter/>
      <Footer></Footer>
    </>
  )
}

export default App
