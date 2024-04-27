import axios from 'axios'
import { API_ENDPOINTS, ADMIN_ROLE, ROOT } from '../apiConfig'

import { jwtDecode } from 'jwt-decode';

import { getCookie } from './CoreMethods';

const csrfToken = getCookie('csrftoken');

export const verifyToken = (navigate) =>{
    axios.get(API_ENDPOINTS.verify,
      {headers: {'Authorization': localStorage.getItem('auth-token-app')}})
      .then((res) => {
        return true
      })
      .catch( (err) => {
        console.log(err)
        navigate(`${ROOT}/login`)
        return
      })
}

export const verifyUser = (navigate) =>{
  fetch(API_ENDPOINTS.user, {
    mode: 'cors',
    method: 'get',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
      'Authorization': localStorage.getItem('auth-token-app')
    }
  })
  .then( resp => {
    if(resp.status !== 200){
      navigate(`${ROOT}/login`)
      localStorage.setItem('auth-token-app','')
      localStorage.setItem('name','')
      localStorage.setItem('customer_id','')
      localStorage.setItem('customer','')
      return false
    }
    return true
  })
  .catch(error => {
    navigate(`${ROOT}/login`)
    localStorage.setItem('auth-token-app','')
    localStorage.setItem('name','')
    localStorage.setItem('customer_id','')
    localStorage.setItem('customer','')
    return false
  })
}


export const isAdmin = () => {
  const token = localStorage.getItem('auth-token-app')
  if(!token){
    return false
  }
  const decoded = jwtDecode(token)
  return decoded.role
}


export const getUserId = () => {
  const token = localStorage.getItem('auth-token-app')
  if(!token){
    return false
  }
  const decoded = jwtDecode(token)
  return decoded.id
}